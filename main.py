import requests
import tkinter as tk
from datetime import datetime


def trackCrypto():
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price)+ " $")
    labelTime.config(text = "It refresh every 3 sec, Updated at: "+ time)

    canvas.after(3000, trackCrypto)

canvas = tk.Tk()
canvas.geometry("1280x720")
canvas.title("Crypto Tracker")

f1 = ("Helvetica", 24, "bold")
f2 = ("Helvetica", 22, "bold")
f3 = ("Helvetica", 18, "normal")

label = tk.Label(canvas, text= "Crypto Tracker", font= f1)
label.pack(pady = 20)


labelBTC = tk.Label(canvas, font= f2)
labelBTC.config(text = "BTC")
labelBTC.pack(pady = 20)

labelPrice = tk.Label(canvas, font= f2)
labelPrice.pack(pady = 20)

labelTime = tk.Label(canvas, font= f3)
labelTime.pack(pady=20)

trackCrypto()

canvas.mainloop()