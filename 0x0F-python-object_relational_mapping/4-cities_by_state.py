#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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

    # Execute SQL query to retrieve cities and sort by cities.id
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up resources
    cur.close()
    db.close()

