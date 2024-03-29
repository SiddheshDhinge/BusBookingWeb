from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .common import Common
from .. import label

class Passenger(Base, Common):
    __tablename__ = 'Passenger'
    objName = __tablename__.lower()
    objListName = f'list-{__tablename__.lower()}'

    __table_args__ = (
        CheckConstraint('contact ~* \'^[0-9]{10}$\''),
    )

    passengerId = Column('passengerId', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(64), nullable=False)
    gender = Column('gender', CHAR, nullable=False)
    age = Column('age', Integer, nullable=False)
    contact = Column('contact', String(10), nullable=False)
    username = Column('username', String(16), ForeignKey('Customer.username'), nullable=False)
    
    def __init__(self, name: str, gender: str, age: int, contact: str, username: str):
        self.name = name
        self.gender = gender
        self.age = age
        self.contact = contact
        self.username = username

    def __repr__(self):
        return f"{self.__tablename__} => ({self.passengerId}) : {self.name}, {self.gender}, {self.age}, {self.contact}, {self.username}"

    def serialize(self):
        return {
            label.passenger_id: self.passengerId,
            label.passenger_name: self.name,
            label.passenger_gender: self.gender,
            label.passenger_age: self.age,
            label.passenger_contact: self.contact,
            label.customer_username: self.username
        }