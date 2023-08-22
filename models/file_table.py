from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FileTable(Base):
    __tablename__ = "file_table"

    id = Column(Integer, primary_key=True)
    fileName = Column(String) 
    createdAt = Column(Integer)
    notificationSended = Column(bool, default=False)
