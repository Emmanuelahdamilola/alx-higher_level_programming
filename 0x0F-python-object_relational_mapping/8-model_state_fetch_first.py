#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Create a SQLAlchemy engine for the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Query and print the first State object, ordered by their 'id' attribute
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()

