from sqlalchemy import create_engine, PrimaryKeyConstraint, ForeignKey, Column, String, Boolean, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common
from .. import label

class Seat(Base, Common):
    __tablename__ = 'Seat'
    objName = __tablename__.lower()
    objListName = f'list-{__tablename__.lower()}'

    seatNo = Column('seatNo', String(4), nullable=False)
    isEnabled = Column('isEnabled', Boolean, nullable=False)
    numberPlate = Column('numberPlate', String(16), ForeignKey('Bus.numberPlate'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(seatNo, numberPlate),
    )

    def __init__(self, numberPlate: str, seatNo: str, isEnabled: bool):
        self.seatNo = seatNo
        self.isEnabled = isEnabled
        self.numberPlate = numberPlate

    def __repr__(self):
        return f"{self.__tablename__} => ({self.numberPlate}, {self.seatNo}) : {self.isEnabled}"

    def serialize(self):
        return {
            label.seat_seatNo : self.seatNo,
            label.seat_is_enabled : self.isEnabled,
            label.bus_numberPlate : self.numberPlate
        }