# -*- coding:utf-8 -*-
import requests
import json

# 気象庁データの取得
jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
jma_json = requests.get(jma_url).json()

# 取得したいデータを選ぶ
jma_date = jma_json[0]["timeSeries"][0]["timeDefines"][0]
jma_area = jma_json[0]["publishingOffice"]
jma_weatherCode = int(jma_json[0]["timeSeries"][0]["areas"][0]["weatherCodes"][0])
jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
#jma_rainfall = jma_json["Feature"][0]["Property"]["WeatherList"]["Weather"][0]["Rainfall"]
# 全角スペースの削除
jma_weather = jma_weather.replace('　', '')

print(jma_date)
print(jma_area)
print(jma_weatherCode)
print(jma_weather)
#print(jma_rainfall)
