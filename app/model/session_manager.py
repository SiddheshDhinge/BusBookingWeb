from flask import session
from base64 import b64encode
from os import urandom
from .. import label

def addActiveSession(username, accessType):
    session[label.username] = username
    session[label.accessType] = accessType
    return True
    
def getSessionStatus():
    if(label.username in session and label.accessType in session):
        return (True, session[label.accessType])
    else:
        return (False, None)

def removeSession():
    session.pop(label.username, None)
    session.pop(label.accessType, None)
    session.clear()