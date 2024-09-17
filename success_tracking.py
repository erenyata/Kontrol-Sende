from gettext import dgettext, find
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.uic import loadUi
import sys
import datetime

class Success_Tracking(QWidget):
    def __init__(self):
        super(Success_Tracking, self).__init__()
        loadUi("ui/success-tracking.ui", self)
        self.addButton.clicked.connect(self.addObject)
        self.showData.clicked.connect(self.showDataF)
        self.setWindowTitle("Başarı Takip Aracı")
        self.setWindowIcon(QIcon("icons/success.ico"))                


    def showDataF(self):
        with open("basari-takip.txt","r") as file:
            self.textEdit.setText(file.read())

    def addObject(self):
        
        date = datetime.datetime.today()
        tarih = date.strftime("%d.%m.%y")
        ders = self.lineSubject.text()
        dogru = int(self.spinTrue.value())
        yanlis = int(self.spinFalse.value())
        net = float(dogru - (yanlis*0.25))
        if yanlis >= 4:
            net = dogru - (yanlis*0.25) - (yanlis//4*0.25) + 0.25
            

        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        
        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(ders)))
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(dogru)))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(yanlis)))
        self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(net)))
        self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(tarih))

        with open("basari-takip.txt","a") as file:
            file.write(f"Ders: {ders}\nDoğru: {dogru}\nYanlış: {yanlis}\nNet: {net}\nTarih: {tarih}\n" + "-"*50 + "\n")




'''
    def updateTaskList(self, date):
        self.tableWidget.clear()

        db = sqlite3.connect("success-tracking.db")
        cursor = db.cursor()



    def saveChanges(self):
        db = sqlite3.connect("success-tracking.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()



        db.commit()

        messageBox = QMessageBox()
        messageBox.setText("Değişiklikler Kaydedildi!")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.setWindowTitle("Yapılacaklar Listesi")
        messageBox.setWindowIcon(QIcon("icons/todo.ico"))
        messageBox.exec()

    def addObject(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        newTask = str(self.taskLineEdit.text())
        date = self.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
        row = (newTask, "NO", date,)

        cursor.execute(query, row)
        db.commit()
        self.updateTaskList(date)
        self.taskLineEdit.clear()
'''