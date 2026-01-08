from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QWidget,
)

class NumButton(QPushButton):
    def __init__(self, n, calc):
        super().__init__(str(n))
        self.calc = calc
        self.pressed.connect(self.push)

    def push(self):
        self.calc.current.setText(self.calc.current.text() + str(self.text()))

class AddButton(QPushButton):
    def __init__(self, calc):
        super().__init__('Add')
        self.calc = calc
        self.pressed.connect(self.push)

    def push(self):
        if self.calc.sum.text() == '':
            self.calc.sum.setText('0')
        self.calc.sum.setText(str(int(self.calc.sum.text()) + int(self.calc.current.text())))
        self.calc.current.setText('')

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sum = QLabel('')
        self.current = QLineEdit()
        # Rows
        layout1 = QVBoxLayout()
        layout1.addWidget(self.sum)
        layout1.addWidget(self.current)
        # Grid
        layout2 = QGridLayout()
        for i in range(1, 10):
            layout2.addWidget(NumButton(i, self), 2 - ((i-1) // 3), (i-1) % 3)
        layout2.addWidget(NumButton(0, self), 3, 0)
        layout2.addWidget(AddButton(self), 3, 1, 1, 2)
        grid = QWidget()
        grid.setLayout(layout2)
        layout1.addWidget(grid)
        # Overall widget
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication([])
window = Calc()
window.show()
app.exec()