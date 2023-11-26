from PyQt5.QtWidgets import QTableView

from components.app_table.data_model import DataModel
from data_base.db_engine import DataBaseEngine
from dataclass.table_config import TableConfig


class Table(QTableView):
    def __init__(self, table_name: str = None, db: DataBaseEngine = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = db
        self._table_name = table_name
        self.setModel(DataModel(data=self.get_data(), columns=self.get_columns()))

    def get_data(self):
        return self.db.list(self._table_name)

    def get_columns(self):
        return self.db.get_columns(self._table_name)


    def add_row(self):
        self.insertRow(self.rowCount())

    def delete_row(self):
        pass
