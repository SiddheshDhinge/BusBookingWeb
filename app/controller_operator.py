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
from .model.session_manager import getSessionStatus, isLoggedOn
# from model.session_manager import getSessionStatus, addActiveSession

from . import label

class ControllerOperator:

    def __init__(self):
        self.response_data = {}

    def handleRequest(self):
        service_id = int(request.form.get(label.service))

        if(service_id == 1):
            # create Owner
            self.handleAccountCreation()

        elif(service_id == 2):
            #login
            self.handleLogin()

        elif(service_id == 3):
            #logout
            self.handleLogout()

        elif(service_id == 4):
            #register bus
            self.handleBusRegistration()

        elif(service_id == 5):
            #View All Registered Bus
            self.handleViewBus()

        elif(service_id == 6):
            #add a Landmark
            self.handleLandmarkCreation()
        
        elif(service_id == 7):
            #view all LandMark
            self.handleViewLandmark()

        elif(service_id == 8):
            #add a Stop
            self.handleStopCreation()
            pass

        elif(service_id == 9):
            #view all stop
            self.handleViewStop()
        
        elif(service_id == 10):
            #add a schedule
            self.handleScheduleCreation()
            pass

        elif(service_id == 11):
            #view schedules
            self.handleViewSchedule()
            pass

        elif(service_id == 12):
            #update profile
            self.handleUpdateAccountProfile()

        else:
            self.response_data[label.success] = label.invalid

        return jsonify(self.response_data)
        

    def handleAccountCreation(self):
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        name = request.form.get(label.name)
        address = request.form.get(label.operator_address)
        contact = request.form.get(label.contact)
        res = Operator(username=username, password=password, name=name, address=address, contact=contact).createOperator()
        self.response_data[label.success] = res

    def handleLogin(self):
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        req = Operator(username=username, password=password, name=None, address=None, contact=None).loginOperator()
        self.response_data[label.success] = req[0]
        self.response_data[label.session] = req[1]

    def handleLogout(self):
        if isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        try:
            Operator(username=None, password=None, name=None, address=None, contact=None).logoutOperator()
        except:
            self.response_data[label.success] = False
        else:
            self.response_data[label.success] = True

    def handleUpdateAccountProfile(self):
        if isLoggedOn() == False:
            self.self.response_data[label.success] = label.authReq
            return
        
        name = request.form.get(label.name)
        address = request.form.get(label.operator_address)
        contact = request.form.get(label.contact)
        username = session[label.username]
        operatorObj = Operator(username=username, password=None, name=name, address=address, contact=contact)
        operatorObj.loadSession()
        res = operatorObj.updateInformation()
        self.response_data[label.success] = res

    def handleViewSchedule(self):
        if isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        
        username = session[label.username]
        qryResult = DB_session.query(Schedule, Bus, Owner, Stop, Landmark).select_from(Schedule).join(Bus, Owner, At, Stop, Landmark).filter(
            Schedule.username == username
        ).all()
        self.response_data = [
            {
                Schedule.__tablename__ : scheduleObj.serialize(),
                Bus.__tablename__ : busObj.serialize(),
                Owner.__tablename__ : ownerObj.serialize(),
                Stop.__tablename__ : stopObj.serialize(),
                Landmark.__tablename__ : landmarkObj.serialize()
            } for (scheduleObj, busObj, ownerObj, stopObj, landmarkObj) in qryResult
        ]