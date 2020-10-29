import sys
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QDialog, QMainWindow
from layout import Ui_MainWindow
from database import MyDatabase
from PyQt5 import QtGui, QtWidgets
import widgets as wdg

#### Here we implement the main working structure of the application and laying out full working logic behind it ##########


class MainWindow:
    def __init__(self):
        # main window
        self.main_win = QMainWindow()  # quick QMainWindow access
        self.ui = Ui_MainWindow()  # quick layout access
        self.ui.setupUi(self.main_win)
        self.db = MyDatabase()  # initializing Postgres database connection and methods

#?### here we describe functionality of all input/interaction elements (buttons,menu fiels ect.) ####

        # menu buttons
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageNoData)  # if db connection inactive
        # pradzia menu button, sets screen to pradzia
        self.ui.pushButton.clicked.connect(self.pradzia_screen)
        # nustatymai menu button, sets screen to nustatymai -> islaidu-tipai
        self.ui.pushButton_2.clicked.connect(self.nustatymai_screen)
        # islaidos menu button, sets screen to islaidos -> islaidos
        self.ui.pushButton_3.clicked.connect(self.islaidos_screen)
        # 'prideti tipa' button calls islaidu_tipai dialog
        self.ui.pushButton_4.clicked.connect(self.islaidu_dialog)

        # islaidu-tipai table
        # disabling double click editing by default
        self.ui.tableWidgetIslaidos.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        # getting values of a selected row and passing to the editor screen
        self.ui.tableWidgetIslaidos.itemDoubleClicked.connect(self.isl_data)
#?###############################################################################################

    #### main screens menu-elements/buttons functionality ########
    def pradzia_screen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)

    def nustatymai_screen(self):
        self.load_data_islaidos()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageNustatymai)
        # self.ui.tableWidgetIslaidos.viewport().repaint()

    def islaidos_screen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageIslaidos)
    ###############################################################

    ############### dialog functionality ##########################
    # islaidu_tipai dialog pop-up
    def islaidu_dialog(self):
        _ap = wdg.Dialog()
        _ap.exec_()

    # islaidu-tipai edit widget
    def isl_data(self):
        # getting current clicked row value,data=None
        def _getting_data() -> str:
            _ind = (self.ui.tableWidgetIslaidos.currentRow())
            _row_data = self.ui.tableWidgetIslaidos.item(
                _ind, 0).text()  # (_ind - row, 0 - column)
            return _row_data
        _app = wdg.DialogEdit(data=_getting_data())
        _app.exec_()

    ###############################################################

    #!####### data laoding into the nustatymai page (islaidu_tipai) table, refreshed every single time screen methods are called ################################

    def load_data_islaidos(self):
        # changing bool value from db to aktyvus/neaktyvus
        def _boolean_convert(item: bool) -> str:
            if item == True:
                return 'Aktyvus'
            else:
                return 'Neaktyvus'

        try:
            _data = self.db.islaidos_query()  # getting data,already ordered
            print(_data)  # !## delete #####
            if len(_data) == 0:
                pass
            else:
                # setting exact number of rows to populate into the table widget
                self.ui.tableWidgetIslaidos.setRowCount(len(_data))
                row = 0
                for val in _data:
                    # populating data into rows
                    self.ui.tableWidgetIslaidos.setItem(
                        row, 0, QtWidgets.QTableWidgetItem(str(val[1])))
                    self.ui.tableWidgetIslaidos.setItem(
                        row, 1, QtWidgets.QTableWidgetItem(_boolean_convert(val[2])))
                    row += 1
        except Exception as e:
            print(e)

    #  method to show output

    def show_main(self):
        self.main_win.show()


if __name__ == '__main__':
    # application setup
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show_main()
    sys.exit(app.exec_())
