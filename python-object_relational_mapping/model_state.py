from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

username = 'root'
password = 'St10285515'
database = 'test_6'
# Create connection URL
connector = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)

# Create an SQLAlchemy engine
engine = create_engine(connector)

# Establish a connection to the database
connection = engine.connect()

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


Base.metadata.create_all(bind=engine)