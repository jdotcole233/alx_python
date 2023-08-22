#! /usr/bin/python3
# Some comments goes here
# Some more comments goes here
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(username, password, database))

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()
counter = 1
for state in states:
    print("{}: {}".format(counter, state.name))
    counter = counter + 1
