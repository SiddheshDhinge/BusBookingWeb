from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from session_manager import getSessionStatus, addActiveSession
from database import Base, DB_session
from common import Common

class Landmark(Base, Common):
    __tablename__ = 'Landmark'

    LandmarkId = Column('landmarkId', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(64), nullable=False)
    
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.__tablename__} => ({self.LandmarkId}) : {self.name}"