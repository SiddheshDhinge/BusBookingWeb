from sqlalchemy import create_engine, CheckConstraint, PrimaryKeyConstraint, ForeignKey, ForeignKeyConstraint, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common

class Booking(Base, Common):
    __tablename__ = 'Booking'
    objName = __tablename__.lower()
    objListName = f'list-{__tablename__.lower()}'

    numberPlate = Column('numberPlate', String(16), nullable=False)
    seatNo = Column('seatNo', String(4), nullable=False)
    scheduleId = Column('scheduleId', Integer, ForeignKey('Schedule.scheduleId'), nullable=False)
    passengerId = Column('passengerId', Integer, ForeignKey('Passenger.passengerId'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(seatNo, numberPlate, scheduleId, passengerId),
        ForeignKeyConstraint([numberPlate, seatNo], ['Seat.numberPlate', 'Seat.seatNo'])
    )

    def __init__(self, numberPlate: str, seatNo: str, scheduleId: int, passengerId: int):
        self.numberPlate = numberPlate
        self.seatNo = seatNo
        self.scheduleId = scheduleId
        self.passengerId = passengerId

    def __repr__(self):
        return f"{self.__tablename__} => ({self.numberPlate}, {self.seatNo}) : {self.scheduleId} {self.passengerId}"