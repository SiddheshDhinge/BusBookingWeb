from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

Base = declarative_base()

class Passenger(Base):
    __tablename__ = 'Passenger'
    __table_args__ = (
        UniqueConstraint('contact'), 
        CheckConstraint('contact ~* \'^[0-9]{10}$\''),
    )

    passengerId = Column('passengerId', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(64), nullable=False)
    gender = Column('gender', CHAR, nullable=False)
    age = Column('age', Integer, nullable=False)
    contact = Column('contact', String(10), nullable=False)
    username = Column('username', String(16), ForeignKey('Customer.username'), nullable=False)
    
    def __init__(self, name, gender, age, contact, username):
        self.name = name
        self.gender = gender
        self.age = age
        self.contact = contact
        self.username = username

    def __repr__(self):
        return f"{self.__tablename__} => ({self.passengerId}) : {self.name}, {self.gender}, {self.age}, {self.contact}, {self.username}"