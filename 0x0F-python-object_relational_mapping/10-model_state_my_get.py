#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa
that have a name matching the specified name
provided as a command-line argument.
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Create a SQLAlchemy engine for the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Initialize a flag to check if any matching State objects are found
    flag = 0

    # Query and print State objects with a name
    # that matches the specified name
    for state in session.query(State).filter_by(name=argv[4]).order_by(State.id).all():
        print("{}".format(state.id))
        flag = 1

    # Check if any matching State objects were found
    # and print "Not found" if none were found
    if flag != 1:
        print("Not found")

    # Close the session
    session.close()
