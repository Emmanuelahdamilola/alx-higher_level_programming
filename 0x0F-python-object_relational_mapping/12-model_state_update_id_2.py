#!/usr/bin/python3
"""
This script changes the name of a State object in the database hbtn_0e_6_usa.
"""

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

    # Query and update the name of a State object with id=2
    for state in session.query(State).filter_by(id=2).order_by(State.id).all():
        state.name = "New Mexico"

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

