import sys
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QDialog, QApplication

from src.controllers.dashboard_contoller import Dashboard

app=QApplication(sys.argv)
mainwindow = Dashboard()

# stacked_widget=QtWidgets.QStackedWidget()
# stacked_widget.addWidget(mainwindow)
# stacked_widget.resize(800, 600)

mainwindow.show()
app.exec()