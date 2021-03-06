import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui


# Initialize class Calculator
class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

# Load interface and define all 18 calculator inputs
    def initUI(self):
        self.ui = uic.loadUi("calculator.ui", self)
        self.show()
        self.ui.button1.clicked.connect(self.method_1)
        self.ui.button2.clicked.connect(self.method_2)
        self.ui.button3.clicked.connect(self.method_3)
        self.ui.button4.clicked.connect(self.method_4)
        self.ui.button5.clicked.connect(self.method_5)
        self.ui.button6.clicked.connect(self.method_6)
        self.ui.button7.clicked.connect(self.method_7)
        self.ui.button8.clicked.connect(self.method_8)
        self.ui.button9.clicked.connect(self.method_9)
        self.ui.button0.clicked.connect(self.method_0)
        self.ui.buttonclear.clicked.connect(self.method_clear)
        self.ui.buttondelete.clicked.connect(self.method_delete)
        self.ui.buttondiv.clicked.connect(self.method_div)
        self.ui.buttonminus.clicked.connect(self.method_minus)
        self.ui.buttonmult.clicked.connect(self.method_mult)
        self.ui.buttonplus.clicked.connect(self.method_plus)
        self.ui.dot.clicked.connect(self.method_dot)
        self.ui.pushButton.clicked.connect(self.method_result)

    # Define all methods for text input
    def method_1(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "1")
        print(text + "1")

    def method_2(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "2")
        print(text + "2")

    def method_3(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "3")
        print(text + "3")

    def method_4(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "4")
        print(text + "4")

    def method_5(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "5")
        print(text + "5")

    def method_6(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "6")
        print(text + "6")

    def method_7(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "7")
        print(text + "7")

    def method_8(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "8")
        print(text + "8")

    def method_9(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "9")
        print(text + "9")

    def method_0(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "0")
        print(text + "0")

    def method_dot(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + ".")
        print(text + ".")

    def method_plus(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "+")
        print(text + "+")

    def method_minus(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "-")
        print(text + "-")

    def method_mult(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "*")
        print(text + "*")

    def method_div(self):
        text = self.output_Results.text()
        self.output_Results.setText(text + "/")
        print(text + "/")

    def method_clear(self):
        self.output_Results.setText("")
        print("")

    def method_delete(self):
        text = self.output_Results.text()
        self.output_Results.setText(text[:len(text) - 1])
        print(text[:len(text) - 1])

    def method_result(self):
        text = self.output_Results.text()

        try:
            result = eval(text)
            self.output_Results.setText(str(result))
            print(result)
        except Exception:
            self.output_Results.setText("This input can't be calculated")
            print("Sorry, this input can't be calculated")

    # Implement key inputs for all relevant buttons
    def keyPressEvent(self, event):
        if event.text() == '1':
            text = self.output_Results.text()
            self.output_Results.setText(text + "1")
            print(text + "1")
        if event.text() == '2':
            text = self.output_Results.text()
            self.output_Results.setText(text + "2")
            print(text + "2")
        if event.text() == '3':
            text = self.output_Results.text()
            self.output_Results.setText(text + "3")
            print(text + "3")
        if event.text() == '4':
            text = self.output_Results.text()
            self.output_Results.setText(text + "4")
            print(text + "4")
        if event.text() == '5':
            text = self.output_Results.text()
            self.output_Results.setText(text + "5")
            print(text + "5")
        if event.text() == '6':
            text = self.output_Results.text()
            self.output_Results.setText(text + "6")
            print(text + "6")
        if event.text() == '7':
            text = self.output_Results.text()
            self.output_Results.setText(text + "7")
            print(text + "7")
        if event.text() == '8':
            text = self.output_Results.text()
            self.output_Results.setText(text + "8")
            print(text + "8")
        if event.text() == '9':
            text = self.output_Results.text()
            self.output_Results.setText(text + "9")
            print(text + "9")
        if event.text() == '0':
            text = self.output_Results.text()
            self.output_Results.setText(text + "0")
            print(text + "0")
        if event.text() == '.':
            text = self.output_Results.text()
            self.output_Results.setText(text + ".")
            print(text + ".")
        if event.text() == '+':
            text = self.output_Results.text()
            self.output_Results.setText(text + "+")
            print(text + "+")
        if event.text() == '-':
            text = self.output_Results.text()
            self.output_Results.setText(text + "-")
            print(text + "-")
        if event.text() == '*':
            text = self.output_Results.text()
            self.output_Results.setText(text + "*")
            print(text + "*")
        if event.text() == '/':
            text = self.output_Results.text()
            self.output_Results.setText(text + "/")
            print(text + "/")
        if event.text() == 'd':
            text = self.output_Results.text()
            self.output_Results.setText(text[:len(text) - 1])
            print(text[:len(text) - 1])
        if event.text() == 'c':
            self.output_Results.setText("")
            print("")
        if event.text() == '=':
            text = self.output_Results.text()

            try:
                result = eval(text)
                self.output_Results.setText(str(result))
                print(result)
            except Exception:
                self.output_Results.setText("This input can't be calculated")
                print("Sorry, this input can't be calculated")


def main():

    app = QtWidgets.QApplication(sys.argv)
    cnt = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
