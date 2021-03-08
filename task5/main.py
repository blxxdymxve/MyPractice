import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from random import randint
import design


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.array = []
        self.pushButton.clicked.connect(self.exec)
        self.radioButton.toggled.connect(self.hand_insert)
        self.radioButton_2.toggled.connect(self.random_insert)

    def hand_insert(self):
        radioButton = self.sender()

        if radioButton.isChecked():
            rows = self.spinBox.value()
            cols = self.spinBox_2.value()

            self.rows = rows
            self.cols = cols

            self.tableWidget.setRowCount(rows)
            self.tableWidget.setColumnCount(cols)

            for i in range(rows):
                for j in range(cols):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(0)))

    def random_insert(self):
        radioButton = self.sender()
        if radioButton.isChecked():

            rows = self.spinBox.value()
            cols = self.spinBox_2.value()

            self.rows = rows
            self.cols = cols

            self.tableWidget.setRowCount(rows)
            self.tableWidget.setColumnCount(cols)

            for i in range(rows):
                for j in range(cols):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(randint(-10, 10))))

    def exec(self):
        matrix = []

        for row in range(0, self.rows):
            arr = []
            for col in range(self.cols):
                item = self.tableWidget.item(row, col)
                arr.append(int(item.text()))
            matrix.append(arr)

        five_divisor_idx = [0, 0]
        for row in range(0, self.rows):
            isFound = False
            for col in range(0, self.cols):
                if (matrix[row][col] % 5 == 0):
                    five_divisor_idx = [row, col]
                    isFound = True
                    break
            if (isFound == True):
                break

        min_item_idx = [0, 0]
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if (matrix[row][col] < matrix[min_item_idx[0]][min_item_idx[1]]):
                    min_item_idx = [row, col]
                    break

        temp = matrix[five_divisor_idx[0]][five_divisor_idx[1]]
        matrix[five_divisor_idx[0]][five_divisor_idx[1]] = matrix[min_item_idx[0]][min_item_idx[1]]
        matrix[min_item_idx[0]][min_item_idx[1]] = temp

        for i in range(self.rows):
            for j in range(self.cols):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(matrix[i][j])))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()