from abc import ABC

import pandas as pd
from PyQt5.QtCore import QModelIndex


class Business:

    def evaluate(self,data_frame: pd.DataFrame = None, index: QModelIndex = None):
        raise NotImplemented()


class Calculate(Business):

    def evaluate(self, data_frame: pd.DataFrame = None, index: QModelIndex = None):
        row = data_frame.iloc[[index.row()]]
        row['Сумма'] = data_frame.iloc[:, 4: len(data_frame.columns)].sum(axis=1)[0]
        data_frame.iloc[[index.row()]] = row
        return data_frame
