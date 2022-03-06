#!/usr/bin/python3
'''
lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
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
    query = sa.select([states])

    ResultProxy = conn.execute(query)
    ResultSet = ResultProxy.fetchall()

    for key, value in ResultSet:
        if 'a' in value:
            print("{}: {}".format(key, value))
