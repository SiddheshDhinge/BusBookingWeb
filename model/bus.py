# import database
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

Base = declarative_base()

class Bus(Base):
    __tablename__ = 'Bus'

    numberPlate = Column('numberPlate', String(16), primary_key=True)
    totalSeats = Column('totalSeats', Integer, nullable=False)
    busType = Column('busType', String(16), nullable=False)
    username = Column('username', String(16), ForeignKey('Owner.username'), nullable=False)

    def __init__(self, numberPlate, totalSeats, bustype, username):
        self.numberPlate = numberPlate
        self.totalSeats = totalSeats
        self.busType = bustype
        self.username = username

    def __repr__(self):
        return f"{self.__tablename__} => ({self.numberPlate}) : {self.totalSeats}, {self.busType}, {self.username}"
 
    def createBus(self, DB_session):
        try:
            DB_session.add(self)
            DB_session.commit()
        except(exc.IntegrityError):
            DB_session.rollback()
            return False
        except:
            print(f'CREATE BUS : {self}')
            return False
        else:
            return True
