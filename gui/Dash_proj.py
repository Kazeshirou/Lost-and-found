from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Engine import Engine

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.engine = Engine(self.first_table, self.second_table)
        self.UndoBatton.clicked.connect(self.engine.button_update_clicked)
        self.first_table.cellClicked.connect(self.engine.update_found_table)
       



    def __init_ui(self):
        self.setGeometry(100,100, 1200, 500)
        self.setWindowTitle('GPX Viewer')
        
        self.first_table = QtWidgets.QTableWidget(self)
        self.first_table.setGeometry(10,10,500,400)
        self.first_table.setColumnCount(4)
        self.first_table.setHorizontalHeaderLabels(["id","Текст","Дата","Ссылка VK"])

        self.second_table = QtWidgets.QTableWidget(self)
        self.second_table.setGeometry(520,10,500,400)
        self.second_table.setColumnCount(4)
        self.second_table.setHorizontalHeaderLabels(["id","Текст","Дата","Ссылка VK"])

        self.first_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.second_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.first_table.setColumnWidth(0,30)
        self.first_table.setColumnWidth(1,300)


        self.second_table.setColumnWidth(0,30)
        self.second_table.setColumnWidth(1,300)

        self.UndoBatton = QtWidgets.QPushButton("Обновить",self)
        self.UndoBatton.move(10,450)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = UI()
    MainWindow.show()

    sys.exit(app.exec_())
