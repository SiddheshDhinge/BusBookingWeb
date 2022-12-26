from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common
from .. import label

class Stop(Base, Common):
    __tablename__ = 'Stop'
    objName = __tablename__.lower()

    stopId = Column('stopId', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(64), nullable=False)
    address = Column('address', String(128), nullable=False)
    cityId = Column('cityId', Integer, ForeignKey('City.cityId'), nullable=False)
    
    def __init__(self, name: str, address: str, cityId: int):
        self.name = name
        self.address = address
        self.cityId = cityId

    def __repr__(self):
        return f"{self.__tablename__} => ({self.stopId}) : {self.name} {self.address} {self.cityId}"
    
    def serialize(self):
        return {
            label.stop_id : self.stopId,
            label.stop_name : self.name,
            label.stop_address : self.address,
            label.city_id : self.cityId,
        }