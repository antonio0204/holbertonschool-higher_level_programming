#!/usr/bin/python3
"""Start link class to table"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'. \
        format(argv[1], argv[2], argv[3])

    engine = create_engine(connect, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    for row in query:
        print("{}: {}".format(row.id, row.name))
