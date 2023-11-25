from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QPushButton, QListWidget, QHBoxLayout, QComboBox, QLineEdit
from PyQt5.QtCore import Qt

class Filter(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout()

    def layout(self):
        hlay = QHBoxLayout()

        search = QLineEdit()
        search.setToolTip('Поиск')
        submit = QPushButton('Найти')
        submit.setFixedSize(QSize(80, 25))
        hlay.addWidget(search)
        hlay.addWidget(submit)

        hlay.setAlignment(Qt.AlignLeft)

        self.setLayout(hlay)
        self.show()