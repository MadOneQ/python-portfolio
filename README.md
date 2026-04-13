Python Portfolio
Scripts I'm building while learning Python through real-world projects.

Projects
1. 🗂️ File Organizer
Scans a folder and automatically sorts files into subfolders by extension (PDFs, Images, Documents, etc.).
What it demonstrates:

File I/O with os and shutil
Dictionaries, loops, conditionals

How to run:
python file_organizer.py


2. 🏦 Bank Statement Parser
Loads a CSV bank statement, cleans messy data, categorizes transactions by keyword matching and outputs a spending summary.
What it demonstrates:

pandas fundamentals (load, clean, filter, group)
Custom functions + .apply()
Handling missing data (NaN)
Data export to CSV

Requirements:
pip install pandas

How to run:
python bank_parser.py

Input: bank_statement.csv
date,description,amount,currency
2024-01-02,AMAZON MARKETPLACE,-45.99,EUR
...

Output:
Total Income:   4350.00 EUR
Total Expenses: -445.30 EUR
Net:            3904.70 EUR


summary.csv — spending by category
monthly_summary.csv — spending by month and category
bank_statement_clean.csv — cleaned full statement


🗺️ Roadmap

 File Organizer
 Bank Statement Parser
 Commodity Dashboard
 FP&A Report Generator
 Flask Web Dashboard


🛠️ Stack

Python 3.x
pandas
os, shutil
