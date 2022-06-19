import requests
import datetime
import openpyxl
import config
import telegram_msg


def pool_data():
    reply = requests.get(config.url)
    time_stamp = reply.json()['payments'][0]['timestamp']
    amount_eth = reply.json()['payments'][0]['amount']
    date_payments(time_stamp, amount_eth)


def date_payments(time_stamp, amount_eth):
    today_date = datetime.date.today()
    date_from_miner = datetime.date.fromtimestamp(time_stamp)
    if today_date == date_from_miner:
        in_excel(date_from_miner, amount_eth)
    else:
        in_excel(today_date, 0)


def in_excel(date, amount_eth):
    file_excel = openpyxl.load_workbook(config.file_path)
    activ_list = file_excel.active
    for row in activ_list['A']:
        if row.value is None:
            activ_list['A'+str(row.row)].value = date
            activ_list['C'+str(row.row)].value = amount_eth/10**9
            file_excel.save(config.file_path)
            break
    telegram_msg.send_telegram(date)
    telegram_msg.send_telegram(amount_eth/10**9)


pool_data()
