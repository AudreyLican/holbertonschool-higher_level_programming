#!/usr/bin/python3
"""
Listing all states in DB hbtn_0e_0-_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
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

    # Execute SQL query, to fecth rows from result set in the table "states"
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Process data
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
