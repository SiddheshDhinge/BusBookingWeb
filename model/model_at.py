from sqlalchemy import create_engine, PrimaryKeyConstraint, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from session_manager import getSessionStatus, addActiveSession
from database import Base, DB_session

class At(Base):
    __tablename__ = 'At'

    scheduleId = Column('scheduleId', Integer, ForeignKey('Schedule.scheduleId'), nullable=False)
    stopId = Column('stopId', Integer, ForeignKey('Stop.stopId'), nullable=False)
    
    __table_args__ = (
        PrimaryKeyConstraint(scheduleId, stopId),
    )

    def __init__(self, scheduleId: int, stopId: int):
        self.scheduleId = scheduleId
        self.stopId = stopId

    def __repr__(self):
        return f"{self.__tablename__} => ({self.scheduleId}) : {self.stopId}"