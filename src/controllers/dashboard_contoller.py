import sys
import os
from PyQt6 import QtWidgets, uic
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '...')))
from resources.views.dashboard import Ui_Dashboard
from test_controller import Test
from history_controller import History

class Dashboard(QtWidgets.QMainWindow, Ui_Dashboard):
    def __init__(self, *args, obj=None, **kwargs):
        super(Dashboard, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.test_btn.clicked.connect(self.handle_test)
        self.history_btn.clicked.connect(self.handle_history)


    def handle_test(self):
        self.a = Test()
        self.a.show()
        self.close()

    def handle_history(self):
        self.a = History()
        self.a.show()
        self.close()

        