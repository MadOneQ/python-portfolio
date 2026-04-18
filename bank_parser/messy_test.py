import pandas as pd

df_messy = pd.read_csv("bank_statement_messy.csv")
print(df_messy)
print(df_messy.info())

df_messy["description"] = df_messy["description"].str.upper()
print(df_messy["description"])

df_messy = df_messy.dropna(subset=["date"])
print(df_messy)

df_messy["amount"] = df_messy["amount"].fillna(0)
print(df_messy)
