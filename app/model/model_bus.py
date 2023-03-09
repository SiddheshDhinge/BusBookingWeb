from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common
from .. import label

class Bus(Base, Common):
    __tablename__ = 'Bus'
    objName = __tablename__.lower()
    objListName = f'list-{__tablename__.lower()}'

    numberPlate = Column('numberPlate', String(16), primary_key=True)
    busType = Column('busType', String(6), nullable=False)
    totalFloors = Column('totalFloors', Integer, nullable=False)
    floorRows = Column('floorRows', Integer, nullable=False)
    floorColumns = Column('floorColumns', Integer, nullable=False)
    walkingGapRow = Column('walkingGapRow', Integer, nullable=False)
    username = Column('username', String(16), ForeignKey('Owner.username'), nullable=False)

    def __init__(self, numberPlate: str, bustype: str, totalFloors: int, floorRows: int, floorColumns: int, walkingGapRow: int, username: str):
        self.numberPlate = numberPlate
        self.busType = bustype
        self.totalFloors = totalFloors
        self.floorRows = floorRows
        self.floorColumns = floorColumns
        self.walkingGapRow = walkingGapRow
        self.username = username

    def __repr__(self):
        return f"{self.__tablename__} => ({self.numberPlate}) : {self.busType}, {self.totalFloors}, {self.floorRows}, {self.floorColumns}, {self.walkingGapRow}, {self.username}"

    def serialize(self):
        return {
            label.bus_numberPlate : self.numberPlate,
            label.bus_busType : self.busType,
            label.bus_totalFloors : self.totalFloors,
            label.bus_floorRows : self.floorRows,
            label.bus_floorColumns : self.floorColumns,
            label.bus_walkingGapRow : self.walkingGapRow,
            label.owner_username : self.username
        }