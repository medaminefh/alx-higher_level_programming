#!/usr/bin/python3
"""
first module using MySQL
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    word = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, database=db)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name from cities JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name = %s ORDER BY cities.id ASC", (word,))
    rows = cursor.fetchall()
    cities = list(row[0] for row in rows)
    print(*cities, sep=", ")
    cursor.close()
    db.close()
