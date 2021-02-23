import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=18)


import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

# (1) Google Spread Sheetsにアクセス
def connect_gspread(jsonf,key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    workbook = gc.open_by_key(SPREADSHEET_KEY)
    return workbook

# ここでjsonfile名と2-2で用意したkeyを入力
jsonf = "python/spread-sheets-python-305515-ddfdfe4016ac.json"
jsonf = "/home/pi/gpio/tmp2spread/spread-sheets-python-305515-ddfdfe4016ac.json"
spread_sheet_key = "1-w4ohqSVR0GwYknfssP-pBpS4RYZ839ygSeUJsDTUaM"
wb = connect_gspread(jsonf,spread_sheet_key)

# ワークシートを選択
ws = wb.sheet1

# 最終行の判定
col_list = ws.col_values(1)

j = 0
for i in col_list:
  j += 1
  if not i:
    break
  else:
    continue
  break

# 最終行へ時刻、温度、湿度を入力
result = instance.read()
if result.is_valid():
    ws.update_cell(j+1,1,str(datetime.datetime.now()))
    ws.update_cell(j+1,2,result.temperature)
    ws.update_cell(j+1,3,result.humidity)
GPIO.cleanup()