#! /usr/bin/python3
# Some comments that goes here
# Some additional comments
# More
import MySQLdb
import sys

host = "localhost"
port = 3306
user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db_connect = MySQLdb.connect(
    host=host, user=user, passwd=password, db=database, port=port)

cursor = db_connect.cursor()
statement = """
    SELECT cities.id, cities.name, states.name FROM cities
    JOIN states on cities.state_id=states.id
"""

cursor.execute(statement)
results = cursor.fetchall()

for result in results:
    print(result)
