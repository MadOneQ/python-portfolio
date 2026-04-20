from dotenv import load_dotenv
import requests
import os
import pandas as pd

load_dotenv()
api_key = os.getenv("GOLDAPI_KEY")

#    FETCH PRICES
def fetch_prices(api_key):
    results = []
    for k in ["XAU", "XAG", "XPT", "XPD"]:
        response = requests.get(
        f"https://www.goldapi.io/api/{k}/USD",
        headers={"x-access-token": api_key})
        results.append(response.json())
    return results


#    BUILD DATAFRAME
def build_dataframe(results):
    df = pd.DataFrame(results)
    df = df[["metal", "price", "ch", "chp", "high_price", "low_price"]]
    return df


#    DISPLAY
def display(df):
    df = df.rename(columns={"ch": "change", "chp":"change_pct"})
    df = df.round(2)
    pd.set_option("display.max_columns", None)
    print(df)


#    MAIN
def main():
    results = fetch_prices(api_key)
    df = build_dataframe(results)
    df = display(df)

if __name__ == "__main__":
    main()

