from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common
from .. import label

class Schedule(Base, Common):
    __tablename__ = 'Schedule'
    objName = __tablename__.lower()

    __table_args__ = (
        CheckConstraint('("fromDate" < "toDate") OR (("fromDate" = "toDate") AND "departureTime" < "dropTime")'),
    )

    scheduleId = Column('scheduleId', Integer, primary_key=True, autoincrement=True)
    fromDate = Column('fromDate', Date, nullable=False)
    toDate = Column('toDate', Date, nullable=False)
    departureTime = Column('departureTime', Time, nullable=False)
    dropTime = Column('dropTime', Time, nullable=False)
    fairFees = Column('fairFees', Integer, nullable=False)
    fromCity = Column('fromCity', Integer, ForeignKey('City.cityId'), nullable=False)
    toCity = Column('toCity', Integer, ForeignKey('City.cityId'), nullable=False)
    numberPlate = Column('numberPlate', String(16), ForeignKey('Bus.numberPlate'), nullable=False)
    username = Column('username', String(16), ForeignKey('Operator.username'), nullable=False)

    def __init__(self, fromDate, toDate, departureTime, dropTime, fairFees, fromCity, toCity, numberPlate, username):
        self.fromDate = fromDate
        self.toDate = toDate
        self.departureTime = departureTime
        self.dropTime = dropTime
        self.fairFees = fairFees
        self.fromCity = fromCity
        self.toCity = toCity
        self.numberPlate = numberPlate
        self.username = username

    def __repr__(self):
        return f"{self.__tablename__} => ({self.scheduleId}) : {self.fromDate}, {self.toDate}, {self.departureTime}, {self.dropTime}, {self.fairFees}, {self.fromCity}, {self.toCity}, {self.numberPlate}, {self.username}"
    
    def serialize(self):
        return {
            label.schedule_id : self.scheduleId,
            label.schedule_fromDate : f'{self.fromDate:%m/%d/%Y}',
            label.schedule_toDate : f'{self.toDate:%m/%d/%Y}',
            label.schedule_departureTime : f'{self.departureTime:%H:%M:%S}',
            label.schedule_dropTime : f'{self.dropTime:%H:%M:%S}',
            label.schedule_fairFees : self.fairFees,
            label.schedule_fromCity : self.fromCity,
            label.schedule_toCity : self.toCity,
            label.schedule_numberPlate : self.numberPlate,
            label.operator_username : self.username
        }