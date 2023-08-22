#! /usr/bin/python3
# Some comments should go here
# Some more comments should go here
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(username, password, database))

Session = sessionmaker()
session = Session()

state = session.query(State).first()
print("1. {}".format(state.name))
