print("\n\n\nSTARTED\n\n\n")
from flask import Flask, render_template, session, flash, request, jsonify, redirect, url_for
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
from app.model.complex_operations import ComplexOperation

import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_url_path="", static_folder="app/web/static", template_folder="app/web/templates")
app.secret_key = os.environ['app_secret']
app.permanent_session_lifetime = timedelta(minutes= 5)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', response_data= {
        label.options : label.optionsAll
    })

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


@app.route('/choosesignup')
def chooseSignUp():
    return render_template('chooseSignUp.html', response_data= {
        label.options : label.optionsUserLogin
    })


@app.route('/signUp/<role>', methods=['GET', 'POST'])
def signUp(role):
    if(request.method == 'POST'):
        if(role == Owner.accessType):
            return ControllerOwner().handleAccountCreation()
        elif(role == Operator.accessType):
            return ControllerOperator().handleAccountCreation()
        elif(role == Customer.accessType):
            return ControllerCustomer().handleAccountCreation()
        else:
            return label_reason.error
    else:
        if role not in (Owner.accessType, Customer.accessType, Operator.accessType):
            #Tried to access invalid role, returned role choice
            return redirect(url_for('chooseSignUp'))
        #Returned valid role login
        return render_template('signUp.html', response_data={
            'username' : label.username,
            'password' : label.password,
            'name' : label.owner_name,
            'contact' : label.owner_contact, 
            'role' : role
        })


@app.route('/chooselogin', methods=['GET'])
def chooseLogin():
    return render_template('chooseLogin.html', response_data= {
        label.options : label.optionsUserSignUp
    })

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
            #Tried to access invalid role, returned role choice
            return redirect(url_for('chooseLogin'))
        #Returned valid role login
        return render_template('login.html', response_data={
            'username' : label.username,
            'password' : label.password,
            'role' : role
        })


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
    return render_template('landingOwner.html', response_data= {
        label.options : label.optionsUserLogout
    })

@app.route('/registerbus', methods=['GET', 'POST'])
@Owner.requireLogin
def registerBus():
    if(request.method == 'POST'):
        return ControllerOwner().handleBusRegistration()
    else:
        return render_template('registerBusForm.html', response_data= {
            label.options : label.optionsUserLogout
        })

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
        return render_template('updateOwnerProfile.html', response_data= {
            label.options : label.optionsUserLogout
        })

@app.route('/viewcity', methods=['GET', 'POST'])
@Owner.requireLogin
def viewCity():
    search = request.form.get(label.search)
    response_data = ComplexOperation().getAllCity(search=search)
    response_data[label.options] = label.optionsUserLogout
    return render_template('viewCity.html', response_data= response_data)
        

@app.route('/addCity', methods=['GET', 'POST'])
@Owner.requireLogin
def addCity():
    if(request.method == 'POST'):
        return ControllerOwner().handleCityCreation()
    else:
        return render_template('addCity.html', response_data= {
            label.options: label.optionsUserLogout
        })

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

@app.errorhandler(404)
def page_not_found(e):
    # fallback handler in case of not found
    return render_template('404.html', response_data={
        label.options: label.optionsAll
    })

@app.route('/layout')
def lay1():
    flash(label_reason.loginInRequired)
    return render_template('layout.html')

if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app