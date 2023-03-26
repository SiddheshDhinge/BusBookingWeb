from .model_owner import Owner
from .model_customer import Customer
from .model_operator import Operator
from .model_bus import Bus
from .model_seat import Seat
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
        self.response_data[label.data][City.objListName] = [
            cityObj.serialize() for cityObj in queryResult
        ]
        return self.response_data


    def getAllOwner(self, search):
        if(search):
            search = f'%{search}%'
            queryResult = DB_session.query(Owner).filter(Owner.username.ilike(search)).all()
        else:
            queryResult = DB_session.query(Owner).all()
        self.response_data[label.data][Owner.objListName] = [
            ownerObj.serialize() for ownerObj in queryResult
        ]
        return self.response_data


    def getAllStop(self, search):
        if(search):
            search = f'%{search}%'
            queryResult = DB_session.query(Stop, City).join(City).filter(Stop.name.ilike(search)).all()
        else:
            queryResult = DB_session.query(Stop, City).join(City).all()
        
        self.response_data[label.data][Stop.objListName] = [
            {
                Stop.objName : stopObj.serialize(),
                City.objName : cityObj.serialize(),
            } for stopObj, cityObj in queryResult
        ]
        
        return self.response_data


    def getSchedule(self, scheduleId: int, ownerUsername: str, useOwnerUsername= True):
        City1 = aliased(City)
        City2 = aliased(City)
        queryResult = DB_session.query(Schedule, Bus, Owner, City1, City2)\
            .select_from(Schedule)\
            .join(City1, City1.cityId == Schedule.fromCity)\
            .join(City2, City2.cityId == Schedule.toCity)\
            .join(Bus, Owner)\
            .filter(Schedule.scheduleId == scheduleId)
        
        if(useOwnerUsername == True):
            queryResult = queryResult.filter(Owner.username == ownerUsername)
        queryResult = queryResult.first()
        
        if queryResult:
            (scheduleObj, busObj, ownerObj, cityObj1, cityObj2) = queryResult
            self.response_data[label.data][Schedule.objName] = {
                    Schedule.objName : scheduleObj.serialize(),
                    Bus.objName : busObj.serialize(),
                    Owner.objName : ownerObj.serialize(),
                    f'from_{City.objName}' : cityObj1.serialize(),
                    f'to_{City.objName}' : cityObj2.serialize(),
                    Stop.objListName : self.getSchedulesStop(scheduleObj.scheduleId)
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
            filters[tripStatus] = complete / incomplete
        '''

        #Join required tables
        City1 = aliased(City)
        City2 = aliased(City)
        queryResult = DB_session.query(Schedule, Bus, Owner, City1, City2)\
            .select_from(Schedule)\
            .join(City1, City1.cityId == Schedule.fromCity)\
            .join(City2, City2.cityId == Schedule.toCity)\
            .join(Bus, Owner)\
        
        #date based filtering
        if(filters[label.filterDate]):
            queryResult = queryResult.filter(Schedule.fromDate == filters[label.filterDate])
        
        # Trip Status based filtering
        queryResult = queryResult.filter(Schedule.isComplete == filters[label.filterTripStatus])

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
        if(filters[label.owner_agencyName]):
            if(filters[label.owner_agencyName] != 'all'):
                agencyName = f'%{filters[label.owner_agencyName]}%'
                queryResult = queryResult.filter(Owner.agencyName.ilike(agencyName))
        
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
                Stop.objListName : self.getSchedulesStop(scheduleObj.scheduleId)
            } for scheduleObj, busObj, ownerObj, cityObj1, cityObj2 in queryResult
        ]
        return self.response_data


    def getOwnerBuses(self, ownerUsername):
        queryResult = DB_session.query(Bus).filter(Bus.username == ownerUsername).all()
        self.response_data[label.data][Bus.objListName] = [
            busObj.serialize() for busObj in queryResult
        ] 
        return self.response_data


    def getOwnerOperators(self, ownerUsername):
        queryResult = DB_session.query(Operator)\
            .filter(Operator.ownerUsername == ownerUsername).all()
        
        self.response_data[label.data][Operator.objListName] = [
            operatorObj.serialize() for operatorObj in queryResult
        ]
        return self.response_data
    

    # rework needed
    def getOperatorSchedules(self, operatorUsername):
        City1 = aliased(City)
        City2 = aliased(City)
        queryResult = DB_session.query(Schedule, Bus, Owner, City1, City2)\
            .select_from(Schedule)\
            .join(City1, City1.cityId == Schedule.fromCity)\
            .join(City2, City2.cityId == Schedule.toCity)\
            .join(Bus, Owner)\
            .filter(Schedule.username == operatorUsername)\
            .filter(Schedule.isComplete == False)\
            .all()
        
        self.response_data[label.data] = [
            {
                Schedule.objName : scheduleObj.serialize(),
                Bus.objName : busObj.serialize(),
                Owner.objName : ownerObj.serialize(),
                Stop.objListName : self.getSchedulesStop(scheduleObj.scheduleId),
                f'from_{City.objName}' : cityObj1.serialize(),
                f'to_{City.objName}' : cityObj2.serialize()
            } for (scheduleObj, busObj, ownerObj, cityObj1, cityObj2) in queryResult
        ]
        return self.response_data


    def getSchedulesStop(self, scheduleId):
        queryResult = DB_session.query(Stop, City)\
            .join(At, At.stopId == Stop.stopId)\
            .join(City, City.cityId == Stop.cityId)\
            .filter(At.scheduleId == scheduleId)\
            .order_by(At.sequence)\
            .all()

        stopObjList = [
            {
                Stop.objName : stopObj.serialize(),
                City.objName : cityObj.serialize()
            }
            for stopObj, cityObj in queryResult
        ]
        return stopObjList


    def getCustomerPassengers(self, customerUsername):
        queryResult = DB_session.query(Passenger)\
            .filter(Passenger.username == customerUsername).all()
        
        self.response_data[label.data][Passenger.objListName] = [
            passengerObj.serialize() for passengerObj in queryResult
        ]
        return self.response_data
    

    def getCustomerBookings(self, customerUsername):    
        queryResult = DB_session.query(Schedule, Owner, City, Passenger, Booking)\
            .join(Booking, Booking.scheduleId == Schedule.scheduleId)\
            .join(City, City.cityId == Schedule.toCity)\
            .join(Bus, Bus.numberPlate == Schedule.numberPlate)\
            .join(Owner, Owner.username == Bus.username)\
            .join(Passenger, Passenger.passengerId == Booking.passengerId)\
            .filter(Passenger.username == customerUsername)\
            .order_by(Schedule.isComplete).all()

        self.response_data[label.data] = [
            {
                Schedule.objName : scheduleObj.serialize(),
                Owner.objName : ownerObj.serialize(),
                City.objName : cityObj.serialize(),
                Passenger.objName : passengerObj.serialize(),
                Booking.objName : bookingObj.serialize()
            } for (scheduleObj, ownerObj, cityObj, passengerObj, bookingObj) in queryResult
        ]
        return self.response_data
    
    
    def getAllStopsByCity(self):
        allCityObj = self.getAllCity(search= None)[label.data][City.objListName]
        self.response_data[label.data] = {}
        for cityObj in allCityObj:
            queryResult = DB_session.query(Stop)\
                .filter(Stop.cityId == cityObj[label.city_id]).all()
            
            self.response_data[label.data][cityObj[label.city_name]] = {
                label.city_id : cityObj[label.city_id],
                Stop.objListName : [
                    stopObj.serialize() for stopObj in queryResult
                ]
            }
        return self.response_data
    

    def isScheduleOfOwner(self, scheduleId, ownerUsername):
        result = DB_session.query(
            DB_session.query(Schedule, Bus)\
                .join(Bus, Bus.numberPlate == Schedule.numberPlate)\
                .filter(Bus.username == ownerUsername)\
                .filter(Schedule.scheduleId == scheduleId).exists()
        ).scalar()
        return result
    

    def updateScheduleStop(self, scheduleId, stopSequence):
        DB_session.query(At)\
            .filter(At.scheduleId == scheduleId).delete()

        for sequenceId, stopId in enumerate(stopSequence):
            result = At(scheduleId= scheduleId, stopId= stopId, sequence= sequenceId).createObject()
            if not result:
                return False
            
        DB_session.commit()
        return True
    

    def updateTripStatus(self, scheduleId):
        DB_session.query(Schedule)\
            .filter(Schedule.scheduleId == scheduleId)\
            .update({Schedule.isComplete : True})
        
        DB_session.commit()


    def getBusDetails(self, numberPlate, ownerUsername, useOwnerUsername= True):
        queryResult = DB_session.query(Bus)\
            .filter(Bus.numberPlate == numberPlate)
        
        if(useOwnerUsername == True):
            queryResult = queryResult.filter(Bus.username == ownerUsername)
        busObj = queryResult.first()
        
        if queryResult:
            self.response_data[label.data] = {
                Bus.objName : busObj.serialize(),
                Seat.objListName : self.getBusSeats(numberPlate= numberPlate)
            }
            self.response_data[label.success] = True
        else:
            self.response_data[label.success] = False

        return self.response_data
    

    def getBusSeats(self, numberPlate):
        queryResult = DB_session.query(Seat)\
            .filter(Seat.numberPlate == numberPlate).all()
        
        data = {}
        for seatObj in queryResult:
            seatNo = seatObj.serialize()[label.seat_seatNo]
            data[seatNo] = seatObj.serialize()

        return data
    

    def getBookedPassengers(self, scheduleId: int):
        FromStop = aliased(Stop)
        ToStop = aliased(Stop)

        queryResult = DB_session.query(Booking, Passenger, Customer, FromStop, ToStop)\
            .join(Passenger, Booking.passengerId == Passenger.passengerId)\
            .join(Customer, Customer.username == Passenger.username)\
            .join(FromStop, FromStop.stopId == Booking.fromStopId)\
            .join(ToStop, ToStop.stopId == Booking.toStopId)\
            .filter(Booking.scheduleId == scheduleId).all()
        
        self.response_data[label.data][Booking.objListName] = [
            {
                Booking.objName : bookingObj.serialize(),
                Passenger.objName : passengerObj.serialize(),
                Customer.objName : customerObj.serialize(),
                f'from-{Stop.objName}' : fromStopObj.serialize(),
                f'to-{Stop.objName}' : toStopObj.serialize()
            } for bookingObj, passengerObj, customerObj, fromStopObj, toStopObj in queryResult
        ]
        return self.response_data
    
    
    def getBookedPassengerDetails(self, bookingId):
        queryResult = DB_session.query(Passenger)\
            .join(Booking, Passenger.passengerId == Booking.bookingId)\
            .where(Booking.bookingId == bookingId).first()
        
        passengerObj = queryResult
        self.response_data[label.data] = {
            Passenger.objName : passengerObj.serialize()
        }
        return self.response_data
    

    def getBookingDetails(self, bookingId):
        FromCity = aliased(City)
        ToCity = aliased(City)
        FromStop = aliased(Stop)
        ToStop = aliased(Stop)

        queryResult = DB_session.query(Booking, Schedule, Passenger, Bus, Owner, Operator, FromCity, ToCity, FromStop, ToStop)\
            .join(Schedule, Schedule.scheduleId == Booking.scheduleId)\
            .join(Passenger, Passenger.passengerId == Booking.passengerId)\
            .join(Bus, Bus.numberPlate == Schedule.numberPlate)\
            .join(Owner, Owner.username == Bus.username)\
            .join(Operator, Operator.username == Schedule.username)\
            .join(FromCity, FromCity.cityId == Schedule.fromCity)\
            .join(ToCity, ToCity.cityId == Schedule.toCity)\
            .join(FromStop, FromStop.stopId == Booking.fromStopId)\
            .join(ToStop, ToStop.stopId == Booking.toStopId)\
            .filter(Booking.bookingId == bookingId).first()
        
        (bookingObj, scheduleObj, passengerObj, busObj, ownerObj, operatorObj, fromCityObj, toCityObj, fromStopObj, toStopObj) = queryResult
        self.response_data[label.data] = {
            Booking.objName : bookingObj.serialize(),
            Schedule.objName : scheduleObj.serialize(),
            Passenger.objName : passengerObj.serialize(),
            Bus.objName : busObj.serialize(),
            Owner.objName : ownerObj.serialize(),
            Operator.objName : operatorObj.serialize(),
            f'from-{City.objName}' : fromCityObj.serialize(),
            f'to-{City.objName}' : toCityObj.serialize(),
            f'from-{Stop.objName}' : fromStopObj.serialize(),
            f'to-{Stop.objName}' : toStopObj.serialize()
        }
        return self.response_data