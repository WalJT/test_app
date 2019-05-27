# This is my first PyQt5 app..

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout

def close_when_clicked():
    app.Close()

# Create Application
app = QApplication([])

# Use a Custom Style
#app.setStyle("fusion")

# Using style sheet to modify button margins
app.setStyleSheet("QPushButton { margin: 10px; }")

# Add Label
#label = QLabel("Hello World")

# Modifications to Colour Pallet
# palette = QPalette()
# palette.setColor(QPalette.ButtonText, Qt.black)
# palette.setColor(QPalette.Button, Qt.white)
# palette.setColor(QPalette.Background, Qt.gray)
# app.setPalette(palette)

# Layouts and Buttons
window = QWidget()
layout = QVBoxLayout()

button1 = QPushButton('Usless Button')
layout.addWidget(button1)

button2 = QPushButton('The Close Button')
layout.addWidget(button2)

window.setLayout(layout)
window.setWindowTitle("A Pointless Application")

# Run a function when a button is clicked
button2.clicked.connect(close_when_clicked)

# Show?
#label.show()
window.show()

# Run app until user quits
app.exec_()