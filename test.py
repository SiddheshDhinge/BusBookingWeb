import colorama
colorama.init()
from termcolor import colored
#Establish database session
from app.model.database import connectDB, createAllTables, dropAllTables
connectDB()
# Import All other Models
from app.model.model_owner import Owner
from app.model.model_customer import Customer
from app.model.model_operator import Operator
from app.model.model_bus import Bus
from app.model.model_passenger import Passenger
from app.model.model_schedule import Schedule
from app.model.model_city import City
from app.model.model_stop import Stop
from app.model.model_booking import Booking
from app.model.model_at import At
from app.model.session_manager import getSessionStatus, addActiveSession

import sys
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        print(colored("\n\n\nSTARTED TESTS: \n\n\n", "green"))
        dropAllTables()
        createAllTables()

    def test_insertData(self):
        assert Owner('Chintan', 'abc1', 'CJ', '9874563210').createOwner() == True
        assert Owner('Siddhesh', 'abc2', 'SD', '0123456789').createOwner() == True
        assert Owner('Manas', 'abc3', 'MS', '7140258963').createOwner() == True
        assert Owner('Sahil', 'abc4', 'SB', '1112223330').createOwner() == True
        assert Owner('Shubham', 'abc5', 'SS', '4411336655').createOwner()== True

        assert Customer('Tanmay', 'abc1', 'TB', '7744112255').createCustomer() == True
        assert Customer('Harshvardhan', 'abc2', 'HP', '4152630014').createCustomer() == True
        assert Customer('Jayesh', 'abc3', 'JK', '4411557788').createCustomer() == True
        assert Customer('Sumit', 'abc4', 'SK', '9856221434').createCustomer() == True
        assert Customer('Omkar', 'abc5', 'OS', '4455667711').createCustomer() == True
        
        assert Operator('Manish', 'abc1', 'MB', 'L1', '4411225549').createOperator() == True
        assert Operator('Guarav', 'abc2', 'GS', 'L2', '7475869421').createOperator() == True
        assert Operator('Ketan', 'abc3', 'KM', 'L3', '1122337495').createOperator() == True
        assert Operator('Akshay', 'abc4', 'AJ', 'L4', '5566442576').createOperator() == True
        assert Operator('Lokesh', 'abc5', 'LD', 'L5', '9988743615').createOperator() == True
        
        assert Passenger('P1', 'M', 23, '7414714714', 'Tanmay').createObject() == True
        assert Passenger('P5', 'M', 26, '8811667725', 'Tanmay').createObject() == True
        assert Passenger('P2', 'F', 22, '4411997733', 'Harshvardhan').createObject() == True
        assert Passenger('P4', 'F', 24, '7766443399', 'Harshvardhan').createObject() == True
        assert Passenger('P3', 'M', 28, '9944331166', 'Jayesh').createObject() == True
        assert Passenger('P3', 'M', 28, '9944331166', 'Jayesh').createObject() == True
        assert Passenger('P4', 'F', 24, '7766443399', 'Sumit').createObject() == True
        assert Passenger('P2', 'F', 22, '4411997733', 'Sumit').createObject() == True
        assert Passenger('P5', 'M', 26, '8811667725', 'Omkar').createObject() == True
        assert Passenger('P1', 'M', 23, '7414714714', 'Omkar').createObject() == True

        assert City('Mumbai').createObject() == True
        assert City('Pune').createObject() == True
        assert City('Nagpur').createObject() == True
        assert City('Nashik').createObject() == True
        assert City('Aurangabad').createObject() == True
        assert City('Amravati').createObject() == True
        assert City('Kolhapur').createObject() == True
        assert City('Thane').createObject() == True
        assert City('Ahmednagar').createObject() == True
        assert City('Jalgaon').createObject() == True

        assert Stop('Stop #1', 'P.O. Box 142, 4327 Tincidunt Ave', 1).createObject() == True
        assert Stop('Stop #2', 'Ap #185-7832 Quisque St.', 2).createObject() == True
        assert Stop('Stop #3', '7627 Bibendum Street', 3).createObject() == True
        assert Stop('Stop #4', 'P.O. Box 535, 8661 Mollis. Road', 4).createObject() == True
        assert Stop('Stop #5', 'Ap #594-2420 Lorem Av.', 5).createObject() == True
        assert Stop('Stop #6', '589-5059 Ornare Avenue', 6).createObject() == True
        assert Stop('Stop #7', '110-2129 Leo, Street', 7).createObject() == True
        assert Stop('Stop #8', '9595 Purus. Rd.', 8).createObject() == True
        assert Stop('Stop #9', 'P.O. Box 235, 2609 Nunc Ave', 9).createObject() == True
        assert Stop('Stop #10', 'Ap #593-244 At St.', 5).createObject() == True
        assert Stop('Stop #11', 'P.O. Box 535, 8661 Mollis. Road', 6).createObject() == True
        assert Stop('Stop #12', '110-2129 Leo, Street', 7).createObject() == True
        assert Stop('Stop #13', 'Ap #185-7832 Quisque St.', 8).createObject() == True
        assert Stop('Stop #14', 'P.O. Box 142, 4327 Tincidunt Ave', 9).createObject() == True
        assert Stop('Stop #15', 'Ap #593-244 At St.', 1).createObject() == True

        assert Bus('MH 12 AB 1234', 40, 'SEAT', 'Chintan').createObject() == True
        assert Bus('MH 12 AB 1235', 40, 'SLEEP', 'Chintan').createObject() == True
        assert Bus('MH 12 AB 1236', 40, 'SEAT', 'Chintan').createObject() == True
        assert Bus('MH 12 AB 1237', 40, 'SLEEP', 'Siddhesh').createObject() == True
        assert Bus('MH 12 AB 1238', 40, 'SEAT', 'Siddhesh').createObject() == True
        assert Bus('MH 12 AB 1239', 40, 'SLEEP', 'Siddhesh').createObject() == True
        assert Bus('MH 12 AB 1240', 40, 'SEAT', 'Manas').createObject() == True
        assert Bus('MH 12 AB 1241', 40, 'SLEEP', 'Manas').createObject() == True
        assert Bus('MH 12 AB 1242', 40, 'SEAT', 'Sahil').createObject() == True
        assert Bus('MH 12 AB 1243', 40, 'SLEEP', 'Shubham').createObject() == True
        
        assert Schedule('2019-12-01', '2019-12-31', '10:00:00', '11:00:00', 10000, 1, 6, 'MH 12 AB 1234', 'Manish').createObject() == True
        assert Schedule('2019-12-01', '2019-12-31', '11:00:00', '12:00:00', 5000, 2, 7, 'MH 12 AB 1235', 'Ketan').createObject() == True
        assert Schedule('2019-12-01', '2019-12-31', '12:00:00', '13:00:00', 9000, 3, 8, 'MH 12 AB 1236', 'Lokesh').createObject() == True
        assert Schedule('2019-12-01', '2019-12-31', '13:00:00', '14:00:00', 7000, 4, 9, 'MH 12 AB 1237', 'Akshay').createObject() == True
        assert Schedule('2019-12-01', '2019-12-31', '14:00:00', '15:00:00', 8000, 5, 10, 'MH 12 AB 1238', 'Guarav').createObject() == True

        assert At(1, 1).createObject() == True
        assert At(2, 3).createObject() == True
        assert At(3, 5).createObject() == True
        assert At(4, 7).createObject() == True
        assert At(5, 8).createObject() == True

        assert Booking(2, 1, 1).createObject() == True
        assert Booking(3, 1, 2).createObject() == True
        assert Booking(4, 2, 3).createObject() == True
        assert Booking(5, 2, 4).createObject() == True
        assert Booking(6, 3, 5).createObject() == True
        assert Booking(7, 3, 6).createObject() == True
        assert Booking(8, 4, 7).createObject() == True
        assert Booking(9, 4, 8).createObject() == True
        assert Booking(10, 5, 9).createObject() == True
        assert Booking(11, 5, 10).createObject() == True
        
def main():
    unittest.main(verbosity=2)

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        print(colored('Script needs Args :-', 'red'))
        print(colored('runtest', 'yellow'))
        print(colored('dropall', 'yellow'))
        exit()
    if(sys.argv[1] == 'runtest'):
        sys.argv.pop()
        main()
    elif(sys.argv[1] == 'createall'):
        createAllTables()
        print(colored('CREATED ALL SCHEMA', 'green'))
    elif(sys.argv[1] == 'dropall'):
        dropAllTables()
        print(colored('DROPPED DB SCHEMA', 'green'))
    else:
        print(colored('INVALID ARGS', 'red'))
        print(colored('Script needs Args :-', 'red'))
        print(colored('runtest', 'yellow'))
        print(colored('dropall', 'yellow'))
        exit()