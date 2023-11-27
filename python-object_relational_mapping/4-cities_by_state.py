#!/usr/bin/python3
"""
Script that lists all cities from database hbtn_0e_4_usa
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
    # execute query
    # Selected merged both tables and commonality is 
    # cities.state_id and states.id
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   LEFT JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id ASC;")
    # fetch rows returned by query
    rows = cursor.fetchall()
    # Iterate and print rows
    for i in rows:
        print(i)
    # Clean up Process, close cursor and db connection
    cursor.close()
    db.close()
