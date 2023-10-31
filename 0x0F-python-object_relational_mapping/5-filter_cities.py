#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities

"""

import MySQLdb
from sys import argv


if __name__ == '__main__':

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],

    )

    # Create a cursor to interact with the database
    cur = db.cursor()

    # Execute SQL query to retrieve cities of the specified
    # state and sort by cities.id
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    # Fetch and print the results
    rows = cur.fetchall()
    # Print each city name in a comma-separated format
    for row in rows:
        print(str(row[0]) + ", " + row[1])

    # Clean up resources
    cur.close()
    db.close()
