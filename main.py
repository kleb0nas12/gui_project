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

#?### here we describe functionality of all input/interaction elements (buttons,menu fiels ect.) of the main page  ####

        # menu and other main screen buttons
        self.ui.stackedWidget.setCurrentWidget(
            self.ui.pageHome)  #
        # pradzia menu button, sets screen to pradzia
        self.ui.pushButton.clicked.connect(self.pradzia_screen)
        # nustatymai menu button, sets screen to nustatymai -> islaidu-tipai
        self.ui.pushButton_2.clicked.connect(self.nustatymai_screen)
        # islaidos menu button, sets screen to islaidos -> islaidos
        self.ui.pushButton_3.clicked.connect(self.islaidos_screen)
        # 'prideti tipa' button calls islaidu_tipai dialog
        self.ui.pushButton_4.clicked.connect(self.islaidu_dialog)
        # 'prideti islaidas' button calls islaidos dialog
        self.ui.pushButton_7.clicked.connect(self.islaidos)
        # Pradzia screen -> prideti islaidas button calls islaidu add_forma
        self.ui.pushButtonIslaidosMain.clicked.connect(self.islaidos)

        # islaidu-tipai table
        # disabling double click editing by default on islaidu-tipai table
        self.ui.tableWidgetIslaidos.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        # getting values of a selected row and passing to the editor screen
        self.ui.tableWidgetIslaidos.itemDoubleClicked.connect(self.isl_data)

        # islaidos table
        # disabling double click editing by default on islaidos table
        self.ui.tableWidgetMain.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        # getting values of a selected row and passing to the editor screen
        self.ui.tableWidgetMain.itemDoubleClicked.connect(self.islaidos_edit)


#?###############################################################################################

    #### main screens menu-elements/buttons functionality ########


    def pradzia_screen(self):
        _wsum = self.db.whole_month_sum()
        self.ui.label_2.setText("{} €".format(_wsum))
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)

    def nustatymai_screen(self):
        self.db.islaidos_query()
        self.load_islaidos_tipai()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageNustatymai)
        # self.ui.tableWidgetIslaidos.viewport().repaint()

    def islaidos_screen(self):
        self.load_islaidos()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageIslaidos)
    ###############################################################

    ############### dialog functionality ##########################
    # islaidu_tipai dialog pop-up
    def islaidu_dialog(self):
        _app = wdg.Dialog()
        _app.exec_()

    # islaidu-tipai edit widget pop-up
    def isl_data(self):
        # getting current clicked row value,data=None
        def _getting_data() -> list:
            _ind = self.ui.tableWidgetIslaidos.currentRow()
            _row_data_type = self.ui.tableWidgetIslaidos.item(
                _ind, 0).text()  # (_ind - row, 0 - column)
            _row_data_status = self.ui.tableWidgetIslaidos.item(
                _ind, 1).text()  # (_ind - row, 1 - column)
            return [_row_data_type, _row_data_status]
        _app = wdg.DialogEdit(data=_getting_data())
        _app.exec_()

    # islaidos dialog pop-up
    def islaidos(self):
        _app = wdg.DialogIslaidos()
        _app.exec_()

    # islaidos edit widget pop-up
    def islaidos_edit(self):
        def _get_curr_data() -> list:  # getting current filled data into edit (islaidos) box
            _index = self.ui.tableWidgetMain.currentRow()
            _data = self.ui.tableWidgetMain.item(_index, 0).text()
            _tipas = self.ui.tableWidgetMain.item(_index, 1).text()
            _tiekejas = self.ui.tableWidgetMain.item(_index, 2).text()
            _dok_nr = self.ui.tableWidgetMain.item(_index, 3).text()
            _sum = self.ui.tableWidgetMain.item(_index, 4).text()
            return [_data, _tipas, _tiekejas, _dok_nr, _sum]
        _app = wdg.DialogIslaidosEdit(data=_get_curr_data())
        _app.exec_()

    ###############################################################

    #!####### data laoding into data tables: islaidu tipai and islaidos screen ################################
    # data population to lsaidu_tipai data screen/widget

    def load_islaidos_tipai(self):
        # changing bool value from db to aktyvus/neaktyvus
        def _boolean_convert(item: bool) -> str:
            if item == True:
                return 'Aktyvus'
            else:
                return 'Neaktyvus'

        try:
            _data = self.db.islaidos_tipai_query()  # getting data,already ordered
            if len(_data) == 0:
                pass
            else:
                # setting exact number of rows to populate into the table widget
                self.ui.tableWidgetIslaidos.setRowCount(len(_data))
                _row = 0
                for val in _data:
                    # populating data into rows
                    self.ui.tableWidgetIslaidos.setItem(
                        _row, 0, QtWidgets.QTableWidgetItem(str(val[1])))
                    self.ui.tableWidgetIslaidos.setItem(
                        _row, 1, QtWidgets.QTableWidgetItem(_boolean_convert(val[2])))
                    _row += 1
        except Exception as e:
            print(e)

    # data population to islaidos data screen/widgets
    def load_islaidos(self):
        try:
            _data = self.db.islaidos_query()  # getting data,already ordered by date
            if (len(_data) == 0):
                pass
            else:
                self.ui.tableWidgetMain.setRowCount(len(_data)+1)
                _row = 0
                _sum: float = 0
                for inf in _data:  # populating data to islaidos table
                    self.ui.tableWidgetMain.setItem(
                        _row, 0, QtWidgets.QTableWidgetItem(str(inf[1])))
                    self.ui.tableWidgetMain.setItem(
                        _row, 1, QtWidgets.QTableWidgetItem(str(inf[2])))
                    self.ui.tableWidgetMain.setItem(
                        _row, 2, QtWidgets.QTableWidgetItem(str(inf[3])))
                    self.ui.tableWidgetMain.setItem(
                        _row, 3, QtWidgets.QTableWidgetItem(str(inf[4])))
                    self.ui.tableWidgetMain.setItem(
                        _row, 4, QtWidgets.QTableWidgetItem(str(inf[5])))
                    self.btn_del = QtWidgets.QPushButton('Delete')
                    # adding delete button to last row cell
                    self.ui.tableWidgetMain.setCellWidget(
                        _row, 5, self.btn_del)
                    _row += 1
                    _sum += float(inf[5])
                self.ui.tableWidgetMain.setItem(
                    _row, 3, QtWidgets.QTableWidgetItem('Viso:'))  # showing extra row label
                self.ui.tableWidgetMain.setItem(
                    _row, 4, QtWidgets.QTableWidgetItem(str(round(_sum, 2))))  # showing whole sum for current selection of data expenses
                self.ui.tableWidgetMain.verticalHeader().setSectionResizeMode(
                    _row, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as e:
            print(e)

    #!############################################################################################################
    #  method to show output

    def show_main(self):
        self.main_win.show()


if __name__ == '__main__':
    # application setup
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show_main()
    sys.exit(app.exec_())
