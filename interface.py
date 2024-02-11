import requests
import json
from PyQt5.QtWidgets import *


app = QApplication([])

valcode = QLineEdit()
date = QLineEdit()
resultbtn = QPushButton("Отримати результат ")
valcodelbl = QLabel("Код валюти")
datelbl = QLabel("Дата")
resultlbl = QLabel("")

window = QWidget()
mainline = QVBoxLayout()
line = QHBoxLayout()
mainline.addLayout(line)
mainline.addWidget(valcodelbl)
mainline.addWidget(valcode)
mainline.addWidget(datelbl)
mainline.addWidget(date)
mainline.addWidget(resultbtn)
mainline.addWidget(resultlbl)


def result():
    valcode_text = valcode.text()
    date_text = date.text()
    a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode_text}&date={date_text}&json")
    if a.status_code == 200:
        data = json.loads(a.text)
        resultlbl.setText(f" {data[0]['txt']}: {data[0]['rate']}")




resultbtn.clicked.connect(result)
window.setLayout(mainline)
window.show()
app.exec()
