import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from utils import load_dataframe

# ------------------------------------------------------------
#               Pie Chart for Category Spending
# ------------------------------------------------------------

def plot_category_pie(data):
    category_stats = {}

    for item in data:
        cat = item["category"]
        amt = item["amount"]
        category_stats[cat] = category_stats.get(cat, 0) + amt

    labels = list(category_stats.keys())
    values = list(category_stats.values())

    plt.figure(figsize=(5, 5))
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.tight_layout()
    plt.savefig('charts/category.png')
    plt.show()

# ------------------------------------------------------------
#               Bar Chart for Monthly Spending
# ------------------------------------------------------------

def plot_monthly_bar(data):
    monthly_stats = {}

    for item in data:
        date_str = item["date"]
        day = datetime.strptime(date_str, "%Y-%m-%d")
        key = f"{day.year}-{day.month:02d}"

        monthly_stats[key] = monthly_stats.get(key, 0) + item["amount"]

    months = list(monthly_stats.keys())
    amounts = list(monthly_stats.values())

    plt.figure(figsize=(6, 4))
    plt.bar(months, amounts)
    plt.xticks(rotation=45)
    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig('charts/monthly.png')
    plt.show()

# ------------------------------------------------------------
#              Line Chart for Daily Spending
# ------------------------------------------------------------

def plot_daily_line(data):
    daily_stats = {}

    for item in data:
        day = datetime.strptime(item["date"], "%Y-%m-%d")
        date_key = day.strftime("%Y-%m-%d")

        daily_stats[date_key] = daily_stats.get(date_key, 0) + item["amount"]

    dates = list(daily_stats.keys())
    amounts = list(daily_stats.values())

    plt.figure(figsize=(6, 4))
    plt.plot(dates, amounts, marker="o")
    plt.xticks(rotation=45)
    plt.title("Daily Spending")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("charts/daily.png")
    plt.show()

#----------------------------------------------------------------------------
#                             Visualizations Menu
#----------------------------------------------------------------------------

def visualization_menu():
    print("=========================")
    print("       Visualize         ")
    print("=========================")
    print("1. Daily Summary")
    print("-------------------------")
    print("2. Monthly Summary")
    print("-------------------------")
    print("3. Category Summary")
    print("-------------------------")
    print("4. Exit")
    print("-------------------------")

    df = load_dataframe()
    df["date"] = df["date"].astype(str)
    data = df.to_dict(orient="records")
    try:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                plot_daily_line(data)
            case 2:
                plot_monthly_bar(data)
            case 3:
                plot_category_pie(data)
            case 4:
                print("Exiting...")
    except ValueError:
        print("Invalid choice. Enter a number from 1–4")