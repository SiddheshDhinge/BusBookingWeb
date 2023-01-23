from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .. import label, label_reason
from flask import flash, redirect, url_for

class Operator(Base):
    __tablename__ = 'Operator'
    accessType = 'operator'
    objName = __tablename__.lower()

    __table_args__ = (
        UniqueConstraint('contact'), 
        CheckConstraint('contact ~* \'^[0-9]{10}$\''),
    )

    username = Column('username', String(16), primary_key=True)
    password = Column('password', String(32), nullable=False)
    name = Column('name', String(64), nullable=False)
    address = Column('address', String(128), nullable=False)
    contact = Column('contact', String(10), nullable=False)
    
    def __init__(self, username: str, password: str, name: str, address: str, contact: str):
        self.username = username
        self.password = password
        self.name = name
        self.address = address
        self.contact = contact

    def __repr__(self):
        return f"{self.__tablename__} => ({self.username}) : {self.password}, {self.name}, {self.address}, {self.contact}"

    def createOperator(self):
        try:
            DB_session.add(self)
            DB_session.commit()
        except(exc.IntegrityError):
            DB_session.rollback()
            return False
        except:
            DB_session.rollback()
            print(f'{self}')
            return False
        else:
            return True
        
    def loginOperator(self):
        qry = DB_session.query(Operator).filter(Operator.username == self.username, Operator.password == self.password)
        if(DB_session.query(qry.exists()).scalar() == True):
            addActiveSession(username= self.username, accessType= Operator.accessType)
            return True
        else:
            return False
        
    def loadSession(self):
        val = getSessionStatus()
        if(val[0] == False):
            return False
            
        self.username = val[1]
        return True
            
    def logoutOperator(self):
        try:
            removeSession()
        except:
            return False
        else:
            return True

    def updateInformation(self):
        try:
            if(self.name):
                DB_session.query(Operator).filter(Operator.username == self.username).update(
                    {
                        Operator.name : self.name
                    }
                )
            if(self.contact):
                DB_session.query(Operator).filter(Operator.username == self.username).update(
                    {
                        Operator.contact : self.contact
                    }
                )
            if(self.address):
                DB_session.query(Operator).filter(Operator.username == self.username).update(
                    {
                        Operator.address : self.address
                    }
                )
            DB_session.commit()
        except Exception as e:
            print(e)
            DB_session.rollback()
            return False
        else:
            return True

    def serialize(self):
        return {
            label.operator_username: self.username,
            label.name: self.name,
            label.contact: self.contact,
            label.operator_address: self.address
        }

    @staticmethod
    def isLoggedOn():
        retVal = getSessionStatus()
        if(retVal[0] == False):
            return False
        if(retVal[1] != Operator.accessType):
            return False
        return True
    
    @staticmethod
    def requireLogin(func):
        def wrap(*args, **kwargs):
            if Operator.isLoggedOn() == False:
                #Not logged in 
                flash(label_reason.loginInRequired)
                return redirect(url_for('login', role='operator'))
            else:
                #Operator is Logined
                return func(*args, **kwargs)

        wrap.__name__ = func.__name__
        return wrap