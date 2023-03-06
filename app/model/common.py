from sqlalchemy import exc
from .database import DB_session

class Common:
    def createObject(self):
        try:
            DB_session.add(self)
            DB_session.commit()
        except exc.IntegrityError as e:
            print(e)
            print(f'{self}')
            DB_session.rollback()
            return False
        except Exception as e:
            DB_session.rollback()
            print(e)
            print(f'{self}')
            return False
        else:
            return True