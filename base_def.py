import requests
import datetime
import openpyxl
import config


def pool_data():
    reply = requests.get(config.url)
    time_stamp = reply.json()['payments'][0]['timestamp']
    amount_eth = '0,00' + str(reply.json()['payments'][0]['amount'])
    print(time_stamp)
    print(amount_eth)
    date_payments(time_stamp, amount_eth)


def date_payments(time_stamp, amount_eth):
    today_date = datetime.date.today()
    date_from_miner = datetime.date.fromtimestamp(time_stamp)
    if today_date == date_from_miner:
        in_excel(date_from_miner, amount_eth)
        print(date_from_miner, '=', today_date, amount_eth)
    else:
        in_excel(today_date, 0)
        print(today_date, '!=', date_from_miner, '0')


def in_excel(date, amount_eth):
    file_excel = openpyxl.load_workbook(config.file_path)
    activ_list = file_excel.active
    for row in activ_list['A']:
        if row.value is None:
            activ_list['A'+str(row.row)].value = date
            activ_list['C'+str(row.row)].value = amount_eth
            file_excel.save(config.file_path)
            break


pool_data()
