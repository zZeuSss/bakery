from sqlalchemy import Integer, Column, String, Float

from database.db_engine import Base


class HistoryPrice(Base):
    __tablename__ = 'history_price'

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    comment = Column(String)
