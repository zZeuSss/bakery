from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy import MetaData

Base = declarative_base(metadata=MetaData())


class Consumer(Base):
    __tablename__: str = 'consumer'

    id = Column(Integer, primary_key=True)
    region: Mapped[int] = mapped_column(ForeignKey('consumer_region.id'))
    name = Column(String)
    price_type = Column(String)
    phone = Column(String)
    address = Column(String)
    email = Column(String)
    comment = Column(String)


class ConsumerRegion(Base):
    __tablename__: str = 'consumer_region'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class HistoryPrice(Base):
    __tablename__ = 'history_price'

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    comment = Column(String)


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True)
    product: Mapped[int] = mapped_column(ForeignKey('product.id'))
    consumer: Mapped[int] = mapped_column(ForeignKey('consumer.id'))
    price = Column(Float)
    comment = Column(String)


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(String)
    file_path = Column(String)
    comment = Column(String)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Float)
    type = Column(String)
    comment = Column(String)


class Order(Base):
    __tablename__: str = 'order'

    id = Column(Integer, primary_key=True)
    price_id: Mapped[int] = mapped_column(ForeignKey('price.id'))
    product: Mapped[int] = mapped_column(ForeignKey('product.id'))
    consumer: Mapped[int] = mapped_column(ForeignKey('consumer.id'))
    order_type: Mapped[int] = mapped_column(ForeignKey('order_type.id'))
    type = Column(String)
    active = Column(Boolean)
    comment = Column(String)


class OrderType(Base):
    __tablename__: str = 'order_type'

    id = Column(Integer, primary_key=True)
    type = Column(String)