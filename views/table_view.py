from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from components.table.component.pagination import Pagination
from components.table.component.row import RowEditor
from components.table.component.table import Table
from database.data_controller import DataController


class TableView(QWidget):
    _data_controller: DataController = None

    def __init__(self, data_controller: DataController = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data_controller = data_controller

        v_lay = QVBoxLayout()
        h_lay = QHBoxLayout()

        self.row_editor = RowEditor(self)
        self.pagination = Pagination(self)
        self.table = Table(self._data_controller)

        self.row_editor.add_signal.data_changed.connect(self.add_empty_row)

        # hlay.addWidget(Filter(self))
        h_lay.addWidget(self.row_editor)
        h_lay.addWidget(self.pagination)
        v_lay.addLayout(h_lay)
        v_lay.addWidget(self.table)

        self.setLayout(v_lay)
        self.show()

    def add_empty_row(self):
        pass
    #     self.table.add_row()
    #
    # def update_row(self):
    #     pass
    #
    # def delete_row(self):
    #     pass
