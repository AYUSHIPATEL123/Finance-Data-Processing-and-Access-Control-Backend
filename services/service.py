from fastapi import HTTPException,Depends,Request,status
from fastapi.security import OAuth2PasswordBearer
import hashlib
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select 
from datetime import datetime,timedelta
import jwt
from jwt.exceptions import PyJWTError
import os
from database import get_db
from models.users import User

pwd_content = CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password:str) -> str:
    
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    return pwd_content.hash(hashed)


def verify_password(plan_password:str,stored_password:str) -> bool:
    
    hashed = hashlib.sha256(plan_password.encode()).hexdigest()
    
    return pwd_content.verify(hashed,stored_password)


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

async def get_jwt_token(email:str):

    # exp = datetime.utcnow() + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    exp = datetime.utcnow() + timedelta(seconds=15)

    token = jwt.encode({"email":email,"exp":exp.timestamp()},os.getenv('SECRET_KEY'),algorithm=os.getenv('ALGORITHM'))
    
    return token


async def decode_jwt_token(token:str):
    try:

        user_data = jwt.decode(token,os.getenv('SECRET_KEY'),algorithm=os.getenv('ALGORITHM'))
        
        return user_data.email
    
    except PyJWTError as e:

        raise HTTPException(status_code=401,detail="Unauthorized User")


async def get_current_user(request:Request,db:AsyncSession = Depends(get_db)):
    
    try:

        token = request.headers.get("Authorization")
        
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="token is missing")
        
        token = token.split(" ")[-1]

        print("++++++",token)

        email = decode_jwt_token(token)

        query = select(User).where(User.email == email)

        user = await db.execute(query)

        await db.commit()
        
        user = user.scalar_one_or_none()

        return user
    
    except TypeError as e:

        HTTPException(status_code=401,detail=f'Unauthorized User,{e}')
