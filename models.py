from sqlalchemy import Column, Integer, String
from database import Base

class Todo_table(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key = True)
    task = Column(String(50))