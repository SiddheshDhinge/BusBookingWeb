from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common
from .. import label

class Stop(Base, Common):
    __tablename__ = 'Stop'

    stopId = Column('stopId', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(64), nullable=False)
    address = Column('address', String(128), nullable=False)
    landmarkId = Column('landmarkId', Integer, ForeignKey('Landmark.landmarkId'), nullable=False)
    
    def __init__(self, name: str, address: str, landmarkId: int):
        self.name = name
        self.address = address
        self.landmarkId = landmarkId

    def __repr__(self):
        return f"{self.__tablename__} => ({self.stopId}) : {self.name} {self.address} {self.landmarkId}"
    
    def serialize(self):
        return {
            label.stop_id : self.stopId,
            label.stop_name : self.name,
            label.stop_address : self.address,
            label.landmark_id : self.landmarkId,
        }