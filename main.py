# This is my first PyQt5 app..

from PyQt5.QtWidgets import QApplication, QLabel

# Create Application
app = QApplication([])

# Add Label
label = QLabel("Hello World")

# Show?
label.show()

# Run app until user quits
app.exec_()