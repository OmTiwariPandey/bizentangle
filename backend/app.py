import sqlite3

def get_top_selling_products():
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()

    # SQL query to join Sales with Inventory and get product name and ID
    query = """
    SELECT 
        Sales.Product_ID, 
        Inventory.Product_Name, 
        SUM(Sales.Total_Sales) AS TotalRevenue
    FROM Sales
    INNER JOIN Inventory
    ON Sales.Product_ID = Inventory.Product_ID
    GROUP BY Sales.Product_ID, Inventory.Product_Name
    ORDER BY TotalRevenue DESC
    LIMIT 5
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def get_inventory_status():
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()
    query = """
    SELECT Product_ID, Product_Name, Stock_Level, Reorder_Level
    FROM Inventory
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def get_sales_trends():
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()
    query = """
    SELECT Date, SUM(Total_Sales) as TotalSales
    FROM Sales
    GROUP BY Date
    ORDER BY Date ASC
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    print("Top Selling Products:", get_top_selling_products())
    print("Inventory Status:", get_inventory_status())
    print("Sales Trends:", get_sales_trends())
