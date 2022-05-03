from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///databse.db")

Base = declarative_base()

session = Session(bind = engine, expire_on_commit = False)