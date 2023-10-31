#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# Define the State class
class State(Base):
    """Class that inherit from Base

    Attributes:
        id = The state id
        name = The state name

    """
    # Defines the table name in the database
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
