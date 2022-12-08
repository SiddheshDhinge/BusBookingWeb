# import database
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Time, Date, CHAR, UniqueConstraint, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from session_manager import getSessionStatus, addActiveSession
import os
from dotenv import load_dotenv
load_dotenv()

print("\n\n\nSTARTED: \n\n\n")

db_name = os.getenv('db_name')
db_username = os.getenv('db_username')
db_password = os.getenv('db_password')

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'Owner'
    __table_args__ = (
        UniqueConstraint('contact'), 
        CheckConstraint('contact ~* \'^[0-9]{10}$\''),
    )

    currentSession = None
    username = Column('username', String(16), primary_key=True)
    password = Column('password', String(32), nullable=False)
    name = Column('name', String(64), nullable=False)
    contact = Column('contact', String(10), nullable=False)

    def __init__(self, username, password, name, contact, currenSesssion = None):
        self.username = username
        self.password = password
        self.name = name
        self.contact = contact
        self.currentSession = currenSesssion

    def __repr__(self):
        return f"{self.__tablename__} => {self.password}, {self.name}, {self.contact}"

    def createOwner(self, DB_session):
        try:
            DB_session.add(o1)
            DB_session.commit()
        except(exc.IntegrityError):
            DB_session.rollback()
            return False
        except:
            print(f'CREATE OWNER : {self}')
            return False
        else:
            return True
        
    def loginOwner(self, DB_session):
        qry = DB_session.query(Owner).filter(Owner.username == self.username, Owner.password == self.password)
        if(DB_session.query(qry.exists()).scalar() == True):
            return (True, addActiveSession(self.username))
        else:
            return (False, None)
        
    def loadSession(self):
        val = getSessionStatus(self.currentSession)
        if(val[0] == False):
            return False

        self.username = val[1]
        return True


connectionURL = f'postgresql+psycopg2://{db_username}:{db_password}@localhost/{db_name}'
engine = create_engine(url=connectionURL, echo=True)
# engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# o2 = Owner('sarvesh', 'abc', 'abcd', '9879870000')
o1 = Owner('Siddhesh', 'abcd', 'abcd', '9879870000')
print(o1.loginOwner(session=session))

# session.add_all((o1, ))
