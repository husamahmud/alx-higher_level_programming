from sys import argv
import MySQLdb

username = argv[1]
password = argv[2]
dbname = argv[3]

db = MySQLdb.connect(host='localhost', port=3306, user=username,
                     passwd=password, db='hbtn_0e_0_usa')

cursor = db.cursor()

query = "SELECT * FROM states ORDER BY id DESC"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
