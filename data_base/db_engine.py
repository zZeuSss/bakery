from sqlite3 import Connection
from typing import Any, Sequence

import pandas
import sqlalchemy as db
from pandas import DataFrame
from sqlalchemy import Engine, MetaData, select
from sqlalchemy.orm import Session

from data_base.models import Base
from config import DB_TYPE_CONNECTION


class DataBaseEngine:
    _engine: Engine = None
    _conn: Connection = None
    _metadata: MetaData = None
    _session: Session = None

    def __init__(self, db_type: str = DB_TYPE_CONNECTION):
        self._engine = db.create_engine(f'{db_type}:///bakery.sqlite')
        self._conn = self._engine.connect()

    def create(self):
        Base.metadata.create_all(self._engine)
        self._metadata = Base.metadata
        self._session = Session(self._engine)

    def get_session(self):
        return self._session

    def set_session(self, session: Session):
        self._session = session

    session = property(get_session, set_session)

    def get_meta_data(self):
        return self._metadata

    def set_meta_data(self, metadata: MetaData):
        self._metadata = metadata

    metadata = property(get_meta_data, set_meta_data)

    def get_data(self, table_name: str) -> DataFrame:
        return pandas.read_sql(select(self._metadata.tables[table_name]), self._engine)

    def get(self, model: Base, id: str):
        return self._session.execute(
            select(
                model,
            ).where(model.id == id)
        ).all()[0]

    def list(self, model: Base, filter=None) -> Sequence[Any]:
        return self._session.execute(
            select(
                model
            )
        ).scalars().all()

    def update(self, model: Base):
        pass

    def delete(self, model: Base):
        pass
