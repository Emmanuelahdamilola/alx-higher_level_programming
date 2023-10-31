#!/usr/bin/python3

"""
Script that takes a state name as an argument and displays all values
"""

import MySQLdb
from sys import argv


if __name__ == '__main':

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to interact with the database
    cur = db.cursor()

    # Execute an SQL query to retrieve states that match the provided name
    query = "SELECT * FROM states WHERE name=s%\
            ORDER BY ASC", (argv[4])
    cur.execute(query)

    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up resources
    cur.close()
    db.close()
