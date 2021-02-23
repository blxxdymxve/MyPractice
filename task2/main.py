<<<<<<< Updated upstream
import sys
from PyQt5 import QtWidgets, QtCore
import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton.clicked.connect(self.calculator)

    def calculator(self):
        textBoxValue = self.lineEdit.text()
        """if int(textBoxValue) % 400 == 0 or int(textBoxValue) % 4 == 0:
            self.label_2.setText("Год является високосным")
        else:
            self.label_2.setText("Год не является високосным")"""

        if int(textBoxValue) % 4 == 0:
            if int(textBoxValue) % 100 and int(textBoxValue) % 400:
                self.label_2.setText("Год является високосным")
            elif int(textBoxValue) % 4 == 0:
                self.label_2.setText("Год является високосным")
            else:
                self.label_2.setText("Год не является високосным")
        else:
            self.label_2.setText("Год не является високосным")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
=======
import sys
from PyQt5 import QtWidgets, QtCore
import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton.clicked.connect(self.calculator)

    def calculator(self):
        textBoxValue = self.lineEdit.text()
        """if int(textBoxValue) % 400 == 0 or int(textBoxValue) % 4 == 0:
            self.label_2.setText("Год является високосным")
        else:
            self.label_2.setText("Год не является високосным")"""

        if int(textBoxValue) % 4 == 0:
            if int(textBoxValue) % 100 and int(textBoxValue) % 400:
                self.label_2.setText("Год является високосным")
            elif int(textBoxValue) % 4 == 0:
                self.label_2.setText("Год является високосным")
            else:
                self.label_2.setText("Год не является високосным")
        else:
            self.label_2.setText("Год не является високосным")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
>>>>>>> Stashed changes
