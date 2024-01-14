#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""


import sys

from sqlalchemy.orm import sessionmaker
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # can use filter_by(name=sys.argv[4])
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
