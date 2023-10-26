#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main':

    # Establish a connection to the MySQL database
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],

    )

    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # # Execute SQL query to retrieve cities and sort by cities.id
    cursor.execute("SELECT * FROM cities ORDER BY cities.id")

    # Fetch and print the results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Clean up resources
    cursor.close()
    connection.close()

