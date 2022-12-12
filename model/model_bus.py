from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common

class Bus(Base, Common):
    __tablename__ = 'Bus'

    numberPlate = Column('numberPlate', String(16), primary_key=True)
    totalSeats = Column('totalSeats', Integer, nullable=False)
    busType = Column('busType', String(16), nullable=False)
    username = Column('username', String(16), ForeignKey('Owner.username'), nullable=False)

    def __init__(self, numberPlate: str, totalSeats: int, bustype: str, username: str):
        self.numberPlate = numberPlate
        self.totalSeats = totalSeats
        self.busType = bustype
        self.username = username

    def __repr__(self):
        return f"{self.__tablename__} => ({self.numberPlate}) : {self.totalSeats}, {self.busType}, {self.username}"