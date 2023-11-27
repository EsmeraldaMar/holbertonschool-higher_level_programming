#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

"""
import MySQLdb
import sys

# Code should not be executed when imported
if __name__ == "__main__":

    # Makes a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # creates cursor to execute query
    cursor = db.cursor()
    # tuple for parametres
    search_name = sys.argv[4]
    # injection free query
    query = """SELECT cities.name FROM states\
        JOIN cities ON states.id = cities.state_id WHERE states.name = %s\
            ORDER BY cities.id ASC;"""
    # execute query with parameters as a tuple
    cursor.execute(query, (search_name,))
    # fetch rows returned by query
    rows = cursor.fetchall()
    # empty tuple to hold row values
    cities_list = ()
    # Iterate and print rows
    for i in rows:
        cities_list = cities_list + i
    # join row values into comma separated string
    cities_string = ', '.join(cities_list)
    # print string of row values
    print(cities_string)
    # close cursor and database connection
    cursor.close()
    db.close()
