#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Create a SQLAlchemy engine for the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True) 
    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Query and print State objects containing
    # the letter 'a' in their name
    for state in session.query(State).order_by(State.id).all():
        for i in state.name:
            if i == 'a':
                print("{}: {}".format(state.id, state.name))
                break

    # Close the session
    session.close()
