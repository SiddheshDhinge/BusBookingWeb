from .model_owner import Owner
from .model_customer import Customer
from .model_operator import Operator
from .model_bus import Bus
from .model_passenger import Passenger
from .model_schedule import Schedule
from .model_landmark import Landmark
from .model_stop import Stop
from .model_booking import Booking
from .model_at import At
from .database import DB_session
from .session_manager import getSessionStatus

class ComplexOperation:
    def __init__(self):
        pass

    def getAllLandmarks(self, search):
        response_data = {}
        if(search):
            search = f'%{search}%'
            queryResult = DB_session.query(Landmark).filter(Landmark.name.ilike(search)).all()
        else:
            queryResult = DB_session.query(Landmark).all()
        response_data['data'] = [landmarkObj.serialize() for landmarkObj in queryResult]
        print(response_data)
        return response_data

    def getAllStops(self):
        queryResult = DB_session.query(Stop).all()
        return queryResult

    def getOwnerSchedules(self, ownerUsername):
        queryResult = DB_session.query(Schedule, Bus, Owner).select_from(Schedule).join(Bus, Owner).filter(
            Owner.username == ownerUsername
        ).all()
        return queryResult

    def getOwnerBuses(self, ownerUsername):
        queryResult = DB_session.query(Bus).filter(Bus.username == ownerUsername).all()
        return queryResult

    def getOperatorSchedules(self, operatorUsername):
        queryResult = DB_session.query(Schedule, Bus, Owner, Stop, Landmark).select_from(Schedule).join(Bus, Owner, At, Stop, Landmark).filter(
            Schedule.username == operatorUsername
        ).all()
        return queryResult

    def getAllOperators(self):
        queryResult = DB_session.query(Operator).all()
        return queryResult

    def getCustomerPassengers(self, customerUsername):
        queryResult = DB_session.query(Passenger).filter(Passenger.username == customerUsername).all()
        return queryResult

    def getAllSchedules(self):
        queryResult = DB_session.query(Schedule, Bus, Owner, Stop, Landmark).select_from(Schedule).join(Bus, Owner, At, Stop, Landmark).all()
        return queryResult

    def getCustomerBooking(self, customerUsername):
        queryResult = DB_session.query(Booking, Passenger, Customer).join(Booking, Passenger, Customer).filter(Customer.username == customerUsername).all()
        return queryResult