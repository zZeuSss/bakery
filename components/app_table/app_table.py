from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from components.app_table.pagination import Pagination
from components.app_table.row import RowEditor
from components.app_table.table import Table
from data_base.db_engine import DataBaseEngine
from dataclass.table_config import TableConfig


class AppTable(QWidget):

    def __init__(self, table_name: str = None, db: DataBaseEngine = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        v_lay = QVBoxLayout()
        h_lay = QHBoxLayout()

        self.row_editor = RowEditor(self)
        self.pagination = Pagination(self)
        self.table = Table(table_name=table_name, db=db)

        self.row_editor.add_signal.data_changed.connect(self.add_empty_row)

        # hlay.addWidget(Filter(self))
        h_lay.addWidget(self.row_editor)
        h_lay.addWidget(self.pagination)
        v_lay.addLayout(h_lay)
        v_lay.addWidget(self.table)

        self.setLayout(v_lay)
        self.show()

    def add_empty_row(self):
        self.table.add_row()

    def update_row(self):
        pass

    def delete_row(self):
        pass
