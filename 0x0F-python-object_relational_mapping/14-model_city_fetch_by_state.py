#!/usr/bin/python3
'''
Lists all Cities objects from the database
'''
from model_state import Base, State
from model_city import City
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
    cities = sa.Table('cities', metadata, autoload=True, autoload_with=engine)
    query = sa.select([cities.c.id, cities.c.name, states.c.name]).\
        where(cities.c.state_id == states.c.id)

    ResultProxy = conn.execute(query)
    ResultSet = ResultProxy.fetchall()

    for city in ResultSet:
        print("{}: ({}) {}".format(city[2], city[0], city[1]))
