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


# Import Dependencies
from flask import render_template, session, flash, request, jsonify, redirect, url_for


class CommonRequestHandler:
    def index(self):
        return render_template('index.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_login_signup
            }
        })

    def bookbus(self):
        return render_template('bookbus.html')

    def details(self):
        return render_template('details.html')

    def ticket(self):
        return render_template('ticket.html')


    # for selection of sign up type
    def chooseSignUp(self):
        return render_template('chooseSignUp.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_login
            }
        })


    # Actual signup (Owner / Operator / Customer)
    def signUp(self, role):
        if(request.method == 'POST'):
            if(role == Owner.accessType):
                return ControllerOwner().handleAccountCreation()
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
            elif role == Customer.accessType:
                response_data[label.name_labels] = label.customer_all_label
            else:
                #Tried to access invalid role, returned role choice
                return redirect(url_for('chooseSignUp'))
            
            #Returned valid role login
            response_data[label.role] = role
            return render_template('signUp.html', response_data= response_data)


    # for selection of login type
    def chooseLogin(self):
        return render_template('chooseLogin.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_signup
            }
        })


    # Actual Login of type (Owner /  Operator / Customer)
    def login(self, role):
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


    # logout works with visiting url via POST
    def logout(self):
        role = session.get(label.accessType, None)
        if(role == Owner.accessType):
            return ControllerOwner().handleLogout()
        elif(role == Operator.accessType):
            return ControllerOperator().handleLogout()
        elif(role == Customer.accessType):
            return ControllerCustomer().handleLogout()
        else:
            return label_reason.error
        

    # Change user Password, needs to be logged in
    def changePassword(self):
        if(request.method == 'POST'):
            role = session[label.accessType]
            if(role == Owner.accessType):
                return ControllerOwner().handleChangePassword()
            elif(role == Operator.accessType):
                return ControllerOperator().handleChangePassword()
            elif(role == Customer.accessType):
                return ControllerCustomer().handleChangePassword()
            else:
                flash(label_reason.error)
                return redirect(url_for('changePassword'))
        else:
            role = session[label.accessType]
            response_data = {}
            if(role == Owner.accessType):
                response_data[label.name_labels] = label.owner_all_label
            elif(role == Operator.accessType):
                response_data[label.name_labels] = label.operator_all_label
            elif(role == Customer.accessType):
                response_data[label.name_labels] = label.customer_all_label
                
            return render_template('changePassword.html', response_data= response_data)


    def layout(self):
        flash(label_reason.loginInRequired)
        return render_template('easterEgg.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_login_signup
            }
        })


    # fallback handler in case of not found (404)
    def pageNotFound(self, e):
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


