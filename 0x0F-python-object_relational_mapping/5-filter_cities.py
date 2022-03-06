#!/usr/bin/python3
'''
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
'''
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()

    cur.execute("SELECT name FROM cities \
    WHERE cities.state_id = \
    (SELECT id FROM states WHERE name = %(name)s) \
    ORDER BY id ASC", {'name': sys.argv[4]})

    query_row = cur.fetchall()

    sep = ""
    for city in query_row:
        print(sep + str(*city), end="")
        sep = ", "

    print()

    cur.close()
    conn.close()
