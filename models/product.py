from sqlalchemy import Integer, Column, String, Float

from database.db_engine import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Float)
    type = Column(String)
    comment = Column(String)
