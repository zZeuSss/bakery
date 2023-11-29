from PyQt5 import QtWidgets  # import PyQt5 widgets
import sys

from qt_material import apply_stylesheet

from data_base.db_engine import DataBaseEngine
from main_window import MainWindow

# Create the application object
app = QtWidgets.QApplication(sys.argv)
apply_stylesheet(app, theme='dark_teal.xml')

db = DataBaseEngine()
db.create()

# Create the form object
window = MainWindow()

# Set the form title
window.setWindowTitle("bakery")

# Show form
window.show()

# Run the program
sys.exit(app.exec())
