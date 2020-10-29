import sys
sys.path.insert(0, 'A:\gui_project')
from layout import Ui_IslTipForma
from database import MyDatabase
import main
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

### Laying out working logic for 'islaidu-tipai prideti' field 
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
