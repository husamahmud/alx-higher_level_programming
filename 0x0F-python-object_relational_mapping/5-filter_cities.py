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
    cursor.execute("""SELECT cities.name
                    FROM cities
                    LEFT JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC""", (argv[4],))

    rows = cursor.fetchall()
    res = []
    for row in rows:
        res.append(row[0])
    print(", ".join(res))

    cursor.close()
    connection.close()
