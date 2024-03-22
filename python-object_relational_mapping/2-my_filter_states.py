#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",   # Host name to DB server
        user=argv[1],       # Username passed in argument
        port=3306,          # Port number of the DB server
        passwd=argv[2],     # Pwd passed in argument
        db=argv[3]
        )         # DataBase passe in argument

    # create cursor object associated to query, to acts as a pointer
    # or iterator that allows us to traverse the result
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
            states.id ASC"

    cur.execute(query.format(argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
