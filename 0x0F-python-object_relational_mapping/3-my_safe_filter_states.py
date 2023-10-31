#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
"""
import MySQLdb
from sys import argv


# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Execute an SQL query to retrieve states that match the provided name
    # and also safe from SQL injection
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY id ASC", (argv[4],))

    rows = cur.fetchall()
    for i in rows:
        print(i)

    # Clean up process
    cur.close()
    db.close()
