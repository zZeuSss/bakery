from typing import List

from sqlalchemy import select, Row
from sqlalchemy.orm import Session

from database.db_engine import Base, DataBaseEngine


class DataController:
    """
        Инкапсулирует методы работы с данными
    """

    def __init__(self, *args, **kwargs):
        self.model: Base = kwargs.get('model')
        self._engine = DataBaseEngine()
        self._session: Session = self._engine.get_session()

    def list(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        data = self._session.execute(
            select(self.model)
        ).all()

    def get_columns(self, table_name: Base):
        """
        :param table_name:
        :return:
        """
        return self._engine.metadata.tables.get(table_name.__name__.lower()).columns

    def get(self, model: Base, id: str) -> object:
        """
        :param model:
        :param id:
        :return:
        """
        return self._session.execute(
            select(
                model
            ).where(model.id == id)
        ).first().data[0]

    def delete(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def insert(self, *args, **kwargs):
        pass

    def _row_to_obj(self, model: Base, rows: List[Row]):
        return [row._data[0] for row in rows]
