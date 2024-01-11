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
    cursor.execute("SELECT * from states WHERE name = %s\
                   ORDER BY id ASC", [word])
    rows = cursor.fetchall()

    for state in rows:
        print(state)
    cursor.close()
    db.close()
