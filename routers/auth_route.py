from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.users import UserOut,UserSchema,LoginSchema
from models.users import User
from typing import Annotated
from database import get_db
import jwt
import os
from dotenv import load_dotenv
from routers.users_route import hash_password,verify_password
from datetime import datetime,timedelta

load_dotenv()


router = APIRouter()

@router.post('/register/',response_model=UserOut)
async def add_user(data:UserSchema,db:Annotated[AsyncSession,Depends(get_db)]):
    user = User(username=data.username,password=hash_password(data.password),email=data.email,role=data.role)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.post('/login/')
async def login(data:LoginSchema,db:Annotated[AsyncSession,Depends(get_db)]):

    query = select(User).where(User.email == data.email)
    user = await db.execute(query)
    await db.commit()
    user = user.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404,detail="user doess not exist")
    if not verify_password(data.password,user.password):
        raise HTTPException(status_code=403,detail="user password is not valid")
    
    exp = datetime.utcnow() + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))

    token = jwt.encode({"usernaem":user.username,"expire":exp.timestamp()},os.getenv('SECRET_KEY'),algorithm=os.getenv('ALGORITHM'))
    
    user_data = {
        "email":user.email,
        "password":user.password,
        "jwt_token":token
    }

    return {
        "message":"user loged in successful",
        "data":user_data
    }