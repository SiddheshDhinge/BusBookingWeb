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
from sqlalchemy.orm import aliased
from .. import label

class ComplexOperation:
    def __init__(self):
        self.response_data = {label.data : {}}


    def getAllCity(self, search):
        if(search):
            search = f'%{search}%'
            queryResult = DB_session.query(City).filter(City.name.ilike(search)).all()
        else:
            queryResult = DB_session.query(City).all()
        self.response_data[label.data][City.objName] = [cityObj.serialize() for cityObj in queryResult]
        return self.response_data


    def getAllOwner(self, search):
        if(search):
            search = f'%{search}%'
            queryResult = DB_session.query(Owner).filter(Owner.username.ilike(search)).all()
        else:
            queryResult = DB_session.query(Owner).all()
        self.response_data[label.data][Owner.objName] = [ownerObj.serialize() for ownerObj in queryResult]
        return self.response_data


    def getAllStop(self, search):
        if(search):
            search = f'%{search}%'
            queryResult = DB_session.query(Stop, City).join(City).filter(Stop.name.ilike(search)).all()
        else:
            queryResult = DB_session.query(Stop, City).join(City).all()
        
        self.response_data.clear()
        self.response_data[label.data] = [
        {
            Stop.objName : stopObj.serialize(),
            City.objName : cityObj.serialize(),
        } for stopObj, cityObj in queryResult]
        
        return self.response_data


    def getSchedule(self, scheduleId: int, owner_username: str):
        City1 = aliased(City)
        City2 = aliased(City)
        queryResult = DB_session.query(Schedule, Bus, Owner, City1, City2).select_from(Schedule)\
            .join(City1, City1.cityId == Schedule.fromCity)\
            .join(City2, City2.cityId == Schedule.toCity)\
            .join(Bus, Owner)\
            .filter(Schedule.scheduleId == scheduleId)\
            .filter(Owner.username == owner_username).first()
        
        if queryResult:
            (scheduleObj, busObj, ownerObj, cityObj1, cityObj2) = queryResult
            self.response_data[label.data][Schedule.objName] = {
                    Schedule.objName : scheduleObj.serialize(),
                    Bus.objName : busObj.serialize(),
                    Owner.objName : ownerObj.serialize(),
                    f'from_{City.objName}' : cityObj1.serialize(),
                    f'to_{City.objName}' : cityObj2.serialize(),
                    Stop.objName : self.getSchedulesStop(scheduleObj.scheduleId)
                }
            self.response_data[label.success] = True
        else:
            self.response_data[label.success] = False
            
        return self.response_data

    def getAllSchedules(self, filters, useDate=True, useCity=True):
        '''
            filters[fromCity] = cityName    (req)
            filters[toCity] = cityName      (req)
            filters[fromDate] = date        (req)
            filters[timeblock] = morning / afternoon / evening / night / all
            filters[busType] = sleep / seat / all
            filters[owner] = ownerUsername / all
            filters[sortPrice] = asc / desc / none
        '''

        #Join required tables
        City1 = aliased(City)
        City2 = aliased(City)
        queryResult = DB_session.query(Schedule, Bus, Owner, City1, City2).select_from(Schedule)\
            .join(City1, City1.cityId == Schedule.fromCity)\
            .join(City2, City2.cityId == Schedule.toCity)\
            .join(Bus, Owner)\
        
        #date based filtering
        if(filters[label.filterDate]):
            queryResult = queryResult.filter(Schedule.fromDate == filters[label.filterDate])
        
        #city based filtering
        if(filters[label.filterFromCity] != 'all'):
            queryResult = queryResult.filter(Schedule.fromCity == filters[label.filterFromCity], Schedule.toCity == filters[label.filterToCity])

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
        if(filters[label.filterBusType] in (label.bus_typeSleep, label.bus_typeSeat)):
            queryResult = queryResult.filter(Bus.busType == filters[label.filterBusType])

        #travel agency based filtering
        if(filters[label.owner_username]):
            if(filters[label.owner_username] != 'all'):
                username = f'%{filters[label.owner_username]}%'
                queryResult = queryResult.filter(Owner.username.ilike(username))
        
        #sort according prices
        if(filters[label.filterSortPrice] == 'asc'):
            queryResult = queryResult.order_by(Schedule.fairFees)
        elif(filters[label.filterSortPrice] == 'desc'):
            queryResult = queryResult.order_by(Schedule.fairFees.desc())

        queryResult = queryResult.all()

        # self.response_data.clear()
        self.response_data[label.data][Schedule.objName] = [
            {
                Schedule.objName : scheduleObj.serialize(),
                Bus.objName : busObj.serialize(),
                Owner.objName : ownerObj.serialize(),
                f'from_{City.objName}' : cityObj1.serialize(),
                f'to_{City.objName}' : cityObj2.serialize(),
                Stop.objName : self.getSchedulesStop(scheduleObj.scheduleId)
            } for scheduleObj, busObj, ownerObj, cityObj1, cityObj2 in queryResult
        ]
        
        return self.response_data


    def getOwnerBuses(self, ownerUsername):
        queryResult = DB_session.query(Bus).filter(Bus.username == ownerUsername).all()
        self.response_data[label.data][Bus.objName] = [busObj.serialize() for busObj in queryResult] 
        return self.response_data


    def getOperatorSchedules(self, operatorUsername):
        City1 = aliased(City)
        City2 = aliased(City)
        queryResult = DB_session.query(Schedule, Bus, Owner, City1, City2).select_from(Schedule)\
            .join(City1, City1.cityId == Schedule.fromCity)\
            .join(City2, City2.cityId == Schedule.toCity)\
            .join(Bus, Owner)\
            .filter(Schedule.username == operatorUsername)\
            .all()
        
        self.response_data[label.data] = [
            {
                Schedule.objName : scheduleObj.serialize(),
                Bus.objName : busObj.serialize(),
                Owner.objName : ownerObj.serialize(),
                Stop.objName : self.getSchedulesStop(scheduleObj.scheduleId),
                f'from_{City.objName}' : cityObj1.serialize(),
                f'to_{City.objName}' : cityObj2.serialize()
            } for (scheduleObj, busObj, ownerObj, cityObj1, cityObj2) in queryResult
        ]
        return self.response_data


    def getSchedulesStop(self, search_scheduleId):
        queryResult = DB_session.query(Stop)\
            .join(At, At.stopId == Stop.stopId)\
            .filter(At.scheduleId == search_scheduleId)\
            .order_by(At.sequence)\
            .all()

        stopObjList = [stopObj.serialize() for stopObj in queryResult]
        return stopObjList

    def getAllOperators(self):
        queryResult = DB_session.query(Operator).all()
        return queryResult

    def getCustomerPassengers(self, customerUsername):
        queryResult = DB_session.query(Passenger).filter(Passenger.username == customerUsername).all()
        return queryResult

    def getCustomerBooking(self, customerUsername):
        queryResult = DB_session.query(Booking, Passenger, Customer).join(Booking, Passenger, Customer).filter(Customer.username == customerUsername).all()
        return queryResult
    
    def getAllStopsByCity(self):
        allCityObj = self.getAllCity(None)[label.data][City.objName]
        self.response_data[label.data] = {}
        for cityObj in allCityObj:
            queryResult = DB_session.query(Stop).filter(Stop.cityId == cityObj[label.city_id]).all()
            self.response_data[label.data][cityObj[label.city_name]] = {
                label.city_id : cityObj[label.city_id],
                Stop.objName : [stopObj.serialize() for stopObj in queryResult]
            }
            
        return self.response_data