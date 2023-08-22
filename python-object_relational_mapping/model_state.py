# Somecomments goes here
# Some more comments
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 

Base = declarative_base()
"""
        Some class comments must go here
"""
class State(Base):
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)