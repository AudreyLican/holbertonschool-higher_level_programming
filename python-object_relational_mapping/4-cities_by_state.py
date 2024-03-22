#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa.
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

    query = "SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC"

    with db.cursor() as cursor:
        cursor.execute(query)

    rows = cursor.fetchall()

    if rows is not None:
        for row in rows:
            print(row)

    # Close all cursors
    cursor.close()
    # Close all databases
    db.close()
