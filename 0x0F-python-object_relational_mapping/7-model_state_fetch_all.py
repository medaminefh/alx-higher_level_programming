#!/usr/bin/python3
"""
first module using MySQL
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, db))
    session = sessionmaker(bind=engine)()
    for state in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
