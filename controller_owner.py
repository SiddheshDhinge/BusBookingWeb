from flask import render_template, session, request, jsonify
from model.model_owner import Owner
from model.model_customer import Customer
from model.model_operator import Operator
from model.model_bus import Bus
from model.model_passenger import Passenger
from model.model_schedule import Schedule
from model.model_landmark import Landmark
from model.model_stop import Stop
from model.model_booking import Booking
from model.model_at import At
# from model.session_manager import getSessionStatus, addActiveSession

def handleRequest():
    service_id = request.form.get('service-id')

    if(service_id == 1):
        #login
        username = request.form.get('username')
        password = request.form.get('password')
        req = Owner(username=username, password=password, contact=None, currentSesssion=None).loginOwner()
        data = {
            'success' : req[0],
            'session-id' : req[1]
        }
        return jsonify(data)

    elif(service_id == 2):
        #logout
        pass
    elif(service_id == 3):
        #register bus
        pass
    elif(service_id == 4):
        #view all bus
        pass
    elif(service_id == 5):
        #add a schedule
        pass
    elif(service_id == 6):
        #view schedules
        pass
    elif(service_id == 7):
        #update profile
        pass
    else:
        f'404'