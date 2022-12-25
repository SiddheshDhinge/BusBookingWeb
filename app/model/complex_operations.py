from .model_owner import Owner
from .model_customer import Customer
from .model_operator import Operator
from .model_bus import Bus
from .model_passenger import Passenger
from .model_schedule import Schedule
from .model_city import City
from .model_stop import Stop
from .model_booking import Booking
from .model_at import At
from .database import DB_session
from .session_manager import getSessionStatus

from .. import label

class ComplexOperation:
    def __init__(self):
        self.response_data = {'data' : {}}


    def getAllCity(self, search):
        if(search):
            search = f'%{search}%'
            queryResult = DB_session.query(City).filter(City.name.ilike(search)).all()
        else:
            queryResult = DB_session.query(City).all()
        self.response_data['data']['city'] = [cityObj.serialize() for cityObj in queryResult]
        return self.response_data


    def getAllStop(self, search):
        if(search):
            search = f'%{search}%'
            queryResult = DB_session.query(Stop, City).join(City).filter(Stop.name.ilike(search)).all()
        else:
            queryResult = DB_session.query(Stop, City).join(City).all()
        
        self.response_data.clear()
        self.response_data['data'] = [
        {
            'stop' : stopObj.serialize(),
            'city' : cityObj.serialize(),
        } for stopObj, cityObj in queryResult]
        
        return self.response_data


    def getAllSchedules(self, filters):
        '''
            filters[fromCity] = cityName
            filters[toCity] = cityName
            filters[timeblock] = morning / afternoon / evening / night / all
            filters[busType] = sleep / seat / all
            filters[owner] = ownerUsername / all
            filters[sortPrice] = asc / desc / none
        '''

        #city based filtering
        # queryResult = DB_session.query(Schedule, Bus, Owner, Stop, City).select_from(Schedule).join(Bus, Owner, At, Stop, City).filter(
            
        queryResult = DB_session.query(Schedule).filter(
            Schedule.fromCity == filters[label.filterFromCity],
            Schedule.toCity == filters[label.filterToCity]
        )
        
        #time based filtering
        if(filters[label.filterTimeBlock] == label.timeBlockMorning):
            queryResult = queryResult.filter(Schedule.departureTime >= '03:00:00', Schedule.departureTime < '09:00:00')
        elif(filters[label.filterTimeBlock] == label.timeBlockNoon):
            queryResult = queryResult.filter(Schedule.departureTime >= '09:00:00', Schedule.departureTime < '15:00:00')
        elif(filters[label.filterTimeBlock] == label.timeBlockEvening):
            queryResult = queryResult.filter(Schedule.departureTime >= '15:00:00', Schedule.departureTime < '21:00:00')
        elif(filters[label.filterTimeBlock] == label.timeBlockNight):
            queryResult = queryResult.filter(Schedule.departureTime >= '15:00:00', Schedule.departureTime < '21:00:00')

        #bus type based filtering 
        # if(filters[label.filterBusType] in (label.bus_typeSleep, label.bus_typeSeat)):
        #     queryResult.filter(Bus.busType == filters[label.filterBusType])

        #travel agency based filtering
        # if(filters[label.owner_username] != 'all'):
        #     username = f'%{[label.owner_username]}%'
        #     queryResult.filter(Owner.username.ilike(username))
        
        #sort according prices
        if(filters[label.filterSortPrice] == 'asc'):
            queryResult = queryResult.order_by(Schedule.fairFees)
        elif(filters[label.filterSortPrice] == 'desc'):
            queryResult = queryResult.order_by(Schedule.fairFees.desc())

        queryResult = queryResult.all()

        self.response_data.clear()
        self.response_data['data'] = [
            {
                Schedule.__tablename__ : scheduleObj.serialize(),
            } for scheduleObj in queryResult
            #     Bus.__tablename__ : busObj.serialize(),
            #     Owner.__tablename__ : ownerObj.serialize(),
            #     Stop.__tablename__ : stopObj.serialize(), 
            #     City.__tablename__ : cityObj.serialize()
            # } for (scheduleObj, busObj, ownerObj, stopObj, cityObj) in queryResult
        ]
        print(self.response_data)
        return self.response_data


    def getOwnerSchedules(self, ownerUsername):
        queryResult = DB_session.query(Schedule, Bus, Owner).select_from(Schedule).join(Bus, Owner).filter(
            Owner.username == ownerUsername
        ).all()
        return queryResult

    def getOwnerBuses(self, ownerUsername):
        queryResult = DB_session.query(Bus).filter(Bus.username == ownerUsername).all()
        return queryResult

    def getOperatorSchedules(self, operatorUsername):
        queryResult = DB_session.query(Schedule, Bus, Owner, Stop, City).select_from(Schedule).join(Bus, Owner, At, Stop, City).all()
        return queryResult

    def getAllOperators(self):
        queryResult = DB_session.query(Operator).all()
        return queryResult

    def getCustomerPassengers(self, customerUsername):
        queryResult = DB_session.query(Passenger).filter(Passenger.username == customerUsername).all()
        return queryResult

    def getCustomerBooking(self, customerUsername):
        queryResult = DB_session.query(Booking, Passenger, Customer).join(Booking, Passenger, Customer).filter(Customer.username == customerUsername).all()
        return queryResult