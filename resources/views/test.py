# Form implementation generated from reading ui file '.\test.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 10, 0, 1, 1)
        self.ans_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ans_2.setFont(font)
        self.ans_2.setWordWrap(True)
        self.ans_2.setObjectName("ans_2")
        self.gridLayout.addWidget(self.ans_2, 5, 1, 1, 4)
        self.ans_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ans_4.setFont(font)
        self.ans_4.setWordWrap(True)
        self.ans_4.setObjectName("ans_4")
        self.gridLayout.addWidget(self.ans_4, 7, 1, 1, 4)
        self.ans_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ans_5.setFont(font)
        self.ans_5.setWordWrap(True)
        self.ans_5.setObjectName("ans_5")
        self.gridLayout.addWidget(self.ans_5, 8, 1, 1, 4)
        self.ans_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ans_3.setFont(font)
        self.ans_3.setWordWrap(True)
        self.ans_3.setObjectName("ans_3")
        self.gridLayout.addWidget(self.ans_3, 6, 1, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 10, 1, 1, 3)
        self.r_4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.r_4.setFont(font)
        self.r_4.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.r_4.setText("")
        self.r_4.setObjectName("r_4")
        self.gridLayout.addWidget(self.r_4, 7, 0, 1, 1)
        self.r_3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.r_3.setFont(font)
        self.r_3.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.r_3.setText("")
        self.r_3.setObjectName("r_3")
        self.gridLayout.addWidget(self.r_3, 6, 0, 1, 1)
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.next_btn.setFont(font)
        self.next_btn.setObjectName("next_btn")
        self.gridLayout.addWidget(self.next_btn, 10, 4, 1, 1)
        self.r_5 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.r_5.setFont(font)
        self.r_5.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.r_5.setText("")
        self.r_5.setObjectName("r_5")
        self.gridLayout.addWidget(self.r_5, 8, 0, 1, 1)
        self.r_1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.r_1.setFont(font)
        self.r_1.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.r_1.setText("")
        self.r_1.setObjectName("r_1")
        self.gridLayout.addWidget(self.r_1, 4, 0, 1, 1)
        self.ans_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ans_1.setFont(font)
        self.ans_1.setWordWrap(True)
        self.ans_1.setObjectName("ans_1")
        self.gridLayout.addWidget(self.ans_1, 4, 1, 1, 4)
        self.r_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.r_2.setFont(font)
        self.r_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.r_2.setText("")
        self.r_2.setObjectName("r_2")
        self.gridLayout.addWidget(self.r_2, 5, 0, 1, 1)
        self.question_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.question_lbl.setFont(font)
        self.question_lbl.setWordWrap(True)
        self.question_lbl.setObjectName("question_lbl")
        self.gridLayout.addWidget(self.question_lbl, 3, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lufthansa Head Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-style: solid;\n"
"border-width: 0px 0px 1px 0px;\n"
"border-bottom-color: rgb(79, 79, 79);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.ans_2.setText(_translate("MainWindow", "TextLabel"))
        self.ans_4.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et dolor ut tortor congue lacinia. In posuere dictum elit, ut malesuada augue bibendum ac."))
        self.ans_5.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et dolor ut tortor congue lacinia. In posuere dictum elit, ut malesuada augue bibendum ac."))
        self.ans_3.setText(_translate("MainWindow", "TextLabel"))
        self.next_btn.setText(_translate("MainWindow", "Next"))
        self.ans_1.setText(_translate("MainWindow", "TextLabel"))
        self.question_lbl.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et dolor ut tortor congue lacinia. In posuere dictum elit, ut malesuada augue bibendum ac."))
        self.label.setText(_translate("MainWindow", "Lenda "))
