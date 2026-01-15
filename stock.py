import finnhub
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")

if not API_KEY:
    raise RuntimeError("FINNHUB_API_KEY not found in .env file")

finnhub_client = finnhub.Client(api_key=API_KEY)

def view_stock(symbol: str):
    try:
        quote = finnhub_client.quote(symbol)
        profile = finnhub_client.company_profile2(symbol=symbol)

        if not profile:
            print("❌ Invalid stock symbol")
            return

        print("\n==============================")
        print(f"{profile['name']} ({symbol})")
        print("==============================")
        print(f"Current Price : ${quote['c']}")
        print(f"High           : ${quote['h']}")
        print(f"Low            : ${quote['l']}")
        print(f"Open           : ${quote['o']}")
        print(f"Prev Close     : ${quote['pc']}")
        print("==============================\n")

    except Exception as e:
        print("⚠️ Error:", e)


def main():
    print("📈 Stock Viewer (Finnhub)")
    print("Type 'q' to quit")

    while True:
        symbol = input("Enter stock symbol: ").upper()
        if symbol == "Q":
            break
        view_stock(symbol)


if __name__ == "__main__":
    main()