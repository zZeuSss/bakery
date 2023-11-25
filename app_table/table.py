from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableView

from app_table.data_model import DataModel
from data_base.db_engine import DataBaseEngine


class Table(QTableView):
    def __init__(self, table_name: str = None, db: DataBaseEngine = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = db
        self.table_name = table_name
        self.setModel(DataModel(data=self.getData(), columns=self.getColumns()))

    def getData(self):
        return self.db.list(self.table_name)

    def getColumns(self):
        return self.db.get_columns(table_name=self.table_name)


    def add_row(self):
        self.insertRow(self.rowCount())

    def delete_row(self):
        pass
