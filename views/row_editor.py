from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout


class RowEditor(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        hlay = QHBoxLayout()

        add = QPushButton('+')
        delete = QPushButton('-')
        submit = QPushButton('✅')

        hlay.setAlignment(Qt.AlignCenter)

        add.setFixedSize((QSize(40, 25)))
        delete.setFixedSize((QSize(40, 25)))
        submit.setFixedSize((QSize(40, 25)))

        hlay.addWidget(add)
        hlay.addWidget(delete)
        hlay.addWidget(submit)

        self.setLayout(hlay)
        self.show()