import sys
sys.path.insert(0,'A:\gui_project')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from layout import Ui_IslTipForma


class TipaiWidget:
    def __init__(self):
        print('As cia')
        self.widget = QtWidgets.QWidget()
        self.ui = Ui_IslTipForma()
        self.ui.setupUi(self.widget)

        
        
        
        self.ui.pushButton_2.clicked.connect(self.psh)
        self.launch()
        print('As cia ir vel')
    def psh(self):
        print('Pavyko')
        sys.exit(0)

    def show(self):
        self.widget.show()

    def launch(self):
        if __name__ == '__main__':
            app = QtWidgets.QDialog(sys.argv)
            main_win_screen = TipaiWidget()
            main_win_screen.show()
            sys.exit(app.exec_())



