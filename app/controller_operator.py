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

from . import label, label_reason

class ControllerOperator:

    def __init__(self):
        self.response_data = {}


    def handleLogin(self):
        username = request.form.get(label.operator_username)
        password = request.form.get(label.operator_password)
        result = Operator(username=username, password=password, name=None, contact=None, ownerUsername=None).loginOperator()
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
        result = Operator(username=None, password=None, name=None, contact=None, ownerUsername=None).logoutOperator()
        self.response_data[label.success] = result

        if(result == True):
            # Logout Success
            flash(label_reason.userLogoutSuccess)
            return redirect(url_for('chooseLogin'))
        else:
            # Logout Failed
            flash(label_reason.userLogoutFailed)
            return redirect(url_for('landingOperator'))


    def handleChangePassword(self):
        username = session[label.username]
        password = request.form.get(label.operator_password)
        result = Operator(username= username, password= password, name= None, contact= None, ownerUsername= None).updatePassword()
        if(result == True):
            flash(label_reason.userPasswordUpdateSuccess)
        else:
            flash(label_reason.userPasswordUpdateFailed)
        return redirect(url_for('landingOperator'))


    def handleUpdateAccountProfile(self):
        name = request.form.get(label.operator_name)
        contact = request.form.get(label.operator_contact)
        username = session[label.username]

        operatorObj = Operator(username=username, password=None, name=name, contact=contact, ownerUsername=None)
        result = operatorObj.updateInformation()
        self.response_data[label.success] = result
        
        if(result == True):
            flash(label_reason.userAccountUpdateSuccess)
        else:
            flash(label_reason.userAccountUpdateFailed)
        return redirect(url_for('landingOperator'))

    
    def handleViewOperatorScheduleDetails(self):
        scheduleId = request.form.get(label.schedule_id, None)
            
        if not scheduleId:
            flash(label_reason.invalidScheduleIdError)
            return redirect(url_for('viewOperatorSchedules'))
        
        response_data = ComplexOperation().getSchedule(scheduleId= scheduleId, ownerUsername= None, useOwnerUsername= False)
        response_data[label.data][Booking.objListName] = ComplexOperation().getBookedPassengers(scheduleId= scheduleId)[label.data][Booking.objListName]

        if not response_data[label.success]:
            flash(label_reason.invalidScheduleIdError)
            return redirect(url_for('viewSchedules'))
        
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        
        # return jsonify(response_data)
        return render_template('viewOperatorScheduleDetails.html', response_data= response_data)