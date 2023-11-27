#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

# Code should not be executed when imported
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
# The database connection details are formatted from the command line arguments
# Create all tables in the database which are defined by Base's subclasses such as State
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance to handle transactions
    session = Session()

    # Query the State table and order by the id of the state
    result = session.query(State).order_by(State.id)

    # Iterate through each row in the query result and print the state id and name
    for instance in result:
        print("{}: {}".format(instance.id, instance.name))

    # Close the session to release the connection
    session.close()
