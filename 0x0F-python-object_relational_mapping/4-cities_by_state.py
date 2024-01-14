#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                    LEFT JOIN states
                        ON cities.state_id = states.id
                ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
