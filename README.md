# 🧾 Inventory Management System (CLI - Python)

## 📌 Description

This project is a **command-line inventory management system** developed in Python.
It allows users to manage products, control stock, generate reports, and perform searches using a CSV file as a database.

The system is designed to simulate a real inventory workflow with features like:

* Product creation
* Stock control
* CSV persistence
* Inventory analytics

---

## 🚀 Features

### 📦 Product Management

* Add new products
* Edit existing products
* Delete products (logical deletion using status)
* Search products by:

  * Name
  * Category
  * Price
  * Stock
  * ID

### 📊 Inventory Control

* Show all available products
* Filter active products with stock
* Stock alerts:

  * 🔴 Zero stock
  * 🟡 Low stock (≤ 50)

### 📈 Statistics & Reports

* Calculate:

  * Total inventory value
  * Total number of products
  * Total stock
* Generate CSV report:

  * `final_report.csv`

### 💾 Data Persistence

* Load inventory from CSV (`inventario.csv`)
* Automatically update CSV on changes
* Append new products without deleting previous data

---

## 🛠️ Technologies Used

* Python 3
* CSV (as database)
* Standard libraries:

  * `csv`
  * `os`

---

## 📁 Project Structure

```
📦 project/
├── main.py
├── gestion_productos.py
├── operaciones_inventario.py
├── inventario.csv
└── final_report.csv (generated)
```

---

## ⚙️ How It Works

The system uses a dictionary structure like:

```python
inventory = {
    1: {
        "name": "Product Name",
        "price": 10.5,
        "stock": 20,
        "category": ["Food", "Snacks"],
        "status": True
    }
}
```

---

## ▶️ How to Run

1. Make sure you have Python installed
2. Place all files in the same folder
3. Run the main script:

```bash
python main.py
```

---

## 🧭 Menu Options

```
1. Add Product
2. Show Inventory
3. Edit Product
4. Delete Product
5. Search Product
6. Stock Alerts
7. Calculate Statistics
8. Exit
```

---

## 📌 Key Functions

### 🔍 `search_product()`

Search products dynamically using multiple fields.

### 📊 `calculate_statistics()`

Calculates inventory metrics and generates CSV report.

### ⚠️ `stock_alerts()`

Displays:

* Products with zero stock
* Products with low stock

### 📦 `add_product()`

Interactive product creation with validations.

### ✏️ `edit_product()`

Allows editing:

* Name
* Price
* Category
* Stock

---

## 🧪 Validations Included

* Empty fields
* Negative values
* Duplicate categories
* Invalid menu options
* Non-numeric input

---

## 📄 CSV Format

### `inventario.csv`

```
id,name,price,stock,category,status
1,Milk,2.5,10,Dairy Products,True
```

Categories are stored as:

```
Food|Snacks|Beverages
```

---

## 🎯 Highlights

* Clean CLI interface with colored output 🎨
* Modular design (separated logic)
* Real-world inventory simulation
* CSV-based persistence (no database required)

---

## 🔮 Possible Improvements

* Add graphical interface (GUI)
* Use a real database (SQLite / PostgreSQL)
* Add user authentication
* Export reports to Excel
* Implement product categories management

---

## 👨‍💻 Author

Developed as a Python practice project focused on:

* Logic building
* Data structures
* File handling
* Real-world problem solving

---

## 📜 License

This project is free to use for educational purposes.
