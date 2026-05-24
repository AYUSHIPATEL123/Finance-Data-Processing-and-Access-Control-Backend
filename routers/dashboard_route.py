from fastapi import APIRouter,Depends,HTTPException,status
from database import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas.users import UserOut
from schemas.records import RecordType
from services.service import require_role
from models.records import Record

router = APIRouter()

@router.get('/total-income/{id}')
async def total_income(id: int,db:Annotated[AsyncSession,Depends(get_db)],access:Annotated[UserOut,Depends(require_role("admin",'analyst','user'))]):


        if access.role == "user" and access.id != id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you have no access to show this data")
        
        query = select(Record).where(Record.user_id == id,Record.type == RecordType.income)

        total_income = await db.execute(query)

        total_income = total_income.scalars().all()

        income =0 

        income = sum(i.amount for i in total_income)

        return {"total-income":income}    


@router.get('/total-expense/{id}')
async def total_expense(id: int,db:Annotated[AsyncSession,Depends(get_db)],access:Annotated[UserOut,Depends(require_role("admin",'analyst','user'))]):


        if access.role == "user" and access.id != id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you have no access to show this data")
        
        query = select(Record).where(Record.user_id == id,Record.type == RecordType.expense)

        total_income = await db.execute(query)

        total_expense = total_income.scalars().all()

        expense = sum(i.amount for i in total_expense)

        return {"total-expense":expense} 

   
@router.get('/net-balance/{id}')
async def total_balance(id: int,db:Annotated[AsyncSession,Depends(get_db)],access:Annotated[UserOut,Depends(require_role("admin",'analyst','user'))]):


        if access.role == "user" and access.id != id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you have no access to show this data")
        
        query1 = select(Record).where(Record.user_id == id,Record.type == RecordType.income)
        query2 = select(Record).where(Record.user_id == id,Record.type == RecordType.expense)

        total_income = await db.execute(query1)
        total_expense = await db.execute(query2)

        total_income = total_income.scalars().all()
        total_expense = total_expense.scalars().all()

        income = sum(i.amount for i in total_income)

        expense = sum(i.amount for i in total_expense)

        if expense > income:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="account out of balance")
        
        net_bal = income - expense           

        return {"Net-balance":net_bal}    


@router.get('/cat-total/{id}')
async def cat_toal(id:int,category:str,db:Annotated[AsyncSession,Depends(get_db)],access:Annotated[UserOut,Depends(require_role("admin","analyst","user"))]):

        if access.role == "user" and id != access.id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you do not have access to this Data")

        query1 = select(Record).where(Record.user_id==id,category==category)

        total = await db.execute(query1)

        total = total.scalars().all()

        total = sum(i.amount for i in total)

        return {f"total as {category} category":total}
