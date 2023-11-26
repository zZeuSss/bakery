from sqlalchemy import Integer, Column, String
from data_base.db_engine import Base


class ConsumerRegion(Base):
    __tablename__: str = 'consumer_region'
    id = Column(Integer, primary_key=True)
    name = Column(String)
