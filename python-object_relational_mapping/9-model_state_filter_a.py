#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
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

    # Query for states containing the letter 'a', sorted by id
    result = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in result:
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()
