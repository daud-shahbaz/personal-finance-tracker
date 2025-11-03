#----------------------------------------------------------------------------
#                           Importing Libraries
#----------------------------------------------------------------------------

import pandas as pd
from utils import load_dataframe
    
#----------------------------------------------------------------------------
#                          Groupby Daily Expenses
#----------------------------------------------------------------------------

def daily_summary():
    # daily_summary()	Groups by date and sums
    loaded_df = load_dataframe()
    return loaded_df.groupby("date")["amount"].sum()

#----------------------------------------------------------------------------
#                          Groupby Monthly Expenses
#----------------------------------------------------------------------------

def monthly_summary():
    # monthly_summary()	Groups by month
    loaded_df = load_dataframe()
    loaded_df['month'] = loaded_df['date'].dt.to_period('M')
    return loaded_df.groupby("month")["amount"].sum()

#----------------------------------------------------------------------------
#                          Groupby Daily Expenses
#----------------------------------------------------------------------------

def category_summary():
    # category_summary()	Groups by category
    loaded_df = load_dataframe()
    return loaded_df.groupby("category")["amount"].sum()

#----------------------------------------------------------------------------
#                             Detect Trends
#----------------------------------------------------------------------------

def detect_trends():
    # detect_trends()	Compare previous month
    monthly = monthly_summary()
    if len(monthly) < 2:
        return "Not enough data to detect trends"
    else:
        return monthly.iloc[-1] - monthly.iloc[-2]

#----------------------------------------------------------------------------
#                             Budget Alert
#----------------------------------------------------------------------------

budget_dict = {
    "Food": 3000,
    "Transport": 5000,
    "Health": 2000,
    "Rent" : 15000,
    "Groceries":4000
    }

def budget_alert(budget_dict):
    # budget_alert(budget_dict)	Warns if spending exceeds set limits
    category_totals = category_summary()

    for category, limit in budget_dict.items():
        if category_totals.get(category, 0) > limit:
            print(f"{category} exceeded its budget! (Limit: {limit})")

#----------------------------------------------------------------------------
#                             Export to CSV
#----------------------------------------------------------------------------

def export_to_csv():
    try:
        loaded_df = load_dataframe()
        if loaded_df.empty:
            print("No data to export")
            return
        loaded_df.to_csv("data/expenses.csv", index=False)
        print(f"Successfully exported {len(loaded_df)} records to expenses.csv")
    except Exception as e:
        print(f"Error exporting CSV: {e}")


#----------------------------------------------------------------------------
#                              Import CSV
#----------------------------------------------------------------------------

def import_csv(path):
    try:
        df = pd.read_csv(path)
        if df.empty:
            print("CSV file is empty")
            return None
        print(f"Successfully imported {len(df)} records from {path}")
        return df
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except Exception as e:
        print(f"Error importing CSV: {e}")
        return None

#----------------------------------------------------------------------------
#                             Analysis Menu
#----------------------------------------------------------------------------

def analysis_menu():
    print("=========================")
    print("        Analyze          ")
    print("=========================")
    print("1. Daily Summary")
    print("-------------------------")
    print("2. Monthly Summary")
    print("-------------------------")
    print("3. Category Summary")
    print("-------------------------")
    print("4. Detect Trends")
    print("-------------------------")
    print("5. Budget Alert")
    print("-------------------------")
    print("6. Save and Exit")
    print("-------------------------")
    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print(daily_summary())
            case 2:
                print(monthly_summary())
            case 3:
                print(category_summary())
            case 4:
                print(f"Current Month - Last Month = ", detect_trends())
            case 5:
                budget_alert(budget_dict)
                # Put budget_alert argument to Input later
                0
            case 6:
                print("Exiting...")
    except ValueError:
        print("Invalid choice. Enter a number from 1–6")