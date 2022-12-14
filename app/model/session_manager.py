from flask import session
from base64 import b64encode
from os import urandom
from .. import label

def addActiveSession(username):
    hash = b64encode(urandom(256)).decode('utf-8')
    session_id = hash
    session[label.session] = session_id
    session[label.username] = username
    return session_id
    
def getSessionStatus():
    if(label.session in session):
        return (True, session[label.username])
    else:
        return (False, None)

def removeSession():
    session.pop(label.session, None)
    session.pop(label.username, None)
    session.clear()