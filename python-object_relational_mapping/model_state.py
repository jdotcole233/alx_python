# Somecomments goes here
# Some more comments
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''
    A classs that models the table 'states', inherited from Base

    Attributes:
        id(int): unique identity number for each state

        name(string): name of each state
    '''
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
