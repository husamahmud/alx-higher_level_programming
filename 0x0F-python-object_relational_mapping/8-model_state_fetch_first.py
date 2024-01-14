#!/usr/bin/python3
"""lists first State objects from the database hbtn_0e_6_usa
"""


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
    record = session.query(State).order_by(State.id).first()
    if record:
        print(f"{record.id}: {record.name}")
    else:
        print("Nothing")
