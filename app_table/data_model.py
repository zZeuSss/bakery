from typing import List

from PyQt5.QtCore import QAbstractTableModel, Qt
from sqlalchemy import Row


class DataModel(QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data: Row, columns: List[str], parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data
        self._columns= columns

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._columns)

    def isValid(self):
        return True

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
