#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa."""
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                    argv[2],
                                                    argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).all()
    for item in res:
        print(f"{item.id}: {item.name}")

    session.close()
