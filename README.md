# **Personal Finance Tracker**

CLI tool to record and monitor your spending.

![MENU](ss/menu.jpg)

## Core Features
- **Add Expense:** Enter the amount, category, date, and an optional note.

![Add Expense](ss/add.jpg)

- **View Expenses:** Display all stored expenses in a clean list.  

![Add Expense](ss/view.jpg)

- **Show Statistics:** View basic spending stats like totals and summaries. 

![Add Expense](ss/stats.jpg) 

- **Exit:** Saves everything to your JSON file before closing.

Expenses are stored in a JSON file using four main datamembers (`amount`, `category`, `date`, `note`)
and handled through the project’s core Python methods.

---

## Features (Phase 2)
- **Monthly Spending:** Automatically groups and totals expenses by month.

![Monthly Chart](charts/monthly.png)

- **Category Breakdown:** Shows how much you’ve spent in each category.

![Category Chart](charts/category.png)  

- **Expenses Over Time:** Tracks your spending trend across dates for simple time-based analysis.  

![Daily Chart](charts/daily.png)

## New Features (Phase 2)
- **Monthly Spending:** Automatically groups and totals expenses by month.

![Monthly Chart](charts/monthly.png)

- **Category Breakdown:** Shows how much you've spent in each category.

![Category Chart](charts/category.png)  

- **Expenses Over Time:** Tracks your spending trend across dates for simple time-based analysis.  

![Daily Chart](charts/daily.png)

---

## Features (Phase 3)
- **Daily Summary:** View total spending per day with detailed breakdown.

![Daily Summary](ss/daily.jpg) 

- **Monthly Summary:** Analyze monthly spending patterns and totals.

![Monthly Summary](ss/monthly.jpg) 

- **Category Summary:** Get a quick overview of expenses by category.

![Category Summary](ss/category.jpg) 

- **Detect Trends:** Compare spending between months to identify trends.

![Detect Trends](ss/trend.jpg) 

- **Budget Alerts:** Set spending limits per category and get warnings when exceeded.

![Budget Alert](ss/budget.jpg) 

- **CSV Import/Export:** 
  - **Export:** Save all expenses to `expenses.csv` for backup or external analysis.
  ![Export](ss/exportcsv.jpg) 
  - **Import:** Load expenses from CSV files directly into the app.
  ![Import](ss/importcsv.jpg) 

- **Analytics Menu:** Access all analysis tools from a dedicated menu.

![Analysis](ss/analyze.jpg) 

- **Chart Visualization Menu:** Generate and save visual representations of your spending habits.

![Visualization](ss/visualize.jpg) 

---

## Technical Stack



- **Language:** Python 3.x
- **Data Storage:** JSON
- **Analysis:** Pandas
- **Visualization:** Matplotlib
- **Architecture:** Modular design with separate utilities, analysis, and visualization modules


