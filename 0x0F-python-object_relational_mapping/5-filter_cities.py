#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                    LEFT JOIN states
                        ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""",
                (args[4],))
    query_rows = cur.fetchall()
    li = []
    for row in query_rows:
        li.append(row[0])
    print(", ".join(li))
    cur.close()
    conn.close()
