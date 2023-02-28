from sqlalchemy import create_engine, PrimaryKeyConstraint, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common

class At(Base, Common):
    __tablename__ = 'At'
    objName = __tablename__.lower()
    objListName = f'list-{__tablename__.lower()}'

    scheduleId = Column('scheduleId', Integer, ForeignKey('Schedule.scheduleId'), nullable=False)
    stopId = Column('stopId', Integer, ForeignKey('Stop.stopId'), nullable=False)
    sequence = Column('sequence', Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(scheduleId, stopId),
    )

    def __init__(self, scheduleId: int, stopId: int, sequence: int):
        self.scheduleId = scheduleId
        self.stopId = stopId
        self.sequence = sequence

    def __repr__(self):
        return f"{self.__tablename__} => ({self.scheduleId}) : {self.stopId}"