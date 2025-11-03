#----------------------------------------------------------------------------
#                          Importing Packages
#----------------------------------------------------------------------------

import json
import pandas as pd

#----------------------------------------------------------------------------
#                          Variable for Path
#----------------------------------------------------------------------------

expenses_path = 'data/expenses.json'

#----------------------------------------------------------------------------
#                              Load JSON
#----------------------------------------------------------------------------

def load_data():
    #load_data() extracts raw json
    print("Loading expenses...")

    try:
        with open(expenses_path, 'r') as file:
            expenses = json.load(file)
        return expenses
    except FileNotFoundError as e:
        print("File does not exist:", e)
        return []
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return []
    
#----------------------------------------------------------------------------
#                             Save JSON
#----------------------------------------------------------------------------

def save_data(expense):
    # save_data()	saves dict to list
    try:
        with open(expenses_path, 'w') as file:
            json.dump(expense, file, indent=4)
    
    except Exception as e:
        print(f" Error saving file: {e}")

#----------------------------------------------------------------------------
#                             Load DataFrame
#----------------------------------------------------------------------------

def load_dataframe():
    # load_dataframe()	Converts expenses.json to pandas DataFrame
    try:
        with open(expenses_path, 'r') as file:
            expenses = json.load(file)

        if isinstance(expenses, list):
            df = pd.DataFrame(expenses)
            df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
            df = df.sort_values(by='date').reset_index(drop=True)
            return df            
        else:
            return pd.DataFrame(columns=['amount','category','date','notes'])
    
    except FileNotFoundError as e:
        print("File does not exist:", e)
        return pd.DataFrame(columns=['amount','category','date','notes'])
    
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return pd.DataFrame(columns=['amount','category','date','notes'])
    


    