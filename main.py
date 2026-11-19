import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(
    "\n ======================= Retail Sales Data Analyzer ==============================="
)


def int_input(message, minimum, maximum):
    while True:
        try:
            number = int(input(message))
            if minimum <= number <= maximum:
                return number

            print(f"Please enter a number between {minimum} and {maximum}.\n")

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


def text_input(message):
    while True:
        text = input(message).strip()
        if text == "":
            print("This field cannot be empty.")
            print()
        else:
            return text


class RetailAnalyzer:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):

        try:

            if not os.path.exists(file_path):
                print("file not found !")

            elif not file_path.lower().endswith(".csv"):
                print("please enter csv file !")

            else:
                data = pd.read_csv(file_path)

                if data.empty:
                    print("file is empty!")
                    return

                self.data = data

                print("\n data loaded succesfully")

                print("\ntotal rows : ", self.data.shape[0])
                print("total columns : ", self.data.shape[1])
                print("\n first 5 rowes :\n", self.data.head(5))

        except FileNotFoundError as e:
            print("file not exist !", e)

        except FileExistsError as e:
            print("file not exist !", e)

        except pd.errors.EmptyDataError:
            print("file is empty!")

    def aggregation(self):
        if self.data is None:
            print("Please load a CSV file first.")
            return

        required_columns = ["Product", "Category", "Date", "Quantity", "Total"]
        for column in required_columns:
            if column not in self.data.columns:
                print("CSV is missing the required column:", column)
                return

        data = self.data.copy()
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
        data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
        data["Total"] = pd.to_numeric(data["Total"], errors="coerce")
        data = data.dropna(subset=["Product", "Category", "Date"])

        if data.empty:
            print("No data available for aggregation.")
            return

        product_summary = data.groupby("Product")[["Quantity", "Total"]].sum()
        category_summary = data.groupby("Category")[["Quantity", "Total"]].sum()
        date_summary = data.groupby("Date")[["Quantity", "Total"]].sum()

        print("\nSales grouped by product:")
        print(product_summary)

        print("\nSales grouped by category:")
        print(category_summary)

        print("\nSales grouped by date:")
        print(date_summary)

    def calculate_metries(self):

        if self.data is None:
            print("Please load a CSV file first.")
            return

        print(self.data.columns)

        # remove missing and duplicate data's rows
        self.data = self.data.dropna()
        self.data = self.data.drop_duplicates()

        if self.data.empty:
            print("No data available after removing missing and duplicate rows.")
            return

        # calaculate total ,average , popular product
        total_sales = self.data["Total"].sum()
        average_sales = self.data["Total"].mean()
        product_quantities = self.data.groupby("Product")["Quantity"].sum()
        most_popular_product = product_quantities.idxmax()

        print("\nTotal sales of product : ", total_sales)
        print("\nAverage sales of product : ", average_sales)
        print(f"\nMost popular product : {most_popular_product} ")

    def filter_data(self):
        if self.data is None:
            print("Please load a CSV file first.")
            return

        # for unchanged original data
        filtered_data = self.data.copy()

        product = input("Enter product (for skip --> Enter): ").strip()
        if product:
            filtered_data = filtered_data[filtered_data["Product"] == product]

        category = input("Enter category (for skip --> Enter): ").strip()
        if category:
            filtered_data = filtered_data[filtered_data["Category"] == category]

        start_date = input("Enter start date YYYY-MM-DD (or press Enter to skip): ")
        end_date = input("Enter end date YYYY-MM-DD (or press Enter to skip): ")

        try:
            if start_date:
                start_date = pd.to_datetime(start_date)
                dates = pd.to_datetime(filtered_data["Date"])
                filtered_data = filtered_data[dates >= start_date]

            if end_date:
                end_date = pd.to_datetime(end_date)
                dates = pd.to_datetime(filtered_data["Date"])
                filtered_data = filtered_data[dates <= end_date]
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")
            return

        if filtered_data.empty:
            print("No rows matched the selected filters.")
            return

        print("\nFiltered data:")
        print(filtered_data)

    def visualize_data(self):
        if self.data is None:
            print("Please load a CSV file first.")
            return

        required_columns = ["Date", "Category", "Total"]
        for column in required_columns:
            if column not in self.data.columns:
                print("CSV is missing the required column:", column)
                return

        data = self.data.copy()
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
        data["Total"] = pd.to_numeric(data["Total"], errors="coerce")
        data = data.dropna(subset=["Date", "Category", "Total"])

        if data.empty:
            print("No valid data available to create charts.")
            return

        category_sales = data.groupby("Category")["Total"].sum()

        plt.figure(figsize=(8, 5))
        category_sales.plot(kind="bar", color="skyblue")
        plt.title("Total Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.tight_layout()

        daily_sales = data.groupby("Date")["Total"].sum().sort_index()

        plt.figure(figsize=(8, 5))
        daily_sales.plot(kind="line", marker="o", color="green")
        plt.title("Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.tight_layout()

        plt.show()

    def show_summary(self):
        if self.data is None:
            print("Please load a CSV file first.")
            return

        required_columns = ["Date", "Product", "Category", "Quantity", "Total"]
        for column in required_columns:
            if column not in self.data.columns:
                print("CSV is missing the required column:", column)
                return

        data = self.data.copy()
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
        data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
        data["Total"] = pd.to_numeric(data["Total"], errors="coerce")

        print("\n===== Sales Summary =====")
        print("Number of records:", len(data))
        print("Number of products:", data["Product"].nunique())
        print("Number of categories:", data["Category"].nunique())

        if data["Total"].notna().any():
            print("Total sales:", data["Total"].sum())
            print("Average sale:", round(data["Total"].mean(), 2))
        else:
            print("Sales totals are not available.")

        product_data = data.dropna(subset=["Product", "Quantity"])
        if not product_data.empty:
            product_sales = product_data.groupby("Product")["Quantity"].sum()
            print("Most popular product:", product_sales.idxmax())
        else:
            print("Popular product not available.")

        category_data = data.dropna(subset=["Category", "Total"])
        if not category_data.empty:
            category_sales = category_data.groupby("Category")["Total"].sum()
            print("Top category by sales:", category_sales.idxmax())
        else:
            print("Top category not available.")

        valid_dates = data["Date"].dropna()
        if not valid_dates.empty:
            print("Date range:", valid_dates.min().date(), "to", valid_dates.max().date())
        else:
            print("Date range not available.")


analysis = RetailAnalyzer()

while True:

    print("Choose an operation : ")
    print("1. load data")
    print("2. show data analysis")
    print("3. filter data")
    print("4. visualize data")
    print("5. show summary")
    print("6. aggregate data")
    print("7. Exit")

    choice = int_input("\nEnter a choice (1 to 7) : ", 1, 7)

    if choice == 1:

        analysis.load_data(text_input("Enter file name : "))

    elif choice == 2:
        analysis.calculate_metries()

    elif choice == 3:
        analysis.filter_data()

    elif choice == 4:
        analysis.visualize_data()

    elif choice == 5:
        analysis.show_summary()

    elif choice == 6:
        analysis.aggregation()

    elif choice == 7:
        print("Goodbey.")

        break

    print("\n** choose another opton : ----------------------------\n")
