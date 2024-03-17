#!/usr/bin/python3
"""Lists of all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    co = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cu = co.cursor()
    cu.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cu.fetchall()
    for row in query_rows:
        print(row)
    cu.close()
    co.close()
