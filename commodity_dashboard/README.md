#    COMMODITY DASHBOARD
Fetching live precious metals prices from GOLDAPI.IO and summarizing through pandas.

##    REQUIREMENTS
Python
pandas
requests
python-dotenv
API KEY from GOLDAPI.IO stored in .env
Free 100 req/month - Account linked to Google with no Credit Card info

##    HOW IT'S BUILT
1. GET request from URL with API as header
2. BUILDING DATAFRAME with selected columns
3. CLEANING DISPLAY with column name changes and rounding to 2 decimals

##    HOW TO RUN
python commodity_dashboard.py

##    OUTPUT
As of April 20th 2026:
  metal    price  change  change_pct  high_price  low_price
0   XAU  4814.96  -14.35       -0.31     4829.30    4737.15
1   XAG    79.88   -0.89       -1.11       80.78      78.65
2   XPT  2088.45  -20.36       -0.97     2112.03    2060.81
3   XPD  1561.67    3.67        0.24     1566.12    1536.00

##    NEXT STEPS
- Business Use-Case: Link it to P&L