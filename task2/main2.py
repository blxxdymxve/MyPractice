<<<<<<< Updated upstream
import sys
from PyQt5 import QtWidgets, QtCore
import design2

class ExampleApp(QtWidgets.QMainWindow, design2.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton.clicked.connect(self.calculator)

    def calculator(self):
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()

        x = int(x)
        y = int(y)

        many = []
        for s in range(x, y+1):
            if s % 400 == 0:
                many.append(str(s))
            else:
                if s % 4 == 0:
                    many.append(str(s))
                else:
                    pass
        many = ", ".join(many)

        self.label_2.setText(many)

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
import design2

class ExampleApp(QtWidgets.QMainWindow, design2.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton.clicked.connect(self.calculator)

    def calculator(self):
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()

        x = int(x)
        y = int(y)

        many = []
        for s in range(x, y+1):
            if s % 400 == 0:
                many.append(str(s))
            else:
                if s % 4 == 0:
                    many.append(str(s))
                else:
                    pass
        many = ", ".join(many)

        self.label_2.setText(many)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
>>>>>>> Stashed changes
