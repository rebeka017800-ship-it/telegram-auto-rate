import requests
import time

TOKEN = "8516309153:AAFL-TXW_msqEvJp23Ywd0pbT4JPjtKt1R8"
CHAT_IDS = ["-1003832598493", "5973756544"]

def send(msg):
    for chat_id in CHAT_IDS:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": msg})

def get_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "tether,bitcoin",
        "vs_currencies": "usd"
    }

    r = requests.get(url, params=params, timeout=10)
    data = r.json()

    btc = data["bitcoin"]["usd"]
    usdt = data["tether"]["usd"]

    return btc / usdt

while True:
    try:
        rate = get_price()
        send(f"🚀 USDT → BTC = {rate:.6f}")
        print("Rate sent:", rate)

    except Exception as e:
        send(f"❌ Error: {e}")
        print("Error:", e)

    time.sleep(60)