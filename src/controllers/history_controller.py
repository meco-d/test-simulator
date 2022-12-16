import sys
import os
from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '...')))
from resources.views.history import Ui_MainWindow
import sqlite3
import random


class History(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(History, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.get_data()
        self.pushButton.clicked.connect(self.handle_back)

    def handle_back(self):
        from dashboard_contoller import Dashboard
        self.a = Dashboard()
        self.a.show()
        self.close()

    def get_data(self):
        sqliteConnection = sqlite3.connect('resources\\db\\data.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_Query = "select * from history;"
        cursor.execute(sqlite_select_Query)
        self.data = cursor.fetchall()
        cursor.close()
        
        self.tableWidget.setColumnCount(3)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setHorizontalHeaderLabels(['ID','Score', 'Timestamp'])
        self.tableWidget.setRowCount(len(self.data))

        self.tableWidget.setColumnWidth(0, int(self.width()/3.05))
        self.tableWidget.setColumnWidth(1, int(self.width()/3.05))
        self.tableWidget.setColumnWidth(2, int(self.width()/3.05))

        self.tableWidget.cellDoubleClicked.connect(self.handle_click)
        row = 0
        for e in self.data:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(e[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(e[1]+"/100"))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(e[2]))
            row += 1

        # self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.editTriggers(False))

    def handle_click(self):
        for idx in self.tableWidget.selectionModel().selectedIndexes():
            row_number = idx.row()
            id = self.data[row_number][0]
            from history_detail_controller import HistoryDetails
            self.a = HistoryDetails(id)
            self.a.show()
            self.close()