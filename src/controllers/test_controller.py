import sys
import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '...')))
from resources.views.test import Ui_MainWindow
import sqlite3
import random


class Test(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.button_id = {
            'r_1': 0,
            'r_2': 1,
            'r_3': 2,
            'r_4': 3,
            'r_5': 4,

        }
        self.nr = 0
        self.question_ids = self.generate_question_id_list()
        self.setupUi(self)
        self.back_btn.setText("Exit")
        self.RadioGroup = QtWidgets.QButtonGroup()
        self.RadioGroup.addButton(self.r_1)
        self.RadioGroup.addButton(self.r_2)
        self.RadioGroup.addButton(self.r_3)
        self.RadioGroup.addButton(self.r_4)
        self.RadioGroup.addButton(self.r_5)
        self.data_list = self.read_question(self.question_ids)
        self.write_data(self.data_list[self.nr])
        self.next_btn.clicked.connect(self.next_handle)
        self.back_btn.clicked.connect(self.back_handle)

    def next_handle(self):
        if self.next_btn.text() == "Finish":
            # self.save_data()
            if self.RadioGroup.checkedButton() != None:
                self.data_list[self.nr]['given_answ'] = self.button_id[self.RadioGroup.checkedButton().objectName()]
            self.go_home(1)
 
        else:
            if self.back_btn.text() == "Exit":
                self.back_btn.setText("Back")

            if self.RadioGroup.checkedButton() != None:
                self.data_list[self.nr]['given_answ'] = self.button_id[self.RadioGroup.checkedButton().objectName()]
           
            self.nr +=1
           
            if self.nr == len(self.question_ids)-1:
                    self.next_btn.setText("Finish")
           
            self.clear_radio()
            self.write_data(self.data_list[self.nr])

    def back_handle(self):
        if self.back_btn.text() == "Exit":
            self.go_home(0)
        else:
            if self.RadioGroup.checkedButton() != None:
                self.data_list[self.nr]['given_answ'] = self.button_id[self.RadioGroup.checkedButton().objectName()]
            self.nr -=1
            if self.nr == 0:
                self.back_btn.setText("Exit")
            self.clear_radio()
            self.write_data(self.data_list[self.nr])

    def write_data(self, data):
        self.ans_1.show()
        self.r_1.show()
        self.ans_2.show()
        self.r_2.show()
        self.ans_3.show()
        self.r_3.show()
        self.ans_4.show()
        self.r_4.show()
        self.ans_5.show()
        self.r_5.show()

        self.question_lbl.setText(str(self.nr+1) + ". "+data['question'])
        self.label.setText(data['subject'])
        if len(data['answers']) == 5:
            self.ans_1.setText(data['answers'][0])
            self.ans_2.setText(data['answers'][1])
            self.ans_3.setText(data['answers'][2])
            self.ans_4.setText(data['answers'][3])
            self.ans_5.setText(data['answers'][4])
        elif len(data['answers']) == 4:
            self.ans_1.setText(data['answers'][0])
            self.ans_2.setText(data['answers'][1])
            self.ans_3.setText(data['answers'][2])
            self.ans_4.setText(data['answers'][3])
            self.ans_5.hide()
            self.r_5.hide()
        elif len(data['answers']) == 3:
            self.ans_1.setText(data['answers'][0])
            self.ans_2.setText(data['answers'][1])
            self.ans_3.setText(data['answers'][2])
        else:
            self.ans_1.setText(data['answers'][0])
            self.ans_2.setText(data['answers'][1])

        if data['given_answ'] == 0:
            self.r_1.setChecked(True)
        elif data['given_answ'] == 1:
            self.r_2.setChecked(True)
        elif data['given_answ'] == 2:
            self.r_3.setChecked(True)
        elif data['given_answ'] == 3:
            self.r_4.setChecked(True)
        elif data['given_answ'] == 4:
            self.r_5.setChecked(True)
    
    def generate_question_id_list(self):
        return random.sample(range(0, 3086), 5)

    def read_question(self, id_list):
        data_list = []
        for id in id_list:
            sqliteConnection = sqlite3.connect('resources\\db\\data.db')
            cursor = sqliteConnection.cursor()
            sqlite_select_Query = "SELECT * FROM questions where id = '{}';".format(id)
            cursor.execute(sqlite_select_Query)
            question_data = cursor.fetchall()[0]  #[(78, "fgfgfhfghgu", 65)]

            sqlite_select_Query = "SELECT description FROM subjects where id = '{}';".format(question_data[2])
            cursor.execute(sqlite_select_Query)
            subject = cursor.fetchall()[0][0]  #[('78',),('asd'),('tyuio')]

            sqlite_select_Query = "SELECT description FROM answers where id_question = '{}';".format(question_data[0])
            cursor.execute(sqlite_select_Query)
            answers = cursor.fetchall()

            # Create list of answers
            answ_list = []
            for x in answers:
                answ_list.append(x[0])

            # Find correct answ index
            sqlite_select_Query = "SELECT description FROM answers where id = '{}';".format(question_data[3])
            cursor.execute(sqlite_select_Query)
            corr_ans_desc = cursor.fetchall()[0][0]
            corr_ans_indx = answ_list.index(corr_ans_desc)
            
            data = {
                'question': question_data[1],
                'answers': answ_list,
                'correct_answ': corr_ans_indx,
                'subject': subject,
                'given_answ': None
            }


            cursor.close()
            data_list.append(data)
        return data_list

    
    def clear_radio(self):
        self.RadioGroup.setExclusive(False)
        self.r_1.setChecked(False)
        self.r_2.setChecked(False)
        self.r_3.setChecked(False)
        self.r_4.setChecked(False)
        self.r_5.setChecked(False)
        self.RadioGroup.setExclusive(True)

    def go_home(self, state):
        msg = ""
        if state == 0:
            msg = "Jeni i sigurt se doni te anulloni testin?"
        else:
            msg = "Jeni i sigurt se do te perfundosh testin?"
        dlg = QMessageBox(self)
        dlg.setWindowTitle("KUJDES!")
        dlg.setText(msg)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Warning)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            if state == 0:
                self.a = Dashboard()
                self.a.show()
                self.close()
            else:
                self.a = TestResult(self.data_list)
                self.a.show()
                self.close()


from dashboard_contoller import Dashboard
from test_result_controller import TestResult