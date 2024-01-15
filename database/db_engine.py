import importlib
import inspect
import pkgutil
from sqlite3 import Connection
from typing import List, Union

import sqlalchemy as db
from sqlalchemy import Engine, MetaData, select
from sqlalchemy.orm import Session, declarative_base
from config import DB_TYPE_CONNECTION

Base = declarative_base(metadata=MetaData())


#SINGLETON
class DataBaseEngine:
    _engine: Engine = None
    _conn: Connection = None
    _metadata: MetaData = None
    _session: Session = None
    _entities: List[Base] = []

    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self, db_type: str = DB_TYPE_CONNECTION):
        self._engine = db.create_engine(f'{db_type}:///bakery.sqlite')
        self._conn = self._engine.connect()
        self.create()

    def create(self):
        self.load_tables()
        Base.metadata.create_all(self._engine, tables=self._entities)
        self._metadata = Base.metadata
        self._session = Session(self._engine)

    def load_tables(self):
        module = importlib.import_module('models')
        for loader, module_name, is_pkg in pkgutil.walk_packages(module.__path__,
                                                                 module.__name__ + '.'):
            if not is_pkg:
                entity_module = importlib.import_module('.', module_name)
                cls: Base = [cls for class_name, cls in inspect.getmembers(entity_module, inspect.isclass) if
                             cls.__module__ == entity_module.__name__]
                self._entities.append(cls[0].__table__)

    def get_session(self):
        return self._session

    def set_session(self, session: Session):
        self._session = session

    session = property(get_session, set_session)

    def get_meta_data(self) -> MetaData:
        return self._metadata

    def set_meta_data(self, metadata: MetaData):
        self._metadata = metadata

    metadata = property(get_meta_data, set_meta_data)