class OwnerRequestHandler:
    # Landing Page for Owner
    @Owner.requireLogin
    def landingOwner(self):
        return render_template('landingOwner.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


    # Bus Registration
    @Owner.requireLogin
    def addBus(self):
        if(request.method == 'POST'):
            if(request.form[label.bus_busType] not in ('SEAT', 'SLEEP')):
                #invalid bus type
                flash(label_reason.busInvalidTypeFailed)
                return redirect(url_for('landingOwner'))
            else:
                #create bus
                return ControllerOwner().handleBusRegistration()
        else:
            return render_template('addBus.html', response_data= {
                label.options : {
                    label.nav_btn : label.btn_logout
                }
            })


    # View All registered bus of the Owner
    @Owner.requireLogin
    def viewBus(self):
        return ControllerOwner().handleViewBus()


    # View Specific Bus Details
    @Owner.requireLogin
    def viewBusDetails(self):
        return ControllerOwner().handleViewBusDetails()


    # Register Operator
    @Owner.requireLogin
    def registerOperator(self):
        if(request.method == 'POST'):
            return ControllerOwner().handleOperatorAccountCreation()
        else:
            response_data = {
                label.name_labels : label.operator_all_label,
                label.role : Operator.accessType
            }
            return render_template('signUp.html', response_data= response_data)


    @Owner.requireLogin
    def viewOperator(self):
        return ControllerOwner().handleViewOperator()


    # Update Owners profile
    @Owner.requireLogin
    def updateOwnerProfile(self):
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
    @Owner.requireLogin
    def viewCity(self):
        search = request.form.get(label.search)
        response_data = ComplexOperation().getAllCity(search=search)
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('viewCity.html', response_data= response_data)
            

    # Register a City
    @Owner.requireLogin
    def addCity(self):
        if(request.method == 'POST'):
            return ControllerOwner().handleCityCreation()
        else:
            return render_template('addCity.html', response_data= {
                label.options : {
                    label.nav_btn : label.btn_logout
                }
            })


    # View all regisited Stop
    @Owner.requireLogin
    def viewStop(self):
        search = request.form.get(label.search)
        response_data = ComplexOperation().getAllStop(search=search)
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('viewStop.html', response_data= response_data)
            

    # Register a Stop
    @Owner.requireLogin
    def addStop(self):
        if(request.method == 'POST'):
            return ControllerOwner().handleStopCreation()
        else:
            response_data = ComplexOperation().getAllCity(search= None)
            response_data[label.options] = {
                label.nav_btn : label.btn_logout
            }
            return render_template('addStop.html', response_data= response_data)
        

    # Add A new schedule
    @Owner.requireLogin
    def addSchedule(self):
        if(request.method == 'POST'):
            return ControllerOwner().handleScheduleCreation()
        else:
            username = session[label.username]
            allCity = ComplexOperation().getAllCity(search= None)
            allOperators = ComplexOperation().getOwnerOperators(ownerUsername= username)
            response_data = ComplexOperation().getOwnerBuses(ownerUsername= username)
            response_data[label.data].update(allOperators[label.data])
            response_data[label.data].update(allCity[label.data])
            response_data[label.options] = {
                label.nav_btn : label.btn_logout
            }
            
            return render_template('addSchedule.html', response_data= response_data)


    # View a Schedule in detail
    @Owner.requireLogin
    def viewScheduleDetails(self):
        return ControllerOwner().handleViewScheduleDetails()


    # Update a Schedules Stops
    @Owner.requireLogin
    def updateStops(self):
        sequence = request.form.get(label.at_sequence, None)
        # Validating Schedule

        scheduleId = request.form.get(label.schedule_id, None)
        if not scheduleId:
            flash(label_reason.invalidScheduleIdError)
            return redirect(url_for("viewSchedules"))
        
        username = session[label.username]
        result = ComplexOperation().isScheduleOfOwner(scheduleId= scheduleId, ownerUsername= username)
        if not result:
            flash(label_reason.invalidScheduleIdError)
            return redirect(url_for("viewSchedules"))

        # Set return point        
        session[label.schedule_id] = request.form.get(label.schedule_id)

        return ControllerOwner().handleScheduleStopUpdation(sequence= sequence)


    @Owner.requireLogin
    def updateTripStatus(self):
        # Validating Schedule
        scheduleId = request.form.get(label.schedule_id, None)
        if not scheduleId:
            flash(label_reason.invalidScheduleIdError)
            return redirect(url_for("viewSchedules"))
        
        username = session[label.username]
        result = ComplexOperation().isScheduleOfOwner(scheduleId= scheduleId, ownerUsername= username)
        if not result:
            flash(label_reason.invalidScheduleIdError)
            return redirect(url_for("viewSchedules"))

        # Set return point        
        session[label.schedule_id] = request.form.get(label.schedule_id)

        return ControllerOwner().handleTripStatusUpdation()



class OperatorRequestHandler:
    # Landing Page for Operator
    @Operator.requireLogin
    def landingOperator(self):
        return render_template('landingOperator.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


    # Update Operators profile
    @Operator.requireLogin
    def updateOperatorProfile(self):
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
    @Operator.requireLogin
    def viewOperatorSchedules(self):
        username = session[label.username]
        response_data = ComplexOperation().getOperatorSchedules(operatorUsername= username)
        response_data[label.options] = {
            label.nav_btn : label.btn_logout
        }
        return render_template('viewOperatorSchedules.html', response_data= response_data)


    @Operator.requireLogin
    def viewOperatorScheduleDetails(self):
        return ControllerOperator().handleViewOperatorScheduleDetails()



class CustomerRequestHandler:
    # Landing Page for Customer
    @Customer.requireLogin
    def landingCustomer(self):
        return render_template('landingCustomer.html', response_data= {
            label.options : {
                label.nav_btn : label.btn_logout
            }
        })


    # Update Customer profile
    @Customer.requireLogin
    def updateCustomerProfile(self):
        if(request.method == 'POST'):
            return ControllerCustomer().handleUpdateAccountProfile()
        else:
            return render_template('updateCustomerProfile.html', response_data= {
                label.name_labels : label.customer_all_label,
                label.options : {
                    label.nav_btn : label.btn_logout
                }
            })


    @Customer.requireLogin
    def registerPassenger(self):
        if(request.method == 'POST'):
            return ControllerCustomer().handleRegisterPassenger()
        else:
            return render_template('registerPassenger.html', response_data={
                label.options : {
                    label.nav_btn : label.btn_logout
                }
            })


    @Customer.requireLogin
    def viewPassengers(self):
        return ControllerCustomer().handleViewPassengers()


    @Customer.requireLogin
    def bookSchedule(self):
        return ControllerCustomer().handleBookSchedule()


    @Customer.requireLogin
    def confirmBookSchedule(self):
        return ControllerCustomer().handleConfirmBookSchedule()


    @Customer.requireLogin
    def viewBookings(self):
        return ControllerCustomer().handleViewBooking()


    @Customer.requireLogin
    def viewBookingDetails(self, bookingId):
        return ControllerCustomer().handleViewBookingDetails(bookingId= bookingId)
        


class CustomCommonRequestHandler:
    # View All Schedules (works with filters => (see ComplexOperation))
    def viewSchedules(self):
        if((Owner.isLoggedOn() or Customer.isLoggedOn()) == False):
            flash(label_reason.loginInRequired)
            return redirect(url_for('chooseLogin'))
        
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
            ownerAgencyName = request.form.get(label.owner_agencyName, 'all')
            sortPrice = request.form.get(label.filterSortPrice, 'no')
            tripStatus = request.form.get(label.filterTripStatus, 'incomplete')
            if(tripStatus == 'incomplete' or Customer.isLoggedOn()):
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
                label.owner_agencyName : ownerAgencyName,
                label.filterSortPrice : sortPrice,
                label.filterTripStatus : tripStatus
            }

            response_data = ComplexOperation().getAllSchedules(filters= filters)
            response_data[label.data][City.objListName] = ComplexOperation().getAllCity(search= None)[label.data][City.objListName]
            response_data[label.options] = {
                label.nav_btn : label.btn_logout,
                label.owner_username : session[label.username],
                label.accessType : session[label.accessType]
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
                label.nav_btn : label.btn_logout,
                label.accessType : session[label.accessType]
            }
            return render_template('viewSchedules.html', response_data= response_data)



class APIRequstHandler:
    # API For getting all stops in cities
    @Owner.requireLogin
    def getStopsByCity(self):
        response_data = ComplexOperation().getAllStopsByCity()
        return jsonify(response_data)


    # View Specific Bus Details API
    def getBusDetails(self):
        if((Owner.isLoggedOn() or Customer.isLoggedOn()) == False):
            flash(label_reason.loginInRequired)
            return redirect(url_for('chooseLogin'))
        
        numberPlate = request.form.get(label.bus_numberPlate)
        response_data = ComplexOperation().getBusDetails(numberPlate= numberPlate, ownerUsername= None, useOwnerUsername= False)
        return jsonify(response_data)