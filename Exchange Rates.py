import json
import requests
import tkinter as tk
from tkinter import messagebox


def convert_currency():
    try:
        from_currency = from_currency_var.get().upper()
        to_currency = to_currency_var.get().upper()
        amount = amount_var.get()

        if not from_currency or not to_currency or not amount:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Make the API request
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
        payload = {}
        headers = {"apikey": "BEvmrzSfPE5XrrqNf69LhEOYpPewZbNp"}
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()

        # Parse the JSON result to Python dictionary
        data = json.loads(response.text)

        result_label.config(text=f"{amount} {from_currency}  = {(data['info']['rate']) * float(amount)} {to_currency}")
        result_label.config(fg="red")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"API request failed: {e}")
    except json.JSONDecodeError as e:
        messagebox.showerror("Error", f"Failed to parse API response: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Currency Converter")
root.geometry('300x300')

from_currency_label = tk.Label(text="From :")
from_currency_label.pack()
from_currency_var = tk.StringVar()
from_currency_entry = tk.Entry(textvariable=from_currency_var)
from_currency_entry.pack()

to_currency_label = tk.Label(text="To :")
to_currency_label.pack()
to_currency_var = tk.StringVar()
to_currency_entry = tk.Entry(textvariable=to_currency_var)
to_currency_entry.pack()

amount_label = tk.Label(text="Amount:")
amount_label.pack()
amount_var = tk.StringVar()
amount_entry = tk.Entry(textvariable=amount_var)
amount_entry.pack()

convert_button = tk.Button(text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(text="")
result_label.pack()

root.mainloop()
