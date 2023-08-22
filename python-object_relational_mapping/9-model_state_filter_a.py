#! /usr/bin/python3
# Some comments goes here
# Some comments goes here
# Some comments goes here
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(username, password, database))

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()

for state in states:
    if 'a' in state.name:
        print("{}: {}".format(state.id, state.name))
