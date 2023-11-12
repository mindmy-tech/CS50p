import requests
import json
import sys

def main():
    args = sys.argv
    if len(args) != 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoins = float(args[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    cost = get_cost()

    quote = bitcoins * cost
    print(f"${quote:,.4f}")

def get_cost():

    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
    except requests.RequestException:
        sys.exit("Error Occured Try Again")

    cost  = response.json()['bpi']['USD']['rate_float']
    return cost
main()