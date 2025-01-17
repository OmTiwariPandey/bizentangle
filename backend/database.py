import sqlite3
import pandas as pd

def load_data_to_db():
    # Connect to SQLite database (creates `analytics.db` if it doesn't exist)
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sales (
        Date TEXT,
        Product_ID TEXT,
        Quantity_Sold INTEGER,
        Price REAL,
        Total_Sales REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
        Product_ID TEXT,
        Product_Name TEXT,
        Stock_Level INTEGER,
        Reorder_Level INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS POS (
        Transaction_ID TEXT,
        Product_ID TEXT,
        Quantity INTEGER,
        Transaction_Date TEXT,
        Amount REAL
    )
    """)

    # Load data from CSV files
    sales = pd.read_csv("data/sales.csv")
    inventory = pd.read_csv("data/inventory.csv")
    pos = pd.read_csv("data/pos.csv")

    # Insert data into tables
    sales.to_sql("Sales", conn, if_exists="replace", index=False)
    inventory.to_sql("Inventory", conn, if_exists="replace", index=False)
    pos.to_sql("POS", conn, if_exists="replace", index=False)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_data_to_db()
    print("Database initialized and data loaded successfully.")
