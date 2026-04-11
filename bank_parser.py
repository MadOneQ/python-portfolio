import pandas as pd


# 1.LOAD

def load_statement(filepath):
    df = pd.read_csv(filepath)
    
    return df


# 2. CLEAN

def clean_statement(df):
    df["description"] = df["description"].str.upper()
    df["date"] = pd.to_datetime(df["date"], errors = "coerce")
    df = df.dropna(subset=["date"])
    df["amount"] = df["amount"].fillna(0)
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    return df


# 3. CATEGORIZE

def categorize(description):
    if "SALARY" in description or "FREELANCE" in description:
        return "Income"
    elif "AMAZON" in description:
        return "Shopping"
    elif "CARREFOUR" in description:
        return "Groceries"
    elif "NETFLIX" in description or "SPOTIFY" in description:
        return "Subscriptions"
    elif "UBER" in description:
        return "Transport"
    elif "ELECTRICITY" in description or "INTERNET" in description:
        return "Bills"
    elif "RESTAURANT" in description:
        return "Dining"
    elif "GYM" in description or "PHARMACY" in description:
        return "Health"
    else:
        return "Other"
    
def add_categories(df):
    df["category"] = df["description"].apply(categorize)
    return(df)


# 4. SUMMARIZE

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


# 5. EXPORT

def export(df, summary, monthly):
    df.to_csv("bank_statement_clean.csv", index = False)
    summary.to_csv("summary.csv", header=["total_amount"])
    monthly.to_csv("monthly_summary.csv", header=["total_amount"])
    print("Files exported.")


# 6. MAIN

def main():
    df = load_statement("bank_statement.csv")
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