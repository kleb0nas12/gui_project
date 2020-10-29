import sys
from layout import Ui_IslTipForma, Ui_Isleditforma
from database import MyDatabase
import main
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

### Laying out working logic for different widgets (dialog forms,boxes) for the application



#### Dialog box (naujo tipo ivedimas) functionality
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
        _new_type :str = self.lineEdit.text()
        print(_new_type)
        self.database.add_islaidos(_new_type,False)
        self.ch.nustatymai_screen() # refreshing main screen to see updated table
        self.close()

class DialogEdit(QDialog, Ui_Isleditforma):
    def __init__(self, parent=None, data=None):
        QDialog.__init__(self, parent)
        self.data = data
        self.database = MyDatabase()
        self.ch = main.MainWindow()
        self.setupUi(self)
        print(self.data)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.close)
    