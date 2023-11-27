#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    # Create new state
    new_state = State(name="Louisiana")
    session.add(new_state)

    result = session.query(State).filter(State.name == "Louisiana")\
        .order_by(State.id.desc()).first()

    if result:
        print(result.id)
    # add changes to add new state
    session.commit()
    # Close the session
    session.close()
