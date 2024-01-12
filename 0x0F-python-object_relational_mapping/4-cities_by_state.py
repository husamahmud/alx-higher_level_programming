#!/usr/bin/python3
"""takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3])

    cursor = connection.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM cities, states
                      WHERE cities.id = states.id""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
