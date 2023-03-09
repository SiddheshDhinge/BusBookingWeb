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
from .model.database import DB_session
from .model.session_manager import getSessionStatus
from .model.complex_operations import ComplexOperation
from . import label, label_reason

class ControllerCustomer:

    def __init__(self):
        self.response_data = {}

    def handleRequest(self):
        service_id = int(request.form.get(label.service))

        if(service_id == 1):
            # create Customer
            self.handleAccountCreation()

        elif(service_id == 2):
            #login Customer
            self.handleLogin()

        elif(service_id == 3):
            #logout Customer
            self.handleLogout()

        elif(service_id == 4):
            #view All schedules
            self.handleViewAllSchedule()

        elif(service_id == 5):
            #update profile
            self.handleUpdateAccountProfile()

        elif(service_id == 6):
            #Add a passenger
            self.handleAddPassenger()

        elif(service_id == 7):
            #View all passenger
            self.handleViewPassenger()
            
        elif(service_id == 8):
            #Add a booking
            self.handleAddBooking()

        elif(service_id == 9):
            #View My All booking
            self.handleViewBooking()

        else:
            self.response_data[label.success] = False

        return jsonify(self.response_data)
        

    def handleAccountCreation(self):
        username = request.form.get(label.customer_username)
        password = request.form.get(label.customer_password)
        name = request.form.get(label.customer_name)
        contact = request.form.get(label.customer_contact)
        result = Customer(username=username, password=password, name=name, contact=contact).createCustomer()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.userCreationSuccess)
            return redirect(url_for('login', role= Customer.accessType))
        else:
            flash(label_reason.userCreationFailed)
            return redirect(url_for('signUp', role= Customer.accessType))


    def handleLogin(self):
        username = request.form.get(label.customer_username)
        password = request.form.get(label.customer_password)
        result = Customer(username=username, password=password, name=None, contact=None).loginCustomer()
        self.response_data[label.success] = result
        
        if(result == True):
            flash(label_reason.userLoginSuccess)
            session.permanent = True
            return redirect(url_for('landingCustomer'))
        else:
            flash(label_reason.userLoginFailed)
            return redirect(url_for('login', role= Customer.accessType))
            

    @Customer.requireLogin
    def handleLogout(self):
        result = Customer(username=None, password=None, name=None, contact=None).logoutCustomer()
        self.response_data[label.success] = result

        if(result == True):
            flash(label_reason.userLogoutSuccess)
            return redirect(url_for('chooseLogin'))
        else:
            flash(label_reason.userLogoutFailed)
            return redirect(url_for('landingCustomer'))


    def handleUpdateAccountProfile(self):
        name = request.form.get(label.customer_name)
        contact = request.form.get(label.customer_contact)
        username = session[label.username]

        customerObj = Customer(username=username, password=None, name=name, contact=contact)
        result = customerObj.updateInformation()
        self.response_data[label.success] = result

        if(result == True):
            flash(label_reason.userAccountUpdateSuccess)
        else:
            flash(label_reason.userAccountUpdateFailed)
        return redirect(url_for('landingCustomer'))


    def handleRegisterPassenger(self):    
        name = request.form.get(label.passenger_name)
        contact = request.form.get(label.passenger_contact)
        gender = request.form.get(label.passenger_gender)
        age = int(request.form.get(label.passenger_age))
        username = session[label.username]
        result = Passenger(name= name, gender= gender, age= age, contact=contact, username= username).createObject()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.passengerCreationSuccess)
        else:
            flash(label_reason.passengerCreationFailed)
        return redirect(url_for('landingCustomer'))


    def handleViewPassengers(self):
        username = session[label.username]
        self.response_data = ComplexOperation().getCustomerPassengers(customerUsername= username)
        self.response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('viewPassengers.html', response_data= self.response_data)


    def handleBookSchedule(self):
        scheduleId = request.form.get(label.schedule_id)
        username = session[label.username]
        session[label.schedule_id] = scheduleId
        
        self.response_data = ComplexOperation().getSchedule(scheduleId= scheduleId, owner_username= None, useOwnerUsername= False)
        self.response_data[label.data][Passenger.objListName] = ComplexOperation().getCustomerPassengers(customerUsername= username)[label.data][Passenger.objListName]
        self.response_data[label.data][Booking.objListName] = ComplexOperation().getBookedPassengers(scheduleId= scheduleId)[label.data][Booking.objListName]
        self.response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }

        # return jsonify(self.response_data)
        return render_template('bookSchedule.html', response_data= self.response_data)


    def handleConfirmBookSchedule(self):
        scheduleId = session[label.schedule_id]
        session.pop(label.schedule_id)
        scheduleObj = ComplexOperation().getSchedule(scheduleId= scheduleId, owner_username= None, useOwnerUsername= False)
        numberPlate = scheduleObj[label.data][Schedule.objName][Bus.objName][label.bus_numberPlate]
        seatNo = request.form.get(label.seat_seatNo)
        passengerId = request.form.get(label.passenger_id)
        fromStopId = request.form.get(label.booking_fromStopId)
        toStopId = request.form.get(label.booking_toStopId)

        bookingObj = Booking(numberPlate= numberPlate, seatNo= seatNo, scheduleId= scheduleId, passengerId= passengerId, fromStopId= fromStopId, toStopId= toStopId)
        result = bookingObj.createObject()

        if(result == True):
            flash(label_reason.bookingCreationSuccess)
            session[label.booking_id] = bookingObj.bookingId
            return redirect(url_for('viewBookingDetails'))
        else:
            flash(label_reason.bookingCreationFailed)
            return redirect(url_for('landingCustomer'))


    def handleViewBooking(self):
        username = session[label.username]
        self.response_data = ComplexOperation().getCustomerBookings(customerUsername= username)
        self.response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }

        # return jsonify(self.response_data)
        return render_template('viewBooking.html', response_data= self.response_data)



    def handleViewBookingDetails(self, bookingId):
        self.response_data = ComplexOperation().getBookingDetails(bookingId= bookingId)


        # return jsonify(self.response_data)
        return render_template('viewBookingDetails.html', response_data= self.response_data)
    

    def handleViewAllSchedule(self):
        if Customer.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        qryResult = ComplexOperation().getAllSchedules()
        self.response_data = [
            {
                Schedule.__tablename__ : scheduleObj.serialize(),
                Bus.__tablename__ : busObj.serialize(),
                Owner.__tablename__ : ownerObj.serialize(),
                Stop.__tablename__ : stopObj.serialize(),
                City.__tablename__ : cityObj.serialize()
            } for (scheduleObj, busObj, ownerObj, stopObj, cityObj) in qryResult
        ]