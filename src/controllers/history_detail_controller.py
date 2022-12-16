import sys
import os
from PyQt6 import QtWidgets, uic, QtCore, QtGui
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '...')))
from resources.views.test_result import Ui_MainWindow
from dashboard_contoller import Dashboard
from datetime import datetime
import sqlite3

class HistoryDetails(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, id):
        super(HistoryDetails, self).__init__()
        self.id = id 
        self.setupUi(self)
        self.pushButton.clicked.connect(self.handle_button)
        self.handle_data()
        

    def handle_button(self):
        self.a = Dashboard()
        self.a.show()
        self.close()

    def handle_data(self):
        sqliteConnection = sqlite3.connect('resources\\db\\data.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_Query = "SELECT * FROM history_details where id_history = '{}';".format(self.id)
        cursor.execute(sqlite_select_Query)
        wrong_data = cursor.fetchall()

        # [(question, prgj_sak, prgj_edhen)]

        for x in wrong_data:
            print(x)
            question_txt = x[2]
            given_answ_txt = x[3]
            correct_answ_txt = x[4]

            self.widget = QtWidgets.QWidget()
            self.widget.setGeometry(QtCore.QRect(50, 50, 681, 78))
            self.widget.setMinimumSize(QtCore.QSize(450, 0))
            self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.widget.setStyleSheet("QWidget{\n"
"    border-radius: 22px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel\n"
"{\n"
"    color: rgb(59, 59, 59);\n"
"}")
            self.widget.setObjectName("widget")
            self.gridLayout = QtWidgets.QGridLayout(self.widget)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("gridLayout")
            self.given_answ = QtWidgets.QLabel(self.widget)
            self.given_answ.setWordWrap(True)
            self.given_answ.setObjectName("given_answ")
            self.given_answ.setStyleSheet("color: black;")
            self.gridLayout.addWidget(self.given_answ, 1, 1, 1, 1)
            self.right_answ = QtWidgets.QLabel(self.widget)
            self.right_answ.setWordWrap(True)
            self.right_answ.setObjectName("right_answ")
            self.right_answ.setStyleSheet("color: black;")
            self.gridLayout.addWidget(self.right_answ, 2, 1, 1, 1)
            self.question = QtWidgets.QLabel(self.widget)
            self.question.setWordWrap(True)
            self.question.setObjectName("question")
            self.question.setStyleSheet("color: black;")
            self.gridLayout.addWidget(self.question, 0, 1, 1, 1)
            spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
            self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
            spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
            self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

            self.question.setText(question_txt.strip())
            self.given_answ.setText("Prgj juaj: " + given_answ_txt.strip())
            self.right_answ.setText("Pregj sakt: " + correct_answ_txt.strip())

            self.verticalLayout.addWidget(self.widget)
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.score = 100 - len(wrong_data)
        self.label_2.setText("Rezultati:{}/{}".format(self.score, 100))


        if self.score > 50:
            self.label.setText("KALON")
            self.label.setStyleSheet("color: #00d400;")
        else:
            self.label.setText("NUK KALON")
            self.label.setStyleSheet("color: #ff2a2a;")
