import requests
import config
import telegram_msg


def binance_data(amount_eth):
    reply_binance = requests.get(config.binance_api)
    price_eth = round(float(reply_binance.json()['price']))
    amount_eth = amount_eth/10**9
    telegram_msg.send_telegram(round(price_eth*amount_eth, 2))
