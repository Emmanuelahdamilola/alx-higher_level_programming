#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor to interact with the database
    cur = db.cursor()

    # Execute an SQL query to retrieve all states and sort by states.id
    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up resources
    cur.close()
    db.close()
