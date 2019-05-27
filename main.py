# This is my first PyQt5 app..

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout

# Create Application
app = QApplication([])

# Use a Custom Style
app.setStyle("Windows")

# Add Label
#label = QLabel("Hello World")

# Layouts and Buttons
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Useless Button 1'))
layout.addWidget(QPushButton('Useless Button 2'))
window.setLayout(layout)

# Show?
#label.show()
window.show()

# Run app until user quits
app.exec_()