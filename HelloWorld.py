import sys
import random
from PySide6 import QtCore as core
from PySide6 import QtWidgets as widg
from PySide6 import QtGui as gui


class MyWidget(widg.QWidget):
  def __init__(self):
    super().__init__()

    self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

    self.button = widg.QPushButton("Click me!")
    self.text = widg.QLabel("Hello World", alignment=core.Qt.AlignCenter)

    self.layout = widg.QVBoxLayout(self)
    self.layout.addWidget(self.text)
    self.layout.addWidget(self.button)

    self.button.clicked.connect(self.magic)
  # @QtCore.Slot()
  def magic(self):
    self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = widg.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    app.exec()
    # sys.exit(app.exec())

app = widg.QApplication([])
label = widg.QLabel('<h1 color=red>Hello World!</h1>')
label.show()
app.exec()
