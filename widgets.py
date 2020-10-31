import sys
from datetime import datetime
from layout import Ui_IslTipForma, Ui_Isleditforma, Ui_IslaidosForma
from database import MyDatabase
import main
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore

# Laying out working logic for different widgets (dialog forms,boxes) for the application
#?#######################################################################################

# Dialog box (naujo tipo ivedimas)  functionality


class Dialog(QDialog, Ui_IslTipForma):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.database = MyDatabase()
        self.ch = main.MainWindow()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_isl_tipa)
        self.pushButton_2.clicked.connect(self.close)

    # adding new 'islaidu tipas' to database
    def add_isl_tipa(self):
        _new_type: str = self.lineEdit.text()
        self.database.add_islaidos_tipai(_new_type, False)
        self.ch.nustatymai_screen()  # refreshing main screen to see updated table
        self.close()

#?#######################################################################################
# Islaidu-tipai edit dialog box functionality


class DialogEdit(QDialog, Ui_Isleditforma):
    def __init__(self, parent=None, data=None):
        QDialog.__init__(self, parent)
        self._data = data
        self.db = MyDatabase()
        self.ch = main.MainWindow()
        self.setupUi(self)

        # showing checked box if record in db is already 'active'
        # setting current type record to the edit box screen
        self.lineEdit.setText('{}'.format(self._data[0]))
        if self.data[1] == 'Aktyvus':
            self.checkBox.setChecked(True)
        self.pushButton.clicked.connect(self.change_state)
        self.pushButton_2.clicked.connect(self.close)
        # self.ch.nustatymai_screen()  # refreshing main screen to see updated table

    # method to change data record of active/inactive and/or type to a database
    def change_state(self):
        try:
            if self._data[0] != self.lineEdit.text():  # if user edit type name
                _edited_type = self.lineEdit.text()
                if self.checkBox.isChecked() == True:
                    self.db.change_active_status(
                        self._data[0], _edited_type, True)
                else:
                    self.db.change_active_status(
                        self._data[0], _edited_type, False)
            else:
                if self.checkBox.isChecked() == True:
                    self.db.change_active_status(
                        self._data[0], self._data[0], True)
                else:
                    self.db.change_active_status(
                        self._data[0], self._data[0], False)
        except Exception as e:
            print(e)
        self.close()
#?#######################################################################################
# Dialog box (nauju islaidu ivedimas)  functionality


class DialogIslaidos(QDialog, Ui_IslaidosForma):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.database = MyDatabase()
        self.ch = main.MainWindow()
        self.setupUi(self)
        # setting calendar pop ups to current dates
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # adding islaidu tipus to choose combo box
        self.comboBox.addItems(self.database.get_box_info())
        # Ivesti nauja button calls add_new_type widget from nustatymai (menu)- > add new type
        self.pushButton_3.clicked.connect(self._call_isl_tipai)
        # saving new islaidos to database
        self.pushButton.clicked.connect(self.add_islaidos_info)
        self.pushButton_2.clicked.connect(self.close)

    def _call_isl_tipai(self):
        _app = Dialog()
        _app.exec_()

    def add_islaidos_info(self):
        # self.database.islaidos_query()
        try:
            def _check_data() -> str:  # checking which option is checked / chosen for date element
                if self.lineEdit.text():
                    _date = self.lineEdit.text()  # if date entered manually
                elif self.checkBox.isChecked():
                    _date = datetime.now().strftime('%Y-%m-%d')
                else:
                    _date = self.dateEdit.date().toString(QtCore.Qt.ISODate)
                return _date
            _type_chosen = self.comboBox.currentText()
            _tiekejas = self.lineEdit_2.text()
            _doc_nr = self.lineEdit_3.text()
            _suma = float(self.lineEdit_4.text())  # !### finish this after all
            self.database.add_islaidos(
                _check_data(), _type_chosen, _tiekejas, _doc_nr, _suma)
            self.close()
        except Exception as e:
            print(e)



# Dialog edit box (nauju islaidu ivedimas)  functionality


class DialogIslaidosEdit(QDialog, Ui_IslaidosForma):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent,)
        self.database = MyDatabase()
        self.ch = main.MainWindow()
        self.setupUi(self)
        # setting calendar pop ups to current dates
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # adding islaidu tipus to choose combo box
        self.comboBox.addItems(self.database.get_box_info())
        # Ivesti nauja button calls add_new_type widget from nustatymai (menu)- > add new type
        self.pushButton_3.clicked.connect(self._call_isl_tipai)
        # saving new islaidos to database
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.close)

    def _call_isl_tipai(self):
        _app = Dialog()
        _app.exec_()

    def update_islaidos_info(self):
        # self.database.islaidos_query()
        try:
            def _check_data() -> str:  # checking which option is checked / chosen for date element
                if self.lineEdit.text():
                    _date = self.lineEdit.text()  # if date entered manually
                elif self.checkBox.isChecked():
                    _date = datetime.now().strftime('%Y-%m-%d')
                else:
                    _date = self.dateEdit.date().toString(QtCore.Qt.ISODate)
                return _date
            _type_chosen = self.comboBox.currentText()
            _tiekejas = self.lineEdit_2.text()
            _doc_nr = self.lineEdit_3.text()
            _suma = float(self.lineEdit_4.text())  # !### finish this after all
            self.database.add_islaidos(
                _check_data(), _type_chosen, _tiekejas, _doc_nr, _suma)
            self.close()
        except Exception as e:
            print(e)


#?#######################################################################################
