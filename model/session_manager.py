import hashlib
import time
import random

activeSessionMapper = {}

def addActiveSession(username):
    hashString = f'{username}{time.time()}{random.randbytes(32)}'
    hash = hashlib.sha256(hashString.encode())
    session_id = hash.hexdigest()
    activeSessionMapper[session_id] = username
    return session_id
    
def getSessionStatus(session_id):
    if(session_id in activeSessionMapper):
        return (True, activeSessionMapper[session_id])
    else:
        return (False, None)