import sys
from PySide6.QtWidgets import QApplication,QPushButton
from PySide6.QtCore import Slot

@Slot()
def sayHello():
  print("Button Clicked. Hello!")

app = QApplication([])
button = QPushButton("Click me!")
button.clicked.connect(sayHello)

button.show()
app.exec()