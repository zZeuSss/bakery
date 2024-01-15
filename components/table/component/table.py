from PyQt5.QtWidgets import QTableView

from database.data_controller import DataController


class Table(QTableView):
    def __init__(self, data_controller: DataController = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_controller = data_controller
        self.setModel(self.data_controller.list())

    def add_row(self):
        self.insertRow(self.rowCount())

    def delete_row(self):
        pass
