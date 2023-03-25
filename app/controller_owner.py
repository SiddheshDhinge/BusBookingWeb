from flask import render_template, session, request, jsonify, redirect, url_for
from .model.model_owner import Owner
from .model.model_customer import Customer
from .model.model_operator import Operator
from .model.model_bus import Bus
from .model.model_seat import Seat
from .model.model_passenger import Passenger
from .model.model_schedule import Schedule
from .model.model_city import City
from .model.model_stop import Stop
from .model.model_booking import Booking
from .model.model_at import At
from .model.session_manager import getSessionStatus
from .model.complex_operations import ComplexOperation

from . import label, label_reason
from .label_reason import flashMessage
import json

class ControllerOwner:

    def __init__(self):
        self.response_data = {}


    def handleAccountCreation(self):
        username = request.form.get(label.owner_username)
        password = request.form.get(label.owner_password)
        name = request.form.get(label.owner_agencyName)
        contact = request.form.get(label.owner_contact)
        result = Owner(username=username, password=password, agencyName=name, contact=contact).createOwner()
        self.response_data[label.success] = result
        if(result == True):
            flashMessage(label_reason.userCreationSuccess)
            return redirect(url_for('.login', role= Owner.accessType))
        else:
            flashMessage(label_reason.userCreationFailed)
            return redirect(url_for('.signUp', role= Owner.accessType))


    def handleLogin(self):
        username = request.form.get(label.owner_username)
        password = request.form.get(label.owner_password)
        result = Owner(username=username, password=password, agencyName=None, contact=None).loginOwner()
        self.response_data[label.success] = result
        
        if(result == True):
            flashMessage(label_reason.userLoginSuccess)
            session.permanent = True
            return redirect(url_for('.landingOwner'))
        else:
            flashMessage(label_reason.userLoginFailed)
            return redirect(url_for('.login', role= Owner.accessType))
    
    
    @Owner.requireLogin
    def handleLogout(self):
        result = Owner(None, None, None, None).logoutOwner()
        self.response_data[label.success] = result

        if(result == True):
            flashMessage(label_reason.userLogoutSuccess)
            return redirect(url_for('.chooseLogin'))
        else:
            flashMessage(label_reason.userLogoutFailed)
            return redirect(url_for('.landingOwner'))


    @Owner.requireLogin
    def handleChangePassword(self):
        username = session[label.username]
        password = request.form.get(label.owner_password)
        result = Owner(username= username, password= password, agencyName= None, contact= None).updatePassword()
        if(result == True):
            flashMessage(label_reason.userPasswordUpdateSuccess)
        else:
            flashMessage(label_reason.userPasswordUpdateFailed)
        return redirect(url_for('.landingOwner'))


    def handleOperatorAccountCreation(self):
        username = request.form.get(label.operator_username)
        password = request.form.get(label.operator_password)
        name = request.form.get(label.operator_name)
        contact = request.form.get(label.operator_contact)
        ownerUsername = session[label.username]
        result = Operator(username=username, password=password, name=name, contact=contact, ownerUsername= ownerUsername).createOperator()
        self.response_data[label.success] = result
        if(result == True):
            flashMessage(label_reason.userCreationSuccess)
        else:
            flashMessage(label_reason.userCreationFailed)
        return redirect(url_for('.landingOwner'))


    def handleViewOperator(self):
        username = session[label.username]
        self.response_data = ComplexOperation().getOwnerOperators(ownerUsername= username)
        self.response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }

        # return jsonify(self.response_data)
        return render_template('viewOperator.html', response_data= self.response_data)


    def handleUpdateAccountProfile(self):
        name = request.form.get(label.owner_agencyName)
        contact = request.form.get(label.owner_contact)
        username = session[label.username]

        ownerObj = Owner(username=username, password=None, agencyName=name, contact=contact)
        result = ownerObj.updateInformation()
        self.response_data[label.success] = result

        if(result == True):
            flashMessage(label_reason.userAccountUpdateSuccess)
        else:
            flashMessage(label_reason.userAccountUpdateFailed)
        return redirect(url_for('.landingOwner'))


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
            flashMessage(label_reason.busRegistrationSuccess)
            self.handleSeatCreation(numberPlate= numberPlate)
        else:
            flashMessage(label_reason.busRegistrationFailed)
        return redirect(url_for('.landingOwner'))


    def handleSeatCreation(self, numberPlate):
        busSeatList = json.loads(request.form.get(Seat.objListName))
        print(busSeatList)
        for seatObj in busSeatList:
            seatNo = seatObj[label.seat_seatNo]
            isEnabled = True if (seatObj[label.seat_is_enabled] == 'true') else False
            Seat(numberPlate= numberPlate, seatNo= seatNo, isEnabled= isEnabled).createObject()


    def handleViewBus(self):
        # get owners all registered bus
        username = session[label.username]
        self.response_data = ComplexOperation().getOwnerBuses(ownerUsername= username)
        self.response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('viewBus.html', response_data= self.response_data)


    def handleViewBusDetails(self):
        numberPlate = request.form.get(label.bus_numberPlate)
        self.response_data[label.options] = {
            label.nav_btn : label.btn_logout,
            label.bus_numberPlate : numberPlate
        }
        return render_template('viewBusDetails.html', response_data= self.response_data)
        

    def handleCityCreation(self):
        cityName = request.form.get(label.city_name)
        result = City(name= cityName).createObject()
        self.response_data[label.success] = result
        if(result == True):
            flashMessage(label_reason.cityCreationSuccess)
        else:
            flashMessage(label_reason.cityCreationFailed)
        return redirect(url_for('.landingOwner'))


    def handleStopCreation(self):
        stopName = request.form.get(label.stop_name)
        stopAddress = request.form.get(label.stop_address)
        cityId = request.form.get(label.city_id)
        result = Stop(name= stopName, address= stopAddress, cityId= cityId).createObject()
        self.response_data[label.success] = result
        if(result == True):
            flashMessage(label_reason.stopCreationSuccess)
        else:
            flashMessage(label_reason.stopCreationFailed)
        return redirect(url_for('.landingOwner'))


    def handleScheduleCreation(self):
        fromDate = request.form.get(label.schedule_fromDate)
        toDate = request.form.get(label.schedule_toDate)
        departureTime = request.form.get(label.schedule_departureTime)
        dropTime = request.form.get(label.schedule_dropTime)
        fairFees = request.form.get(label.schedule_fairFees)
        fromCity = request.form.get(label.schedule_fromCity)
        toCity = request.form.get(label.schedule_toCity)
        numberPlate = request.form.get(label.bus_numberPlate)
        operator_username = request.form.get(label.operator_username)

        scheduleObj = Schedule(
            fromDate=fromDate, toDate=toDate, departureTime=departureTime, dropTime=dropTime, 
            fairFees=fairFees, fromCity=fromCity, toCity=toCity, numberPlate=numberPlate, username=operator_username
        )
        result = scheduleObj.createObject()

        self.response_data[label.success] = result
        if(result == True):
            flashMessage(label_reason.scheduleCreationSuccess)
            session[label.schedule_id] = scheduleObj.scheduleId
            return redirect(url_for('.viewScheduleDetails'))
        else:
            flashMessage(label_reason.scheduleCreationFailed)
            return redirect(url_for('.landingOwner'))
    

    def handleViewScheduleDetails(self):
        try:
            scheduleId = request.form.get(label.schedule_id, None)
            #Load from session
            if not scheduleId:
                scheduleId = session[label.schedule_id]
                session.pop(label.schedule_id, None)
            scheduleId = int(scheduleId)
        except:
            flashMessage(label_reason.invalidScheduleIdError)
            return redirect(url_for('.viewSchedules'))
        
        username = session[label.username]
        response_data = ComplexOperation().getSchedule(scheduleId= scheduleId, ownerUsername= username)
        response_data[label.data][Booking.objListName] = ComplexOperation().getBookedPassengers(scheduleId= scheduleId)[label.data][Booking.objListName]

        if not response_data[label.success]:
            flashMessage(label_reason.invalidScheduleIdError)
            return redirect(url_for('.viewSchedules'))
        
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        
        # return jsonify(response_data)
        return render_template('viewScheduleDetails.html', response_data= response_data)


    def handleScheduleStopUpdation(self, sequence):
        # Validating Stops
        if not sequence:
            # Empty Field Submitted
            flashMessage(label_reason.invalidStopSequenceError)
            return redirect(url_for("viewScheduleDetails"))
        
        stopSequence = []
        invalidFlag = False
        sequence = sequence[:-1].split(',')
        for tmpStop in sequence:
            try:
                tmpStopInt = int(tmpStop)
                if tmpStopInt < 0:
                    invalidFlag = True
                else:
                    stopSequence.append(tmpStopInt)
            except Exception:
                invalidFlag = True

        if invalidFlag:
            # Field either not selected or tampered
            flashMessage(label_reason.invalidStopSequenceError)
            return redirect(url_for("viewScheduleDetails"))
        
        scheduleId = request.form.get(label.schedule_id, None)
        result = ComplexOperation().updateScheduleStop(scheduleId=scheduleId, stopSequence= stopSequence)

        if result:
            # Successfully updated
            flashMessage(label_reason.scheduleStopUpdationSuccess)
        else:
            # Invalid Stop Id entered
            flashMessage(label_reason.scheduleStopUpdationFailed)
        
        return redirect(url_for("viewScheduleDetails"))
    
    
    def handleTripStatusUpdation(self):
        tripStatus = request.form.get(label.schedule_isComplete, None)
        if not tripStatus or tripStatus != "complete":
            flashMessage(label_reason.invalidTripStatusError)
            return redirect(url_for("viewScheduleDetails"))

        scheduleId = request.form.get(label.schedule_id)
        ComplexOperation().updateTripStatus(scheduleId= scheduleId)
        flashMessage(label_reason.tripUpdationSuccess)
        return redirect(url_for("viewScheduleDetails"))