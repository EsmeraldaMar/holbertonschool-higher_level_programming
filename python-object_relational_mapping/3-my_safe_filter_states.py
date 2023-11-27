#!/usr/bin/python3
"""
Script that takes in an argument and displays all (mySQL inj)
values in the states table of hbtn_0e_0_usa where name matches the argument.

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
    # creates cursor to execute query
    cursor = db.cursor()
    # tuple for parametres
    search_name = sys.argv[4]
    # execute query
    cursor.execute("SELECT * FROM states WHERE BINARY name\
                    LIKE %s ORDER BY id ASC;", (search_name,))
    # fetch rpows returned by query
    rows = cursor.fetchall()
    # Iterate and print rows
    for i in rows:
        print(i)
    # Clean up Process, close cursor and db connection
    cursor.close()
    db.close()
