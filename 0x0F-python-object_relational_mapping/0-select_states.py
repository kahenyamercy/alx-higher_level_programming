#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server using command-line arguments
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor
    c = db.cursor()

    # Execute the SQL query to retrieve all states
    c.execute("SELECT * FROM `states`")

    # Use list comprehension to print each state
    [print(state) for state in c.fetchall()]

    # The cursor and database connection will be closed when the script exits
