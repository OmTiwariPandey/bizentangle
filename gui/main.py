import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from backend.app import get_top_selling_products, get_inventory_status, get_sales_trends

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales and Inventory Analytics")
        self.root.geometry("800x600")

        # Title Label
        ttk.Label(self.root, text="Sales and Inventory Dashboard", font=("Arial", 20)).pack(pady=10)

        # Frame for displaying data
        self.display_frame = ttk.Frame(self.root)
        self.display_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Buttons for Analytics
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Top-Selling Products", command=self.show_top_selling).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Inventory Status", command=self.show_inventory_status).grid(row=0, column=1, padx=10)
        ttk.Button(button_frame, text="Sales Trends", command=self.show_sales_trends).grid(row=0, column=2, padx=10)

    def clear_display(self):
        # Clear the current display frame
        for widget in self.display_frame.winfo_children():
            widget.destroy()

    def create_table(self, columns, data):
        # Create a Treeview widget to display tabular data
        tree = ttk.Treeview(self.display_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER)

        for row in data:
            tree.insert("", tk.END, values=row)

        tree.pack(fill=tk.BOTH, expand=True)

    def show_top_selling(self):
        self.clear_display()
        data = get_top_selling_products()
        columns = ["Product ID", "Product Name", "Total Revenue"]
        self.create_table(columns, data)



    def show_inventory_status(self):
        self.clear_display()
        data = get_inventory_status()
        columns = ["Product ID", "Product Name", "Stock Level", "Reorder Level"]
        self.create_table(columns, data)

    def show_sales_trends(self):
        self.clear_display()
        data = get_sales_trends()
        columns = ["Date", "Total Sales"]
        self.create_table(columns, data)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
