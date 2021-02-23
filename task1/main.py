<<<<<<< Updated upstream
import sys
from PyQt5 import QtWidgets
import design
import math

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculator)

    def calculator(self):
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        textBoxValue = self.lineEdit.text()
        x = self.lineEdit_2.text()
        x = float(x)

        if (float(textBoxValue) <= 0 or float(textBoxValue) >= 1):
            self.label_11.setText("Error!")
        else:
            textBoxValue = textBoxValue[2:]
            n = 0
            row = 0
            row = float(row)
            while n <= len(textBoxValue):
                row = row + ((-1)**n*x**(2*n))*x / math.factorial(2*n+1)
                n = n+1 

            self.label_8.setText(str(math.sin(x)))
            self.label_9.setText(str(row))
            self.label_10.setText(str(len(textBoxValue)))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
=======
import sys
from PyQt5 import QtWidgets
import design
import math

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculator)

    def calculator(self):
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        textBoxValue = self.lineEdit.text()
        x = self.lineEdit_2.text()
        x = float(x)

        if (float(textBoxValue) <= 0 or float(textBoxValue) >= 1):
            self.label_11.setText("Error!")
        else:
            textBoxValue = textBoxValue[2:]
            n = 0
            row = 0
            row = float(row)
            while n <= len(textBoxValue):
                row = row + ((-1)**n*x**(2*n))*x / math.factorial(2*n+1)
                n = n+1 

            self.label_8.setText(str(math.sin(x)))
            self.label_9.setText(str(row))
            self.label_10.setText(str(len(textBoxValue)))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
>>>>>>> Stashed changes
    main()