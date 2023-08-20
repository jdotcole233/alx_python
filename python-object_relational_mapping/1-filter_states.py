"""filter states with name starting from N from db"""
#! /usr/bin/python3

import MySQLdb
import sys

# Some comments that goes here

host = "localhost"
port = 3306
user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]


db_connect = MySQLdb.connect(
    host=host, user=user, passwd=password, db=database, port=port)

cursor = db_connect.cursor()
statement = """
    SELECT * FROM states WHERE name Like 'N%'
"""

cursor.execute(statement)
results = cursor.fetchall()

for result in results:
    print(result)
    