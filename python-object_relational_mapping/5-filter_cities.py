#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
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

    query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %(state_name)s
        ORDER BY cities.id ASC"""

    with db.cursor() as cursor:
        cursor.execute(query, {'state_name': argv[4]})

    rows = cursor.fetchall()

    if rows is not None:
        # Print the names of the cities separated by commas
        print(", ".join([row[1] for row in rows]))

    # Close all cursors
    cursor.close()
    # Close all databases
    db.close()
