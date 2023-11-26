from typing import List

from PyQt5.QtCore import QAbstractTableModel, Qt
from sqlalchemy import Row, Column


class DataModel(QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data: List[Row], columns: List[Column], parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data: List[Row] = data
        self._columns: List[Column] = columns

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._columns)

    def isValid(self):
        return False

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._columns[section].info.get('alias', self._columns[section].name)
        return None
