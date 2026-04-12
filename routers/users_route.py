from fastapi import APIRouter,Depends
from sqlalchemy import select
from schemas.users import UserSchema,UserOut
from models.users import User
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from services.service import oauth2_schema,hash_password,get_current_user


router = APIRouter()


@router.get('/users/',response_model=list[UserOut])
async def users(db:Annotated[AsyncSession,Depends(get_db)],user:Annotated[UserSchema,Depends(get_current_user)]):
    query = select(User)
    users = await db.execute(query)
    users = users.scalars().all()
    print(user)
    return users


@router.put('/update-user/{id}',response_model=UserOut)
async def update_user(id:int,new_data:UserSchema,user:Annotated[UserSchema,Depends(get_current_user)],db:AsyncSession=Depends(get_db)):
    user = await db.get(User,id)
    if new_data:
        user.username = new_data.username
        user.password = hash_password(new_data.password)
        user.email = new_data.email
        user.role = new_data.role
    else:
        return {"error":"new data not reached"}

    await db.commit()
    await db.refresh(user)
    return user


@router.delete('/del-user/{id}')
async def del_user(id:int,user:Annotated[UserSchema,Depends(get_current_user)],db:AsyncSession=Depends(get_db)):
    user = await db.get(User,id)
    if not user:
        return {"message": "user not found"}
    await db.delete(user)
    await db.commit()
   
    return {"message":"user deleted successfully"}
