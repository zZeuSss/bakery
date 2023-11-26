from sqlalchemy import Integer, Column, String
from data_base.db_engine import Base


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(String)
    file_path = Column(String)
    comment = Column(String)

