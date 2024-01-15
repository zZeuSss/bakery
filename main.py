from PyQt5 import QtWidgets  # import PyQt5 widgets
import sys

from qt_material import apply_stylesheet

from database.data_controller import DataController
from database.db_engine import DataBaseEngine
from main_window import MainWindow
from models.consumer import Consumer

# Create the application object
app = QtWidgets.QApplication(sys.argv)
apply_stylesheet(app, theme='dark_amber.xml')

# Create the form object
window = MainWindow()

# Set the form title
window.setWindowTitle("PumpkinPie")

# Show form
window.show()

# Run the program
sys.exit(app.exec())