from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from .queries import sql_create_check_valid_seat_function, sql_create_check_valid_seat_trigger
from .queries import sql_drop_check_valid_seat_function, sql_drop_check_valid_seat_trigger

load_dotenv()
db_name = os.getenv('db_name')
db_username = os.getenv('db_username')
db_password = os.getenv('db_password')
Base = declarative_base()
DB_session = None
DB_engine = None

def connectDB():
    connectionURL = f'postgresql+psycopg2://{db_username}:{db_password}@localhost/{db_name}'
    global DB_engine
    DB_engine = create_engine(url=connectionURL, echo=True)
    # engine = create_engine("sqlite:///mydb.db", echo=True)
    Session = sessionmaker(bind=DB_engine)
    global DB_session
    DB_session = Session()


def createAllTables():
    Base.metadata.create_all(bind=DB_engine)
    DB_session.commit()
    print("\n\nCREATED ALL TABLES\n\n")
    DB_session.execute(text(sql_create_check_valid_seat_function))
    print("\n\nCREATED FUNCTION\n\n")
    DB_session.execute(text(sql_create_check_valid_seat_trigger))
    print("\n\nCREATED TRIGGER\n\n")
    DB_session.commit()


def dropAllTables():
    Base.metadata.drop_all(bind=DB_engine)