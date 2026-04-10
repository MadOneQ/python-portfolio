import pandas as pd

df = pd.read_csv("bank_statement.csv")


expenses = df[df["amount"] < 0]
income = df[df["amount"] > 0]
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
def categorize(description):
    description = description.upper()
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
    elif "GYM" in description:
        return "Health"
    elif "PHARMACY" in description:
        return "Health"
    else:
        return "Other"

df["category"] = df["description"].apply(categorize)

summary = df.groupby("category")["amount"].sum()
summary_sorted = summary.sort_values()

expenses_summary = df[df["amount"] < 0].groupby("category")["amount"].sum()
total_expenses = expenses_summary.sum()
total_income = df[df["amount"] > 0]["amount"].sum()
net = total_income + total_expenses

print(f"Total Income: {total_income:.2f} EUR")
print(f"Total Expenses: {total_expenses:.2f} EUR")
print(f"Net: {net:.2f} EUR")
