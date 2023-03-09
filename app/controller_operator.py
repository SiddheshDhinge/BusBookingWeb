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
from .model.complex_operations import ComplexOperation
from .model.session_manager import getSessionStatus
# from model.session_manager import getSessionStatus, addActiveSession

from . import label, label_reason

class ControllerOperator:

    def __init__(self):
        self.response_data = {}


    def handleAccountCreation(self):
        username = request.form.get(label.operator_username)
        password = request.form.get(label.operator_password)
        name = request.form.get(label.operator_name)
        contact = request.form.get(label.operator_contact)
        address = request.form.get(label.operator_address)
        result = Operator(username=username, password=password, name=name, address=address, contact=contact).createOperator()
        self.response_data[label.success] = result
        if(result == True):
            flash(label_reason.userCreationSuccess)
            return redirect(url_for('login', role= Operator.accessType))
        else:
            flash(label_reason.userCreationFailed)
            return redirect(url_for('signUp', role= Operator.accessType))


    def handleLogin(self):
        username = request.form.get(label.operator_username)
        password = request.form.get(label.operator_password)
        result = Operator(username=username, password=password, name=None, address=None, contact=None).loginOperator()
        self.response_data[label.success] = result
          
        if(result == True):
            # Successful login redirect to landing page
            flash(label_reason.userLoginSuccess)
            session.permanent = True
            return redirect(url_for('landingOperator'))
        else:
            # failed login try again
            flash(label_reason.userLoginFailed)
            return redirect(url_for('login', role= Operator.accessType))
    

    @Operator.requireLogin
    def handleLogout(self):
        result = Operator(username=None, password=None, name=None, address=None, contact=None).logoutOperator()
        self.response_data[label.success] = result

        if(result == True):
            # Logout Success
            flash(label_reason.userLogoutSuccess)
            return redirect(url_for('chooseLogin'))
        else:
            # Logout Failed
            flash(label_reason.userLogoutFailed)
            return redirect(url_for('landingOperator'))


    def handleUpdateAccountProfile(self):
        name = request.form.get(label.operator_name)
        contact = request.form.get(label.operator_contact)
        address = request.form.get(label.operator_address).strip()
        username = session[label.username]

        operatorObj = Operator(username=username, password=None, name=name, address=address, contact=contact)
        result = operatorObj.updateInformation()
        self.response_data[label.success] = result
        
        if(result == True):
            flash(label_reason.userAccountUpdateSuccess)
        else:
            flash(label_reason.userAccountUpdateFailed)
        return redirect(url_for('landingOperator'))

    

    # def handleViewAllOperator(self):
    #     if Operator.isLoggedOn() == False:
    #         self.response_data[label.success] = label.authReq
    #         return

    #     qryResult = ComplexOperation().getAllOperators()
    #     self.response_data = [operatorObj.serialize() for operatorObj in qryResult]