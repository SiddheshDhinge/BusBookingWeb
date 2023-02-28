from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common
from .. import label

class City(Base, Common):
    __tablename__ = 'City'
    objName = __tablename__.lower()
    objListName = f'list-{__tablename__.lower()}'

    cityId = Column('cityId', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(64), nullable=False)
    
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.__tablename__} => ({self.cityId}) : {self.name}"

    def serialize(self):
        return {
            label.city_id : self.cityId,
            label.city_name : self.name
        }