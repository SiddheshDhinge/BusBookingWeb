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
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        name = request.form.get(label.name)
        contact = request.form.get(label.contact)
        result = Customer(username=username, password=password, name=name, contact=contact).createCustomer()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.userCreationSuccess
        else:
            self.response_data[label.details] = label_reason.userCreationFailed

    def handleLogin(self):
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        result = Customer(username=username, password=password, name=None, contact=None).loginCustomer()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.userLoginSuccess
        else:
            self.response_data[label.details] = label_reason.userLoginFailed


    def handleLogout(self):
        if Customer.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        result = Customer(username=None, password=None, name=None, address=None, contact=None).logoutCustomer()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.userLogoutSuccess
        else:
            self.response_data[label.details] = label_reason.userLogoutFailed


    def handleUpdateAccountProfile(self):
        if Customer.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        name = request.form.get(label.name)
        contact = request.form.get(label.contact)
        username = session[label.username]
        customerObj = Customer(username=username, password=None, name=name, contact=contact)
        result = customerObj.updateInformation()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.userAccountUpdateSuccess
        else:
            self.response_data[label.details] = label_reason.userAccountUpdateFailed


    def handleAddPassenger(self):
        if Customer.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        name = request.form.get(label.passenger_name)
        contact = request.form.get(label.passenger_contact)
        gender = request.form.get(label.passenger_gender)
        age = int(request.form.get(label.passenger_age))
        username = session[label.username]
        result = Passenger(name= name, gender= gender, age= age, contact=contact, username= username).createObject()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.passengerCreationSuccess
        else:
            self.response_data[label.details] = label_reason.passengerCreationFailed


    def handleViewPassenger(self):
        if Customer.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        username = session[label.username]
        queryResult = ComplexOperation().getCustomerPassengers(customerUsername= username)
        self.response_data = [passengerObj.serialize() for passengerObj in queryResult]


    def handleAddBooking(self):
        if Customer.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return

        seatNo = int(request.form.get(label.booking_seatNo))
        passengerId = request.form.get(label.passenger_id)
        scheduleId = request.form.get(label.schedule_id)

        result = Booking(seatNo= seatNo, scheduleId= scheduleId, passengerId= passengerId).createObject()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.bookingCreationSuccess
        else:
            self.response_data[label.details] = label_reason.bookingCreationFailed


    def handleViewBooking(self):
        if Customer.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        username = session[label.username]
        queryResult = ComplexOperation().getCustomerBooking(customerUsername= username)
        self.response_data = [
            {
                Booking.__tablename__ : bookingObj.serialize(),
                Passenger.__tablename__ : passengerObj.serialize(),
                Customer.__tablename__ : customerObj.serialize()
            } for (bookingObj, passengerObj, customerObj) in queryResult
        ]


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
                Landmark.__tablename__ : landmarkObj.serialize()
            } for (scheduleObj, busObj, ownerObj, stopObj, landmarkObj) in qryResult
        ]