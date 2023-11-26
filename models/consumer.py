from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from data_base.db_engine import Base


class Consumer(Base):
    __tablename__: str = 'consumer'

    id = Column(Integer, primary_key=True, info={'alias': '№'})
    region: Mapped[int] = mapped_column(ForeignKey('consumer_region.id'), info={'alias': 'Маршрут'})
    name = Column(String, info={'alias': 'Наименование'})
    price_type = Column(String, info={'alias': 'Тип оплаты'})
    phone = Column(String, info={'alias': 'Номер телефона'})
    address = Column(String, info={'alias': 'Адрес'})
    email = Column(String, info={'alias': 'Почта'})
    comment = Column(String, info={'alias': 'Комментарий'})
