print("\n\n\nSTARTED\n\n\n")


# Configure Database Connection
from app.model.database import connectDB, createAllTables
connectDB()

# Import App Modules
from app import label, label_reason
from app.controller_owner import ControllerOwner
from app.controller_operator import ControllerOperator
from app.controller_customer import ControllerCustomer
from app.model.model_owner import Owner
from app.model.model_operator import Operator
from app.model.model_customer import Customer
from app.model.complex_operations import ComplexOperation
from app.model.session_manager import getSessionStatus
from app.model.model_bus import Bus
from app.model.model_passenger import Passenger
from app.model.model_schedule import Schedule
from app.model.model_city import City
from app.model.model_stop import Stop
from app.model.model_booking import Booking
from app.model.model_at import At

#Create All Database Tables
createAllTables()


# Import Dependencies
from flask import Flask, render_template, session, flash, request, jsonify, redirect, url_for
import os
from dotenv import load_dotenv
from datetime import timedelta
load_dotenv()


# Create App and Set Secret Key, session_lifetime
app = Flask(__name__, static_url_path="", static_folder="app/web/static", template_folder="app/web/templates")
app.secret_key = os.environ['app_secret']
app.permanent_session_lifetime = timedelta(minutes= 15)
ip_address = os.environ['ip_address']


# Start Routes


# COMMON BEGIN
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', response_data= {
        label.options : {
            label.nav_btn : label.btn_login_signup
        }
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

# deprecated
# @app.route('/owner', methods=['POST'])
# def owner():
#     return ControllerOwner().handleRequest()

# @app.route('/customer', methods=['POST'])
# def customer():
#     return ControllerCustomer().handleRequest()

# @app.route('/operator', methods=['POST'])
# def operator():
#     return ControllerOperator().handleRequest()


# for selection of sign up type
@app.route('/choosesignup')
def chooseSignUp():
    return render_template('chooseSignUp.html', response_data= {
        label.options : {
            label.nav_btn : label.btn_login
        }
    })


# Actual signup (Owner / Operator / Customer)
@app.route('/signup/<role>', methods=['GET', 'POST'])
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
        response_data = {
            label.options : {}
        }
        if role == Owner.accessType:
            response_data[label.name_labels] = label.owner_all_label
        elif role == Operator.accessType:
            response_data[label.name_labels] = label.operator_all_label
        elif role == Customer.accessType:
            response_data[label.name_labels] = label.customer_all_label
        else:
            #Tried to access invalid role, returned role choice
            return redirect(url_for('chooseSignUp'))
        
        #Returned valid role login
        response_data[label.role] = role
        return render_template('signUp.html', response_data= response_data)


# for selection of login type
@app.route('/chooselogin', methods=['GET'])
def chooseLogin():
    return render_template('chooseLogin.html', response_data= {
        label.options : {
            label.nav_btn : label.btn_signup
        }
    })


# Actual Login of type (Owner /  Operator / Customer)
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
        response_data = {
            label.options : {}
        }
        if role == Owner.accessType:
            response_data[label.name_labels] = label.owner_all_label
        elif role == Operator.accessType:
            response_data[label.name_labels] = label.operator_all_label
        elif role == Customer.accessType:
            response_data[label.name_labels] = label.customer_all_label
        else:
            #Tried to access invalid role, returned role choice
            return redirect(url_for('chooseLogin'))
        
        #Returned valid role login
        response_data[label.role] = role
        return render_template('login.html', response_data= response_data)


# logout works with visiting url via POST, no Type needed
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
    

# COMMON END

# OWNER BEGIN

# Landing Page for Owner
@app.route('/landingowner')
@Owner.requireLogin
def landingOwner():
    return render_template('landingOwner.html', response_data= {
        label.options : {
            label.nav_btn : label.btn_logout
        }
    })


