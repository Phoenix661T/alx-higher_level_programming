#!/usr/bin/python3
'''
That creates the State “California” with
the City “San Francisco” from the database
'''
from relationship_state import Base, State
from relationship_city import City
import sys
import sqlalchemy as sa
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    conn = engine.connect()
    metadata = sa.MetaData()

    cities = sa.Table('cities', metadata, autoload=True, autoload_with=engine)
    states = sa.Table('states', metadata, autoload=True, autoload_with=engine)

    query = sa.insert(states).values(name='Louisiana', cities=[City(name="San Francisco")])

    ResultProxy = conn.execute(query)
