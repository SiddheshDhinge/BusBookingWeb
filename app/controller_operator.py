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
from .model.complex_operations import ComplexOperation
from .model.session_manager import getSessionStatus
# from model.session_manager import getSessionStatus, addActiveSession

from . import label

class ControllerOperator:

    def __init__(self):
        self.response_data = {}

    def handleRequest(self):
        service_id = int(request.form.get(label.service))

        if(service_id == 1):
            # create Operator
            self.handleAccountCreation()

        elif(service_id == 2):
            #login Operator
            self.handleLogin()

        elif(service_id == 3):
            #logout Operator
            self.handleLogout()

        elif(service_id == 4):
            #view schedules
            self.handleViewSchedule()

        elif(service_id == 5):
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
        if Operator.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        result = Operator(username=None, password=None, name=None, address=None, contact=None).logoutOperator()
        self.response_data[label.success] = result

    def handleUpdateAccountProfile(self):
        if Operator.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
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
        if Operator.isLoggedOn() == False:
            self.response_data[label.success] = label.authReq
            return
        
        username = session[label.username]
        qryResult = ComplexOperation().getOperatorSchedules(operatorUsername= username)
        self.response_data = [
            {
                Schedule.__tablename__ : scheduleObj.serialize(),
                Bus.__tablename__ : busObj.serialize(),
                Owner.__tablename__ : ownerObj.serialize(),
                Stop.__tablename__ : stopObj.serialize(),
                Landmark.__tablename__ : landmarkObj.serialize()
            } for (scheduleObj, busObj, ownerObj, stopObj, landmarkObj) in qryResult
        ]

    # def handleViewAllOperator(self):
    #     if Operator.isLoggedOn() == False:
    #         self.response_data[label.success] = label.authReq
    #         return

    #     qryResult = ComplexOperation().getAllOperators()
    #     self.response_data = [operatorObj.serialize() for operatorObj in qryResult]