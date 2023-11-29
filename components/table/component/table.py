from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtWidgets import QTableView


class Table(QTableView):
    def __init__(self, data_model: QAbstractTableModel = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setModel(data_model)

    def get_data(self):
        return self.db.list(self._table_name)

    def get_columns(self):
        return self.db.get_columns(self._table_name)


    def add_row(self):
        self.insertRow(self.rowCount())

    def delete_row(self):
        pass
