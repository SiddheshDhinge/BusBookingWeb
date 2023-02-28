from sqlalchemy import create_engine, PrimaryKeyConstraint, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common

class Booking(Base, Common):
    __tablename__ = 'Booking'
    objName = __tablename__.lower()
    objListName = f'list-{__tablename__.lower()}'

    seatNo = Column('seatNo', Integer, nullable=False)
    scheduleId = Column('scheduleId', Integer, ForeignKey('Schedule.scheduleId'), nullable=False)
    passengerId = Column('passengerId', Integer, ForeignKey('Passenger.passengerId'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(seatNo, scheduleId, passengerId),
    )

    def __init__(self, seatNo: int, scheduleId: int, passengerId: int):
        self.seatNo = seatNo
        self.scheduleId = scheduleId
        self.passengerId = passengerId

    def __repr__(self):
        return f"{self.__tablename__} => ({self.seatNo}) : {self.scheduleId} {self.passengerId}"