#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa,.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_db,
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute SQL query to select states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
        cursor.execute(query)

        # Fetch all results
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.OperationalError as e:
        print(f"❌ Connection error: {e}")
