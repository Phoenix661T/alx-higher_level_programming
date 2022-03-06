#!/usr/bin/python3
'''
Changes the name of a State object
from the database
'''
from model_state import Base, State
import sys
import sqlalchemy as sa
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    conn = engine.connect()
    metadata = sa.MetaData()

    states = sa.Table('states', metadata, autoload=True, autoload_with=engine)

    query = sa.update(states).where(states.c.id == 2).values(name='New Mexico')
    ResultProxy = conn.execute(query)
