import sys
import random

import PyQt6.QtCore as QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import ( QWidget, QApplication, QMainWindow, QLabel,
                             QPushButton, QVBoxLayout)


# Subclass QMainWindow to customize your application's main window
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())