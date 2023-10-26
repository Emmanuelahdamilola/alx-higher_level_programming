#!/usr/bin/python3
"""
Script that takes a state name as an argument and displays all values
in the 'states' table of 'hbtn_0e_0_usa' where the name matches the argument.
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
        charset="utf8"
    )

    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Execute an SQL query to retrieve states that match the provided name
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY id ASC".format(sys.argv[4]))

    # Fetch and print the results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Clean up resources
    cursor.close()
    connection.close()

