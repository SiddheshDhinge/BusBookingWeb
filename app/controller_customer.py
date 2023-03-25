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
from .label_reason import flashMessage

class ControllerCustomer:

    def __init__(self):
        self.response_data = {}


    def handleAccountCreation(self):
        username = request.form.get(label.customer_username)
        password = request.form.get(label.customer_password)
        name = request.form.get(label.customer_name)
        contact = request.form.get(label.customer_contact)
        result = Customer(username=username, password=password, name=name, contact=contact).createCustomer()
        self.response_data[label.success] = result
        if(result == True):
            flashMessage(label_reason.userCreationSuccess)
            return redirect(url_for('.login', role= Customer.accessType))
        else:
            flashMessage(label_reason.userCreationFailed)
            return redirect(url_for('.signUp', role= Customer.accessType))


    def handleLogin(self):
        username = request.form.get(label.customer_username)
        password = request.form.get(label.customer_password)
        result = Customer(username=username, password=password, name=None, contact=None).loginCustomer()
        self.response_data[label.success] = result
        
        if(result == True):
            flashMessage(label_reason.userLoginSuccess)
            session.permanent = True
            return redirect(url_for('.landingCustomer'))
        else:
            flashMessage(label_reason.userLoginFailed)
            return redirect(url_for('.login', role= Customer.accessType))
            

    @Customer.requireLogin
    def handleLogout(self):
        result = Customer(username=None, password=None, name=None, contact=None).logoutCustomer()
        self.response_data[label.success] = result

        if(result == True):
            flashMessage(label_reason.userLogoutSuccess)
            return redirect(url_for('.chooseLogin'))
        else:
            flashMessage(label_reason.userLogoutFailed)
            return redirect(url_for('.landingCustomer'))


    @Customer.requireLogin
    def handleChangePassword(self):
        username = session[label.username]
        oldPassword = request.form.get(label.customer_old_password)
        password = request.form.get(label.customer_password)
        result = Customer(username= username, password= password, name= None, contact= None).updatePassword(oldPassword= oldPassword)
        if(result == True):
            flashMessage(label_reason.userPasswordUpdateSuccess)
        else:
            flashMessage(label_reason.userPasswordUpdateFailed)
        return redirect(url_for('.landingCustomer'))


    def handleUpdateAccountProfile(self):
        name = request.form.get(label.customer_name)
        contact = request.form.get(label.customer_contact)
        username = session[label.username]

        customerObj = Customer(username=username, password=None, name=name, contact=contact)
        result = customerObj.updateInformation()
        self.response_data[label.success] = result

        if(result == True):
            flashMessage(label_reason.userAccountUpdateSuccess)
        else:
            flashMessage(label_reason.userAccountUpdateFailed)
        return redirect(url_for('.landingCustomer'))


    def handleRegisterPassenger(self):    
        name = request.form.get(label.passenger_name)
        contact = request.form.get(label.passenger_contact)
        gender = request.form.get(label.passenger_gender)
        age = int(request.form.get(label.passenger_age))
        username = session[label.username]
        result = Passenger(name= name, gender= gender, age= age, contact=contact, username= username).createObject()
        self.response_data[label.success] = result
        if(result == True):
            flashMessage(label_reason.passengerCreationSuccess)
        else:
            flashMessage(label_reason.passengerCreationFailed)
        return redirect(url_for('.landingCustomer'))


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
        
        self.response_data = ComplexOperation().getSchedule(scheduleId= scheduleId, ownerUsername= None, useOwnerUsername= False)
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
        scheduleObj = ComplexOperation().getSchedule(scheduleId= scheduleId, ownerUsername= None, useOwnerUsername= False)
        numberPlate = scheduleObj[label.data][Schedule.objName][Bus.objName][label.bus_numberPlate]
        seatNo = request.form.get(label.seat_seatNo)
        passengerId = request.form.get(label.passenger_id)
        fromStopId = request.form.get(label.booking_fromStopId)
        toStopId = request.form.get(label.booking_toStopId)

        bookingObj = Booking(numberPlate= numberPlate, seatNo= seatNo, scheduleId= scheduleId, passengerId= passengerId, fromStopId= fromStopId, toStopId= toStopId)
        result = bookingObj.createObject()

        if(result == True):
            flashMessage(label_reason.bookingCreationSuccess)
            return redirect(url_for('.viewBookingDetails', bookingId= bookingObj.bookingId))
        else:
            flashMessage(label_reason.bookingCreationFailed)
            return redirect(url_for('.landingCustomer'))


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