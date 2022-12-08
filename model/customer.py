from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customer'
    __table_args__ = (
        UniqueConstraint('contact'), 
        CheckConstraint('contact ~* \'^[0-9]{10}$\''),
    )

    username = Column('username', String(16), primary_key=True)
    password = Column('password', String(32), nullable=False)
    name = Column('name', String(64), nullable=False)
    contact = Column('contact', String(10), nullable=False)
    
    def __init__(self, username, password, name, contact):
        self.username = username
        self.password = password
        self.name = name
        self.contact = contact

    def __repr__(self):
        return f"{self.__tablename__} => ({self.username}) : {self.password}, {self.name}, {self.contact}"