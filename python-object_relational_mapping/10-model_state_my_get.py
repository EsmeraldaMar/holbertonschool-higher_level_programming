#!/usr/bin/python3
"""
Script that prints state object with name passed
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Set up a session factory
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()
    # Query the first state object that
    # matches the name provided as a command-line argument
    result = session.query(State).filter(State.name == sys.argv[4]).first()

    if result:
        print(result.id)
    else:
        print("Not found")
    # Close the session
    session.close()
