import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from layout import Ui_MainWindow
from database import MyDatabase

#### Here we implement the main working structure of the application and laying out full working logic behind it ##########
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()  # quick QMainWindow access
        self.ui = Ui_MainWindow()  # quick layout access
        self.db = MyDatabase()  # initializing Postgres database connection and methods
        self.ui.setupUi(self.main_win)
        self.db.islaidos_query()


####### here we describe main screens (pradiza,nustatymai,islaidos) and implement functionality ########
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageNoData)

        self.ui.pushButton.clicked.connect(self.pradzia_screen)
        self.ui.pushButton_2.clicked.connect(self.nustatymai_screen)
        self.ui.pushButton_3.clicked.connect(self.islaidos_screen)
################################################################################################
    def pradzia_screen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)

    def nustatymai_screen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageNustatymai)

    def islaidos_screen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageIslaidos)
    # method to show output

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    # application setup
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
