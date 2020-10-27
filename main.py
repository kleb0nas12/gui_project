import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from layout import Ui_MainWindow
from database import MyDatabase
from PyQt5 import QtWidgets

#### Here we implement the main working structure of the application and laying out full working logic behind it ##########


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()  # quick QMainWindow access
        self.ui = Ui_MainWindow()  # quick layout access
        self.db = MyDatabase()  # initializing Postgres database connection and methods
        self.ui.setupUi(self.main_win)


#?### here we describe main screens (pradzia,nustatymai,islaidos) and implement functionality ####
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageNoData)
        self.ui.pushButton.clicked.connect(self.pradzia_screen)
        self.ui.pushButton_2.clicked.connect(self.nustatymai_screen)
        self.ui.pushButton_3.clicked.connect(self.islaidos_screen)
#?###############################################################################################

    #### main screens menu-elements/buttons functionality ########
    def pradzia_screen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)

    def nustatymai_screen(self):
        self.load_data_islaidos()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageNustatymai)

    def islaidos_screen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageIslaidos)
    ###############################################################

    #!####### data laoding into the nustatymai page (islaidu_tipai) table, refreshed every single time screen methods are called ################################

    def load_data_islaidos(self):
        ## changing bool value from db to aktyvus/neaktyvus 
        def _boolean_convert(item : bool) -> str:
            if item == True:
                return 'Aktyvus'
            else:
                return 'Neaktyvus'

        try:
            _data = self.db.islaidos_query() # getting data,already ordered 
            self.ui.tableWidgetIslaidos.setRowCount(len(_data)) # setting exact number of rows to populate into the table widget
            row = 0
            for val in _data:
                self.ui.tableWidgetIslaidos.setItem(row, 0 , QtWidgets.QTableWidgetItem(str(val[1])))
                self.ui.tableWidgetIslaidos.setItem(row, 1 , QtWidgets.QTableWidgetItem(_boolean_convert(val[2])))
                row += 1
        except Exception as e:
            print(e)
        



    #  method to show output
    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    # application setup
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
