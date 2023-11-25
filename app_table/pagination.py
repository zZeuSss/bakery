from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QComboBox
from PyQt5.QtCore import Qt


class Pagination(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout()

    def layout(self):
        hlay = QHBoxLayout()

        next = QPushButton('->')
        prev = QPushButton('<-')
        end = QPushButton('>>')
        first = QPushButton('<<')

        self.select = QComboBox(self)


        self.setValues()

        hlay.addWidget(first)
        hlay.addWidget(prev)
        hlay.addWidget(next)
        hlay.addWidget(end)
        hlay.addWidget(self.select)

        hlay.setAlignment(Qt.AlignRight)

        self.setLayout(hlay)
        self.show()

    def setValues(self):
        for inx in ['10', '20', '40', '100']:
            self.select.addItem(str(inx))
