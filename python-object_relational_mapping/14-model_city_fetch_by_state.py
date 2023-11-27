#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create engine to connect to the MySQL database,
    # using credentials passed as command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the database (from models inherited from Base)
    Base.metadata.create_all(engine)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session to interact with the database
    session = Session()

    # Query to join State and City tables,
    # then select state name, city id, and city name
    cities = session.query(State.name, City.id, City.name)\
        .join(City, State.id == City.state_id)

    # Iterate through the query results and print each city's details
    for state_name, city_id, city_name in cities:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    # Commit any changes to the database
    session.commit()

    # Close the session to release resources
    session.close()
