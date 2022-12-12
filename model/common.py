from sqlalchemy import exc
from database import DB_session

class Common:
    def createObject(self):
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