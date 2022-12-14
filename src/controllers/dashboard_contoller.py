import sys
import os
from PyQt6 import QtWidgets, uic
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '...')))
from resources.views.dashboard import Ui_Dashboard
from test_controller import Test

class Dashboard(QtWidgets.QMainWindow, Ui_Dashboard):
    def __init__(self, *args, obj=None, **kwargs):
        super(Dashboard, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.test_btn.clicked.connect(self.handle_test)
        self.test_btn.clicked.connect(self.close)


    def handle_test(self):
        self.a = Test()
        self.a.show()

        