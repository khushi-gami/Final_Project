# 📊 Retail Sales Data Analyzer

A Python-based **Retail Sales Data Analyzer** that allows users to load sales data from CSV files, perform data analysis, filter records, calculate important business metrics, and visualize sales performance using charts.

This project uses **Object-Oriented Programming (OOP)** along with NumPy, Pandas, Matplotlib, and Seaborn libraries to demonstrate practical data analysis concepts.

---

## 🚀 Features

### 1. Load Sales Data
- Accepts a CSV file from the user.
- Checks whether the specified file exists.
- Validates the CSV file extension.
- Handles empty CSV files.
- Loads data into a Pandas DataFrame.
- Displays the total number of rows and columns.
- Shows the first five records using `head()`.

### 2. Sales Data Analysis
Calculates important sales metrics, including:
- Total sales using `sum()`.
- Average sales using `mean()`.
- Most popular product based on total quantity sold.
- Removes missing values using `dropna()`.
- Removes duplicate records using `drop_duplicates()`.

### 3. Filter Sales Data
Allows users to filter sales records based on:
- Product name.
- Product category.
- Start date.
- End date.

Uses Pandas filtering and Boolean indexing to retrieve matching records without modifying the original DataFrame.

### 4. Data Visualization
Generates graphical representations of sales data using Matplotlib.

**Available Charts:**
- **Bar Chart:** Displays total sales by product category.
- **Line Chart:** Displays sales trends over time.

### 5. Sales Summary
Provides an overall overview of the sales dataset, including:
- Total number of records.
- Number of unique products.
- Number of unique categories.
- Total sales.
- Average sales.
- Most popular product.
- Top-performing category.
- Sales date range.

### 6. Data Aggregation
Groups sales records using Pandas `groupby()` and calculates total quantities and sales.

**Available Aggregations:**
- Product-wise sales summary.
- Category-wise sales summary.
- Date-wise sales summary.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical computing |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical data visualization library |
| OS | File existence and path handling |

---

## 🧠 Python Concepts Implemented

- Object-Oriented Programming (OOP).
- Classes and Objects.
- Constructor (`__init__`).
- Instance attributes (`self.data`).
- Encapsulation.
- Functions and Methods.
- Conditional Statements.
- While Loops.
- Exception Handling (`try-except`).
- File Handling and Validation.
- List and DataFrame operations.
- Data Cleaning.
- Data Aggregation.
- Boolean Indexing.

---

## 📂 Project Structure

```text
Retail-Sales-Data-Analyzer/
│
├── main.py
│
├── sales_data.csv
│
└── README.md
```

**File Description:**

- `main.py` – Contains the RetailAnalyzer class, data loading, cleaning, filtering, analysis, aggregation, visualization, and menu-driven program.
- `sales_data.csv` – Contains the retail sales dataset.
- `README.md` – Project documentation.

---

## 📋 CSV Dataset Format

The program expects a CSV file containing the following columns:

| Column | Description |
|---|---|
| Product | Name of the product |
| Category | Product category |
| Date | Date of the transaction |
| Quantity | Quantity of products sold |
| Total | Total sales amount |

**Sample Dataset:**

```csv
Product,Category,Date,Quantity,Total
Laptop,Electronics,2026-01-01,2,100000
Mobile,Electronics,2026-01-02,5,75000
Chair,Furniture,2026-01-03,3,15000
Table,Furniture,2026-01-04,2,20000
Headphones,Electronics,2026-01-05,4,12000
Laptop,Electronics,2026-01-06,1,50000
```

---

## 💻 Application Menu

After executing the program, the following menu appears:

```text
======================= Retail Sales Data Analyzer ===============================

Choose an operation:

1. Load Data
2. Show Data Analysis
3. Filter Data
4. Visualize Data
5. Show Summary
6. Aggregate Data
7. Exit

Enter a choice (1 to 7):
```

### Example Operations

1. Select **Load Data** and enter your CSV filename.
2. Select **Show Data Analysis** to calculate total sales, average sales, and the most popular product.
3. Select **Filter Data** to filter records by product, category, or date range.
4. Select **Visualize Data** to generate sales charts.
5. Select **Show Summary** to view overall sales statistics.
6. Select **Aggregate Data** to generate product-wise, category-wise, and date-wise summaries.
7. Select **Exit** to close the application.

---

## 📈 Learning Outcomes

Through this project, I practiced and implemented:

- Reading and processing CSV files using Pandas.
- Working with DataFrames and Series.
- Cleaning datasets by handling missing and duplicate records.
- Performing numerical calculations and statistical analysis.
- Applying grouping and aggregation operations.
- Filtering datasets using multiple conditions.
- Converting string dates into Pandas datetime objects.
- Creating bar charts and line charts.
- Implementing OOP concepts in a practical data analysis project.
- Building a menu-driven Python application.

---

## 🔮 Future Improvements

- Add interactive visualizations using Plotly.
- Integrate Seaborn for advanced statistical charts.
- Add monthly, quarterly, and yearly sales reports.
- Implement category-wise and product-wise comparisons.
- Export filtered and analyzed data into CSV and Excel files.
- Add a graphical user interface (GUI).
- Improve data validation and error handling.

---

**Developed as a Python Data Analysis Project**

This project demonstrates the practical implementation of Python, Object-Oriented Programming, NumPy, Pandas, and data visualization techniques in a retail sales analysis application.
