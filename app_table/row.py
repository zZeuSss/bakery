from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout


class AddSignal(QObject):
    data_changed = pyqtSignal(bool, )


class DeleteSignal(QObject):
    data_changed = pyqtSignal(bool, )


class SubmitSignal(QObject):
    data_changed = pyqtSignal(bool, )


class RowEditor(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        hlay = QHBoxLayout()

        add = QPushButton('+')
        delete = QPushButton('-')
        submit = QPushButton('✅')

        self.add_signal = AddSignal()
        self.delete_signal = DeleteSignal()
        self.submit_signal = SubmitSignal()

        add.clicked.connect(self.add)
        delete.clicked.connect(self.delete)
        submit.clicked.connect(self.submit)

        hlay.setAlignment(Qt.AlignCenter)

        hlay.addWidget(add)
        hlay.addWidget(delete)
        hlay.addWidget(submit)

        self.setLayout(hlay)
        self.show()

    @QtCore.pyqtSlot()
    def add(self):
        self.add_signal.data_changed.emit(True)

    @QtCore.pyqtSlot()
    def delete(self):
        self.delete_signal.data_changed.emit(True)

    def submit(self):
        self.submit_signal.data_changed.emit(True)
