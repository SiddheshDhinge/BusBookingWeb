from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy import exc
from .session_manager import getSessionStatus, addActiveSession, removeSession
from .database import Base, DB_session
from .. import label

class Customer(Base):
    __tablename__ = 'Customer'
    accessType = 'customer'
    __table_args__ = (
        UniqueConstraint('contact'), 
        CheckConstraint('contact ~* \'^[0-9]{10}$\''),
    )

    username = Column('username', String(16), primary_key=True)
    password = Column('password', String(32), nullable=False)
    name = Column('name', String(64), nullable=False)
    contact = Column('contact', String(10), nullable=False)
    
    def __init__(self, username: str, password: str, name: str, contact: str):
        self.username = username
        self.password = password
        self.name = name
        self.contact = contact

    def __repr__(self):
        return f"{self.__tablename__} => ({self.username}) : {self.password}, {self.name}, {self.contact}"

    def createCustomer(self):
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
        
    def loginCustomer(self):
        qry = DB_session.query(Customer).filter(Customer.username == self.username, Customer.password == self.password)
        if(DB_session.query(qry.exists()).scalar() == True):
            addActiveSession(username= self.username, accessType= Customer.accessType)
            return True 
        else:
            return False
        
    def loadSession(self):
        val = getSessionStatus()
        if(val[0] == False):
            return False
            
        self.username = val[1]
        return True
        
    def logoutCustomer(self):
        try:
            removeSession()
        except:
            return False
        else:
            return True
            
    def updateInformation(self):
        try:
            DB_session.query(Customer).filter(Customer.username == self.username).update(
                {
                    Customer.name : self.name,
                    Customer.contact : self.contact
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
            label.username: self.username,
            label.name: self.name,
            label.contact: self.contact
        }

    @staticmethod
    def isLoggedOn():
        retVal = getSessionStatus()
        if(retVal[0] == False):
            return False
        if(retVal[1] != Customer.accessType):
            return False
        return True