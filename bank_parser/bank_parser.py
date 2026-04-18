import pandas as pd
import sys

# 1.LOAD

def load_statement(filepath):
    df = pd.read_csv(filepath)
    
    return df

# 2. DETECT and LOAD

def detect_and_load(filepath):
    # Detect Separator
    with open(filepath, 'r') as f:
        first_line = f.readline()
        separator = ";" if ";" in first_line else ","

    df = pd.read_csv(filepath, sep=separator)

    # Normalize column names to lowercase
    df.columns = df.columns.str.lower().str.strip()

    print(f"Detected separator: '{separator}'")
    print(f"Columns found: {list(df.columns)}")

    return df

# 3. CLEAN

def clean_statement(df):
    df["description"] = df["description"].str.upper()
    df["date"] = pd.to_datetime(df["date"], errors = "coerce")
    df = df.dropna(subset=["date"])
    df["amount"] = df["amount"].fillna(0)
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    return df


# 4. CATEGORIZE

def categorize(description):
    if any(k in description for k in ["SALARY", "SALAIRE", "FREELANCE", "VIREMENT"]):
        return "Income"
    elif any(k in description for k in ["AMAZON"]):
        return "Shopping"
    elif any(k in description for k in ["CARREFOUR", "SUPERMARKET", "LECLERC", "LIDL", "ALDI"]):
        return "Groceries"
    elif any(k in description for k in ["NETFLIX", "SPOTIFY", "DEEZER", "CANAL"]):
        return "Subscriptions"
    elif any(k in description for k in ["UBER", "TAXI", "SNCF", "RATP"]):
        return "Transport"
    elif any(k in description for k in ["ELECTRICITY", "ELECTRICITE", "EDF", "INTERNET", "ENGIE", "FREE", "ORANGE"]):
        return "Bills"
    elif any(k in description for k in ["RESTAURANT", "BRASSERIE", "CAFE", "McDONALD"]):
        return "Dining"
    elif any(k in description for k in ["GYM", "PHARMACY", "PHARMACIE", "DOCTOR"]):
        return "Health"
    else:
        return "Other"
    
def add_categories(df):
    df["category"] = df["description"].apply(categorize)
    return(df)


# 5. SUMMARIZE

def summarize(df):
    expenses = df[df["amount"] < 0]["amount"].sum()
    income = df[df["amount"] > 0]["amount"].sum()
    net = income + expenses
    print(f"Total Income: {income:.2f} EUR")
    print(f"Total Expenses: {expenses:.2f} EUR")
    print(f"Net: {net:.2f} EUR")

def category_summary(df):
    summary = df.groupby("category")["amount"].sum().sort_values()
    return summary

def monthly_summary(df):
    monthly = df.groupby(["month", "category"])["amount"].sum()
    return monthly


# 6. EXPORT

def export(df, summary, monthly):
    df.to_csv("bank_statement_clean.csv", index = False)
    summary.to_csv("summary.csv", header=["total_amount"])
    monthly.to_csv("monthly_summary.csv", header=["total_amount"])
    print("Files exported.")


# 7. MAIN

def main():
    if len(sys.argv) < 2:
        filepath = "bank_statement.csv"
        print("No file specified, using default: bank_statement.csv")
    else:
        filepath = sys.argv[1]
        print(f"Loading: {filepath}")
      
    df = detect_and_load(filepath)
    df = clean_statement(df)
    df = add_categories(df)
    summarize(df)
    summary = category_summary(df)
    monthly = monthly_summary(df)
    export(df, summary, monthly)
    print("\nCategory Summary:")
    print(summary)
    print("\nMonthly Summary:")
    print(monthly)

if __name__ == "__main__":
    main()