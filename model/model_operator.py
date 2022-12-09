from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from session_manager import getSessionStatus, addActiveSession
from database import Base, DB_session

class Operator(Base):
    __tablename__ = 'Operator'
    __table_args__ = (
        UniqueConstraint('contact'), 
        CheckConstraint('contact ~* \'^[0-9]{10}$\''),
    )

    username = Column('username', String(16), primary_key=True)
    password = Column('password', String(32), nullable=False)
    name = Column('name', String(64), nullable=False)
    address = Column('address', String(128), nullable=False)
    contact = Column('contact', String(10), nullable=False)
    
    def __init__(self, username, password, name, address, contact):
        self.username = username
        self.password = password
        self.name = name
        self.address = address
        self.contact = contact

    def __repr__(self):
        return f"{self.__tablename__} => ({self.username}) : {self.password}, {self.name}, {self.address}, {self.contact}"