#!/usr/bin/python3
"""Lists all states with a name starting with N from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) >= 4:
        # Connect to MySQL server using provided arguments
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        # Create a cursor
        cursor = db.cursor()

        # Execute the SQL query to retrieve states starting with 'N', sorted by states.id
        cursor.execute("""
        SELECT * FROM states
        WHERE name IS NOT NULL
        AND LEFT(CAST(name AS BINARY), 1) = 'N'
        ORDER BY states.id;
        """)

        # Fetch all the rows from the result set
        records = cursor.fetchall()

        # Display the results
        for record in records:
            print(record)

        # Close the cursor and database connection
        db.close()
