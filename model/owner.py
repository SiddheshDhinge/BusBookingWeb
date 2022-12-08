import hashlib
import random
from database import con, cur
from bus import Bus
class Owner:
    
    ## queries    
    sql_insert_owner = "insert into Owner(Owner_username, Owner_password, Owner_name, Owner_contact) values(%s, %s, %s, %s);"

    sql_select_exists_owner = "select exists(select * from Owner where Owner_username = %s and Owner_password = %s)"

    #manage active sessions
    sessionMapper = {}

    def __init__(self, username, password, name, contact):
        self.username = username
        self.password = password
        self.name = name
        self.contact = contact

    def createOwner(self):
        cur.execute(Owner.sql_insert_owner, (self.username, self.password, self.name, self.contact))
        con.commit()

    def login(user_username, user_password):
        cur.execute(Owner.sql_select_exists_owner, (user_username, user_password))
        if(cur.fetchone()[0] == True):
            hash = hashlib.sha256(f'{user_username}{user_password}{random.randint(1000, 10000)}')
            session_id = hash.hexdigest()
            Owner.sessionMapper[session_id] = user_username
            return (True, session_id)
        return (False, None)

    # def addBus(session_id, Bus bus):
    #     pass
