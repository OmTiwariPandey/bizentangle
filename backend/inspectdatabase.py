import sqlite3

def inspect_db():
    # Connect to the SQLite database
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    # List all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)

    # Query each table
    for table_name in tables:
        print(f"\nData in table '{table_name[0]}':")
        cursor.execute(f"SELECT * FROM {table_name[0]} LIMIT 10;")  # Limit to first 10 rows
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    inspect_db()
