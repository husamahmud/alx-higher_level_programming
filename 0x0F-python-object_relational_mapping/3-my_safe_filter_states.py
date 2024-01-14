#!/usr/bin/python3
"""Once again, write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name
matches the argument. But this time, write one that is safe
from MySQL injections!"""


import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == args[4]:
            print(row)
    cur.close()
    conn.close()