# Bus Registration
@app.route('/registerbus', methods=['GET', 'POST'])
@Owner.requireLogin
def registerBus():
    if(request.method == 'POST'):
        if(request.form[label.bus_busType] not in ('SEAT', 'SLEEP')):
            #invalid bus type
            flash(label_reason.busInvalidTypeFailed)
            return redirect(url_for('landingOwner'))
        else:
            #create bus
            return ControllerOwner().handleBusRegistration()
    else:
        return render_template('registerBusForm.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


# View All registered bus of the Owner
@app.route('/viewbus', methods=['GET'])
@Owner.requireLogin
def viewBus():
    return ControllerOwner().handleViewBus()


# Update Owners profile
@app.route('/updateownerprofile', methods=['GET', 'POST'])
@Owner.requireLogin
def updateOwnerProfile():
    if(request.method == 'POST'):
        return ControllerOwner().handleUpdateAccountProfile()
    else:
        return render_template('updateOwnerProfile.html', response_data= {
            label.name_labels : label.owner_all_label,
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


# View all registered Cities
@app.route('/viewcity', methods=['GET', 'POST'])
@Owner.requireLogin
def viewCity():
    search = request.form.get(label.search)
    response_data = ComplexOperation().getAllCity(search=search)
    response_data[label.options] = {
        label.nav_btn : label.btn_logout
    }
    return render_template('viewCity.html', response_data= response_data)
        

# Register a City
@app.route('/addcity', methods=['GET', 'POST'])
@Owner.requireLogin
def addCity():
    if(request.method == 'POST'):
        return ControllerOwner().handleCityCreation()
    else:
        return render_template('addCity.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


# View all regisited Stop
@app.route('/viewstop', methods=['GET', 'POST'])
@Owner.requireLogin
def viewStop():
    search = request.form.get(label.search)
    response_data = ComplexOperation().getAllStop(search=search)
    response_data[label.options] = {
        label.nav_btn : label.btn_logout
    }
    return render_template('viewStop.html', response_data= response_data)
        

# Register a Stop
@app.route('/addstop', methods=['GET', 'POST'])
@Owner.requireLogin
def addStop():
    if(request.method == 'POST'):
        return ControllerOwner().handleStopCreation()
    else:
        response_data = ComplexOperation().getAllCity(search= None)
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('addStop.html', response_data= response_data)


# View All Schedules (works with filters => (see ComplexOperation))
@app.route('/viewschedules', methods=['GET', 'POST'])
@Owner.requireLogin
def viewSchedules():
    if(request.method == 'POST'):
        # create filters
        fromCity = request.form.get(label.filterFromCity, None)
        toCity = request.form.get(label.filterToCity, None)
        fromDate = request.form.get(label.filterDate, None)
    
        #cant accept empty from and to city
        if not(fromCity and toCity):
            flash(label_reason.sourceDestinatioFailed)
            return redirect(url_for('viewSchedules'))

        #cant accept empty schedule date
        if not fromDate:
            flash(label_reason.scheduleDateFailed)
            return redirect(url_for('viewSchedules'))

        timeBlock = request.form.get(label.filterTimeBlock, 'all')
        busType = request.form.get(label.filterBusType, 'all')
        ownerUsername = request.form.get(label.owner_username, 'all')
        sortPrice = request.form.get(label.filterSortPrice, 'no')
        tripStatus = request.form.get(label.filterTripStatus, 'incomplete')
        if(tripStatus == 'incomplete'):
            tripStatus = False
        else:
            tripStatus = True
        # Build filters object
        filters = {
            label.filterDate : fromDate,
            label.filterFromCity : fromCity,
            label.filterToCity : toCity,
            label.filterTimeBlock : timeBlock,
            label.filterBusType : busType,
            label.owner_username : ownerUsername,
            label.filterSortPrice : sortPrice,
            label.filterTripStatus : tripStatus
        }

        response_data = ComplexOperation().getAllSchedules(filters= filters)
        response_data[label.data][City.objName] = ComplexOperation().getAllCity(search= None)[label.data][City.objName]
        response_data[label.options] = {
            label.nav_btn : label.btn_logout,
            label.owner_username : session[label.username]
        }        
        if(len(response_data[label.data][Schedule.objName]) == 0):
            # No results
            flash(label_reason.filterNoMatch)
        else:
            # Results found
            flash(label_reason.filterMatch)
        # return jsonify(response_data)
        return render_template('viewSchedules.html', response_data= response_data)

    else:
        # return form for filling filters of schedules
        response_data = ComplexOperation().getAllCity(search= None)
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('viewSchedules.html', response_data= response_data)


# Add A new schedule
@app.route('/addschedule', methods=['GET', 'POST'])
@Owner.requireLogin
def addSchedule():
    if(request.method == 'POST'):
        return ControllerOwner().handleScheduleCreation()
    else:
        username = session[label.username]
        allCity = ComplexOperation().getAllCity(search= None)
        response_data = ComplexOperation().getOwnerBuses(ownerUsername= username)
        response_data[label.data].update(allCity[label.data])
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('addSchedule.html', response_data= response_data)


# View a Schedule in detail
@app.route('/viewscheduledetails', methods=['GET', 'POST'])
@Owner.requireLogin
def viewScheduleDetails():
    return ControllerOwner().handleViewScheduleDetails()


# Update a Schedules Stops
@app.route('/updatestops', methods=['POST'])
@Owner.requireLogin
def updateStops():
    sequence = request.form.get(label.stop_sequence, None)
    # Validating Schedule

    scheduleId = request.form.get(label.schedule_id, None)
    if not scheduleId:
        flash(label_reason.invalidScheduleIdError)
        return redirect(url_for("viewSchedules"))
    
    username = session[label.username]
    result = ComplexOperation().isScheduleOfOwner(scheduleId= scheduleId, owner_username= username)
    if not result:
        flash(label_reason.invalidScheduleIdError)
        return redirect(url_for("viewSchedules"))

    # Set return point        
    session[label.schedule_id] = request.form.get(label.schedule_id)

    return ControllerOwner().handleScheduleStopUpdation(sequence= sequence)


@app.route('/updatetripstatus', methods=['POST'])
@Owner.requireLogin
def updateTripStatus():
    # Validating Schedule
    scheduleId = request.form.get(label.schedule_id, None)
    if not scheduleId:
        flash(label_reason.invalidScheduleIdError)
        return redirect(url_for("viewSchedules"))
    
    username = session[label.username]
    result = ComplexOperation().isScheduleOfOwner(scheduleId= scheduleId, owner_username= username)
    if not result:
        flash(label_reason.invalidScheduleIdError)
        return redirect(url_for("viewSchedules"))

    # Set return point        
    session[label.schedule_id] = request.form.get(label.schedule_id)

    return ControllerOwner().handleTripStatusUpdation()

# OWNER END


# OPERATOR BEGIN

# Landing Page for Operator
@app.route('/landingoperator')
@Operator.requireLogin
def landingOperator():
    return render_template('landingOperator.html', response_data= {
        label.options : {
            label.nav_btn : label.btn_logout
        }
    })



# Update Operators profile
@app.route('/updateoperatorprofile', methods=['GET', 'POST'])
@Operator.requireLogin
def updateOperatorProfile():
    if(request.method == 'POST'):
        return ControllerOperator().handleUpdateAccountProfile()
    else:
        return render_template('updateOperatorProfile.html', response_data= {
            label.name_labels : label.operator_all_label,
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


# View all Operator's Assigned Schedules
@app.route('/viewoperatorschedules')
@Operator.requireLogin
def viewOperatorSchedules():
    username = session[label.username]
    response_data = ComplexOperation().getOperatorSchedules(operatorUsername= username)
    response_data[label.options] = {
        label.nav_btn : label.btn_logout
    }
    return render_template('viewOperatorSchedules.html', response_data= response_data)

# OPERATOR END


# CUSTOMER BEGIN

# Landing Page for Customer
@app.route('/landingcustomer')
@Customer.requireLogin
def landingCustomer():
    return render_template('landingCustomer.html', response_data= {
        label.options : {
            label.nav_btn : label.btn_logout
        }
    })


# Update Customer profile
@app.route('/updatecustomerprofile', methods=['GET', 'POST'])
@Customer.requireLogin
def updateCustomerProfile():
    if(request.method == 'POST'):
        return ControllerCustomer().handleUpdateAccountProfile()
    else:
        return render_template('updateCustomerProfile.html', response_data= {
            label.name_labels : label.customer_all_label,
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


@app.route('/registerPassenger', methods=['GET', 'POST'])
@Customer.requireLogin
def registerPassenger():
    if(request.method == 'POST'):
        return ControllerCustomer().handleRegisterPassenger()
    else:
        return render_template('registerPassenger.html', response_data={
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


@app.route('/viewPassengers', methods=['GET'])
@Customer.requireLogin
def viewPassengers():
    return ControllerCustomer().handleViewPassengers()

# CUSTOMER END

# API BEGIN

# API For getting all stops in cities
@app.route('/getstopsbycity')
@Owner.requireLogin
def getStopsByCity():
    response_data = ComplexOperation().getAllStopsByCity()
    return jsonify(response_data)

# API END


# used for testing
@app.route('/busseats')
def busSeats():
    return render_template('registerBusForm.html', response_data= {
        label.options : {
            label.nav_btn : label.btn_login_signup
        }
    })

# @app.route('/debug')
# def debug():
#     flash('YES OWNER!!!')
#     getSessionStatus(session[model.label.])
#     return f'Session : '


@app.route('/layout')
def layout():
    flash(label_reason.loginInRequired)
    return render_template('easterEgg.html', response_data= {
        label.options : {
            label.nav_btn : label.btn_login_signup
        }
    })


# fallback handler in case of not found (404)
@app.errorhandler(404)
def page_not_found(e):
    result = getSessionStatus()[0]
    response_data = {label.options : {}}

    if(result == True):
        # User is logged In
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
    else:
        # User is Anonymous (not logged in)
        response_data[label.options] = {
            label.nav_btn : label.btn_login_signup
        }
    
    return render_template('404.html', response_data= response_data)


if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app