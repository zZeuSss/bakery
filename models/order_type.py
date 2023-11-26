from sqlalchemy import Integer, Column, String

from data_base.db_engine import Base


class OrderType(Base):
    __tablename__: str = 'order_type'

    id = Column(Integer, primary_key=True)
    type = Column(String)