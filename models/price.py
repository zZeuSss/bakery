from sqlalchemy import Integer, Column, String, ForeignKey, Float
from sqlalchemy.orm import mapped_column, Mapped

from database.db_engine import Base


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True)
    product: Mapped[int] = mapped_column(ForeignKey('product.id'))
    consumer: Mapped[int] = mapped_column(ForeignKey('consumer.id'))
    price = Column(Float)
    comment = Column(String)