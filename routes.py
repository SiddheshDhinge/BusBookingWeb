from flask import Blueprint

# Import Request Handler Classes
from app.request_handler import CommonRequestHandler, OwnerRequestHandler, CustomerRequestHandler, OperatorRequestHandler, CustomCommonRequestHandler, APIRequstHandler


requestRoutes = Blueprint('request_routes', __name__)
# Start Routes


# COMMON BEGIN
@requestRoutes.route('/index')
@requestRoutes.route('/')
def index():
    return CommonRequestHandler().index()

@requestRoutes.route('/bookbus')
def bookbus():
    return CommonRequestHandler().bookbus()

@requestRoutes.route('/details')
def details():
    return CommonRequestHandler().details()

@requestRoutes.route('/ticket')
def ticket():
    return CommonRequestHandler().ticket()


# for selection of sign up type
@requestRoutes.route('/choosesignup')
def chooseSignUp():
    return CommonRequestHandler().chooseSignUp()


# Actual signup (Owner / Operator / Customer)
@requestRoutes.route('/signup/<role>', methods=['GET', 'POST'])
def signUp(role):
    return CommonRequestHandler().signUp(role= role)


# for selection of login type
@requestRoutes.route('/chooselogin', methods=['GET'])
def chooseLogin():
    return CommonRequestHandler().chooseLogin()


# Actual Login of type (Owner /  Operator / Customer)
@requestRoutes.route('/login/<role>', methods=['GET', 'POST'])
def login(role):
    return CommonRequestHandler().login(role= role)


# logout works with visiting url via POST, no Type needed
@requestRoutes.route('/logout', methods=['POST'])
def logout():
    return CommonRequestHandler().logout()    


@requestRoutes.route('/changepassword', methods=['GET', 'POST'])
def changePassword():
    return CommonRequestHandler().changePassword()


@requestRoutes.route('/viewbookingdetails/<uuid:bookingId>', methods=['GET'])
def viewBookingDetails(bookingId):
    return CustomerRequestHandler().viewBookingDetails(bookingId= bookingId)
    

# View All Schedules (works with filters => (see ComplexOperation))
@requestRoutes.route('/viewschedules', methods=['GET', 'POST'])
def viewSchedules():
    return CustomCommonRequestHandler().viewSchedules()


@requestRoutes.route('/layout')
def layout():
    return CommonRequestHandler().layout()


# fallback handler in case of not found (404)
@requestRoutes.app_errorhandler(404)
def pageNotFound(e):
    return CommonRequestHandler().pageNotFound(e= e)


# COMMON END

# OWNER BEGIN

# Landing Page for Owner
@requestRoutes.route('/landingowner')
def landingOwner():
    return OwnerRequestHandler().landingOwner()


# Bus Registration
@requestRoutes.route('/addbus', methods=['GET', 'POST'])
def addBus():
    return OwnerRequestHandler().addBus()


# View All registered bus of the Owner
@requestRoutes.route('/viewbus', methods=['GET'])
def viewBus():
    return OwnerRequestHandler().viewBus()


# View Specific Bus Details
@requestRoutes.route('/viewbusdetails', methods=['POST'])
def viewBusDetails():
    return OwnerRequestHandler().viewBusDetails()


# Register Operator
@requestRoutes.route('/registeroperator', methods=['GET', 'POST'])
def registerOperator():
    return OwnerRequestHandler().registerOperator()


@requestRoutes.route('/viewoperator', methods=['GET'])
def viewOperator():
    return OwnerRequestHandler().viewOperator()


# Update Owners profile
@requestRoutes.route('/updateownerprofile', methods=['GET', 'POST'])
def updateOwnerProfile():
    return OwnerRequestHandler().updateOwnerProfile()


# View all registered Cities
@requestRoutes.route('/viewcity', methods=['GET', 'POST'])
def viewCity():
    return OwnerRequestHandler().viewCity()
        

# Register a City
@requestRoutes.route('/addcity', methods=['GET', 'POST'])
def addCity():
    return OwnerRequestHandler().addCity()


# View all regisited Stop
@requestRoutes.route('/viewstop', methods=['GET', 'POST'])
def viewStop():
    return OwnerRequestHandler().viewStop()
        

# Register a Stop
@requestRoutes.route('/addstop', methods=['GET', 'POST'])
def addStop():
    return OwnerRequestHandler().addStop()
    

# Add A new schedule
@requestRoutes.route('/addschedule', methods=['GET', 'POST'])
def addSchedule():
    return OwnerRequestHandler().addSchedule()


# View a Schedule in detail
@requestRoutes.route('/viewscheduledetails', methods=['GET', 'POST'])
def viewScheduleDetails():
    return OwnerRequestHandler().viewScheduleDetails()


# Update a Schedules Stops
@requestRoutes.route('/updatestops', methods=['POST'])
def updateStops():
    return OwnerRequestHandler().updateStops()


@requestRoutes.route('/updatetripstatus', methods=['POST'])
def updateTripStatus():
    return OwnerRequestHandler().updateTripStatus()



# OWNER END


# OPERATOR BEGIN

# Landing Page for Operator
@requestRoutes.route('/landingoperator')
def landingOperator():
    return OperatorRequestHandler().landingOperator()


# Update Operators profile
@requestRoutes.route('/updateoperatorprofile', methods=['GET', 'POST'])
def updateOperatorProfile():
    return OperatorRequestHandler().updateOperatorProfile()


# View all Operator's Assigned Schedules
@requestRoutes.route('/viewoperatorschedules', methods=['GET'])
def viewOperatorSchedules():
    return OperatorRequestHandler().viewOperatorSchedules()


@requestRoutes.route('/viewoperatorscheduledetails', methods=['POST'])
def viewOperatorScheduleDetails():
    return OperatorRequestHandler().viewOperatorScheduleDetails()



# OPERATOR END


# CUSTOMER BEGIN

# Landing Page for Customer
@requestRoutes.route('/landingcustomer')
def landingCustomer():
    return CustomerRequestHandler().landingCustomer()


# Update Customer profile
@requestRoutes.route('/updatecustomerprofile', methods=['GET', 'POST'])
def updateCustomerProfile():
    return CustomerRequestHandler().updateCustomerProfile()


@requestRoutes.route('/registerpassenger', methods=['GET', 'POST'])
def registerPassenger():
    return CustomerRequestHandler().registerPassenger()


@requestRoutes.route('/viewpassengers', methods=['GET'])
def viewPassengers():
    return CustomerRequestHandler().viewPassengers()


@requestRoutes.route('/bookschedule', methods=['POST'])
def bookSchedule():
    return CustomerRequestHandler().bookSchedule()


@requestRoutes.route('/confirmbookschedule', methods=['POST'])
def confirmBookSchedule():
    return CustomerRequestHandler().confirmBookSchedule()


@requestRoutes.route('/viewbooking', methods=['GET'])
def viewBookings():
    return CustomerRequestHandler().viewBookings()



# CUSTOMER END


# API BEGIN

# API For getting all stops in cities
@requestRoutes.route('/getstopsbycity')
def getStopsByCity():
    return APIRequstHandler().getStopsByCity()


# View Specific Bus Details API
@requestRoutes.route('/getbusdetails', methods=['POST'])
def getBusDetails():
    return APIRequstHandler().getBusDetails()    


# API END