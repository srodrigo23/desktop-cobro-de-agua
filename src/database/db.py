

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import create_engine, MetaData

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):

  __tablename__ = "users"
  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(10), unique=True, nullable=False)
  lastlogin = Column(Date, nullable=True)

# class 



engine = create_engine("sqlite:///data_otb.db")
# metadata = MetaData()

Base.metadata.create_all(engine)

# from sqlalchemy.orm import sessionmaker
# from .db import engine

# Session = sessionmaker(bind=engine)
# session = Session()
