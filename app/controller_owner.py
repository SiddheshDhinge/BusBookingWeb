from flask import render_template, session, request, jsonify, flash, redirect, url_for
from .model.model_owner import Owner
from .model.model_customer import Customer
from .model.model_operator import Operator
from .model.model_bus import Bus
from .model.model_passenger import Passenger
from .model.model_schedule import Schedule
from .model.model_city import City
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
            #add a City
            self.handleCityCreation()
        
        elif(service_id == 7):
            #add a Stop
            self.handleStopCreation()

        elif(service_id == 8):
            #add a schedule
            self.handleScheduleCreation()

        elif(service_id == 9):
            #update profile
            self.handleUpdateAccountProfile()

        else:
            self.response_data[label.success] = False

        return jsonify(self.response_data)
        

    def handleAccountCreation(self):
        username = request.form.get(label.owner_username)
        password = request.form.get(label.owner_password)
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
        username = request.form.get(label.owner_username)
        password = request.form.get(label.owner_password)
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
            return redirect(url_for('landingOwner'))


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


    def handleBusRegistration(self):
        numberPlate = request.form.get(label.bus_numberPlate)
        busType = request.form.get(label.bus_busType)
        totalFloors = request.form.get(label.bus_totalFloors)
        floorRows = request.form.get(label.bus_floorRows)
        floorColumns = request.form.get(label.bus_floorColumns)
        walkingGapRow = request.form.get(label.bus_walkingGapRow)
        username = session[label.username]
        result = Bus(numberPlate=numberPlate, bustype=busType, totalFloors=totalFloors, floorRows=floorRows, floorColumns=floorColumns, walkingGapRow=walkingGapRow, username=username).createObject()
        self.response_data[label.success] = result

        if(result == True):
            flash(label_reason.busRegistrationSuccess)
        else:
            flash(label_reason.busRegistrationFailed)
        return redirect(url_for('landingOwner'))


    def handleViewBus(self):
        # get all owners registered bus
        username = session[label.username]
        self.response_data = ComplexOperation().getOwnerBuses(ownerUsername= username)
        self.response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('viewBus.html', response_data= self.response_data)


    def handleCityCreation(self):
        city_name = request.form.get(label.city_name)
        result = City(name= city_name).createObject()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.cityCreationSuccess)
        else:
            flash(label_reason.cityCreationFailed)
        return redirect(url_for('landingOwner'))


    def handleStopCreation(self):
        stop_name = request.form.get(label.stop_name)
        stop_address = request.form.get(label.stop_address)
        city_id = request.form.get(label.city_id)
        result = Stop(name= stop_name, address= stop_address, cityId= city_id).createObject()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.stopCreationSuccess)
        else:
            flash(label_reason.stopCreationFailed)
        return redirect(url_for('landingOwner'))


    def handleScheduleCreation(self):
        operator_username = request.form.get(label.operator_username)
        fromDate = request.form.get(label.schedule_fromDate)
        toDate = request.form.get(label.schedule_toDate)
        departureTime = request.form.get(label.schedule_departureTime)
        dropTime = request.form.get(label.schedule_dropTime)
        fairFees = request.form.get(label.schedule_fairFees)
        fromCity = request.form.get(label.schedule_fromCity)
        toCity = request.form.get(label.schedule_toCity)
        numberPlate = request.form.get(label.schedule_numberPlate)
        scheduleObj = Schedule(
            fromDate=fromDate, toDate=toDate, departureTime=departureTime, dropTime=dropTime, 
            fairFees=fairFees, fromCity=fromCity, toCity=toCity, numberPlate=numberPlate, username=operator_username
        )
        result = scheduleObj.createObject()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.scheduleCreationSuccess)
            session[label.schedule_id] = scheduleObj.scheduleId
            return redirect(url_for('viewScheduleDetails'))
        else:
            flash(label_reason.scheduleCreationFailed)
            return redirect(url_for('landingOwner'))
    

    def handleViewScheduleDetails(self):
        try:
            scheduleId = request.form.get(label.schedule_id, None)
            #Load from session
            if not scheduleId:
                scheduleId = session[label.schedule_id]
                session.pop(label.schedule_id, None)
            scheduleId = int(scheduleId)
        except:
            flash(label_reason.invalidScheduleIdError)
            return redirect(url_for('viewSchedules'))
        
        username = session[label.username]
        response_data = ComplexOperation().getSchedule(scheduleId= scheduleId, owner_username= username)

        if not response_data[label.success]:
            flash(label_reason.invalidScheduleIdError)
            return redirect(url_for('viewSchedules'))
        
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        
        # return jsonify(response_data)
        return render_template('viewScheduleDetails.html', response_data= response_data)

    def handleScheduleStopUpdation(self, sequence):
        # Validating Stops
        if not sequence:
            # Empty Field Submitted
            flash(label_reason.invalidStopSequenceError)
            return redirect(url_for("viewScheduleDetails"))
        
        stop_sequence = []
        invalidFlag = False
        sequence = sequence[:-1].split(',')
        for tmpStop in sequence:
            try:
                tmpStopInt = int(tmpStop)
                if tmpStopInt < 0:
                    invalidFlag = True
                else:
                    stop_sequence.append(tmpStopInt)
            except Exception:
                invalidFlag = True

        if invalidFlag:
            # Field either not selected or tampered
            flash(label_reason.invalidStopSequenceError)
            return redirect(url_for("viewScheduleDetails"))
        
        scheduleId = request.form.get(label.schedule_id, None)
        result = ComplexOperation().updateScheduleStop(scheduleId=scheduleId, stop_sequence= stop_sequence)

        if result:
            # Successfully updated
            flash(label_reason.scheduleStopUpdationSuccess)
        else:
            # Invalid Stop Id entered
            flash(label_reason.scheduleStopUpdationFailed)
        
        return redirect(url_for("viewScheduleDetails"))
    
    def handleTripStatusUpdation(self):
        tripStatus = request.form.get(label.schedule_isComplete, None)
        if not tripStatus or tripStatus != "complete":
            flash(label_reason.invalidTripStatusError)
            return redirect(url_for("viewScheduleDetails"))

        scheduleId = request.form.get(label.schedule_id)
        ComplexOperation().updateTripStatus(scheduleId= scheduleId)
        flash(label_reason.tripUpdationSuccess)
        return redirect(url_for("viewScheduleDetails"))