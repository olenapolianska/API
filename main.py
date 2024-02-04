import requests
import json

valcode = input("Введіть код валюти")
date = input("Введіть дату")


a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json")


if a.status_code == 200:
    data = json.loads(a. text)
    print(data[0]["txt"], data[0]["rate"])