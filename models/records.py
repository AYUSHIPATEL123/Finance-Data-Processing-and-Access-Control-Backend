from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Date,String
from ..database import Base
from .users import User

class Record(Base):
    __tablename__ = "records"

    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True,index=True)
    