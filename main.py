import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MyApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self) -> None:
        self.layout = QVBoxLayout()

        self.label = QLabel("Press & Input 1 for +, 2 for -, 3 for *, 4 for /. Second field means A(first number), 3rd one is B(Second number)")

        self.input_field = QLineEdit(self)
        self.input_fieldA = QLineEdit(self)
        self.input_fieldB = QLineEdit(self)

        self.button = QPushButton("Calculate", self)
        self.button.clicked.connect(self.on_button_click)


        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.input_fieldA)
        self.layout.addWidget(self.input_fieldB)
        #self.input_fieldA.setVisible(False)
        #self.input_fieldB.setVisible(False)

        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def on_button_click(self) -> None:
        text = self.input_field.text()
        global textA
        global textB
        textA = 0
        textB = 0
        self.button.setVisible(False)
        cycle = 0
        while cycle != 2:
            if self.input_fieldA.text() != "":
                textA = int(self.input_fieldA.text())
                cycle += 1

            if self.input_fieldB.text() != "":
                textB = int(self.input_fieldB.text())
                cycle += 1

        if cycle == 2:
            actionChooser(int(text), textA, textB)
        print(text)

#print("Press & Input 1 for +, 2 for -, 3 for *, 4 for /")
#actionInput = int(input())
#answer = 0
def minus(a, b):
    global answer
    answer = a - b
    print("A minus B = ",answer)

def plus(a, b):
    global answer
    answer = a + b
    print("A plus B = ", answer)

def multiply(a, b):
    global answer
    answer = a * b
    print("A multiply B = ", answer)

def devide(a, b):
    global answer
    answer = a / b
    print("A devide B = ", answer)

def actionChooser(actionInput,a,b):
    if actionInput == 2:
        print("Now input number A and number B")
        minus(int(a), int(b))
    if actionInput == 1:
        print("Now input number A and number B")
        plus(int(a), int(b))
    if actionInput == 3:
        print("Now input number A and number B")
        multiply(int(a), int(b))
    if actionInput == 4:
        print("Now input number A and number B")
        devide(int(a), int(b))



app = QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())

