from flask import session
from base64 import b64encode
from os import urandom

def addActiveSession(username):
    hash = b64encode(urandom(256)).decode('utf-8')
    session_id = hash
    session['session-id'] = session_id
    session['user-name'] = username
    return session_id
    
def getSessionStatus():
    if('session-id' in session):
        return (True, session['user-name'])
    else:
        return (False, None)

def removeSession():
    session.pop('session-id', None)
    session.pop('user-id', None)