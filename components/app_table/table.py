from PyQt5.QtWidgets import QTableView

from components.app_table.data_model import DataModel
from data_base.db_engine import DataBaseEngine
from dataclass.table_config import TableConfig


class Table(QTableView):
    def __init__(self, table: TableConfig = None, db: DataBaseEngine = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = db
        self.table = table
        self.setModel(DataModel(data=self.getData(), columns=self.getColumns()))

    def getData(self):
        return self.db.list(self.table)

    def getColumns(self):
        return self.db.get_columns(table_name=self.table)


    def add_row(self):
        self.insertRow(self.rowCount())

    def delete_row(self):
        pass
