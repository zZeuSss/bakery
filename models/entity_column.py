from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import mapped_column

from database.db_engine import Base


class EntityColumn(Base):
    __tablename__: str = 'entity_column'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    alias = Column(String)
    entity = mapped_column(ForeignKey('entity.id'))
