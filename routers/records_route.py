from fastapi import APIRouter,Depends,HTTPException
from schemas.records import RecordOut,RecordSchema
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base,get_db
from models.records import Record
from schemas.users import UserSchema
from services.service import get_current_user
router = APIRouter()


@router.get('/records/',response_model=list[RecordOut])
async def records(db:Annotated[AsyncSession,Depends(get_db)],user:Annotated[UserSchema,Depends(get_current_user)],):
    query = select(Record)
    records = await db.execute(query)
    records = records.scalars().all()
    
    return records

@router.post('/add-record/',response_model=RecordOut)
async def add_record(data:RecordSchema,db:Annotated[AsyncSession,Depends(get_db)],user:Annotated[UserSchema,Depends(get_current_user)],):
    record = Record(amount=data.amount,type=data.type,category=data.category,notes=data.notes,user_id=data.user_id)

    db.add(record)
    await db.commit()
    await db.refresh(record)

    return record

@router.put('/update-record/{id}',response_model=RecordOut)
async def update_record(id:int,new_data:RecordSchema,db:Annotated[AsyncSession,Depends(get_db)],user:Annotated[UserSchema,Depends(get_current_user)],):
    record = await db.get(Record,id)
    if record:
        record.amount=new_data.amount
        record.category=new_data.category
        record.type=new_data.type
        record.notes=new_data.notes
    else:
        return {"error":"record not found"}    

    await db.commit()
    await db.refresh(record)

    return record

@router.delete('/del-record/{id}',response_model=RecordOut) 
async def del_record(id:int,db:Annotated[AsyncSession,Depends(get_db)],user:Annotated[UserSchema,Depends(get_current_user)]):
    record = await db.get(Record,id) 
    if not record:
        raise HTTPException(status_code=404,detail="record not found")
    await db.delete(record)
    await db.commit()

    return record

