#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' from hbtn_0e_0_usa
"""
import MySQLdb
import sys

# Code should not be executed when imported
if __name__ == "__main__":

    # Makes a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Gives us the ability to have multiple separate working environments
    # through the same connection to the database
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name\
                   LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()
    for i in rows:
        print(i)
    # Clean up Process
    cursor.close()
    db.close()
