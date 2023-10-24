#!/usr/bin/python3
"""
Script that lists all states from the database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    # Establish a connection to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor to interact with the database
    cursor = db.cursor()

    # Execute an SQL query to retrieve all states
    cursor.execute("SELECT * FROM states")

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up resources
    cursor.close()
    db.close()


