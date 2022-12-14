from flask import render_template, session, request, jsonify
from .model.model_owner import Owner
from .model.model_customer import Customer
from .model.model_operator import Operator
from .model.model_bus import Bus
from .model.model_passenger import Passenger
from .model.model_schedule import Schedule
from .model.model_landmark import Landmark
from .model.model_stop import Stop
from .model.model_booking import Booking
from .model.model_at import At
from .model.database import DB_session
from .model.session_manager import getSessionStatus
# from model.session_manager import getSessionStatus, addActiveSession

from . import label

def handleRequest():
    service_id = int(request.form.get(label.service))
    response_data = {}
    if(service_id == 1):
        # create Owner
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        name = request.form.get(label.name)
        contact = request.form.get(label.contact)

        res = Owner(username=username, password=password, name=name, contact=contact).createOwner()
        response_data[label.success] = res

    elif(service_id == 2):
        #login
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        req = Owner(username=username, password=password, name=None, contact=None, currentSesssion=None).loginOwner()
        response_data = {
            label.success : req[0],
            label.session : req[1]
        }

    elif(service_id == 3):
        #logout
        try:
            session_id = session[label.session]
            Owner(None, None, None, None, currentSesssion=session_id).logoutOwner()
        except:
            response_data[label.success] = False
        else:
            response_data[label.success] = True

    elif(service_id == 4):
        #register bus
        if getSessionStatus()[0] == False:
            response_data[label.success] = label.authReq
        else:
            # session_id = session[label.session]
            # obj = Owner(username=None, password=None, name=None, contact=None, currentSesssion=session_id)
            numberPlate = request.form.get(label.bus_numberPlate)
            totalSeats = request.form.get(label.bus_totalSeats)
            busType = request.form.get(label.bus_busType)
            username = session[label.username]
            busObj = Bus(numberPlate=numberPlate, totalSeats=totalSeats, bustype=busType, username=username)
            response_data[label.success] = busObj.createObject()

    elif(service_id == 5):
        # get all registered bus
        if getSessionStatus()[0] == False:
            response_data[label.success] = label.authReq
        else:
            username = session[label.username]
            busObjLst = DB_session.query(Bus).filter(Bus.username == username).all()
            response_data = [busObj.serialize() for busObj in busObjLst]
    
    elif(service_id == 6):
        #add a schedule
        pass
    elif(service_id == 7):
        #view schedules
        pass
    elif(service_id == 8):
        #update profile
        name = request.form.get(label.name)
        contact = request.form.get(label.contact)
        username = session[label.username]
        ownerObj = Owner(username=username, password=None, name=name, contact=contact)
        ownerObj.loadSession()
        res = ownerObj.updateInformation()
        response_data[label.success] = res
        
    else:
        response_data[label.success] = label.invalid

    return jsonify(response_data)