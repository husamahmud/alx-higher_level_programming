#!/usr/bin/python3
"""lists all states with a name starting with N from hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)

    cursor.close()
    db.close()
