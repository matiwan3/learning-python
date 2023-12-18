import requests
import json

def get_cryptocurrency_prices(api_key, secret_key, symbols_of_interest):
    base_url = "https://api.bybit.com/v2/public/tickers"
    headers = {
        "Content-Type": "application/json",
        "api_key": api_key,
        "api_secret": secret_key,
    }

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()  # Check for errors in the response
        data = response.json()

        for ticker in data['result']:
            symbol = ticker['symbol']
            if symbol in symbols_of_interest:
                price = ticker['last_price']
                print(f"{symbol}: {price}$")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Load API keys from a separate file
    with open("api_keys.json") as api_key_file:
        api_keys = json.load(api_key_file)

    api_key = api_keys.get("api_key")
    secret_key = api_keys.get("secret_key")

    # Get user input for cryptocurrencies
    user_input = input("Which cryptocurrencies are you interested in? (comma-separated): ")
    symbols_of_interest = [symbol.strip() for symbol in user_input.split(",")]

    # Run the script in a loop
    while True:
        # Run the script to get prices for the specified cryptocurrency pairs
        get_cryptocurrency_prices(api_key, secret_key, symbols_of_interest)

        # Wait for user input to refresh prices
        input("Press Enter to refresh prices...")
