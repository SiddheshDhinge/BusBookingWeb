print("\n\n\nSTARTED: \n\n\n")
#Establish database session
from database import connectDB, createAllTables, dropAllTables
connectDB()
# Import All other Models
from model_owner import Owner
from model_customer import Customer
from model_operator import Operator
from model_bus import Bus
from model_passenger import Passenger
from model_schedule import Schedule
from model_landmark import Landmark
from model_stop import Stop
from model_booking import Booking
from model_at import At

from session_manager import getSessionStatus, addActiveSession

from termcolor import colored
import colorama
colorama.init()
import unittest
#create Database schema if not exists
createAllTables()

class Tests(unittest.TestCase):
    def setUp(self):
        dropAllTables()
        createAllTables()

    def test_insertData(self):
        try:
            assert Owner('Chintan', 'abc1', 'CJ', '9874563210').createOwner() == True
            assert Owner('Siddhesh', 'abc2', 'SD', '0123456789').createOwner() == True
            assert Owner('Manas', 'abc3', 'MS', '7140258963').createOwner() == True
            assert Owner('Sahil', 'abc4', 'SB', '1112223330').createOwner() == True
            assert Owner('Shubham', 'abc5', 'SS', '4411336655').createOwner()== True
        except(AssertionError):
            print(colored("Insertion Owner Failed"))
            raise AssertionError
        else:
            print(colored(""))

        assert Customer('Tanmay', 'abc1', 'TB', '7744112255').createCustomer() == True
        assert Customer('Harshvardhan', 'abc2', 'HP', '4152630014').createCustomer() == True
        assert Customer('Jayesh', 'abc3', 'JK', '4411557788').createCustomer() == True
        assert Customer('Sumit', 'abc4', 'SK', '9856221434').createCustomer() == True
        assert Customer('Omkar', 'abc5', 'OS', '4455667711').createCustomer() == True
        
        assert Operator('Manish', 'abc1', 'MB', 'L1', '4411225549').createOperator() == True
        assert Operator('Garuav', 'abc2', 'GS', 'L2', '7475869421').createOperator() == True
        assert Operator('Ketan', 'abc3', 'KM', 'L3', '1122337495').createOperator() == True
        assert Operator('Akshay', 'abc4', 'AJ', 'L4', '5566442576').createOperator() == True
        assert Operator('Lokesh', 'abc5', 'LD', 'L5', '9988743615').createOperator() == True
        
        assert Passenger('P1', 'M', 23, '7414714714', 'Tanmay').createPassenger() == True
        assert Passenger('P5', 'M', 26, '8811667725', 'Tanmay').createPassenger() == True
        assert Passenger('P2', 'F', 22, '4411997733', 'Harshvardhan').createPassenger() == True
        assert Passenger('P4', 'F', 24, '7766443399', 'Harshvardhan').createPassenger() == True
        assert Passenger('P3', 'M', 28, '9944331166', 'Jayesh').createPassenger() == True
        assert Passenger('P3', 'M', 28, '9944331166', 'Jayesh').createPassenger() == True
        assert Passenger('P4', 'F', 24, '7766443399', 'Sumit').createPassenger() == True
        assert Passenger('P2', 'F', 22, '4411997733', 'Sumit').createPassenger() == True
        assert Passenger('P5', 'M', 26, '8811667725', 'Omkar').createPassenger() == True
        assert Passenger('P1', 'M', 23, '7414714714', 'Omkar').createPassenger() == True

        print(colored("ALL TESTS PASSED", "green"))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
    # dropAllTables()