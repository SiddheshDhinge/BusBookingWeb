from sqlalchemy import create_engine, CheckConstraint, PrimaryKeyConstraint, ForeignKey, ForeignKeyConstraint, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common
from .. import label


class Booking(Base, Common):
    __tablename__ = 'Booking'
    objName = __tablename__.lower()
    objListName = f'list-{__tablename__.lower()}'

    bookingId = Column(UUID(as_uuid=True), primary_key= True, default= uuid.uuid4)
    numberPlate = Column('numberPlate', String(16), nullable=False)
    seatNo = Column('seatNo', String(4), nullable=False)
    scheduleId = Column('scheduleId', Integer, ForeignKey('Schedule.scheduleId'), nullable=False)
    passengerId = Column('passengerId', Integer, ForeignKey('Passenger.passengerId'), nullable=False)
    fromStopId = Column('fromStopId', Integer, ForeignKey('Stop.stopId'), nullable=False)
    toStopId = Column('toStopId', Integer, ForeignKey('Stop.stopId'), nullable=False)

    __table_args__ = (
        UniqueConstraint(scheduleId, seatNo),
        ForeignKeyConstraint([numberPlate, seatNo], ['Seat.numberPlate', 'Seat.seatNo'])
    )

    def __init__(self, numberPlate: str, seatNo: str, scheduleId: int, passengerId: int, fromStopId: int, toStopId: int):
        self.numberPlate = numberPlate
        self.seatNo = seatNo
        self.scheduleId = scheduleId
        self.passengerId = passengerId
        self.fromStopId = fromStopId
        self.toStopId = toStopId

    def __repr__(self):
        return f"{self.__tablename__} => ({self.bookingId}) : {self.numberPlate}, {self.seatNo}, {self.scheduleId}, {self.passengerId}, {self.fromStopId}, {self.toStopId}"
    
    def serialize(self):
        return {
            label.booking_id : self.bookingId,
            label.bus_numberPlate : self.numberPlate,
            label.seat_seatNo : self.seatNo,
            label.schedule_id : self.scheduleId,
            label.passenger_id : self.passengerId,
            label.booking_fromStopId : self.fromStopId,
            label.booking_toStopId : self.toStopId
        }