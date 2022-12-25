from flask import render_template, session, request, jsonify, flash, redirect, url_for
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
from .model.session_manager import getSessionStatus
from .model.complex_operations import ComplexOperation

from . import label, label_reason

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
            self.response_data[label.success] = False

        return jsonify(self.response_data)
        

    def handleAccountCreation(self):
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        name = request.form.get(label.owner_name)
        contact = request.form.get(label.owner_contact)
        result = Owner(username=username, password=password, name=name, contact=contact).createOwner()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.userCreationSuccess)
            return redirect(url_for('login', role= Owner.accessType))
        else:
            flash(label_reason.userCreationFailed)
            return redirect(url_for('signUp', role= Owner.accessType))

    def handleLogin(self):
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        result = Owner(username=username, password=password, name=None, contact=None, currentSesssion=None).loginOwner()
        self.response_data[label.success] = result
        
        if(result == True):
            flash(label_reason.userLoginSuccess)
            session.permanent = True
            return redirect(url_for('landingOwner'))
        else:
            flash(label_reason.userLoginFailed)
            return redirect(url_for('login', role= Owner.accessType))
    
    @Owner.requireLogin
    def handleLogout(self):
        result = Owner(None, None, None, None, currentSesssion=None).logoutOwner()
        self.response_data[label.success] = result

        if(result == True):
            flash(label_reason.userLogoutSuccess)
            return redirect(url_for('chooseLogin'))
        else:
            flash(label_reason.userLogoutFailed)
            return redirect(url_for('index'))


    def handleBusRegistration(self):
        numberPlate = request.form.get(label.bus_numberPlate)
        totalSeats = request.form.get(label.bus_totalSeats)
        busType = request.form.get(label.bus_busType)
        username = session[label.username]
        busObj = Bus(numberPlate=numberPlate, totalSeats=totalSeats, bustype=busType, username=username)
        result = busObj.createObject()
        self.response_data[label.success] = result

        if(result == True):
            flash(label_reason.busRegistrationSuccess)
        else:
            flash(label_reason.busRegistrationFailed)
        return redirect(url_for('landingOwner'))


    def handleViewBus(self):
        # get all owners registered bus
        username = session[label.username]
        queryResult = ComplexOperation().getOwnerBuses(ownerUsername= username)
        self.response_data[label.data] = [busObj.serialize() for busObj in queryResult]
        self.response_data[label.options] = label.optionsUserLogout
        return render_template('viewBus.html', response_data= self.response_data)


    def handleUpdateAccountProfile(self):
        name = request.form.get(label.owner_name, default=None)
        contact = request.form.get(label.owner_contact, default=None)
        username = session[label.username]

        ownerObj = Owner(username=username, password=None, name=name, contact=contact)
        result = ownerObj.updateInformation()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.userAccountUpdateSuccess)
        else:
            flash(label_reason.userAccountUpdateFailed)
        return redirect(url_for('landingOwner'))


    def handleLandmarkCreation(self):
        landmark_name = request.form.get(label.landmark_name)
        result = Landmark(landmark_name).createObject()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.landmarkCreationSuccess)
        else:
            flash(label_reason.landmarkCreationFailed)
        return redirect('landingOwner')


    def handleViewStop(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        queryResult = ComplexOperation().getAllStops()
        self.response_data = [stopObj.serialize() for stopObj in queryResult]


    def handleStopCreation(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        stop_name = request.form.get(label.stop_name)
        stop_address = request.form.get(label.stop_address)
        landmark_id = request.form.get(label.landmark_id)
        result = Stop(name= stop_name, address= stop_address, landmarkId= landmark_id).createObject()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.stopCreationSuccess
        else:
            self.response_data[label.details] = label_reason.stopCreationFailed


    def handleScheduleCreation(self):
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
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
        result = scheduleObj.createObject()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.scheduleCreationSuccess
        else:
            self.response_data[label.details] = label_reason.scheduleCreationFailed

    def handleViewSchedule(self):
        print(session.keys())
        print(session[label.username],
        session[label.session])
        if Owner.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        username = session[label.username]
        queryResult = ComplexOperation().getOwnerSchedules(ownerUsername= username)
        self.response_data = [
            {
                Schedule.__tablename__ : scheduleObj.serialize(),
                Bus.__tablename__ : busObj.serialize(),
                Owner.__tablename__ : ownerObj.serialize()
            } for (scheduleObj, busObj, ownerObj) in queryResult
        ]

