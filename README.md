# Sales and Inventory Analytics

This is a Python-based project that uses **Tkinter** for the GUI and **SQLite** for managing sales and inventory data. The project analyzes sales trends, inventory levels, and top-selling products, displaying the results in an interactive desktop application.

## Features
- View **Top-Selling Products** (Product ID, Name, and Revenue).
- Monitor **Inventory Status** (Stock Levels and Reorder Levels).
- Track **Sales Trends** over time.

## File Structure
```
project-root/
│
├── data/                      # Mock data for the application
│   ├── sales.csv              # Sales data
│   ├── inventory.csv          # Inventory data
│   └── pos.csv                # POS data
│
├── backend/                   # Backend logic
│   ├── app.py                 # Core logic for data processing and analytics
│   └── database.py            # SQLite connection and initialization
│
├── gui/                       # GUI components for the application
│   └── main.py                # Main entry point for the Tkinter app
│
├── analytics.db               # SQLite database file (generated at runtime)
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and instructions
```

## Prerequisites
- **Python 3.8+** installed.
- Basic understanding of Python and Tkinter.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/OmTiwariPandey/bizentangle.git
cd bizentangle
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare the SQLite Database
1. Edit the mock data files (`sales.csv`, `inventory.csv`, and `pos.csv`) present in the `data/` folder.
2. Run the database initialization script:
```bash
python backend/database.py
```
This will:
- Create `analytics.db` in the project root by running backend/database.py.

### 5. Run the Application
To launch the Tkinter GUI:
```bash
python gui/main.py
```

## How to Use
1. **Top-Selling Products**: Displays the top 5 products by revenue, showing both their IDs and names.
2. **Inventory Status**: Displays current stock levels and reorder levels for all products.
3. **Sales Trends**: Displays total sales grouped by date.

## Sample Data
### `sales.csv`
```csv
Date,Product_ID,Quantity_Sold,Price,Total_Sales
2025-01-01,P001,5,20,100
2025-01-01,P002,3,15,45
2025-01-01,P003,2,50,100
2025-01-02,P001,7,20,140
```

### `inventory.csv`
```csv
Product_ID,Product_Name,Stock_Level,Reorder_Level
P001,Wireless Mouse,50,10
P002,USB Keyboard,30,5
P003,27-inch Monitor,20,5
```

### `pos.csv`
```csv
Transaction_ID,Product_ID,Quantity,Transaction_Date,Amount
T001,P001,2,2025-01-01,40
T002,P002,1,2025-01-01,15
T003,P003,1,2025-01-01,50
```

## Additional Notes
- The database (`analytics.db`) will be overwritten each time `backend/database.py` is run.
- Ensure the `data/` folder contains the correct CSV files before initializing the database.


---
Feel free to contact Om, the team leader of The Saturated for any queries or suggestions.
