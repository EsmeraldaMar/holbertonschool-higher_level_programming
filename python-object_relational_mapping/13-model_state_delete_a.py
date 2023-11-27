#!/usr/bin/python3
"""
script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa
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
    result = session.query(State).filter(State.name.like('%a%')).all()

    # Deletes query results
    for state in result:
        session.delete(state)

    # Add the changes to database
    session.commit()
    # Close the session
    session.close()
