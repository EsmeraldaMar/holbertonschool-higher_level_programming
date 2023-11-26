#!/usr/bin/python3
"""
Script that lists all states from database hbtn_0e_0_usa
"""
import MySQLdb
import sys

# Code should not be executed when imported
if __name__ == "__main__":

    # Makes a connection to database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    #Gives us the ability to have multiple separate working environments through
    #the same connection to the database

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    # Clean Up process
    cursor.close()
    db.close()