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

class ControllerOwner:

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
        contact = request.form.get(label.contact)
        res = Owner(username=username, password=password, name=name, contact=contact).createOwner()
        self.response_data[label.success] = res

    def handleLogin(self):
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        req = Owner(username=username, password=password, name=None, contact=None, currentSesssion=None).loginOwner()
        self.response_data[label.success] = req[0]
        self.response_data[label.session] = req[1]

    def handleLogout(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        try:
            Owner(None, None, None, None, currentSesssion=None).logoutOwner()
        except:
            self.response_data[label.success] = False
        else:
            self.response_data[label.success] = True

    def handleBusRegistration(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
            
        numberPlate = request.form.get(label.bus_numberPlate)
        totalSeats = request.form.get(label.bus_totalSeats)
        busType = request.form.get(label.bus_busType)
        username = session[label.username]
        busObj = Bus(numberPlate=numberPlate, totalSeats=totalSeats, bustype=busType, username=username)
        self.response_data[label.success] = busObj.createObject()

    def handleViewBus(self):
        # get all owners registered bus
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return

        username = session[label.username]
        busObjLst = DB_session.query(Bus).filter(Bus.username == username).all()
        self.response_data = [busObj.serialize() for busObj in busObjLst]
        
    def handleUpdateAccountProfile(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        
        name = request.form.get(label.name)
        contact = request.form.get(label.contact)
        username = session[label.username]
        ownerObj = Owner(username=username, password=None, name=name, contact=contact)
        ownerObj.loadSession()
        res = ownerObj.updateInformation()
        self.response_data[label.success] = res

    def handleViewLandmark(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return

        landmarkObjList = DB_session.query(Landmark).all()
        self.response_data = [landmarkObj.serialize() for landmarkObj in landmarkObjList]

    def handleViewStop(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        
        stopObjList = DB_session.query(Stop).all()
        self.response_data = [stopObj.serialize() for stopObj in stopObjList]

    def handleLandmarkCreation(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return

        landmark_name = request.form.get(label.landmark_name)
        val = Landmark(landmark_name).createObject()
        self.response_data[label.success] = val

    def handleStopCreation(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        
        stop_name = request.form.get(label.stop_name)
        stop_address = request.form.get(label.stop_address)
        landmark_id = request.form.get(label.landmark_id)
        val = Stop(name= stop_name, address= stop_address, landmarkId= landmark_id).createObject()
        self.response_data[label.success] = val

    def handleScheduleCreation(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return

        operator_username = request.form.get(label.username)
        fromDate = request.form.get(label.schedule_fromDate)
        toDate = request.form.get(label.schedule_toDate)
        departureTime = request.form.get(label.schedule_departureTime)
        dropTime = request.form.get(label.schedule_dropTime)
        fairFees = request.form.get(label.schedule_fairFees)
        numberPlate = request.form.get(label.schedule_numberPlate)
        scheduleObj = Schedule(
            fromDate=fromDate, toDate=toDate, departureTime=departureTime, dropTime=dropTime, 
            fairFees=fairFees, numberPlate=numberPlate, username=operator_username
        )
        retVal = scheduleObj.createObject()
        self.response_data[label.success] = retVal

    def handleViewSchedule(self):
        print(session.keys())
        print(session[label.username],
        session[label.session])
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        
        username = session[label.username]
        qryResult = DB_session.query(Schedule, Bus, Owner).select_from(Schedule).join(Bus, Owner).filter(
            Owner.username == username
        ).all()
        self.response_data = [
            {
                Schedule.__tablename__ : scheduleObj.serialize(),
                Bus.__tablename__ : busObj.serialize(),
                Owner.__tablename__ : ownerObj.serialize()
            } for (scheduleObj, busObj, ownerObj) in qryResult
        ]