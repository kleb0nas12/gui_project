import sys
from layout import Ui_IslTipForma, Ui_Isleditforma
from database import MyDatabase
import main
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

# Laying out working logic for different widgets (dialog forms,boxes) for the application


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
        self.database.add_islaidos(_new_type, False)
        self.ch.nustatymai_screen()  # refreshing main screen to see updated table
        self.close()
# Islaidu-tipai edit dialog box functionality


class DialogEdit(QDialog, Ui_Isleditforma):
    def __init__(self, parent=None, data=None):
        QDialog.__init__(self, parent)
        self.data = data
        self.database = MyDatabase()
        self.ch = main.MainWindow()
        self.setupUi(self)
        # showing checked box if record in db is already 'active'
        if self.data[1] == 'Aktyvus':
            self.checkBox.setChecked()
        self.pushButton.clicked.connect(self.change_state)
        self.pushButton_2.clicked.connect(self.close)
        self.ch.nustatymai_screen()  # refreshing main screen to see updated table
    
    # method to change data record of active/inactive to a database
    def change_state(self):
        if self.checkBox.isChecked():
            self.database.change_active_status(self.data[0], True)
        else:
            self.database.change_active_status(self.data[0], False)
