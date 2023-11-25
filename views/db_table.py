import pandas as pd
from PyQt5.QtGui import QContextMenuEvent
from PyQt5.QtWidgets import QTableView,  QMenu

from data_base.db_engine import DataBaseEngine
from data_base.pandas_model import PandasModel


class DataBaseTable(QTableView):
    _data: pd.DataFrame = None

    def __init__(self, *args, **kwargs):
        self.db: DataBaseEngine = kwargs.pop('db')
        self.table = kwargs.pop('table')
        super().__init__(*args, **kwargs)
        self.setAutoScroll(True)
        self.db_data()

    def db_data(self):
        self._data: pd.DataFrame = self.db.get_data(self.table)
        self.setModel(PandasModel(self._data))

    def contextMenuEvent(self, event: QContextMenuEvent):
        menu = QMenu()
        menu.addAction("Добавить").triggered.connect(self.newEmptyRow)
        menu.exec_(event.globalPos())

    def newEmptyRow(self):
        self.data = pd.concat([self._data, pd.DataFrame([pd.Series()])], ignore_index=True)
