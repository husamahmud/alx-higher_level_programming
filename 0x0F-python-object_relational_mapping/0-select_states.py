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
    cursor.execute("""SELECT * FROM states ORDER BY id ASC""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
