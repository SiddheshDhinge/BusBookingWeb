from flask import flash, redirect
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .. import label, label_reason

class Owner(Base):
    __tablename__ = 'Owner'
    accessType = 'owner'
    __table_args__ = (
        UniqueConstraint('contact'), 
        CheckConstraint('contact ~* \'^[0-9]{10}$\''),
    )

    currentSession = None
    username = Column('username', String(16), primary_key=True)
    password = Column('password', String(32), nullable=False)
    name = Column('name', String(64), nullable=False)
    contact = Column('contact', String(10), nullable=False)

    def __init__(self, username: str, password: str, name: str, contact: str, currentSesssion: str = None):
        self.username = username
        self.password = password
        self.name = name
        self.contact = contact
        self.currentSession = currentSesssion

    def __repr__(self):
        return f"{self.__tablename__} => {self.password}, {self.name}, {self.contact}"

    def createOwner(self):
        try:
            DB_session.add(self)
            DB_session.commit()
        except(exc.IntegrityError):
            DB_session.rollback()
            return False
        except:
            print(f'{self}')
            return False
        else:
            return True
        
    def loginOwner(self):
        qry = DB_session.query(Owner).filter(Owner.username == self.username, Owner.password == self.password)
        if(DB_session.query(qry.exists()).scalar() == True):
            addActiveSession(username= self.username, accessType= Owner.accessType)
            return True
        else:
            return False
        
    def loadSession(self):
        val = getSessionStatus()
        if(val[0] == False):
            return False
            
        self.username = val[1]
        return True
    
    def logoutOwner(self):
        try:
            removeSession()
        except:
            return False
        else:
            return True

    def updateInformation(self):
        try:
            if(self.name and self.contact):
                DB_session.query(Owner).filter(Owner.username == self.username).update(
                {
                    Owner.name : self.name,
                    Owner.contact : self.contact
                })
            elif(self.name):
                DB_session.query(Owner).filter(Owner.username == self.username).update(
                {
                    Owner.name : self.name
                })
            elif(self.contact):
                DB_session.query(Owner).filter(Owner.username == self.username).update(
                {
                    Owner.contact : self.contact
                })
            DB_session.commit()
        except Exception as e:
            print(e)
            DB_session.rollback()
            return False
        else:
            return True

    def serialize(self):
        return {
            label.username: self.username,
            label.name: self.name,
            label.contact: self.contact
        }

    @staticmethod
    def isLoggedOn():
        retVal = getSessionStatus()
        if(retVal[0] == False):
            return False
        if(retVal[1] != Owner.accessType):
            return False
        return True

    @staticmethod
    def requireLogin(func):
        def wrap(*args, **kwargs):
            if Owner.isLoggedOn() == False:
                #Not logged in 
                flash(label_reason.loginInRequired)
                return redirect('login/owner')
            else:
                #Owner is Logined
                return func(*args, **kwargs)

        wrap.__name__ = func.__name__
        return wrap