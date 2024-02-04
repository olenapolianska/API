from PyQt5.QtWidgets import *

app = QApplication([])

valcode = QLineEdit()
date = QLineEdit()
result = QPushButton("Отримати результат ")
valcodelbl = QLabel("Код валюти")
datelbl = QLabel("Дата")
window = QWidget()
mainline = QVBoxLayout()
line = QHBoxLayout()
mainline.addLayout(line)
mainline.addWidget(valcodelbl)
mainline.addWidget(valcode)
mainline.addWidget(datelbl)
mainline.addWidget(date)
mainline.addWidget(result)

def result():
    





window.setLayout(mainline)
window.show()
app.exec()
