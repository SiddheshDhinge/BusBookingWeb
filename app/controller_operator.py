from flask import render_template, session, request, jsonify, flash, redirect
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

from . import label, label_reason

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
            self.response_data[label.success] = False

        return jsonify(self.response_data)
        

    def handleAccountCreation(self):
        username = request.form.get(label.username)
        password = request.form.get(label.password)
        name = request.form.get(label.name)
        address = request.form.get(label.operator_address)
        contact = request.form.get(label.contact)
        result = Operator(username=username, password=password, name=name, address=address, contact=contact).createOperator()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.userCreationSuccess
        else:
            self.response_data[label.details] = label_reason.userCreationFailed


    def handleLogin(self):
        if(request.method == 'POST'):
            username = request.form.get(label.username)
            password = request.form.get(label.password)
            result = Operator(username=username, password=password, name=None, address=None, contact=None).loginOperator()
            self.response_data[label.success] = result
            
            if(result == True):
                flash(label_reason.userLoginSuccess)
                session.permanent = True
                return redirect('/')
            else:   
                flash(label_reason.userLoginFailed)
                return render_template('login.html', 
                    username = label.username,
                    password = label.password,
                    role = Operator.accessType
                )
        else:
            return render_template('login.html', 
                username = label.username,
                password = label.password,
                role = Operator.accessType
            )

    def handleLogout(self):
        if Operator.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        result = Operator(username=None, password=None, name=None, address=None, contact=None).logoutOperator()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.userLogoutSuccess
        else:
            self.response_data[label.details] = label_reason.userLogoutFailed


    def handleUpdateAccountProfile(self):
        if Operator.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
            return
        
        name = request.form.get(label.name)
        address = request.form.get(label.operator_address)
        contact = request.form.get(label.contact)
        username = session[label.username]
        operatorObj = Operator(username=username, password=None, name=name, address=address, contact=contact)
        result = operatorObj.updateInformation()
        self.response_data[label.success] = result
        if(result == True):
            self.response_data[label.details] = label_reason.userAccountUpdateSuccess
        else:
            self.response_data[label.details] = label_reason.userAccountUpdateFailed


    def handleViewSchedule(self):
        if Operator.isLoggedOn() == False:
            self.response_data[label.success] = label_reason.loginInRequired
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