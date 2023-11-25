from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from app_table.filter import Filter
from app_table.pagination import Pagination
from views.row_editor import RowEditor


class Table(QWidget):

    def __init__(self, table: QWidget = None,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        vlay = QVBoxLayout()

        hlay = QHBoxLayout()

        hlay.addWidget(Filter(self))
        hlay.addWidget(RowEditor(self))
        hlay.addWidget(Pagination(self))
        vlay.addLayout(hlay)

        vlay.addWidget(table)

        self.setLayout(vlay)
        self.show()

    def add_empty_row(self):
        pass

    def update_row(self):
        pass

    def delete_row(self):
        pass