from PyQt5.QtCore import QAbstractTableModel

from database.data_model import DataModel


class DataController:
    """
            Инкапсулирует методы работы с данными
            list
            get
            delete
            update
    """
    def __init__(self, *args, **kwargs):
        pass

    # _model: DataModel = None

    # def set_model(self, model: QAbstractTableModel):
    #     self._model = model
    #
    # def get_model(self) -> QAbstractTableModel:
    #     return self._model


    # def get(self, model: Base, id: str):
    #     return self._session.execute(
    #         select(
    #             model,
    #         ).where(model.id == id)
    #     ).first()
    #
    # def list(self, model: str, filter=None, fields=None):
    #     return self._session.execute(
    #         select(
    #             self._metadata.tables.get(model)
    #         )
    #     ).all()
