#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa."""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3],
                                 port=3306)

    cursor = connection.cursor()
    query = "SELECT name FROM cities"
    cursor.execute(query)

    rows = cursor.fetchall()
    res = []
    for row in rows:
        if row[0] == argv[4]:
            res.append(row[0])
    print(", ".join(res))

    cursor.close()
    connection.close()
