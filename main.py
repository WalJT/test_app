# This is my first PyQt5 app..

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout

# Create Application
app = QApplication([])

# Add Label
label = QLabel("Hello World")

# Layouts and Buttons
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)

# Show?
label.show()
window.show()

# Run app until user quits
app.exec_()