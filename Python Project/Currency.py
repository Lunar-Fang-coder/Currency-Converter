from tkinter import Tk, ttk
from tkinter import *
import json
import requests

# gui box
window = Tk()
window.title("Currency Converter")
window.geometry("500x600")
window.config(bg="#ffcccb")


# rapid api for conversion rates
def conversion():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency_1 = combo1.get()
    currency_2 = combo2.get()
    value = amount.get()
    querystring = {"from": currency_1, "to": currency_2, "amount": value}

    headers = {
        "X-RapidAPI-Key": "344c2a4c7fmsh2ef2875463e0dd8p19c8dbjsna002afdf5c32",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com",
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = "{:,.2f}".format(converted_amount)
    answer["text"] = formatted
    print(converted_amount, formatted)
    # print(data)


# formating of header
top = Frame(window, width=600, height=100, bg="Grey")
top.grid(row=0, column=0)
# formation of bosy
bot = Frame(window, width=600, height=500, bg="orange")
bot.grid(row=1, column=0)

# formation of header name
app_name = Label(
    top,
    text="Currency Converter 101",
    fg="white",
    bg="Grey",
    height=3,
    width=28,
    font=("TimesNewRoman 20 bold"),
    anchor=CENTER,
)
app_name.place(x=0, y=0)


# formation of answer box
answer = Label(
    bot,
    text=" ",
    fg="black",
    bg="white",
    height=2,
    width=20,
    padx=10,
    pady=10,
    font=("TimesNewRoman 15 bold"),
    anchor=CENTER,
)
answer.place(x=130, y=20)


# currency ISO codes
currency = [
    "AFN",
    "ALL",
    "AMD",
    "ANG",
    "AOA",
    "ARS",
    "AUD",
    "AWG",
    "AZN",
    "BAM",
    "BBD",
    "BDT",
    "BGN",
    "BHD",
    "BIF",
    "BMD",
    "BND",
    "BOB",
    "BOV",
    "BRL",
    "BSD",
    "BTN",
    "BWP",
    "BYN",
    "BZD",
    "CAD",
    "CDF",
    "CHE",
    "CHF",
    "CHW",
    "CLF",
    "CLP",
    "CNY",
    "COP",
    "COU",
    "CRC",
    "CUC",
    "CUP",
    "CVE",
    "CZK",
    "DJF",
    "DKK",
    "DOP",
    "DZD",
    "EGP",
    "ERN",
    "ETB",
    "EUR",
    "FJD",
    "FKP",
    "GBP",
    "GEL",
    "GHS",
    "GIP",
    "GMD",
    "GNF",
    "GTQ",
    "GYD",
    "HKD",
    "HNL",
    "HRK",
    "HTG",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "JMD",
    "JOD",
    "JPY",
    "KES",
    "KGS",
    "KHR",
    "KMF",
    "KPW",
    "KRW",
    "KWD",
    "KYD",
    "KZT",
    "LAK",
    "LBP",
    "LKR",
    "LRD",
    "LSL",
    "LYD",
    "MAD",
    "MDL",
    "MGA",
    "MKD",
    "MMK",
    "MNT",
    "MOP",
    "MRU",
    "MUR",
    "MVR",
    "MWK",
    "MXN",
    "MXV",
    "MYR",
    "MZN",
    "NAD",
    "NGN",
    "NIO",
    "NOK",
    "NPR",
    "NZD",
    "OMR",
    "PAB",
    "PEN",
    "PGK",
    "PHP",
    "PKR",
    "PLN",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "RWF",
    "SAR",
    "SBD",
    "SCR",
    "SDG",
    "SEK",
    "SGD",
    "SHP",
    "SLL",
    "SOS",
    "SRD",
    "SSP",
    "STN",
    "SVC",
    "SYP",
    "SZL",
    "THB",
    "TJS",
    "TMT",
    "TND",
    "TOP",
    "TRY",
    "TTD",
    "TWD",
    "TZS",
    "UAH",
    "UGX",
    "USD",
    "USN",
    "UYI",
    "UYU",
    "UYW",
    "UZS",
    "VES",
    "VND",
    "VUV",
    "WST",
    "XAF",
    "XAG",
    "XAU",
    "XBA",
    "XBB",
    "XBC",
    "XBD",
    "XCD",
    "XDR",
    "XOF",
    "XPD",
    "XPF",
    "XPT",
    "XSU",
    "XTS",
    "XUA",
    "YER",
    "ZAR",
    "ZMW",
    "ZWL",
]

# Formation of drop down list of currencies
from_label = Label(
    bot,
    text="From",
    fg="black",
    bg="Grey",
    height=1,
    width=10,
    pady=0,
    padx=0,
    relief="flat",
    font=("TimesNewRoman 15"),
    anchor=CENTER,
)
from_label.place(x=110, y=145)

combo1 = ttk.Combobox(bot, width=10, justify=CENTER, font=("TimesNewRoman"))
combo1["values"] = currency
combo1.place(x=110, y=175)

to_label = Label(
    bot,
    text="To",
    fg="black",
    bg="Grey",
    height=1,
    width=10,
    pady=0,
    padx=0,
    relief="flat",
    font=("TimesNewRoman 15"),
    anchor=CENTER,
)
to_label.place(x=310, y=145)


combo2 = ttk.Combobox(bot, width=10, justify=CENTER, font=("TimesNewRoman"))
combo2["values"] = currency
combo2.place(x=310, y=175)

# Formation of box to enter the value to be converted
amount = Entry(bot, width=20, justify=CENTER,
               font=("TimesNewRoman 15"), relief=SOLID)
amount.place(x=135, y=300)

# Formation of button
button = Button(
    bot,
    text="CONVERTER",
    width=20,
    height=1,
    bg="grey",
    fg="orange",
    font=("TimesNewRoman"),
    command=conversion,
)
button.place(x=150, y=350)

# Calling the box
window.mainloop()
