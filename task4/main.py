import sys
from PyQt5 import QtGui,QtWidgets
from random import randint
import array
import design

class TableModel(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arr = []
        self.new_arr = []
        self.radioButton.toggled.connect(self.byHand)
        self.radioButton_2.toggled.connect(self.random)
        self.pushButton_2.clicked.connect(self.button)
        self.pushButton.clicked.connect(self.calculator)

    def byHand(self):
        radioButton = self.sender()
        if radioButton.isChecked():

            value = self.spinBox.value()

            self.arr = array.array('i', [0]) * value
            model = QtGui.QStandardItemModel()
            items = [(self.arr)]

            for row_number, row_data in enumerate(items):
                tableItem = []
                model.insertRow(row_number)
                for value in row_data:
                    item = QtGui.QStandardItem(str(value))
                    tableItem.append(item)
                model.insertRow(row_number, tableItem)

            self.tableView.setModel(model)

    def random(self):
        radioButton = self.sender()
        if radioButton.isChecked():

            value = self.spinBox.value()
            self.new_arr = [randint(-10, 10) for i in range(value)]
            model = QtGui.QStandardItemModel()
            items = [(self.new_arr)]

            for row_number, row_data in enumerate(items):
                tableItem = []
                model.insertRow(row_number)
                for value in row_data:
                    item = QtGui.QStandardItem(str(value))
                    tableItem.append(item)
                model.insertRow(row_number, tableItem)

            self.tableView.setModel(model)

    def button(self):
        x = 0
        row = self.tableView.currentIndex().row()
        for i in range(self.spinBox.value()):
            self.new_arr.append(int(self.tableView.model().index(row, x).data()))
            x = x + 1
            i = i + 1

    def calculator(self):
        firstIndex = 0
        lastIndex = 0
        for i, elem in enumerate(self.new_arr):
            if elem < 0:
                firstIndex = i
                self.label_6.setText(str(int(firstIndex) + 1))
                break

        idx = []
        for i in range(len(self.new_arr)):
            if (self.new_arr[i] < 0):
                idx.append(i)
        lastIndex = max(idx)
        self.label_7.setText(str(int(lastIndex) + 1))

        sum = 1
        firstIndex = firstIndex + 1
        for i, elem in enumerate(self.new_arr[firstIndex:lastIndex]):
            sum = sum*elem
        self.label_8.setText(str(sum))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TableModel()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()