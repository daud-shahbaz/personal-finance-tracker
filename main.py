#----------------------------------------------------------------------------
#                          Importing Packages
#----------------------------------------------------------------------------

import json
from datetime import datetime as dt
from utils import load_data, save_data
from visualizations import visualization_menu
from analysis import export_to_csv, import_csv, analysis_menu
    
#----------------------------------------------------------------------------
#                            Adding a expense
#----------------------------------------------------------------------------

def add_expense():
    print("Adding expense...")

    loaded = load_data()

    try:
        amount = int(input("Enter the amount:"))
    except ValueError as e:
        print("Enter a valid integer", e)
        return
    
    category = input("Enter category: ")

    try:
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        date = dt(year, month, day).strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid dateinput. Please enter valid year, month, and day.")
        return

    note = input("Any notes you would like to add: ")

    expense = {
            "amount": amount,
            "category": category,
            "date":date,
            "note": note
    }
    
    loaded.append(expense)
    save_data(loaded)
    print("Expense Added successfully")

#----------------------------------------------------------------------------
#                          Viewing all expenses
#----------------------------------------------------------------------------

def view_expense():
    print("Viewing expense...")

    loaded = load_data()

    if not loaded:
        print("No expenses found")
        return

    print(f"\n{'Sr':<3} | {'Amount':<10} | {'Category':<13} | {'Date':<12} | Note")
    print("-" * 70)

    for i, exp in enumerate(loaded, start=1):
        note = str(exp.get('note', '')).replace('\n', ' ')
        print(f"{i:<3} | {exp['amount']:<10} | {exp['category']:<13} | {exp['date']:<12} | {note}")
    
    print("-" * 70 + "\n")

#----------------------------------------------------------------------------
#                          Showing main statisitcs
#----------------------------------------------------------------------------

def show_stats():
    print("Showing all statisitcs...")

    loaded = load_data()
    
    if not loaded:
        print("No expenses found")
        return
    
    print("==============================================================")
    print("               Overall Statistics of Expenses                ")
    print("==============================================================")
    print("--------------------------------------------------------------")
    print("Total Amount Spent: ", calculate_total(loaded))
    print("--------------------------------------------------------------")
    print("Total Amount Spent by Category:")
    category_data = category_summary(loaded)
    for category, amount in category_data.items():
        print(f"  {category}: {amount}")
    print("--------------------------------------------------------------")
    print("Total Amount Spent per month:")
    monthly_data = monthly_spending(loaded)
    for month, amount in monthly_data.items():
        print(f"  {month}: {amount}")
    print("--------------------------------------------------------------")


#----------------------------------------------------------------------------
#                        Calculating total expenses
#----------------------------------------------------------------------------

def calculate_total(data):
    total_amount = 0
    for i in data:
        total_amount += i['amount']
    return total_amount

#----------------------------------------------------------------------------
#                         Expenses by Category
#----------------------------------------------------------------------------

def category_summary(data):
    category_stats= {}

    for i in data:
        category = i["category"]
        amount = i["amount"]
        category_stats[category] = category_stats.get(category, 0) + amount
    
    return category_stats

#----------------------------------------------------------------------------
#                            Monthly Expenses
#----------------------------------------------------------------------------

def monthly_spending(data):
    monthly_spent = {}

    for i in data:
        ymd = dt.strptime(i["date"], "%Y-%m-%d")

        year = ymd.year
        month = ymd.month

        ym = f"{year}-{month:02d}"

        amount = i["amount"]
        monthly_spent[ym] = monthly_spent.get(ym, 0) + amount

    return monthly_spent

#----------------------------------------------------------------------------
#                             Daily Expenses
#----------------------------------------------------------------------------

def amount_per_day(data):
    daily_spent = {}

    for i in data:
        date = i["date"]
        ymd = dt.strptime(date, "%Y-%m-%d")

        day = ymd.date()

        amount = i["amount"]
        daily_spent[day] = daily_spent.get(day, 0) + amount
    
    sorted_daily = sorted(daily_spent.items())

    dates_list = []
    amounts_list = []

    for day, amount in sorted_daily:
        dates_list.append(day.strftime("%Y-%m-%d"))
        amounts_list.append(amount)

    return dates_list, amounts_list

#----------------------------------------------------------------------------
#                                   MENU
#----------------------------------------------------------------------------

def main():
    while True:
        print("=========================")
        print("           Menu          ")
        print("=========================")
        print("1. Add Expense")
        print("-------------------------")
        print("2. View Expense")
        print("-------------------------")
        print("3. Show Statistics")
        print("-------------------------")
        print("4. Visualize")
        print("-------------------------")
        print("5. Analyze")
        print("-------------------------")
        print("6. Import CSV")
        print("-------------------------")
        print("7. Export CSV")
        print("-------------------------")
        print("8. Save and Exit")
        print("-------------------------")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    add_expense()
                case 2:
                    view_expense()
                case 3:
                    show_stats()
                case 4:
                    visualization_menu()
                case 5:
                    analysis_menu()
                case 6:
                    path = input("Enter CSV file path to import: ")
                    result = import_csv(path)
                    if result is not None:
                        print(result.head())
                case 7:
                    export_to_csv()
                case 8:
                    print("Saving and Exiting...")
                    break
        except ValueError:
            print("Invalid choice. Enter a number from 1–8")
            continue

if __name__ == "__main__":
    main()