import json
import requests



from_currency = input("from_currency : ").upper()
to_currency = input("to_currency : ").upper()
amount = input("amount : ")
url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

payload = {}
headers = {
    "apikey": "BEvmrzSfPE5XrrqNf69LhEOYpPewZbNp"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
JSON_result = response.text

# Parse the JSON result to Python dictionary.
data = json.loads(JSON_result)


print("*********")
print(f"{amount} {from_currency}  = {(data['info']['rate'])*float(amount)} {to_currency}")

