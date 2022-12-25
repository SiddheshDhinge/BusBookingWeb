print("\n\n\nSTARTED\n\n\n")
from flask import Flask, render_template, session, flash, request, jsonify, redirect
from app.model.database import connectDB, createAllTables, dropAllTables
from datetime import timedelta
# Establish database session
connectDB()
createAllTables()
# from model.session_manager import getSessionStatus, addActiveSession
from app import label, label_reason
from app.controller_owner import ControllerOwner
from app.controller_operator import ControllerOperator
from app.controller_customer import ControllerCustomer

from app.model.model_owner import Owner
from app.model.model_operator import Operator
from app.model.model_customer import Customer

import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_url_path="", static_folder="app/web/static", template_folder="app/web/templates")
app.secret_key = os.environ['app_secret']
app.permanent_session_lifetime = timedelta(minutes= 5)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bookbus')
def bookbus():
    return render_template('bookbus.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

@app.route('/owner', methods=['POST'])
def owner():
    return ControllerOwner().handleRequest()

@app.route('/customer', methods=['POST'])
def customer():
    return ControllerCustomer().handleRequest()

@app.route('/operator', methods=['POST'])
def operator():
    return ControllerOperator().handleRequest()

@app.route('/chooselogin', methods=['GET'])
def chooseLogin():
    return render_template('chooseLogin.html')

@app.route('/login/<role>', methods=['GET', 'POST'])
def login(role):
    if(request.method == 'POST'):
        if(role == Owner.accessType):
            return ControllerOwner().handleLogin()
        elif(role == Operator.accessType):
            return ControllerOperator().handleLogin()
        elif(role == Customer.accessType):
            return ControllerCustomer().handleLogin()
        else:
            return label_reason.error
    else:
        if role not in (Owner.accessType, Customer.accessType, Operator.accessType):
            return render_template('chooselogin.html')
        return render_template('login.html', 
            username = label.username,
            password = label.password,
            role = role
        )


@app.route('/logout', methods=['POST'])
def logout():
    role = session.get(label.accessType, None)
    if(role == Owner.accessType):
        return ControllerOwner().handleLogout()
    elif(role == Operator.accessType):
        return ControllerOperator().handleLogout()
    elif(role == Customer.accessType):
        return ControllerCustomer().handleLogout()
    else:
        return label_reason.error
    

# OWNER BEGIN

@app.route('/landingOwner')
@Owner.requireLogin
def landingOwner():
    return render_template('landingOwner.html')

@app.route('/registerbus', methods=['GET', 'POST'])
@Owner.requireLogin
def registerBus():
    if(request.method == 'POST'):
        return ControllerOwner().handleBusRegistration()
    else:
        return render_template('registerBusForm.html')

@app.route('/viewbus', methods=['GET'])
@Owner.requireLogin
def viewBus():
    return ControllerOwner().handleViewBus()

@app.route('/updateownerprofile', methods=['GET', 'POST'])
@Owner.requireLogin
def updateOwnerProfle():
    if(request.method == 'POST'):
        return ControllerOwner().handleUpdateAccountProfile()
    else:
        return render_template('updateOwnerProfile.html')



# OWNER END


@app.route('/viewSchedules')
def viewSchedules():
    controllerObj = ControllerOperator()
    controllerObj.handleViewSchedule()
    return render_template('table.html', response_data= controllerObj.response_data)

@app.route('/debug')
def debug():
    # flash('YES OWNER!!!')
    # getSessionStatus(session[model.label.])
    return f'Session : '

@app.route('/layout')
def lay1():
    flash(label_reason.loginInRequired)
    return render_template('layout.html')

if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app