#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of that
state."""
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
                      FROM cities
                      JOIN states ON cities.state_id = states.id""")

    rows = cursor.fetchall()
    for row in rows:
        if row[2] == argv[4]:
            print(row)

    cursor.close()
    connection.close()
