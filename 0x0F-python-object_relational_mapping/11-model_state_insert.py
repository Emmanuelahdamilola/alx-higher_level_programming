#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa and adds a new State object named "Louisiana" to the database.
"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import update

if __name__ == "__main__":
    # Create a SQLAlchemy engine for the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")
    
    # Add the new State object to the database and commit the transaction
    session.add(new_state)
    session.commit()

    # Query and print the State object with the name "Louisiana"
    for state in session.query(State).filter_by(name="Louisiana").order_by(State.id).all():
        print("{}".format(state.id))

    # Close the session
    session.close()
