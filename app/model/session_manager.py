from flask import session
from base64 import b64encode
from os import urandom
from .. import label

def addActiveSession(username,accessType):
    hash = b64encode(urandom(256)).decode('utf-8')
    session_id = hash
    session[label.session] = session_id
    session[label.username] = username
    session[label.accessType] = accessType
    return True
    
def getSessionStatus():
    if(label.session in session and label.username in session and label.accessType in session):
        return (True, session[label.accessType])
    else:
        return (False, None)

def removeSession():
    session.pop(label.session, None)
    session.pop(label.username, None)
    session.pop(label.accessType, None)
    session.clear()