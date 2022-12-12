from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from session_manager import getSessionStatus, addActiveSession
from database import Base, DB_session
from common import Common

class Schedule(Base, Common):
    __tablename__ = 'Schedule'
    __table_args__ = (
        CheckConstraint('("fromDate" < "toDate") OR (("fromDate" = "toDate") AND "departureTime" < "dropTime")'),
    )

    scheduleId = Column('scheduleId', Integer, primary_key=True, autoincrement=True)
    fromDate = Column('fromDate', Date, nullable=False)
    toDate = Column('toDate', Date, nullable=False)
    departureTime = Column('departureTime', Time, nullable=False)
    dropTime = Column('dropTime', Time, nullable=False)
    fairFees = Column('fairFees', Integer, nullable=False)
    numberPlate = Column('numberPlate', String(16), ForeignKey('Bus.numberPlate'), nullable=False)
    username = Column('username', String(16), ForeignKey('Operator.username'), nullable=False)

    def __init__(self, fromDate, toDate, departureTime, dropTime, fairFees, numberPlate, username):
        self.fromDate = fromDate
        self.toDate = toDate
        self.departureTime = departureTime
        self.dropTime = dropTime
        self.fairFees = fairFees
        self.numberPlate = numberPlate
        self.username = username

    def __repr__(self):
        return f"{self.__tablename__} => ({self.scheduleId}) : {self.fromDate}, {self.toDate}, {self.departureTime}, {self.dropTime}, {self.fairFees}, {self.numberPlate}, {self.username}"