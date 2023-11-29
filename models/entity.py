from sqlalchemy import Integer, Column, String
from database.db_engine import Base


class Entity(Base):
    __tablename__: str = 'entity'

    id = Column(Integer, primary_key=True)
    name = Column(String)
