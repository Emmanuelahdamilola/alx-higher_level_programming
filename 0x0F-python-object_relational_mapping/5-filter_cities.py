#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.

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

    # Execute SQL query to retrieve cities of the specified state and sort by cities.id
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities " \
                "JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s", [argv[4]])

    # Fetch and print the results
    query_rows = cursor.fetchall()
    print(", ".join([row[0] for row in query_rows]))

    # Clean up resources
    cursor.close()
    connection.close()

