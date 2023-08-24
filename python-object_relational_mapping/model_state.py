from sqlalchemy.ext.declarative import declarative_base

# Base class
Base = declarative_base()
'''
A base class that serves as the foundation for defining
database models (tables) using the
Object-Relational Mapping (ORM) approach.
'''

# A class to create the tables
class State(Base):
    '''
    A class that models the table 'states', inherited from Base

    Attributes:

        id(int): unique identity number of each state
    
        name(string): name of each state
    '''
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
