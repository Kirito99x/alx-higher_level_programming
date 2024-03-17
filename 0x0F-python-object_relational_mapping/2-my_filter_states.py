#!/usr/bin/python3
"""  lists all states of database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    co = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cu = co.cursor()
    cu.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    co.close()