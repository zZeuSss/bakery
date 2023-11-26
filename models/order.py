from sqlalchemy import Integer, Column, String, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from data_base.db_engine import Base


class Order(Base):
    __tablename__: str = 'order'

    id = Column(Integer, primary_key=True)
    price_id: Mapped[int] = mapped_column(ForeignKey('price.id'))
    product: Mapped[int] = mapped_column(ForeignKey('product.id'))
    consumer: Mapped[int] = mapped_column(ForeignKey('consumer.id'))
    order_type: Mapped[int] = mapped_column(ForeignKey('order_type.id'))
    active = Column(Boolean)
    comment = Column(String)