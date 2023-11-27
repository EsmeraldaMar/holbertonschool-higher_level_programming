#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
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
    # Create session
    session = Session()

    state_to_update = session.query(State).get(2)
    # Check if the state exists and then update its name
    if state_to_update:
        state_to_update.name = "New Mexico"

    # add changes to add new state
    session.commit()
    # Close the session
    session.close()
