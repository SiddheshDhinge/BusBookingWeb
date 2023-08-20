import colorama
colorama.init()
from termcolor import colored

from dotenv import load_dotenv
import os
# Load Environments
load_dotenv() # Load .env file
# Load environment specific file
if os.getenv("DEBUG") == "True":
    load_dotenv(".dev.env")
else:
    load_dotenv(".prod.env")
    
from app.model.database import connectDB, createAllTables, dropAllTables
#Establish database session
connectDB()
# Import All other Models
from app.model.model_owner import Owner
from app.model.model_customer import Customer
from app.model.model_operator import Operator
from app.model.model_bus import Bus
from app.model.model_seat import Seat
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
        assert Owner('Chintan', 'abc1', 'CJ Tours and Travels', '9874563210').createOwner() == True
        assert Owner('Siddhesh', 'abc2', 'SD Tours and Travels', '0123456789').createOwner() == True
        assert Owner('Manas', 'abc3', 'MS Tours and Travels', '7140258963').createOwner() == True
        assert Owner('Sahil', 'abc4', 'SB Tours and Travels', '1112223330').createOwner() == True
        assert Owner('Shubham', 'abc5', 'SS Tours and Travels', '4411336655').createOwner() == True
        assert Owner('jack123', 'J@ckp@ss', 'Jack Smith Tours and Travels', '5555551212').createOwner() == True
        assert Owner('emmam', 'emm@p@ss', 'Emma Morris Tours and Travels', '5555551213').createOwner() == True
        assert Owner('brianb', 'br1@np@ss', 'Brian Baker Tours and Travels', '5555551214').createOwner() == True
        assert Owner('katherineg', 'k@thp@ss', 'Katherine Graham Tours and Travels', '5555551215').createOwner() == True
        assert Owner('chrisd', 'chr1sp@ss', 'Chris Davis Tours and Travels', '5555551216').createOwner() == True
        assert Owner('samuelm', 's@mp@ss', 'Samuel Mitchell Tours and Travels', '5555551217').createOwner() == True
        assert Owner('laurar', 'l@urp@ss', 'Laura Roberts Tours and Travels', '5555551218').createOwner() == True
        assert Owner('davids', 'd@v1dp@ss', 'David Scott Tours and Travels', '5555551219').createOwner() == True
        assert Owner('jennifert', 'j@nnyp@ss', 'Jennifer Taylor Tours and Travels', '5555551220').createOwner() == True
        assert Owner('michaelw', 'm1k3wp@ss', 'Michael Williams Tours and Travels', '5555551221').createOwner() == True
        assert Owner('susanb', 'sus@np@ss', 'Susan Brown Tours and Travels', '5555551222').createOwner() == True
        assert Owner('jamesm', 'j@m3sp@ss', 'James Miller Tours and Travels', '5555551223').createOwner() == True
        assert Owner('lisaq', 'l1s@qp@ss', 'Lisa Quinn Tours and Travels', '5555551224').createOwner() == True
        assert Owner('matthewr', 'm@ttp@ss', 'Matthew Reed Tours and Travels', '5555551225').createOwner() == True
        assert Owner('nicolej', 'n1c@lp@ss', 'Nicole Jackson Tours and Travels', '5555551226').createOwner() == True


        assert Customer('Tanmay', 'abc1', 'TB', '7744112255').createCustomer() == True
        assert Customer('Harshvardhan', 'abc2', 'HP', '4152630014').createCustomer() == True
        assert Customer('Jayesh', 'abc3', 'JK', '4411557788').createCustomer() == True
        assert Customer('Sumit', 'abc4', 'SK', '9856221434').createCustomer() == True
        assert Customer('Omkar', 'abc5', 'OS', '4455667711').createCustomer() == True
        assert Customer('timothyb', 'abc', 'Timothy Bennett', '5555551227').createCustomer() == True
        assert Customer('rachelc', 'abc', 'Rachel Campbell', '5555551228').createCustomer() == True
        assert Customer('michaelg', 'abc', 'Michael Green', '5555551229').createCustomer() == True
        assert Customer('jenniferl', 'abc', 'Jennifer Larson', '5555551230').createCustomer() == True
        assert Customer('davidm', 'abc', 'David Mason', '5555551231').createCustomer() == True
        assert Customer('sarahp', 'abc', 'Sarah Peterson', '5555551232').createCustomer() == True
        assert Customer('matthewr', 'abc', 'Matthew Roberts', '5555551233').createCustomer() == True
        assert Customer('lisaq', 'abc', 'Lisa Quinn', '5555551234').createCustomer() == True
        assert Customer('katherinet', 'abc', 'Katherine Taylor', '5555551235').createCustomer() == True
        assert Customer('johnd', 'abc', 'John Davis', '5555551236').createCustomer() == True
        assert Customer('sarahm', 'abc', 'Sarah Morgan', '5555551237').createCustomer() == True
        assert Customer('michaelw', 'abc', 'Michael Williams', '5555551238').createCustomer() == True
        assert Customer('jenniferh', 'abc', 'Jennifer Howard', '5555551239').createCustomer() == True
        assert Customer('davids', 'abc', 'David Scott', '5555551240').createCustomer() == True
        assert Customer('laurar', 'abc', 'Laura Reed', '5555551241').createCustomer() == True


        assert Operator('Manish', 'abc1', 'MB', '4411225549', 'Chintan').createOperator() == True
        assert Operator('Guarav', 'abc2', 'GS', '7475869421', 'Chintan').createOperator() == True
        assert Operator('Ketan', 'abc3', 'KM', '1122337495', 'Siddhesh').createOperator() == True
        assert Operator('Akshay', 'abc4', 'AJ', '5566442576', 'Siddhesh').createOperator() == True
        assert Operator('Lokesh', 'abc5', 'LD', '9988743615', 'Siddhesh').createOperator() == True
        assert Operator('timothyb', 'abc', 'Timothy Bennett', '5555551227', 'Siddhesh').createOperator() == True
        assert Operator('rachelc', 'abc', 'Rachel Campbell', '5555551228', 'Siddhesh').createOperator() == True
        assert Operator('michaelg', 'abc', 'Michael Green', '5555551229', 'Manas').createOperator() == True
        assert Operator('jenniferl', 'abc', 'Jennifer Larson', '5555551230', 'Manas').createOperator() == True
        assert Operator('davidm', 'abc', 'David Mason', '5555551231', 'Shubham').createOperator() == True
        assert Operator('sarahp', 'abc', 'Sarah Peterson', '5555551232', 'Shubham').createOperator() == True
        assert Operator('matthewr', 'abc', 'Matthew Roberts', '5555551233', 'Shubham').createOperator() == True
        assert Operator('lisaq', 'abc', 'Lisa Quinn', '5555551234', 'Sahil').createOperator() == True
        assert Operator('katherinet', 'abc', 'Katherine Taylor', '5555551235', 'Sahil').createOperator() == True
        assert Operator('johnd', 'abc', 'John Davis', '5555551236', 'Sahil').createOperator() == True


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
        assert Passenger('P6', 'M', 26, '5555551242', 'Tanmay').createObject() == True
        assert Passenger('P7', 'M', 32, '5555551243', 'Harshvardhan').createObject() == True
        assert Passenger('P8', 'M', 29, '5555551244', 'Jayesh').createObject() == True
        assert Passenger('P9', 'M', 27, '5555551245', 'Sumit').createObject() == True
        assert Passenger('P10', 'M', 25, '5555551246', 'Omkar').createObject() == True
        assert Passenger('P11', 'M', 30, '5555551227', 'timothyb').createObject() == True
        assert Passenger('P12', 'F', 28, '5555551228', 'rachelc').createObject() == True
        assert Passenger('P13', 'M', 35, '5555551229', 'michaelg').createObject() == True
        assert Passenger('P14', 'F', 31, '5555551230', 'jenniferl').createObject() == True
        assert Passenger('P15', 'M', 33, '5555551231', 'davidm').createObject() == True
        assert Passenger('P16', 'F', 29, '5555551232', 'sarahp').createObject() == True
        assert Passenger('P17', 'M', 34, '5555551233', 'matthewr').createObject() == True
        assert Passenger('P18', 'F', 27, '5555551234', 'lisaq').createObject() == True
        assert Passenger('P19', 'F', 32, '5555551235', 'katherinet').createObject() == True
        assert Passenger('P20', 'M', 31, '5555551236', 'johnd').createObject() == True
        assert Passenger('P21', 'F', 26, '5555551237', 'sarahm').createObject() == True
        assert Passenger('P22', 'M', 29, '5555551238', 'michaelw').createObject() == True
        assert Passenger('P23', 'F', 28, '5555551239', 'jenniferh').createObject() == True
        assert Passenger('P24', 'M', 35, '5555551240', 'davids').createObject() == True
        assert Passenger('P25', 'F', 33, '5555551241', 'laurar').createObject() == True
        assert Passenger('P26', 'F', 31, '5555551247', 'timothyb').createObject() == True
        assert Passenger('P27', 'M', 29, '5555551248', 'rachelc').createObject() == True
        assert Passenger('P28', 'F', 28, '5555551249', 'michaelg').createObject() == True
        assert Passenger('P29', 'M', 27, '5555551250', 'jenniferl').createObject() == True
        assert Passenger('P30', 'F', 26, '5555551251', 'davidm').createObject() == True
        assert Passenger('P31', 'M', 25, '5555551252', 'sarahp').createObject() == True
        assert Passenger('P32', 'F', 24, '5555551253', 'michaelw').createObject() == True
        assert Passenger('P33', 'M', 23, '5555551254', 'jenniferh').createObject() == True
        assert Passenger('P34', 'F', 22, '5555551255', 'davids').createObject() == True
        assert Passenger('P35', 'M', 21, '5555551256', 'laurar').createObject() == True


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
        assert City('New York').createObject() == True
        assert City('Los Angeles').createObject() == True
        assert City('Chicago').createObject() == True
        assert City('Houston').createObject() == True
        assert City('Phoenix').createObject() == True
        assert City('Philadelphia').createObject() == True
        assert City('San Antonio').createObject() == True
        assert City('San Diego').createObject() == True
        assert City('Dallas').createObject() == True
        assert City('San Jose').createObject() == True


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
        assert Stop('Stop #16', '876 Radnom-HSYF St.', 9).createObject() == True
        assert Stop('Stop #17', '123 Radnom-5jyn St.', 14).createObject() == True
        assert Stop('Stop #18', '456 Radnom-lSo+ St.', 12).createObject() == True
        assert Stop('Stop #19', '789 Radnom-qb3K St.', 5).createObject() == True
        assert Stop('Stop #20', '135 Radnom-SYuK St.', 7).createObject() == True
        assert Stop('Stop #21', '246 Radnom-z0Fu St.', 10).createObject() == True
        assert Stop('Stop #22', '357 Radnom-BBW5 St.', 15).createObject() == True
        assert Stop('Stop #23', '468 Radnom-R9mN St.', 19).createObject() == True
        assert Stop('Stop #24', '579 Radnom-ppze St.', 16).createObject() == True
        assert Stop('Stop #25', '690 Radnom-LX79 St.', 4).createObject() == True
        assert Stop('Stop #26', '801 Radnom-HSYF St.', 18).createObject() == True
        assert Stop('Stop #27', '912 Radnom-5jyn St.', 8).createObject() == True
        assert Stop('Stop #28', '023 Radnom-lSo+ St.', 2).createObject() == True
        assert Stop('Stop #29', '134 Radnom-qb3K St.', 11).createObject() == True
        assert Stop('Stop #30', '245 Radnom-SYuK St.', 19).createObject() == True


        assert Bus('MH 8 AB 8272', 'SLEEP', 2, 3, 5, 1, 'susanb').createObject() == True
        assert Bus('MH 12 AB 9096', 'SEAT', 2, 3, 5, 1, 'Chintan').createObject() == True
        assert Bus('MH 9 AB 8797', 'SLEEP', 2, 3, 5, 1, 'chrisd').createObject() == True
        assert Bus('MH 11 AB 9332', 'SLEEP', 2, 3, 5, 2, 'michaelw').createObject() == True
        assert Bus('MH 14 AB 6870', 'SEAT', 2, 3, 5, 1, 'Chintan').createObject() == True
        assert Bus('MH 5 AB 6693', 'SEAT', 2, 3, 5, 2, 'jamesm').createObject() == True
        assert Bus('MH 11 AB 5703', 'SLEEP', 2, 3, 5, 2, 'jamesm').createObject() == True
        assert Bus('MH 11 AB 7989', 'SEAT', 2, 3, 5, 1, 'nicolej').createObject() == True
        assert Bus('MH 5 AB 7650', 'SEAT', 2, 3, 5, 1, 'chrisd').createObject() == True
        assert Bus('MH 19 AB 9404', 'SLEEP', 2, 3, 5, 1, 'jamesm').createObject() == True
        assert Bus('MH 19 AB 5367', 'SLEEP', 2, 3, 5, 1, 'jack123').createObject() == True
        assert Bus('MH 11 AB 8643', 'SEAT', 2, 3, 5, 1, 'Shubham').createObject() == True
        assert Bus('MH 12 AB 5440', 'SLEEP', 2, 3, 5, 2, 'samuelm').createObject() == True
        assert Bus('MH 17 AB 8217', 'SEAT', 2, 3, 5, 1, 'lisaq').createObject() == True
        assert Bus('MH 6 AB 5509', 'SEAT', 2, 3, 5, 1, 'samuelm').createObject() == True
        assert Bus('MH 19 AB 8932', 'SLEEP', 2, 3, 5, 2, 'chrisd').createObject() == True
        assert Bus('MH 12 AB 8578', 'SEAT', 2, 3, 5, 2, 'brianb').createObject() == True
        assert Bus('MH 17 AB 5987', 'SEAT', 2, 3, 5, 2, 'michaelw').createObject() == True
        assert Bus('MH 13 AB 5137', 'SEAT', 2, 3, 5, 2, 'lisaq').createObject() == True
        assert Bus('MH 12 AB 7062', 'SLEEP', 2, 3, 5, 1, 'Siddhesh').createObject() == True
        assert Bus('MH 17 AB 5692', 'SEAT', 2, 3, 5, 1, 'lisaq').createObject() == True
        assert Bus('MH 18 AB 7004', 'SLEEP', 2, 3, 5, 1, 'brianb').createObject() == True
        assert Bus('MH 14 AB 9684', 'SEAT', 2, 3, 5, 1, 'jennifert').createObject() == True
        assert Bus('MH 14 AB 6518', 'SLEEP', 2, 3, 5, 1, 'Siddhesh').createObject() == True
        assert Bus('MH 13 AB 9993', 'SLEEP', 2, 3, 5, 2, 'jennifert').createObject() == True
        assert Bus('MH 8 AB 6980', 'SLEEP', 2, 3, 5, 1, 'laurar').createObject() == True
        assert Bus('MH 10 AB 9617', 'SLEEP', 2, 3, 5, 1, 'katherineg').createObject() == True
        assert Bus('MH 17 AB 9316', 'SEAT', 2, 3, 5, 2, 'brianb').createObject() == True
        assert Bus('MH 19 AB 8198', 'SEAT', 2, 3, 5, 2, 'jamesm').createObject() == True
        assert Bus('MH 11 AB 7659', 'SEAT', 2, 3, 5, 2, 'chrisd').createObject() == True
        assert Bus('MH 9 AB 8308', 'SLEEP', 2, 3, 5, 1, 'laurar').createObject() == True
        assert Bus('MH 20 AB 8094', 'SLEEP', 2, 3, 5, 1, 'laurar').createObject() == True
        assert Bus('MH 16 AB 7222', 'SLEEP', 2, 3, 5, 2, 'davids').createObject() == True
        assert Bus('MH 16 AB 7740', 'SEAT', 2, 3, 5, 1, 'laurar').createObject() == True
        assert Bus('MH 14 AB 5997', 'SLEEP', 2, 3, 5, 1, 'Manas').createObject() == True
        assert Bus('MH 15 AB 9478', 'SEAT', 2, 3, 5, 2, 'jack123').createObject() == True
        assert Bus('MH 7 AB 6536', 'SLEEP', 2, 3, 5, 1, 'davids').createObject() == True
        assert Bus('MH 8 AB 5155', 'SLEEP', 2, 3, 5, 1, 'michaelw').createObject() == True
        assert Bus('MH 10 AB 5575', 'SLEEP', 2, 3, 5, 1, 'Shubham').createObject() == True
        assert Bus('MH 11 AB 7889', 'SLEEP', 2, 3, 5, 2, 'laurar').createObject() == True


        assert Seat('MH 8 AB 8272', '1L', True).createObject() == True
        assert Seat('MH 8 AB 8272', '2L', False).createObject() == True
        assert Seat('MH 8 AB 8272', '3L', False).createObject() == True
        assert Seat('MH 8 AB 8272', '4U', True).createObject() == True
        assert Seat('MH 8 AB 8272', '5U', False).createObject() == True
        assert Seat('MH 8 AB 8272', '6U', False).createObject() == True
        assert Seat('MH 8 AB 8272', '7L', False).createObject() == True
        assert Seat('MH 8 AB 8272', '8L', True).createObject() == True
        assert Seat('MH 8 AB 8272', '9L', False).createObject() == True
        assert Seat('MH 8 AB 8272', '10U', True).createObject() == True
        assert Seat('MH 8 AB 8272', '11U', True).createObject() == True
        assert Seat('MH 8 AB 8272', '12U', False).createObject() == True
        assert Seat('MH 8 AB 8272', '13L', True).createObject() == True
        assert Seat('MH 8 AB 8272', '14L', False).createObject() == True
        assert Seat('MH 8 AB 8272', '15L', True).createObject() == True
        assert Seat('MH 8 AB 8272', '16U', True).createObject() == True
        assert Seat('MH 8 AB 8272', '17U', False).createObject() == True
        assert Seat('MH 8 AB 8272', '18U', True).createObject() == True
        assert Seat('MH 8 AB 8272', '19L', False).createObject() == True
        assert Seat('MH 8 AB 8272', '20L', False).createObject() == True
        assert Seat('MH 8 AB 8272', '21L', False).createObject() == True
        assert Seat('MH 8 AB 8272', '22U', True).createObject() == True
        assert Seat('MH 8 AB 8272', '23U', False).createObject() == True
        assert Seat('MH 8 AB 8272', '24U', True).createObject() == True
        assert Seat('MH 8 AB 8272', '25L', True).createObject() == True
        assert Seat('MH 8 AB 8272', '26L', True).createObject() == True
        assert Seat('MH 8 AB 8272', '27L', True).createObject() == True
        assert Seat('MH 8 AB 8272', '28U', False).createObject() == True
        assert Seat('MH 8 AB 8272', '29U', True).createObject() == True
        assert Seat('MH 8 AB 8272', '30U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '1L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '2L', False).createObject() == True
        assert Seat('MH 12 AB 9096', '3L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '4U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '5U', True).createObject() == True
        assert Seat('MH 12 AB 9096', '6U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '7L', False).createObject() == True
        assert Seat('MH 12 AB 9096', '8L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '9L', False).createObject() == True
        assert Seat('MH 12 AB 9096', '10U', True).createObject() == True
        assert Seat('MH 12 AB 9096', '11U', True).createObject() == True
        assert Seat('MH 12 AB 9096', '12U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '13L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '14L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '15L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '16U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '17U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '18U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '19L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '20L', False).createObject() == True
        assert Seat('MH 12 AB 9096', '21L', False).createObject() == True
        assert Seat('MH 12 AB 9096', '22U', True).createObject() == True
        assert Seat('MH 12 AB 9096', '23U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '24U', True).createObject() == True
        assert Seat('MH 12 AB 9096', '25L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '26L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '27L', True).createObject() == True
        assert Seat('MH 12 AB 9096', '28U', False).createObject() == True
        assert Seat('MH 12 AB 9096', '29U', True).createObject() == True
        assert Seat('MH 12 AB 9096', '30U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '1L', False).createObject() == True
        assert Seat('MH 9 AB 8797', '2L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '3L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '4U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '5U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '6U', False).createObject() == True
        assert Seat('MH 9 AB 8797', '7L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '8L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '9L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '10U', False).createObject() == True
        assert Seat('MH 9 AB 8797', '11U', False).createObject() == True
        assert Seat('MH 9 AB 8797', '12U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '13L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '14L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '15L', False).createObject() == True
        assert Seat('MH 9 AB 8797', '16U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '17U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '18U', False).createObject() == True
        assert Seat('MH 9 AB 8797', '19L', False).createObject() == True
        assert Seat('MH 9 AB 8797', '20L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '21L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '22U', False).createObject() == True
        assert Seat('MH 9 AB 8797', '23U', False).createObject() == True
        assert Seat('MH 9 AB 8797', '24U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '25L', False).createObject() == True
        assert Seat('MH 9 AB 8797', '26L', True).createObject() == True
        assert Seat('MH 9 AB 8797', '27L', False).createObject() == True
        assert Seat('MH 9 AB 8797', '28U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '29U', True).createObject() == True
        assert Seat('MH 9 AB 8797', '30U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '1L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '2L', False).createObject() == True
        assert Seat('MH 11 AB 9332', '3L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '4U', True).createObject() == True
        assert Seat('MH 11 AB 9332', '5U', True).createObject() == True
        assert Seat('MH 11 AB 9332', '6U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '7L', False).createObject() == True
        assert Seat('MH 11 AB 9332', '8L', False).createObject() == True
        assert Seat('MH 11 AB 9332', '9L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '10U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '11U', True).createObject() == True
        assert Seat('MH 11 AB 9332', '12U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '13L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '14L', False).createObject() == True
        assert Seat('MH 11 AB 9332', '15L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '16U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '17U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '18U', True).createObject() == True
        assert Seat('MH 11 AB 9332', '19L', False).createObject() == True
        assert Seat('MH 11 AB 9332', '20L', False).createObject() == True
        assert Seat('MH 11 AB 9332', '21L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '22U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '23U', True).createObject() == True
        assert Seat('MH 11 AB 9332', '24U', True).createObject() == True
        assert Seat('MH 11 AB 9332', '25L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '26L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '27L', True).createObject() == True
        assert Seat('MH 11 AB 9332', '28U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '29U', False).createObject() == True
        assert Seat('MH 11 AB 9332', '30U', False).createObject() == True
        assert Seat('MH 14 AB 6870', '1L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '2L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '3L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '4U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '5U', False).createObject() == True
        assert Seat('MH 14 AB 6870', '6U', False).createObject() == True
        assert Seat('MH 14 AB 6870', '7L', True).createObject() == True
        assert Seat('MH 14 AB 6870', '8L', True).createObject() == True
        assert Seat('MH 14 AB 6870', '9L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '10U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '11U', False).createObject() == True
        assert Seat('MH 14 AB 6870', '12U', False).createObject() == True
        assert Seat('MH 14 AB 6870', '13L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '14L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '15L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '16U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '17U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '18U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '19L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '20L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '21L', True).createObject() == True
        assert Seat('MH 14 AB 6870', '22U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '23U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '24U', False).createObject() == True
        assert Seat('MH 14 AB 6870', '25L', False).createObject() == True
        assert Seat('MH 14 AB 6870', '26L', True).createObject() == True
        assert Seat('MH 14 AB 6870', '27L', True).createObject() == True
        assert Seat('MH 14 AB 6870', '28U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '29U', True).createObject() == True
        assert Seat('MH 14 AB 6870', '30U', False).createObject() == True
        assert Seat('MH 5 AB 6693', '1L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '2L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '3L', True).createObject() == True
        assert Seat('MH 5 AB 6693', '4U', False).createObject() == True
        assert Seat('MH 5 AB 6693', '5U', False).createObject() == True
        assert Seat('MH 5 AB 6693', '6U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '7L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '8L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '9L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '10U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '11U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '12U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '13L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '14L', True).createObject() == True
        assert Seat('MH 5 AB 6693', '15L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '16U', False).createObject() == True
        assert Seat('MH 5 AB 6693', '17U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '18U', False).createObject() == True
        assert Seat('MH 5 AB 6693', '19L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '20L', True).createObject() == True
        assert Seat('MH 5 AB 6693', '21L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '22U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '23U', False).createObject() == True
        assert Seat('MH 5 AB 6693', '24U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '25L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '26L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '27L', False).createObject() == True
        assert Seat('MH 5 AB 6693', '28U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '29U', True).createObject() == True
        assert Seat('MH 5 AB 6693', '30U', True).createObject() == True
        assert Seat('MH 11 AB 5703', '1L', False).createObject() == True
        assert Seat('MH 11 AB 5703', '2L', False).createObject() == True
        assert Seat('MH 11 AB 5703', '3L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '4U', False).createObject() == True
        assert Seat('MH 11 AB 5703', '5U', True).createObject() == True
        assert Seat('MH 11 AB 5703', '6U', False).createObject() == True
        assert Seat('MH 11 AB 5703', '7L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '8L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '9L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '10U', False).createObject() == True
        assert Seat('MH 11 AB 5703', '11U', True).createObject() == True
        assert Seat('MH 11 AB 5703', '12U', True).createObject() == True
        assert Seat('MH 11 AB 5703', '13L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '14L', False).createObject() == True
        assert Seat('MH 11 AB 5703', '15L', False).createObject() == True
        assert Seat('MH 11 AB 5703', '16U', False).createObject() == True
        assert Seat('MH 11 AB 5703', '17U', True).createObject() == True
        assert Seat('MH 11 AB 5703', '18U', True).createObject() == True
        assert Seat('MH 11 AB 5703', '19L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '20L', False).createObject() == True
        assert Seat('MH 11 AB 5703', '21L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '22U', True).createObject() == True
        assert Seat('MH 11 AB 5703', '23U', False).createObject() == True
        assert Seat('MH 11 AB 5703', '24U', False).createObject() == True
        assert Seat('MH 11 AB 5703', '25L', False).createObject() == True
        assert Seat('MH 11 AB 5703', '26L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '27L', True).createObject() == True
        assert Seat('MH 11 AB 5703', '28U', False).createObject() == True
        assert Seat('MH 11 AB 5703', '29U', True).createObject() == True
        assert Seat('MH 11 AB 5703', '30U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '1L', False).createObject() == True
        assert Seat('MH 11 AB 7989', '2L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '3L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '4U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '5U', False).createObject() == True
        assert Seat('MH 11 AB 7989', '6U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '7L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '8L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '9L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '10U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '11U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '12U', False).createObject() == True
        assert Seat('MH 11 AB 7989', '13L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '14L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '15L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '16U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '17U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '18U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '19L', False).createObject() == True
        assert Seat('MH 11 AB 7989', '20L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '21L', False).createObject() == True
        assert Seat('MH 11 AB 7989', '22U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '23U', False).createObject() == True
        assert Seat('MH 11 AB 7989', '24U', True).createObject() == True
        assert Seat('MH 11 AB 7989', '25L', False).createObject() == True
        assert Seat('MH 11 AB 7989', '26L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '27L', True).createObject() == True
        assert Seat('MH 11 AB 7989', '28U', False).createObject() == True
        assert Seat('MH 11 AB 7989', '29U', False).createObject() == True
        assert Seat('MH 11 AB 7989', '30U', True).createObject() == True
        assert Seat('MH 5 AB 7650', '1L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '2L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '3L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '4U', True).createObject() == True
        assert Seat('MH 5 AB 7650', '5U', False).createObject() == True
        assert Seat('MH 5 AB 7650', '6U', True).createObject() == True
        assert Seat('MH 5 AB 7650', '7L', True).createObject() == True
        assert Seat('MH 5 AB 7650', '8L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '9L', True).createObject() == True
        assert Seat('MH 5 AB 7650', '10U', True).createObject() == True
        assert Seat('MH 5 AB 7650', '11U', False).createObject() == True
        assert Seat('MH 5 AB 7650', '12U', True).createObject() == True
        assert Seat('MH 5 AB 7650', '13L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '14L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '15L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '16U', False).createObject() == True
        assert Seat('MH 5 AB 7650', '17U', False).createObject() == True
        assert Seat('MH 5 AB 7650', '18U', True).createObject() == True
        assert Seat('MH 5 AB 7650', '19L', True).createObject() == True
        assert Seat('MH 5 AB 7650', '20L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '21L', True).createObject() == True
        assert Seat('MH 5 AB 7650', '22U', False).createObject() == True
        assert Seat('MH 5 AB 7650', '23U', False).createObject() == True
        assert Seat('MH 5 AB 7650', '24U', False).createObject() == True
        assert Seat('MH 5 AB 7650', '25L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '26L', True).createObject() == True
        assert Seat('MH 5 AB 7650', '27L', False).createObject() == True
        assert Seat('MH 5 AB 7650', '28U', True).createObject() == True
        assert Seat('MH 5 AB 7650', '29U', True).createObject() == True
        assert Seat('MH 5 AB 7650', '30U', False).createObject() == True
        assert Seat('MH 19 AB 9404', '1L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '2L', False).createObject() == True
        assert Seat('MH 19 AB 9404', '3L', False).createObject() == True
        assert Seat('MH 19 AB 9404', '4U', True).createObject() == True
        assert Seat('MH 19 AB 9404', '5U', False).createObject() == True
        assert Seat('MH 19 AB 9404', '6U', False).createObject() == True
        assert Seat('MH 19 AB 9404', '7L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '8L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '9L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '10U', False).createObject() == True
        assert Seat('MH 19 AB 9404', '11U', True).createObject() == True
        assert Seat('MH 19 AB 9404', '12U', False).createObject() == True
        assert Seat('MH 19 AB 9404', '13L', False).createObject() == True
        assert Seat('MH 19 AB 9404', '14L', False).createObject() == True
        assert Seat('MH 19 AB 9404', '15L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '16U', True).createObject() == True
        assert Seat('MH 19 AB 9404', '17U', True).createObject() == True
        assert Seat('MH 19 AB 9404', '18U', False).createObject() == True
        assert Seat('MH 19 AB 9404', '19L', False).createObject() == True
        assert Seat('MH 19 AB 9404', '20L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '21L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '22U', False).createObject() == True
        assert Seat('MH 19 AB 9404', '23U', True).createObject() == True
        assert Seat('MH 19 AB 9404', '24U', False).createObject() == True
        assert Seat('MH 19 AB 9404', '25L', False).createObject() == True
        assert Seat('MH 19 AB 9404', '26L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '27L', True).createObject() == True
        assert Seat('MH 19 AB 9404', '28U', True).createObject() == True
        assert Seat('MH 19 AB 9404', '29U', True).createObject() == True
        assert Seat('MH 19 AB 9404', '30U', False).createObject() == True
        assert Seat('MH 19 AB 5367', '1L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '2L', True).createObject() == True
        assert Seat('MH 19 AB 5367', '3L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '4U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '5U', False).createObject() == True
        assert Seat('MH 19 AB 5367', '6U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '7L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '8L', True).createObject() == True
        assert Seat('MH 19 AB 5367', '9L', True).createObject() == True
        assert Seat('MH 19 AB 5367', '10U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '11U', False).createObject() == True
        assert Seat('MH 19 AB 5367', '12U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '13L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '14L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '15L', True).createObject() == True
        assert Seat('MH 19 AB 5367', '16U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '17U', False).createObject() == True
        assert Seat('MH 19 AB 5367', '18U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '19L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '20L', True).createObject() == True
        assert Seat('MH 19 AB 5367', '21L', True).createObject() == True
        assert Seat('MH 19 AB 5367', '22U', False).createObject() == True
        assert Seat('MH 19 AB 5367', '23U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '24U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '25L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '26L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '27L', False).createObject() == True
        assert Seat('MH 19 AB 5367', '28U', False).createObject() == True
        assert Seat('MH 19 AB 5367', '29U', True).createObject() == True
        assert Seat('MH 19 AB 5367', '30U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '1L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '2L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '3L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '4U', False).createObject() == True
        assert Seat('MH 11 AB 8643', '5U', False).createObject() == True
        assert Seat('MH 11 AB 8643', '6U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '7L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '8L', True).createObject() == True
        assert Seat('MH 11 AB 8643', '9L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '10U', False).createObject() == True
        assert Seat('MH 11 AB 8643', '11U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '12U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '13L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '14L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '15L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '16U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '17U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '18U', False).createObject() == True
        assert Seat('MH 11 AB 8643', '19L', True).createObject() == True
        assert Seat('MH 11 AB 8643', '20L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '21L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '22U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '23U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '24U', True).createObject() == True
        assert Seat('MH 11 AB 8643', '25L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '26L', False).createObject() == True
        assert Seat('MH 11 AB 8643', '27L', True).createObject() == True
        assert Seat('MH 11 AB 8643', '28U', False).createObject() == True
        assert Seat('MH 11 AB 8643', '29U', False).createObject() == True
        assert Seat('MH 11 AB 8643', '30U', True).createObject() == True
        assert Seat('MH 12 AB 5440', '1L', True).createObject() == True
        assert Seat('MH 12 AB 5440', '2L', True).createObject() == True
        assert Seat('MH 12 AB 5440', '3L', True).createObject() == True
        assert Seat('MH 12 AB 5440', '4U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '5U', True).createObject() == True
        assert Seat('MH 12 AB 5440', '6U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '7L', True).createObject() == True
        assert Seat('MH 12 AB 5440', '8L', False).createObject() == True
        assert Seat('MH 12 AB 5440', '9L', True).createObject() == True
        assert Seat('MH 12 AB 5440', '10U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '11U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '12U', True).createObject() == True
        assert Seat('MH 12 AB 5440', '13L', False).createObject() == True
        assert Seat('MH 12 AB 5440', '14L', False).createObject() == True
        assert Seat('MH 12 AB 5440', '15L', True).createObject() == True
        assert Seat('MH 12 AB 5440', '16U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '17U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '18U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '19L', False).createObject() == True
        assert Seat('MH 12 AB 5440', '20L', True).createObject() == True
        assert Seat('MH 12 AB 5440', '21L', False).createObject() == True
        assert Seat('MH 12 AB 5440', '22U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '23U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '24U', False).createObject() == True
        assert Seat('MH 12 AB 5440', '25L', True).createObject() == True
        assert Seat('MH 12 AB 5440', '26L', False).createObject() == True
        assert Seat('MH 12 AB 5440', '27L', False).createObject() == True
        assert Seat('MH 12 AB 5440', '28U', True).createObject() == True
        assert Seat('MH 12 AB 5440', '29U', True).createObject() == True
        assert Seat('MH 12 AB 5440', '30U', False).createObject() == True
        assert Seat('MH 17 AB 8217', '1L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '2L', True).createObject() == True
        assert Seat('MH 17 AB 8217', '3L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '4U', True).createObject() == True
        assert Seat('MH 17 AB 8217', '5U', True).createObject() == True
        assert Seat('MH 17 AB 8217', '6U', False).createObject() == True
        assert Seat('MH 17 AB 8217', '7L', True).createObject() == True
        assert Seat('MH 17 AB 8217', '8L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '9L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '10U', True).createObject() == True
        assert Seat('MH 17 AB 8217', '11U', False).createObject() == True
        assert Seat('MH 17 AB 8217', '12U', True).createObject() == True
        assert Seat('MH 17 AB 8217', '13L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '14L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '15L', True).createObject() == True
        assert Seat('MH 17 AB 8217', '16U', False).createObject() == True
        assert Seat('MH 17 AB 8217', '17U', True).createObject() == True
        assert Seat('MH 17 AB 8217', '18U', False).createObject() == True
        assert Seat('MH 17 AB 8217', '19L', True).createObject() == True
        assert Seat('MH 17 AB 8217', '20L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '21L', True).createObject() == True
        assert Seat('MH 17 AB 8217', '22U', False).createObject() == True
        assert Seat('MH 17 AB 8217', '23U', False).createObject() == True
        assert Seat('MH 17 AB 8217', '24U', True).createObject() == True
        assert Seat('MH 17 AB 8217', '25L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '26L', True).createObject() == True
        assert Seat('MH 17 AB 8217', '27L', False).createObject() == True
        assert Seat('MH 17 AB 8217', '28U', True).createObject() == True
        assert Seat('MH 17 AB 8217', '29U', False).createObject() == True
        assert Seat('MH 17 AB 8217', '30U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '1L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '2L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '3L', True).createObject() == True
        assert Seat('MH 6 AB 5509', '4U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '5U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '6U', True).createObject() == True
        assert Seat('MH 6 AB 5509', '7L', True).createObject() == True
        assert Seat('MH 6 AB 5509', '8L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '9L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '10U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '11U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '12U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '13L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '14L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '15L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '16U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '17U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '18U', True).createObject() == True
        assert Seat('MH 6 AB 5509', '19L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '20L', True).createObject() == True
        assert Seat('MH 6 AB 5509', '21L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '22U', True).createObject() == True
        assert Seat('MH 6 AB 5509', '23U', True).createObject() == True
        assert Seat('MH 6 AB 5509', '24U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '25L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '26L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '27L', False).createObject() == True
        assert Seat('MH 6 AB 5509', '28U', True).createObject() == True
        assert Seat('MH 6 AB 5509', '29U', False).createObject() == True
        assert Seat('MH 6 AB 5509', '30U', True).createObject() == True
        assert Seat('MH 19 AB 8932', '1L', True).createObject() == True
        assert Seat('MH 19 AB 8932', '2L', True).createObject() == True
        assert Seat('MH 19 AB 8932', '3L', False).createObject() == True
        assert Seat('MH 19 AB 8932', '4U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '5U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '6U', True).createObject() == True
        assert Seat('MH 19 AB 8932', '7L', True).createObject() == True
        assert Seat('MH 19 AB 8932', '8L', False).createObject() == True
        assert Seat('MH 19 AB 8932', '9L', False).createObject() == True
        assert Seat('MH 19 AB 8932', '10U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '11U', True).createObject() == True
        assert Seat('MH 19 AB 8932', '12U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '13L', False).createObject() == True
        assert Seat('MH 19 AB 8932', '14L', True).createObject() == True
        assert Seat('MH 19 AB 8932', '15L', False).createObject() == True
        assert Seat('MH 19 AB 8932', '16U', True).createObject() == True
        assert Seat('MH 19 AB 8932', '17U', True).createObject() == True
        assert Seat('MH 19 AB 8932', '18U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '19L', True).createObject() == True
        assert Seat('MH 19 AB 8932', '20L', False).createObject() == True
        assert Seat('MH 19 AB 8932', '21L', False).createObject() == True
        assert Seat('MH 19 AB 8932', '22U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '23U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '24U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '25L', True).createObject() == True
        assert Seat('MH 19 AB 8932', '26L', True).createObject() == True
        assert Seat('MH 19 AB 8932', '27L', False).createObject() == True
        assert Seat('MH 19 AB 8932', '28U', False).createObject() == True
        assert Seat('MH 19 AB 8932', '29U', True).createObject() == True
        assert Seat('MH 19 AB 8932', '30U', False).createObject() == True
        assert Seat('MH 12 AB 8578', '1L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '2L', False).createObject() == True
        assert Seat('MH 12 AB 8578', '3L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '4U', False).createObject() == True
        assert Seat('MH 12 AB 8578', '5U', False).createObject() == True
        assert Seat('MH 12 AB 8578', '6U', False).createObject() == True
        assert Seat('MH 12 AB 8578', '7L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '8L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '9L', False).createObject() == True
        assert Seat('MH 12 AB 8578', '10U', True).createObject() == True
        assert Seat('MH 12 AB 8578', '11U', True).createObject() == True
        assert Seat('MH 12 AB 8578', '12U', False).createObject() == True
        assert Seat('MH 12 AB 8578', '13L', False).createObject() == True
        assert Seat('MH 12 AB 8578', '14L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '15L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '16U', False).createObject() == True
        assert Seat('MH 12 AB 8578', '17U', True).createObject() == True
        assert Seat('MH 12 AB 8578', '18U', True).createObject() == True
        assert Seat('MH 12 AB 8578', '19L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '20L', False).createObject() == True
        assert Seat('MH 12 AB 8578', '21L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '22U', False).createObject() == True
        assert Seat('MH 12 AB 8578', '23U', True).createObject() == True
        assert Seat('MH 12 AB 8578', '24U', False).createObject() == True
        assert Seat('MH 12 AB 8578', '25L', False).createObject() == True
        assert Seat('MH 12 AB 8578', '26L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '27L', True).createObject() == True
        assert Seat('MH 12 AB 8578', '28U', True).createObject() == True
        assert Seat('MH 12 AB 8578', '29U', True).createObject() == True
        assert Seat('MH 12 AB 8578', '30U', False).createObject() == True
        assert Seat('MH 17 AB 5987', '1L', True).createObject() == True
        assert Seat('MH 17 AB 5987', '2L', True).createObject() == True
        assert Seat('MH 17 AB 5987', '3L', False).createObject() == True
        assert Seat('MH 17 AB 5987', '4U', True).createObject() == True
        assert Seat('MH 17 AB 5987', '5U', False).createObject() == True
        assert Seat('MH 17 AB 5987', '6U', True).createObject() == True
        assert Seat('MH 17 AB 5987', '7L', False).createObject() == True
        assert Seat('MH 17 AB 5987', '8L', True).createObject() == True
        assert Seat('MH 17 AB 5987', '9L', False).createObject() == True
        assert Seat('MH 17 AB 5987', '10U', True).createObject() == True
        assert Seat('MH 17 AB 5987', '11U', True).createObject() == True
        assert Seat('MH 17 AB 5987', '12U', False).createObject() == True
        assert Seat('MH 17 AB 5987', '13L', True).createObject() == True
        assert Seat('MH 17 AB 5987', '14L', True).createObject() == True
        assert Seat('MH 17 AB 5987', '15L', True).createObject() == True
        assert Seat('MH 17 AB 5987', '16U', True).createObject() == True
        assert Seat('MH 17 AB 5987', '17U', False).createObject() == True
        assert Seat('MH 17 AB 5987', '18U', True).createObject() == True
        assert Seat('MH 17 AB 5987', '19L', False).createObject() == True
        assert Seat('MH 17 AB 5987', '20L', False).createObject() == True
        assert Seat('MH 17 AB 5987', '21L', False).createObject() == True
        assert Seat('MH 17 AB 5987', '22U', True).createObject() == True
        assert Seat('MH 17 AB 5987', '23U', False).createObject() == True
        assert Seat('MH 17 AB 5987', '24U', False).createObject() == True
        assert Seat('MH 17 AB 5987', '25L', False).createObject() == True
        assert Seat('MH 17 AB 5987', '26L', True).createObject() == True
        assert Seat('MH 17 AB 5987', '27L', False).createObject() == True
        assert Seat('MH 17 AB 5987', '28U', False).createObject() == True
        assert Seat('MH 17 AB 5987', '29U', False).createObject() == True
        assert Seat('MH 17 AB 5987', '30U', True).createObject() == True
        assert Seat('MH 13 AB 5137', '1L', True).createObject() == True
        assert Seat('MH 13 AB 5137', '2L', False).createObject() == True
        assert Seat('MH 13 AB 5137', '3L', True).createObject() == True
        assert Seat('MH 13 AB 5137', '4U', True).createObject() == True
        assert Seat('MH 13 AB 5137', '5U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '6U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '7L', False).createObject() == True
        assert Seat('MH 13 AB 5137', '8L', True).createObject() == True
        assert Seat('MH 13 AB 5137', '9L', True).createObject() == True
        assert Seat('MH 13 AB 5137', '10U', True).createObject() == True
        assert Seat('MH 13 AB 5137', '11U', True).createObject() == True
        assert Seat('MH 13 AB 5137', '12U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '13L', False).createObject() == True
        assert Seat('MH 13 AB 5137', '14L', True).createObject() == True
        assert Seat('MH 13 AB 5137', '15L', True).createObject() == True
        assert Seat('MH 13 AB 5137', '16U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '17U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '18U', True).createObject() == True
        assert Seat('MH 13 AB 5137', '19L', False).createObject() == True
        assert Seat('MH 13 AB 5137', '20L', False).createObject() == True
        assert Seat('MH 13 AB 5137', '21L', False).createObject() == True
        assert Seat('MH 13 AB 5137', '22U', True).createObject() == True
        assert Seat('MH 13 AB 5137', '23U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '24U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '25L', False).createObject() == True
        assert Seat('MH 13 AB 5137', '26L', True).createObject() == True
        assert Seat('MH 13 AB 5137', '27L', True).createObject() == True
        assert Seat('MH 13 AB 5137', '28U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '29U', False).createObject() == True
        assert Seat('MH 13 AB 5137', '30U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '1L', False).createObject() == True
        assert Seat('MH 12 AB 7062', '2L', True).createObject() == True
        assert Seat('MH 12 AB 7062', '3L', True).createObject() == True
        assert Seat('MH 12 AB 7062', '4U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '5U', True).createObject() == True
        assert Seat('MH 12 AB 7062', '6U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '7L', True).createObject() == True
        assert Seat('MH 12 AB 7062', '8L', True).createObject() == True
        assert Seat('MH 12 AB 7062', '9L', False).createObject() == True
        assert Seat('MH 12 AB 7062', '10U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '11U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '12U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '13L', False).createObject() == True
        assert Seat('MH 12 AB 7062', '14L', True).createObject() == True
        assert Seat('MH 12 AB 7062', '15L', False).createObject() == True
        assert Seat('MH 12 AB 7062', '16U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '17U', True).createObject() == True
        assert Seat('MH 12 AB 7062', '18U', True).createObject() == True
        assert Seat('MH 12 AB 7062', '19L', False).createObject() == True
        assert Seat('MH 12 AB 7062', '20L', False).createObject() == True
        assert Seat('MH 12 AB 7062', '21L', True).createObject() == True
        assert Seat('MH 12 AB 7062', '22U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '23U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '24U', True).createObject() == True
        assert Seat('MH 12 AB 7062', '25L', False).createObject() == True
        assert Seat('MH 12 AB 7062', '26L', True).createObject() == True
        assert Seat('MH 12 AB 7062', '27L', False).createObject() == True
        assert Seat('MH 12 AB 7062', '28U', True).createObject() == True
        assert Seat('MH 12 AB 7062', '29U', False).createObject() == True
        assert Seat('MH 12 AB 7062', '30U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '1L', False).createObject() == True
        assert Seat('MH 17 AB 5692', '2L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '3L', False).createObject() == True
        assert Seat('MH 17 AB 5692', '4U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '5U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '6U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '7L', False).createObject() == True
        assert Seat('MH 17 AB 5692', '8L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '9L', False).createObject() == True
        assert Seat('MH 17 AB 5692', '10U', False).createObject() == True
        assert Seat('MH 17 AB 5692', '11U', False).createObject() == True
        assert Seat('MH 17 AB 5692', '12U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '13L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '14L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '15L', False).createObject() == True
        assert Seat('MH 17 AB 5692', '16U', False).createObject() == True
        assert Seat('MH 17 AB 5692', '17U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '18U', False).createObject() == True
        assert Seat('MH 17 AB 5692', '19L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '20L', False).createObject() == True
        assert Seat('MH 17 AB 5692', '21L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '22U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '23U', False).createObject() == True
        assert Seat('MH 17 AB 5692', '24U', False).createObject() == True
        assert Seat('MH 17 AB 5692', '25L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '26L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '27L', True).createObject() == True
        assert Seat('MH 17 AB 5692', '28U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '29U', True).createObject() == True
        assert Seat('MH 17 AB 5692', '30U', False).createObject() == True
        assert Seat('MH 18 AB 7004', '1L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '2L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '3L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '4U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '5U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '6U', False).createObject() == True
        assert Seat('MH 18 AB 7004', '7L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '8L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '9L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '10U', False).createObject() == True
        assert Seat('MH 18 AB 7004', '11U', False).createObject() == True
        assert Seat('MH 18 AB 7004', '12U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '13L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '14L', True).createObject() == True
        assert Seat('MH 18 AB 7004', '15L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '16U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '17U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '18U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '19L', True).createObject() == True
        assert Seat('MH 18 AB 7004', '20L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '21L', False).createObject() == True
        assert Seat('MH 18 AB 7004', '22U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '23U', False).createObject() == True
        assert Seat('MH 18 AB 7004', '24U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '25L', True).createObject() == True
        assert Seat('MH 18 AB 7004', '26L', True).createObject() == True
        assert Seat('MH 18 AB 7004', '27L', True).createObject() == True
        assert Seat('MH 18 AB 7004', '28U', False).createObject() == True
        assert Seat('MH 18 AB 7004', '29U', True).createObject() == True
        assert Seat('MH 18 AB 7004', '30U', False).createObject() == True
        assert Seat('MH 14 AB 9684', '1L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '2L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '3L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '4U', False).createObject() == True
        assert Seat('MH 14 AB 9684', '5U', True).createObject() == True
        assert Seat('MH 14 AB 9684', '6U', False).createObject() == True
        assert Seat('MH 14 AB 9684', '7L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '8L', False).createObject() == True
        assert Seat('MH 14 AB 9684', '9L', False).createObject() == True
        assert Seat('MH 14 AB 9684', '10U', True).createObject() == True
        assert Seat('MH 14 AB 9684', '11U', False).createObject() == True
        assert Seat('MH 14 AB 9684', '12U', False).createObject() == True
        assert Seat('MH 14 AB 9684', '13L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '14L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '15L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '16U', True).createObject() == True
        assert Seat('MH 14 AB 9684', '17U', False).createObject() == True
        assert Seat('MH 14 AB 9684', '18U', False).createObject() == True
        assert Seat('MH 14 AB 9684', '19L', False).createObject() == True
        assert Seat('MH 14 AB 9684', '20L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '21L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '22U', True).createObject() == True
        assert Seat('MH 14 AB 9684', '23U', True).createObject() == True
        assert Seat('MH 14 AB 9684', '24U', True).createObject() == True
        assert Seat('MH 14 AB 9684', '25L', False).createObject() == True
        assert Seat('MH 14 AB 9684', '26L', True).createObject() == True
        assert Seat('MH 14 AB 9684', '27L', False).createObject() == True
        assert Seat('MH 14 AB 9684', '28U', True).createObject() == True
        assert Seat('MH 14 AB 9684', '29U', False).createObject() == True
        assert Seat('MH 14 AB 9684', '30U', False).createObject() == True
        assert Seat('MH 14 AB 6518', '1L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '2L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '3L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '4U', True).createObject() == True
        assert Seat('MH 14 AB 6518', '5U', True).createObject() == True
        assert Seat('MH 14 AB 6518', '6U', False).createObject() == True
        assert Seat('MH 14 AB 6518', '7L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '8L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '9L', False).createObject() == True
        assert Seat('MH 14 AB 6518', '10U', False).createObject() == True
        assert Seat('MH 14 AB 6518', '11U', True).createObject() == True
        assert Seat('MH 14 AB 6518', '12U', False).createObject() == True
        assert Seat('MH 14 AB 6518', '13L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '14L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '15L', False).createObject() == True
        assert Seat('MH 14 AB 6518', '16U', True).createObject() == True
        assert Seat('MH 14 AB 6518', '17U', False).createObject() == True
        assert Seat('MH 14 AB 6518', '18U', False).createObject() == True
        assert Seat('MH 14 AB 6518', '19L', False).createObject() == True
        assert Seat('MH 14 AB 6518', '20L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '21L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '22U', True).createObject() == True
        assert Seat('MH 14 AB 6518', '23U', True).createObject() == True
        assert Seat('MH 14 AB 6518', '24U', False).createObject() == True
        assert Seat('MH 14 AB 6518', '25L', False).createObject() == True
        assert Seat('MH 14 AB 6518', '26L', True).createObject() == True
        assert Seat('MH 14 AB 6518', '27L', False).createObject() == True
        assert Seat('MH 14 AB 6518', '28U', True).createObject() == True
        assert Seat('MH 14 AB 6518', '29U', True).createObject() == True
        assert Seat('MH 14 AB 6518', '30U', True).createObject() == True
        assert Seat('MH 13 AB 9993', '1L', True).createObject() == True
        assert Seat('MH 13 AB 9993', '2L', False).createObject() == True
        assert Seat('MH 13 AB 9993', '3L', True).createObject() == True
        assert Seat('MH 13 AB 9993', '4U', False).createObject() == True
        assert Seat('MH 13 AB 9993', '5U', False).createObject() == True
        assert Seat('MH 13 AB 9993', '6U', False).createObject() == True
        assert Seat('MH 13 AB 9993', '7L', False).createObject() == True
        assert Seat('MH 13 AB 9993', '8L', True).createObject() == True
        assert Seat('MH 13 AB 9993', '9L', False).createObject() == True
        assert Seat('MH 13 AB 9993', '10U', True).createObject() == True
        assert Seat('MH 13 AB 9993', '11U', True).createObject() == True
        assert Seat('MH 13 AB 9993', '12U', False).createObject() == True
        assert Seat('MH 13 AB 9993', '13L', False).createObject() == True
        assert Seat('MH 13 AB 9993', '14L', False).createObject() == True
        assert Seat('MH 13 AB 9993', '15L', False).createObject() == True
        assert Seat('MH 13 AB 9993', '16U', True).createObject() == True
        assert Seat('MH 13 AB 9993', '17U', True).createObject() == True
        assert Seat('MH 13 AB 9993', '18U', True).createObject() == True
        assert Seat('MH 13 AB 9993', '19L', True).createObject() == True
        assert Seat('MH 13 AB 9993', '20L', True).createObject() == True
        assert Seat('MH 13 AB 9993', '21L', True).createObject() == True
        assert Seat('MH 13 AB 9993', '22U', False).createObject() == True
        assert Seat('MH 13 AB 9993', '23U', False).createObject() == True
        assert Seat('MH 13 AB 9993', '24U', False).createObject() == True
        assert Seat('MH 13 AB 9993', '25L', True).createObject() == True
        assert Seat('MH 13 AB 9993', '26L', False).createObject() == True
        assert Seat('MH 13 AB 9993', '27L', True).createObject() == True
        assert Seat('MH 13 AB 9993', '28U', True).createObject() == True
        assert Seat('MH 13 AB 9993', '29U', True).createObject() == True
        assert Seat('MH 13 AB 9993', '30U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '1L', False).createObject() == True
        assert Seat('MH 8 AB 6980', '2L', True).createObject() == True
        assert Seat('MH 8 AB 6980', '3L', True).createObject() == True
        assert Seat('MH 8 AB 6980', '4U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '5U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '6U', True).createObject() == True
        assert Seat('MH 8 AB 6980', '7L', True).createObject() == True
        assert Seat('MH 8 AB 6980', '8L', True).createObject() == True
        assert Seat('MH 8 AB 6980', '9L', True).createObject() == True
        assert Seat('MH 8 AB 6980', '10U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '11U', True).createObject() == True
        assert Seat('MH 8 AB 6980', '12U', True).createObject() == True
        assert Seat('MH 8 AB 6980', '13L', False).createObject() == True
        assert Seat('MH 8 AB 6980', '14L', True).createObject() == True
        assert Seat('MH 8 AB 6980', '15L', False).createObject() == True
        assert Seat('MH 8 AB 6980', '16U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '17U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '18U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '19L', False).createObject() == True
        assert Seat('MH 8 AB 6980', '20L', False).createObject() == True
        assert Seat('MH 8 AB 6980', '21L', True).createObject() == True
        assert Seat('MH 8 AB 6980', '22U', True).createObject() == True
        assert Seat('MH 8 AB 6980', '23U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '24U', True).createObject() == True
        assert Seat('MH 8 AB 6980', '25L', False).createObject() == True
        assert Seat('MH 8 AB 6980', '26L', True).createObject() == True
        assert Seat('MH 8 AB 6980', '27L', False).createObject() == True
        assert Seat('MH 8 AB 6980', '28U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '29U', False).createObject() == True
        assert Seat('MH 8 AB 6980', '30U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '1L', False).createObject() == True
        assert Seat('MH 10 AB 9617', '2L', False).createObject() == True
        assert Seat('MH 10 AB 9617', '3L', False).createObject() == True
        assert Seat('MH 10 AB 9617', '4U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '5U', False).createObject() == True
        assert Seat('MH 10 AB 9617', '6U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '7L', True).createObject() == True
        assert Seat('MH 10 AB 9617', '8L', True).createObject() == True
        assert Seat('MH 10 AB 9617', '9L', True).createObject() == True
        assert Seat('MH 10 AB 9617', '10U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '11U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '12U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '13L', True).createObject() == True
        assert Seat('MH 10 AB 9617', '14L', True).createObject() == True
        assert Seat('MH 10 AB 9617', '15L', True).createObject() == True
        assert Seat('MH 10 AB 9617', '16U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '17U', False).createObject() == True
        assert Seat('MH 10 AB 9617', '18U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '19L', False).createObject() == True
        assert Seat('MH 10 AB 9617', '20L', True).createObject() == True
        assert Seat('MH 10 AB 9617', '21L', True).createObject() == True
        assert Seat('MH 10 AB 9617', '22U', False).createObject() == True
        assert Seat('MH 10 AB 9617', '23U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '24U', False).createObject() == True
        assert Seat('MH 10 AB 9617', '25L', False).createObject() == True
        assert Seat('MH 10 AB 9617', '26L', False).createObject() == True
        assert Seat('MH 10 AB 9617', '27L', False).createObject() == True
        assert Seat('MH 10 AB 9617', '28U', False).createObject() == True
        assert Seat('MH 10 AB 9617', '29U', True).createObject() == True
        assert Seat('MH 10 AB 9617', '30U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '1L', True).createObject() == True
        assert Seat('MH 17 AB 9316', '2L', False).createObject() == True
        assert Seat('MH 17 AB 9316', '3L', False).createObject() == True
        assert Seat('MH 17 AB 9316', '4U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '5U', True).createObject() == True
        assert Seat('MH 17 AB 9316', '6U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '7L', False).createObject() == True
        assert Seat('MH 17 AB 9316', '8L', True).createObject() == True
        assert Seat('MH 17 AB 9316', '9L', True).createObject() == True
        assert Seat('MH 17 AB 9316', '10U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '11U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '12U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '13L', True).createObject() == True
        assert Seat('MH 17 AB 9316', '14L', True).createObject() == True
        assert Seat('MH 17 AB 9316', '15L', False).createObject() == True
        assert Seat('MH 17 AB 9316', '16U', True).createObject() == True
        assert Seat('MH 17 AB 9316', '17U', True).createObject() == True
        assert Seat('MH 17 AB 9316', '18U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '19L', True).createObject() == True
        assert Seat('MH 17 AB 9316', '20L', False).createObject() == True
        assert Seat('MH 17 AB 9316', '21L', True).createObject() == True
        assert Seat('MH 17 AB 9316', '22U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '23U', True).createObject() == True
        assert Seat('MH 17 AB 9316', '24U', False).createObject() == True
        assert Seat('MH 17 AB 9316', '25L', True).createObject() == True
        assert Seat('MH 17 AB 9316', '26L', False).createObject() == True
        assert Seat('MH 17 AB 9316', '27L', False).createObject() == True
        assert Seat('MH 17 AB 9316', '28U', True).createObject() == True
        assert Seat('MH 17 AB 9316', '29U', True).createObject() == True
        assert Seat('MH 17 AB 9316', '30U', False).createObject() == True
        assert Seat('MH 19 AB 8198', '1L', True).createObject() == True
        assert Seat('MH 19 AB 8198', '2L', True).createObject() == True
        assert Seat('MH 19 AB 8198', '3L', True).createObject() == True
        assert Seat('MH 19 AB 8198', '4U', True).createObject() == True
        assert Seat('MH 19 AB 8198', '5U', False).createObject() == True
        assert Seat('MH 19 AB 8198', '6U', False).createObject() == True
        assert Seat('MH 19 AB 8198', '7L', True).createObject() == True
        assert Seat('MH 19 AB 8198', '8L', False).createObject() == True
        assert Seat('MH 19 AB 8198', '9L', True).createObject() == True
        assert Seat('MH 19 AB 8198', '10U', True).createObject() == True
        assert Seat('MH 19 AB 8198', '11U', False).createObject() == True
        assert Seat('MH 19 AB 8198', '12U', True).createObject() == True
        assert Seat('MH 19 AB 8198', '13L', False).createObject() == True
        assert Seat('MH 19 AB 8198', '14L', True).createObject() == True
        assert Seat('MH 19 AB 8198', '15L', True).createObject() == True
        assert Seat('MH 19 AB 8198', '16U', False).createObject() == True
        assert Seat('MH 19 AB 8198', '17U', False).createObject() == True
        assert Seat('MH 19 AB 8198', '18U', True).createObject() == True
        assert Seat('MH 19 AB 8198', '19L', False).createObject() == True
        assert Seat('MH 19 AB 8198', '20L', True).createObject() == True
        assert Seat('MH 19 AB 8198', '21L', False).createObject() == True
        assert Seat('MH 19 AB 8198', '22U', True).createObject() == True
        assert Seat('MH 19 AB 8198', '23U', True).createObject() == True
        assert Seat('MH 19 AB 8198', '24U', False).createObject() == True
        assert Seat('MH 19 AB 8198', '25L', False).createObject() == True
        assert Seat('MH 19 AB 8198', '26L', False).createObject() == True
        assert Seat('MH 19 AB 8198', '27L', False).createObject() == True
        assert Seat('MH 19 AB 8198', '28U', False).createObject() == True
        assert Seat('MH 19 AB 8198', '29U', True).createObject() == True
        assert Seat('MH 19 AB 8198', '30U', True).createObject() == True
        assert Seat('MH 11 AB 7659', '1L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '2L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '3L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '4U', True).createObject() == True
        assert Seat('MH 11 AB 7659', '5U', False).createObject() == True
        assert Seat('MH 11 AB 7659', '6U', False).createObject() == True
        assert Seat('MH 11 AB 7659', '7L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '8L', False).createObject() == True
        assert Seat('MH 11 AB 7659', '9L', False).createObject() == True
        assert Seat('MH 11 AB 7659', '10U', True).createObject() == True
        assert Seat('MH 11 AB 7659', '11U', False).createObject() == True
        assert Seat('MH 11 AB 7659', '12U', True).createObject() == True
        assert Seat('MH 11 AB 7659', '13L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '14L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '15L', False).createObject() == True
        assert Seat('MH 11 AB 7659', '16U', True).createObject() == True
        assert Seat('MH 11 AB 7659', '17U', False).createObject() == True
        assert Seat('MH 11 AB 7659', '18U', True).createObject() == True
        assert Seat('MH 11 AB 7659', '19L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '20L', False).createObject() == True
        assert Seat('MH 11 AB 7659', '21L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '22U', True).createObject() == True
        assert Seat('MH 11 AB 7659', '23U', False).createObject() == True
        assert Seat('MH 11 AB 7659', '24U', False).createObject() == True
        assert Seat('MH 11 AB 7659', '25L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '26L', True).createObject() == True
        assert Seat('MH 11 AB 7659', '27L', False).createObject() == True
        assert Seat('MH 11 AB 7659', '28U', False).createObject() == True
        assert Seat('MH 11 AB 7659', '29U', True).createObject() == True
        assert Seat('MH 11 AB 7659', '30U', True).createObject() == True
        assert Seat('MH 9 AB 8308', '1L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '2L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '3L', True).createObject() == True
        assert Seat('MH 9 AB 8308', '4U', True).createObject() == True
        assert Seat('MH 9 AB 8308', '5U', True).createObject() == True
        assert Seat('MH 9 AB 8308', '6U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '7L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '8L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '9L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '10U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '11U', True).createObject() == True
        assert Seat('MH 9 AB 8308', '12U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '13L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '14L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '15L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '16U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '17U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '18U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '19L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '20L', True).createObject() == True
        assert Seat('MH 9 AB 8308', '21L', True).createObject() == True
        assert Seat('MH 9 AB 8308', '22U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '23U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '24U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '25L', True).createObject() == True
        assert Seat('MH 9 AB 8308', '26L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '27L', False).createObject() == True
        assert Seat('MH 9 AB 8308', '28U', False).createObject() == True
        assert Seat('MH 9 AB 8308', '29U', True).createObject() == True
        assert Seat('MH 9 AB 8308', '30U', True).createObject() == True
        assert Seat('MH 20 AB 8094', '1L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '2L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '3L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '4U', True).createObject() == True
        assert Seat('MH 20 AB 8094', '5U', True).createObject() == True
        assert Seat('MH 20 AB 8094', '6U', False).createObject() == True
        assert Seat('MH 20 AB 8094', '7L', False).createObject() == True
        assert Seat('MH 20 AB 8094', '8L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '9L', False).createObject() == True
        assert Seat('MH 20 AB 8094', '10U', False).createObject() == True
        assert Seat('MH 20 AB 8094', '11U', False).createObject() == True
        assert Seat('MH 20 AB 8094', '12U', False).createObject() == True
        assert Seat('MH 20 AB 8094', '13L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '14L', False).createObject() == True
        assert Seat('MH 20 AB 8094', '15L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '16U', True).createObject() == True
        assert Seat('MH 20 AB 8094', '17U', False).createObject() == True
        assert Seat('MH 20 AB 8094', '18U', False).createObject() == True
        assert Seat('MH 20 AB 8094', '19L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '20L', False).createObject() == True
        assert Seat('MH 20 AB 8094', '21L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '22U', True).createObject() == True
        assert Seat('MH 20 AB 8094', '23U', False).createObject() == True
        assert Seat('MH 20 AB 8094', '24U', True).createObject() == True
        assert Seat('MH 20 AB 8094', '25L', False).createObject() == True
        assert Seat('MH 20 AB 8094', '26L', False).createObject() == True
        assert Seat('MH 20 AB 8094', '27L', True).createObject() == True
        assert Seat('MH 20 AB 8094', '28U', True).createObject() == True
        assert Seat('MH 20 AB 8094', '29U', False).createObject() == True
        assert Seat('MH 20 AB 8094', '30U', True).createObject() == True
        assert Seat('MH 16 AB 7222', '1L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '2L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '3L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '4U', True).createObject() == True
        assert Seat('MH 16 AB 7222', '5U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '6U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '7L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '8L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '9L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '10U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '11U', True).createObject() == True
        assert Seat('MH 16 AB 7222', '12U', True).createObject() == True
        assert Seat('MH 16 AB 7222', '13L', True).createObject() == True
        assert Seat('MH 16 AB 7222', '14L', True).createObject() == True
        assert Seat('MH 16 AB 7222', '15L', True).createObject() == True
        assert Seat('MH 16 AB 7222', '16U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '17U', True).createObject() == True
        assert Seat('MH 16 AB 7222', '18U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '19L', True).createObject() == True
        assert Seat('MH 16 AB 7222', '20L', True).createObject() == True
        assert Seat('MH 16 AB 7222', '21L', True).createObject() == True
        assert Seat('MH 16 AB 7222', '22U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '23U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '24U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '25L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '26L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '27L', False).createObject() == True
        assert Seat('MH 16 AB 7222', '28U', True).createObject() == True
        assert Seat('MH 16 AB 7222', '29U', False).createObject() == True
        assert Seat('MH 16 AB 7222', '30U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '1L', False).createObject() == True
        assert Seat('MH 16 AB 7740', '2L', False).createObject() == True
        assert Seat('MH 16 AB 7740', '3L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '4U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '5U', False).createObject() == True
        assert Seat('MH 16 AB 7740', '6U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '7L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '8L', False).createObject() == True
        assert Seat('MH 16 AB 7740', '9L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '10U', False).createObject() == True
        assert Seat('MH 16 AB 7740', '11U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '12U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '13L', False).createObject() == True
        assert Seat('MH 16 AB 7740', '14L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '15L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '16U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '17U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '18U', False).createObject() == True
        assert Seat('MH 16 AB 7740', '19L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '20L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '21L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '22U', False).createObject() == True
        assert Seat('MH 16 AB 7740', '23U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '24U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '25L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '26L', True).createObject() == True
        assert Seat('MH 16 AB 7740', '27L', False).createObject() == True
        assert Seat('MH 16 AB 7740', '28U', False).createObject() == True
        assert Seat('MH 16 AB 7740', '29U', True).createObject() == True
        assert Seat('MH 16 AB 7740', '30U', True).createObject() == True
        assert Seat('MH 14 AB 5997', '1L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '2L', False).createObject() == True
        assert Seat('MH 14 AB 5997', '3L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '4U', False).createObject() == True
        assert Seat('MH 14 AB 5997', '5U', False).createObject() == True
        assert Seat('MH 14 AB 5997', '6U', False).createObject() == True
        assert Seat('MH 14 AB 5997', '7L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '8L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '9L', False).createObject() == True
        assert Seat('MH 14 AB 5997', '10U', True).createObject() == True
        assert Seat('MH 14 AB 5997', '11U', True).createObject() == True
        assert Seat('MH 14 AB 5997', '12U', False).createObject() == True
        assert Seat('MH 14 AB 5997', '13L', False).createObject() == True
        assert Seat('MH 14 AB 5997', '14L', False).createObject() == True
        assert Seat('MH 14 AB 5997', '15L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '16U', False).createObject() == True
        assert Seat('MH 14 AB 5997', '17U', False).createObject() == True
        assert Seat('MH 14 AB 5997', '18U', True).createObject() == True
        assert Seat('MH 14 AB 5997', '19L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '20L', False).createObject() == True
        assert Seat('MH 14 AB 5997', '21L', False).createObject() == True
        assert Seat('MH 14 AB 5997', '22U', False).createObject() == True
        assert Seat('MH 14 AB 5997', '23U', True).createObject() == True
        assert Seat('MH 14 AB 5997', '24U', False).createObject() == True
        assert Seat('MH 14 AB 5997', '25L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '26L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '27L', True).createObject() == True
        assert Seat('MH 14 AB 5997', '28U', True).createObject() == True
        assert Seat('MH 14 AB 5997', '29U', True).createObject() == True
        assert Seat('MH 14 AB 5997', '30U', False).createObject() == True
        assert Seat('MH 15 AB 9478', '1L', False).createObject() == True
        assert Seat('MH 15 AB 9478', '2L', False).createObject() == True
        assert Seat('MH 15 AB 9478', '3L', False).createObject() == True
        assert Seat('MH 15 AB 9478', '4U', True).createObject() == True
        assert Seat('MH 15 AB 9478', '5U', False).createObject() == True
        assert Seat('MH 15 AB 9478', '6U', False).createObject() == True
        assert Seat('MH 15 AB 9478', '7L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '8L', False).createObject() == True
        assert Seat('MH 15 AB 9478', '9L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '10U', False).createObject() == True
        assert Seat('MH 15 AB 9478', '11U', False).createObject() == True
        assert Seat('MH 15 AB 9478', '12U', False).createObject() == True
        assert Seat('MH 15 AB 9478', '13L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '14L', False).createObject() == True
        assert Seat('MH 15 AB 9478', '15L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '16U', False).createObject() == True
        assert Seat('MH 15 AB 9478', '17U', True).createObject() == True
        assert Seat('MH 15 AB 9478', '18U', True).createObject() == True
        assert Seat('MH 15 AB 9478', '19L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '20L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '21L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '22U', False).createObject() == True
        assert Seat('MH 15 AB 9478', '23U', True).createObject() == True
        assert Seat('MH 15 AB 9478', '24U', True).createObject() == True
        assert Seat('MH 15 AB 9478', '25L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '26L', False).createObject() == True
        assert Seat('MH 15 AB 9478', '27L', True).createObject() == True
        assert Seat('MH 15 AB 9478', '28U', True).createObject() == True
        assert Seat('MH 15 AB 9478', '29U', True).createObject() == True
        assert Seat('MH 15 AB 9478', '30U', False).createObject() == True
        assert Seat('MH 7 AB 6536', '1L', True).createObject() == True
        assert Seat('MH 7 AB 6536', '2L', True).createObject() == True
        assert Seat('MH 7 AB 6536', '3L', True).createObject() == True
        assert Seat('MH 7 AB 6536', '4U', False).createObject() == True
        assert Seat('MH 7 AB 6536', '5U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '6U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '7L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '8L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '9L', True).createObject() == True
        assert Seat('MH 7 AB 6536', '10U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '11U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '12U', False).createObject() == True
        assert Seat('MH 7 AB 6536', '13L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '14L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '15L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '16U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '17U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '18U', False).createObject() == True
        assert Seat('MH 7 AB 6536', '19L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '20L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '21L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '22U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '23U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '24U', False).createObject() == True
        assert Seat('MH 7 AB 6536', '25L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '26L', False).createObject() == True
        assert Seat('MH 7 AB 6536', '27L', True).createObject() == True
        assert Seat('MH 7 AB 6536', '28U', True).createObject() == True
        assert Seat('MH 7 AB 6536', '29U', False).createObject() == True
        assert Seat('MH 7 AB 6536', '30U', False).createObject() == True
        assert Seat('MH 8 AB 5155', '1L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '2L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '3L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '4U', True).createObject() == True
        assert Seat('MH 8 AB 5155', '5U', False).createObject() == True
        assert Seat('MH 8 AB 5155', '6U', True).createObject() == True
        assert Seat('MH 8 AB 5155', '7L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '8L', False).createObject() == True
        assert Seat('MH 8 AB 5155', '9L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '10U', True).createObject() == True
        assert Seat('MH 8 AB 5155', '11U', True).createObject() == True
        assert Seat('MH 8 AB 5155', '12U', False).createObject() == True
        assert Seat('MH 8 AB 5155', '13L', False).createObject() == True
        assert Seat('MH 8 AB 5155', '14L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '15L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '16U', False).createObject() == True
        assert Seat('MH 8 AB 5155', '17U', False).createObject() == True
        assert Seat('MH 8 AB 5155', '18U', True).createObject() == True
        assert Seat('MH 8 AB 5155', '19L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '20L', False).createObject() == True
        assert Seat('MH 8 AB 5155', '21L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '22U', True).createObject() == True
        assert Seat('MH 8 AB 5155', '23U', True).createObject() == True
        assert Seat('MH 8 AB 5155', '24U', False).createObject() == True
        assert Seat('MH 8 AB 5155', '25L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '26L', True).createObject() == True
        assert Seat('MH 8 AB 5155', '27L', False).createObject() == True
        assert Seat('MH 8 AB 5155', '28U', False).createObject() == True
        assert Seat('MH 8 AB 5155', '29U', False).createObject() == True
        assert Seat('MH 8 AB 5155', '30U', False).createObject() == True
        assert Seat('MH 10 AB 5575', '1L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '2L', False).createObject() == True
        assert Seat('MH 10 AB 5575', '3L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '4U', True).createObject() == True
        assert Seat('MH 10 AB 5575', '5U', False).createObject() == True
        assert Seat('MH 10 AB 5575', '6U', True).createObject() == True
        assert Seat('MH 10 AB 5575', '7L', False).createObject() == True
        assert Seat('MH 10 AB 5575', '8L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '9L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '10U', False).createObject() == True
        assert Seat('MH 10 AB 5575', '11U', True).createObject() == True
        assert Seat('MH 10 AB 5575', '12U', False).createObject() == True
        assert Seat('MH 10 AB 5575', '13L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '14L', False).createObject() == True
        assert Seat('MH 10 AB 5575', '15L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '16U', True).createObject() == True
        assert Seat('MH 10 AB 5575', '17U', False).createObject() == True
        assert Seat('MH 10 AB 5575', '18U', True).createObject() == True
        assert Seat('MH 10 AB 5575', '19L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '20L', False).createObject() == True
        assert Seat('MH 10 AB 5575', '21L', False).createObject() == True
        assert Seat('MH 10 AB 5575', '22U', True).createObject() == True
        assert Seat('MH 10 AB 5575', '23U', False).createObject() == True
        assert Seat('MH 10 AB 5575', '24U', True).createObject() == True
        assert Seat('MH 10 AB 5575', '25L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '26L', False).createObject() == True
        assert Seat('MH 10 AB 5575', '27L', True).createObject() == True
        assert Seat('MH 10 AB 5575', '28U', False).createObject() == True
        assert Seat('MH 10 AB 5575', '29U', False).createObject() == True
        assert Seat('MH 10 AB 5575', '30U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '1L', False).createObject() == True
        assert Seat('MH 11 AB 7889', '2L', True).createObject() == True
        assert Seat('MH 11 AB 7889', '3L', True).createObject() == True
        assert Seat('MH 11 AB 7889', '4U', True).createObject() == True
        assert Seat('MH 11 AB 7889', '5U', True).createObject() == True
        assert Seat('MH 11 AB 7889', '6U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '7L', False).createObject() == True
        assert Seat('MH 11 AB 7889', '8L', False).createObject() == True
        assert Seat('MH 11 AB 7889', '9L', False).createObject() == True
        assert Seat('MH 11 AB 7889', '10U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '11U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '12U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '13L', True).createObject() == True
        assert Seat('MH 11 AB 7889', '14L', True).createObject() == True
        assert Seat('MH 11 AB 7889', '15L', False).createObject() == True
        assert Seat('MH 11 AB 7889', '16U', True).createObject() == True
        assert Seat('MH 11 AB 7889', '17U', True).createObject() == True
        assert Seat('MH 11 AB 7889', '18U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '19L', False).createObject() == True
        assert Seat('MH 11 AB 7889', '20L', False).createObject() == True
        assert Seat('MH 11 AB 7889', '21L', True).createObject() == True
        assert Seat('MH 11 AB 7889', '22U', True).createObject() == True
        assert Seat('MH 11 AB 7889', '23U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '24U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '25L', True).createObject() == True
        assert Seat('MH 11 AB 7889', '26L', True).createObject() == True
        assert Seat('MH 11 AB 7889', '27L', False).createObject() == True
        assert Seat('MH 11 AB 7889', '28U', False).createObject() == True
        assert Seat('MH 11 AB 7889', '29U', True).createObject() == True
        assert Seat('MH 11 AB 7889', '30U', True).createObject() == True

   
        assert Schedule('2022-12-29', '2022-12-30', '12:44:52', '10:24:50', 4946, 5, 1, 'MH 9 AB 8797', 'davidm').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '00:25:50', '06:47:33', 5624, 4, 4, 'MH 8 AB 6980', 'Ketan').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '03:40:08', '14:51:08', 1241, 1, 4, 'MH 19 AB 8198', 'matthewr').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '15:48:37', '20:28:56', 2980, 1, 1, 'MH 19 AB 8198', 'davidm').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '17:18:59', '05:25:04', 3238, 2, 3, 'MH 10 AB 5575', 'matthewr').createObject() == True
        assert Schedule('2022-12-23', '2022-12-24', '15:30:40', '10:48:26', 8339, 2, 5, 'MH 16 AB 7222', 'davidm').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '02:20:28', '10:19:20', 2084, 3, 1, 'MH 17 AB 9316', 'matthewr').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '13:21:56', '18:28:36', 9274, 1, 4, 'MH 11 AB 9332', 'matthewr').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '08:21:50', '12:04:31', 1758, 3, 2, 'MH 18 AB 7004', 'rachelc').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '16:32:11', '22:48:38', 1396, 1, 3, 'MH 14 AB 6518', 'sarahp').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '17:00:14', '17:40:26', 7605, 3, 3, 'MH 11 AB 9332', 'Akshay').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '06:17:25', '15:29:08', 6099, 5, 4, 'MH 12 AB 8578', 'johnd').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '23:10:49', '14:12:34', 5747, 1, 2, 'MH 11 AB 8643', 'michaelg').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '06:29:20', '07:07:04', 7960, 5, 5, 'MH 10 AB 9617', 'davidm').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '11:29:24', '15:06:40', 8904, 3, 2, 'MH 15 AB 9478', 'johnd').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '14:19:57', '07:49:32', 8947, 4, 2, 'MH 18 AB 7004', 'matthewr').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '19:04:27', '05:37:51', 3862, 2, 4, 'MH 13 AB 9993', 'timothyb').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '20:39:37', '05:00:01', 1585, 4, 1, 'MH 15 AB 9478', 'Ketan').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '20:58:50', '10:38:46', 6986, 1, 3, 'MH 11 AB 7659', 'jenniferl').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '07:52:23', '01:46:11', 6174, 4, 1, 'MH 11 AB 7889', 'timothyb').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '09:15:48', '10:29:57', 6029, 5, 1, 'MH 13 AB 9993', 'Manish').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '16:49:49', '13:10:24', 8667, 1, 3, 'MH 14 AB 5997', 'Guarav').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '07:20:47', '01:01:55', 7635, 2, 4, 'MH 14 AB 9684', 'lisaq').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '15:14:49', '11:19:56', 3430, 2, 3, 'MH 17 AB 9316', 'katherinet').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '10:53:32', '09:31:50', 2537, 3, 4, 'MH 17 AB 9316', 'Manish').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '19:52:07', '16:41:33', 7798, 1, 2, 'MH 11 AB 8643', 'Manish').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '02:06:06', '19:59:29', 2417, 3, 5, 'MH 5 AB 7650', 'Guarav').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '03:03:00', '21:46:13', 4363, 3, 3, 'MH 12 AB 9096', 'Ketan').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '04:14:05', '08:06:41', 2985, 2, 5, 'MH 11 AB 7989', 'katherinet').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '06:48:40', '05:41:37', 6046, 5, 3, 'MH 11 AB 8643', 'Ketan').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '10:44:01', '16:07:21', 8732, 3, 3, 'MH 12 AB 9096', 'Lokesh').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '19:10:41', '08:35:47', 5262, 3, 3, 'MH 8 AB 6980', 'sarahp').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '20:51:22', '02:00:10', 5579, 3, 5, 'MH 15 AB 9478', 'johnd').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '19:17:47', '12:41:02', 9191, 1, 1, 'MH 15 AB 9478', 'katherinet').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '13:17:44', '22:21:45', 7228, 5, 2, 'MH 7 AB 6536', 'timothyb').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '05:45:51', '12:19:07', 1282, 3, 2, 'MH 11 AB 7659', 'rachelc').createObject() == True
        assert Schedule('2022-12-23', '2022-12-24', '20:35:19', '14:55:13', 7475, 3, 3, 'MH 9 AB 8797', 'katherinet').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '11:57:36', '11:19:02', 1019, 3, 1, 'MH 16 AB 7740', 'Lokesh').createObject() == True
        assert Schedule('2022-12-23', '2022-12-24', '10:09:28', '06:19:20', 9748, 3, 5, 'MH 20 AB 8094', 'katherinet').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '09:49:23', '14:35:26', 7890, 5, 5, 'MH 18 AB 7004', 'Manish').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '03:40:33', '04:55:58', 1442, 3, 3, 'MH 19 AB 8198', 'rachelc').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '01:54:32', '00:50:05', 4330, 1, 5, 'MH 16 AB 7740', 'timothyb').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '17:27:00', '19:12:01', 7351, 1, 1, 'MH 17 AB 9316', 'johnd').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '17:17:41', '21:30:05', 2550, 2, 2, 'MH 11 AB 9332', 'matthewr').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '08:20:29', '04:42:56', 4472, 4, 4, 'MH 18 AB 7004', 'lisaq').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '19:16:10', '19:21:44', 5263, 1, 1, 'MH 8 AB 5155', 'Akshay').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '20:15:00', '09:51:19', 9875, 4, 3, 'MH 10 AB 5575', 'johnd').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '22:39:37', '08:47:40', 1013, 1, 3, 'MH 5 AB 6693', 'michaelg').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '14:09:22', '07:16:26', 9728, 1, 3, 'MH 17 AB 9316', 'davidm').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '10:59:48', '01:56:33', 4759, 4, 5, 'MH 16 AB 7740', 'lisaq').createObject() == True
        assert Schedule('2022-12-23', '2022-12-24', '17:33:30', '10:22:55', 4860, 3, 5, 'MH 19 AB 8932', 'Akshay').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '09:59:39', '08:04:27', 6086, 5, 4, 'MH 9 AB 8308', 'Manish').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '16:21:57', '18:54:58', 6720, 1, 3, 'MH 9 AB 8308', 'Manish').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '18:56:18', '19:54:44', 8964, 3, 4, 'MH 6 AB 5509', 'Manish').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '23:31:35', '22:42:29', 4797, 1, 3, 'MH 11 AB 5703', 'jenniferl').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '13:32:57', '00:29:10', 2601, 4, 5, 'MH 19 AB 5367', 'Akshay').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '20:15:49', '13:28:57', 9237, 3, 1, 'MH 13 AB 9993', 'Ketan').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '22:44:49', '01:05:24', 3683, 1, 3, 'MH 17 AB 5987', 'jenniferl').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '12:50:43', '06:31:06', 4781, 1, 4, 'MH 16 AB 7222', 'Manish').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '20:59:35', '03:55:39', 2973, 4, 4, 'MH 11 AB 7989', 'Ketan').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '22:32:39', '09:35:31', 7687, 3, 4, 'MH 16 AB 7740', 'sarahp').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '16:24:03', '21:37:54', 6409, 5, 3, 'MH 19 AB 8932', 'timothyb').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '18:49:55', '06:18:00', 1219, 4, 4, 'MH 17 AB 8217', 'rachelc').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '14:08:03', '05:27:58', 2823, 4, 5, 'MH 5 AB 6693', 'davidm').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '16:09:14', '10:06:49', 1718, 2, 2, 'MH 6 AB 5509', 'Manish').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '01:35:54', '04:01:19', 4314, 5, 4, 'MH 19 AB 8198', 'michaelg').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '02:50:53', '16:33:13', 6847, 3, 1, 'MH 8 AB 8272', 'Ketan').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '09:29:22', '20:41:40', 5546, 1, 5, 'MH 10 AB 5575', 'johnd').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '22:54:35', '02:21:57', 8798, 1, 5, 'MH 8 AB 5155', 'lisaq').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '17:30:33', '13:41:11', 5330, 1, 2, 'MH 6 AB 5509', 'davidm').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '11:54:09', '11:02:12', 1893, 3, 2, 'MH 16 AB 7222', 'timothyb').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '01:50:56', '01:32:29', 5969, 2, 1, 'MH 12 AB 9096', 'Manish').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '14:00:01', '21:05:16', 4824, 2, 5, 'MH 19 AB 5367', 'katherinet').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '15:30:52', '01:44:01', 2047, 4, 5, 'MH 8 AB 6980', 'sarahp').createObject() == True
        assert Schedule('2022-12-23', '2022-12-24', '18:00:56', '05:23:50', 3405, 1, 2, 'MH 17 AB 9316', 'rachelc').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '04:45:55', '15:59:57', 9193, 1, 5, 'MH 10 AB 9617', 'timothyb').createObject() == True
        assert Schedule('2022-12-23', '2022-12-24', '04:31:45', '23:16:49', 1111, 1, 1, 'MH 12 AB 8578', 'Akshay').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '20:19:38', '06:51:51', 1796, 1, 5, 'MH 5 AB 7650', 'Lokesh').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '05:24:19', '00:45:34', 8707, 4, 2, 'MH 19 AB 8198', 'Manish').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '06:32:09', '17:48:01', 7562, 1, 2, 'MH 11 AB 9332', 'timothyb').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '09:51:56', '16:49:22', 4269, 5, 5, 'MH 17 AB 5987', 'timothyb').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '10:50:04', '19:05:55', 2791, 5, 3, 'MH 14 AB 5997', 'katherinet').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '01:11:45', '18:58:25', 1129, 2, 1, 'MH 12 AB 9096', 'rachelc').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '09:59:52', '10:18:15', 2401, 3, 2, 'MH 9 AB 8797', 'Ketan').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '08:50:35', '16:46:07', 9509, 3, 2, 'MH 12 AB 8578', 'jenniferl').createObject() == True
        assert Schedule('2022-12-23', '2022-12-24', '00:11:10', '16:43:31', 9285, 5, 1, 'MH 14 AB 6870', 'johnd').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '14:23:14', '03:35:36', 7696, 1, 2, 'MH 14 AB 6518', 'Manish').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '22:31:48', '00:03:07', 8550, 5, 2, 'MH 14 AB 6870', 'Guarav').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '08:45:18', '07:38:07', 6802, 1, 3, 'MH 14 AB 9684', 'Akshay').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '13:22:03', '00:33:34', 4630, 1, 3, 'MH 12 AB 5440', 'rachelc').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '13:10:44', '11:51:15', 4596, 4, 3, 'MH 5 AB 6693', 'Akshay').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '17:01:56', '08:27:41', 8369, 4, 2, 'MH 18 AB 7004', 'davidm').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '03:15:03', '06:15:33', 1639, 5, 5, 'MH 12 AB 8578', 'Manish').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '07:26:08', '02:10:51', 4437, 5, 3, 'MH 10 AB 5575', 'johnd').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '23:17:56', '05:49:36', 2316, 3, 4, 'MH 6 AB 5509', 'Ketan').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '06:02:44', '03:25:51', 8635, 1, 2, 'MH 12 AB 7062', 'Ketan').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '04:32:18', '10:41:28', 3218, 1, 4, 'MH 8 AB 8272', 'sarahp').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '15:22:18', '10:33:04', 1717, 2, 4, 'MH 18 AB 7004', 'Manish').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '22:37:31', '13:23:40', 3234, 5, 4, 'MH 11 AB 7989', 'Guarav').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '06:49:07', '09:20:22', 8201, 1, 4, 'MH 14 AB 5997', 'michaelg').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '05:14:00', '02:49:29', 3749, 3, 5, 'MH 13 AB 9993', 'Akshay').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '13:17:16', '09:22:01', 5355, 3, 1, 'MH 8 AB 6980', 'Lokesh').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '10:33:22', '10:29:24', 4771, 3, 2, 'MH 10 AB 5575', 'davidm').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '00:42:45', '20:42:31', 9335, 4, 4, 'MH 5 AB 6693', 'Akshay').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '01:47:27', '17:29:46', 5837, 1, 1, 'MH 12 AB 5440', 'rachelc').createObject() == True
        assert Schedule('2022-12-23', '2022-12-24', '03:59:34', '23:25:51', 3750, 2, 4, 'MH 17 AB 9316', 'Akshay').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '12:23:45', '11:30:03', 1631, 3, 3, 'MH 9 AB 8308', 'Ketan').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '09:14:14', '09:35:54', 5112, 1, 4, 'MH 16 AB 7740', 'michaelg').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '12:51:50', '06:10:48', 4794, 4, 5, 'MH 12 AB 7062', 'katherinet').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '06:58:32', '20:24:30', 2778, 5, 4, 'MH 12 AB 7062', 'Akshay').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '00:11:46', '16:23:03', 7013, 4, 3, 'MH 20 AB 8094', 'Lokesh').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '09:12:23', '05:35:20', 4305, 2, 5, 'MH 14 AB 9684', 'davidm').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '07:26:54', '10:18:57', 2957, 4, 4, 'MH 11 AB 9332', 'Akshay').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '01:32:11', '04:13:42', 5139, 4, 3, 'MH 11 AB 9332', 'matthewr').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '14:43:59', '09:13:06', 7965, 4, 1, 'MH 14 AB 9684', 'matthewr').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '23:29:34', '13:59:30', 8330, 4, 2, 'MH 10 AB 9617', 'jenniferl').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '13:54:19', '20:33:13', 9667, 2, 2, 'MH 8 AB 6980', 'matthewr').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '18:05:25', '15:54:22', 5876, 5, 5, 'MH 13 AB 5137', 'katherinet').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '13:32:11', '15:24:54', 4407, 3, 4, 'MH 9 AB 8308', 'matthewr').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '16:07:02', '11:35:53', 8408, 4, 2, 'MH 19 AB 8198', 'Ketan').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '01:48:21', '21:15:47', 2711, 1, 3, 'MH 8 AB 8272', 'michaelg').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '23:45:13', '07:15:25', 9583, 5, 3, 'MH 12 AB 7062', 'matthewr').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '06:29:20', '14:44:01', 2560, 2, 4, 'MH 19 AB 8932', 'Ketan').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '22:06:15', '14:15:18', 5440, 5, 3, 'MH 9 AB 8308', 'Lokesh').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '12:37:31', '02:09:49', 7483, 1, 3, 'MH 17 AB 8217', 'timothyb').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '20:10:40', '06:05:05', 1231, 4, 1, 'MH 8 AB 8272', 'Guarav').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '04:31:45', '06:17:56', 2325, 3, 4, 'MH 11 AB 9332', 'matthewr').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '18:08:09', '13:54:26', 7267, 1, 2, 'MH 19 AB 9404', 'Manish').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '16:33:06', '09:37:18', 5778, 2, 4, 'MH 10 AB 5575', 'sarahp').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '04:58:47', '17:00:40', 4096, 4, 1, 'MH 12 AB 5440', 'sarahp').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '01:18:25', '04:02:31', 8464, 4, 1, 'MH 11 AB 9332', 'timothyb').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '23:20:16', '22:16:31', 8633, 4, 5, 'MH 11 AB 5703', 'lisaq').createObject() == True
        assert Schedule('2022-12-25', '2022-12-26', '10:37:41', '04:20:04', 3461, 1, 2, 'MH 9 AB 8308', 'michaelg').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '14:52:34', '06:41:54', 8233, 4, 5, 'MH 17 AB 9316', 'michaelg').createObject() == True
        assert Schedule('2022-12-27', '2022-12-28', '17:45:51', '13:26:09', 8215, 5, 1, 'MH 17 AB 9316', 'matthewr').createObject() == True
        assert Schedule('2022-12-26', '2022-12-27', '08:26:32', '10:46:45', 9777, 4, 2, 'MH 17 AB 8217', 'Manish').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '03:50:10', '16:28:35', 8960, 5, 2, 'MH 17 AB 5692', 'matthewr').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '21:33:06', '17:32:17', 3965, 1, 4, 'MH 19 AB 9404', 'Guarav').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '18:24:08', '21:40:38', 6192, 5, 3, 'MH 11 AB 7989', 'katherinet').createObject() == True
        assert Schedule('2022-12-22', '2022-12-23', '10:19:48', '16:21:44', 6327, 4, 2, 'MH 9 AB 8797', 'jenniferl').createObject() == True
        assert Schedule('2022-12-24', '2022-12-25', '18:06:29', '04:11:55', 8067, 4, 5, 'MH 16 AB 7740', 'Guarav').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '14:44:43', '13:54:25', 1764, 5, 5, 'MH 19 AB 5367', 'Manish').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '05:37:17', '00:23:13', 3250, 2, 1, 'MH 10 AB 5575', 'davidm').createObject() == True
        assert Schedule('2022-12-20', '2022-12-21', '08:46:20', '20:44:51', 1302, 2, 1, 'MH 11 AB 7889', 'Manish').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '23:09:04', '02:04:10', 1003, 1, 2, 'MH 17 AB 5692', 'rachelc').createObject() == True
        assert Schedule('2022-12-21', '2022-12-22', '10:32:24', '23:38:53', 1761, 2, 3, 'MH 13 AB 5137', 'Akshay').createObject() == True
        assert Schedule('2022-12-30', '2022-12-31', '16:58:44', '12:27:52', 3144, 4, 2, 'MH 11 AB 7989', 'timothyb').createObject() == True
        assert Schedule('2022-12-29', '2022-12-30', '17:31:01', '09:53:54', 5755, 2, 4, 'MH 11 AB 7889', 'sarahp').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '07:31:22', '11:11:43', 2443, 2, 2, 'MH 8 AB 8272', 'Manish').createObject() == True
        assert Schedule('2022-12-28', '2022-12-29', '09:20:27', '16:02:09', 3227, 1, 4, 'MH 16 AB 7740', 'davidm').createObject() == True


        assert At(1, 18, 1).createObject() == True
        assert At(1, 3, 2).createObject() == True
        assert At(1, 9, 3).createObject() == True
        assert At(1, 20, 4).createObject() == True
        assert At(1, 4, 5).createObject() == True
        assert At(1, 26, 6).createObject() == True
        assert At(1, 16, 7).createObject() == True
        assert At(1, 21, 8).createObject() == True
        assert At(1, 29, 9).createObject() == True
        assert At(2, 23, 1).createObject() == True
        assert At(2, 28, 2).createObject() == True
        assert At(2, 24, 3).createObject() == True
        assert At(2, 2, 4).createObject() == True
        assert At(2, 1, 5).createObject() == True
        assert At(2, 22, 6).createObject() == True
        assert At(3, 21, 1).createObject() == True
        assert At(3, 6, 2).createObject() == True
        assert At(3, 20, 3).createObject() == True
        assert At(3, 14, 4).createObject() == True
        assert At(3, 15, 5).createObject() == True
        assert At(3, 13, 6).createObject() == True
        assert At(3, 24, 7).createObject() == True
        assert At(3, 8, 8).createObject() == True
        assert At(3, 10, 9).createObject() == True
        assert At(3, 16, 10).createObject() == True
        assert At(4, 17, 1).createObject() == True
        assert At(4, 6, 2).createObject() == True
        assert At(4, 2, 3).createObject() == True
        assert At(4, 20, 4).createObject() == True
        assert At(4, 25, 5).createObject() == True
        assert At(4, 23, 6).createObject() == True
        assert At(4, 10, 7).createObject() == True
        assert At(4, 11, 8).createObject() == True
        assert At(4, 27, 9).createObject() == True
        assert At(4, 5, 10).createObject() == True
        assert At(5, 23, 1).createObject() == True
        assert At(5, 29, 2).createObject() == True
        assert At(5, 25, 3).createObject() == True
        assert At(5, 4, 4).createObject() == True
        assert At(5, 15, 5).createObject() == True
        assert At(5, 26, 6).createObject() == True
        assert At(5, 22, 7).createObject() == True
        assert At(5, 13, 8).createObject() == True
        assert At(6, 13, 1).createObject() == True
        assert At(6, 16, 2).createObject() == True
        assert At(6, 23, 3).createObject() == True
        assert At(6, 2, 4).createObject() == True
        assert At(6, 11, 5).createObject() == True
        assert At(7, 6, 1).createObject() == True
        assert At(7, 1, 2).createObject() == True
        assert At(7, 17, 3).createObject() == True
        assert At(7, 18, 4).createObject() == True
        assert At(7, 25, 5).createObject() == True
        assert At(7, 19, 6).createObject() == True
        assert At(7, 29, 7).createObject() == True
        assert At(7, 13, 8).createObject() == True
        assert At(8, 1, 1).createObject() == True
        assert At(8, 5, 2).createObject() == True
        assert At(8, 21, 3).createObject() == True
        assert At(8, 28, 4).createObject() == True
        assert At(8, 24, 5).createObject() == True
        assert At(9, 24, 1).createObject() == True
        assert At(9, 27, 2).createObject() == True
        assert At(9, 16, 3).createObject() == True
        assert At(9, 22, 4).createObject() == True
        assert At(9, 28, 5).createObject() == True
        assert At(10, 22, 1).createObject() == True
        assert At(10, 6, 2).createObject() == True
        assert At(10, 8, 3).createObject() == True
        assert At(10, 17, 4).createObject() == True
        assert At(10, 4, 5).createObject() == True
        assert At(10, 24, 6).createObject() == True
        assert At(10, 26, 7).createObject() == True
        assert At(11, 29, 1).createObject() == True
        assert At(11, 23, 2).createObject() == True
        assert At(11, 12, 3).createObject() == True
        assert At(11, 15, 4).createObject() == True
        assert At(11, 8, 5).createObject() == True
        assert At(12, 7, 1).createObject() == True
        assert At(12, 26, 2).createObject() == True
        assert At(12, 25, 3).createObject() == True
        assert At(12, 21, 4).createObject() == True
        assert At(12, 10, 5).createObject() == True
        assert At(13, 21, 1).createObject() == True
        assert At(13, 8, 2).createObject() == True
        assert At(13, 22, 3).createObject() == True
        assert At(13, 13, 4).createObject() == True
        assert At(13, 12, 5).createObject() == True
        assert At(13, 10, 6).createObject() == True
        assert At(13, 16, 7).createObject() == True
        assert At(13, 7, 8).createObject() == True
        assert At(13, 14, 9).createObject() == True
        assert At(13, 4, 10).createObject() == True
        assert At(14, 23, 1).createObject() == True
        assert At(14, 10, 2).createObject() == True
        assert At(14, 27, 3).createObject() == True
        assert At(14, 21, 4).createObject() == True
        assert At(14, 25, 5).createObject() == True
        assert At(14, 5, 6).createObject() == True
        assert At(15, 16, 1).createObject() == True
        assert At(15, 7, 2).createObject() == True
        assert At(15, 26, 3).createObject() == True
        assert At(15, 19, 4).createObject() == True
        assert At(15, 5, 5).createObject() == True
        assert At(16, 18, 1).createObject() == True
        assert At(16, 1, 2).createObject() == True
        assert At(16, 22, 3).createObject() == True
        assert At(16, 20, 4).createObject() == True
        assert At(16, 10, 5).createObject() == True
        assert At(16, 28, 6).createObject() == True
        assert At(17, 17, 1).createObject() == True
        assert At(17, 19, 2).createObject() == True
        assert At(17, 25, 3).createObject() == True
        assert At(17, 9, 4).createObject() == True
        assert At(17, 3, 5).createObject() == True
        assert At(18, 19, 1).createObject() == True
        assert At(18, 16, 2).createObject() == True
        assert At(18, 1, 3).createObject() == True
        assert At(18, 23, 4).createObject() == True
        assert At(18, 10, 5).createObject() == True
        assert At(18, 29, 6).createObject() == True
        assert At(18, 8, 7).createObject() == True
        assert At(18, 15, 8).createObject() == True
        assert At(18, 4, 9).createObject() == True
        assert At(19, 1, 1).createObject() == True
        assert At(19, 27, 2).createObject() == True
        assert At(19, 21, 3).createObject() == True
        assert At(19, 16, 4).createObject() == True
        assert At(19, 5, 5).createObject() == True
        assert At(19, 20, 6).createObject() == True
        assert At(19, 19, 7).createObject() == True
        assert At(19, 18, 8).createObject() == True
        assert At(19, 4, 9).createObject() == True
        assert At(20, 8, 1).createObject() == True
        assert At(20, 10, 2).createObject() == True
        assert At(20, 5, 3).createObject() == True
        assert At(20, 29, 4).createObject() == True
        assert At(20, 4, 5).createObject() == True
        assert At(20, 3, 6).createObject() == True
        assert At(20, 11, 7).createObject() == True
        assert At(20, 12, 8).createObject() == True
        assert At(21, 22, 1).createObject() == True
        assert At(21, 25, 2).createObject() == True
        assert At(21, 21, 3).createObject() == True
        assert At(21, 1, 4).createObject() == True
        assert At(21, 26, 5).createObject() == True
        assert At(21, 24, 6).createObject() == True
        assert At(21, 10, 7).createObject() == True
        assert At(21, 6, 8).createObject() == True
        assert At(22, 6, 1).createObject() == True
        assert At(22, 21, 2).createObject() == True
        assert At(22, 12, 3).createObject() == True
        assert At(22, 5, 4).createObject() == True
        assert At(22, 25, 5).createObject() == True
        assert At(22, 8, 6).createObject() == True
        assert At(22, 29, 7).createObject() == True
        assert At(22, 14, 8).createObject() == True
        assert At(22, 18, 9).createObject() == True
        assert At(22, 20, 10).createObject() == True
        assert At(23, 2, 1).createObject() == True
        assert At(23, 4, 2).createObject() == True
        assert At(23, 20, 3).createObject() == True
        assert At(23, 29, 4).createObject() == True
        assert At(23, 24, 5).createObject() == True
        assert At(23, 6, 6).createObject() == True
        assert At(23, 21, 7).createObject() == True
        assert At(24, 20, 1).createObject() == True
        assert At(24, 28, 2).createObject() == True
        assert At(24, 18, 3).createObject() == True
        assert At(24, 17, 4).createObject() == True
        assert At(24, 10, 5).createObject() == True
        assert At(24, 6, 6).createObject() == True
        assert At(24, 12, 7).createObject() == True
        assert At(24, 7, 8).createObject() == True
        assert At(24, 19, 9).createObject() == True
        assert At(24, 25, 10).createObject() == True
        assert At(25, 9, 1).createObject() == True
        assert At(25, 8, 2).createObject() == True
        assert At(25, 23, 3).createObject() == True
        assert At(25, 6, 4).createObject() == True
        assert At(25, 16, 5).createObject() == True
        assert At(26, 1, 1).createObject() == True
        assert At(26, 9, 2).createObject() == True
        assert At(26, 17, 3).createObject() == True
        assert At(26, 3, 4).createObject() == True
        assert At(26, 2, 5).createObject() == True
        assert At(26, 18, 6).createObject() == True
        assert At(26, 19, 7).createObject() == True
        assert At(26, 7, 8).createObject() == True
        assert At(26, 11, 9).createObject() == True
        assert At(27, 5, 1).createObject() == True
        assert At(27, 1, 2).createObject() == True
        assert At(27, 28, 3).createObject() == True
        assert At(27, 27, 4).createObject() == True
        assert At(27, 8, 5).createObject() == True
        assert At(28, 23, 1).createObject() == True
        assert At(28, 15, 2).createObject() == True
        assert At(28, 21, 3).createObject() == True
        assert At(28, 10, 4).createObject() == True
        assert At(28, 9, 5).createObject() == True
        assert At(29, 18, 1).createObject() == True
        assert At(29, 17, 2).createObject() == True
        assert At(29, 24, 3).createObject() == True
        assert At(29, 29, 4).createObject() == True
        assert At(29, 4, 5).createObject() == True
        assert At(29, 9, 6).createObject() == True
        assert At(29, 23, 7).createObject() == True
        assert At(30, 20, 1).createObject() == True
        assert At(30, 9, 2).createObject() == True
        assert At(30, 7, 3).createObject() == True
        assert At(30, 25, 4).createObject() == True
        assert At(30, 27, 5).createObject() == True
        assert At(30, 28, 6).createObject() == True
        assert At(30, 22, 7).createObject() == True
        assert At(31, 4, 1).createObject() == True
        assert At(31, 7, 2).createObject() == True
        assert At(31, 9, 3).createObject() == True
        assert At(31, 16, 4).createObject() == True
        assert At(31, 28, 5).createObject() == True
        assert At(32, 15, 1).createObject() == True
        assert At(32, 13, 2).createObject() == True
        assert At(32, 7, 3).createObject() == True
        assert At(32, 29, 4).createObject() == True
        assert At(32, 25, 5).createObject() == True
        assert At(32, 22, 6).createObject() == True
        assert At(32, 24, 7).createObject() == True
        assert At(32, 18, 8).createObject() == True
        assert At(32, 28, 9).createObject() == True
        assert At(33, 12, 1).createObject() == True
        assert At(33, 7, 2).createObject() == True
        assert At(33, 9, 3).createObject() == True
        assert At(33, 21, 4).createObject() == True
        assert At(33, 27, 5).createObject() == True
        assert At(33, 16, 6).createObject() == True
        assert At(33, 1, 7).createObject() == True
        assert At(33, 24, 8).createObject() == True
        assert At(33, 4, 9).createObject() == True
        assert At(34, 19, 1).createObject() == True
        assert At(34, 11, 2).createObject() == True
        assert At(34, 14, 3).createObject() == True
        assert At(34, 26, 4).createObject() == True
        assert At(34, 16, 5).createObject() == True
        assert At(34, 1, 6).createObject() == True
        assert At(35, 28, 1).createObject() == True
        assert At(35, 8, 2).createObject() == True
        assert At(35, 11, 3).createObject() == True
        assert At(35, 26, 4).createObject() == True
        assert At(35, 15, 5).createObject() == True
        assert At(35, 24, 6).createObject() == True
        assert At(35, 16, 7).createObject() == True
        assert At(35, 1, 8).createObject() == True
        assert At(35, 14, 9).createObject() == True
        assert At(36, 14, 1).createObject() == True
        assert At(36, 7, 2).createObject() == True
        assert At(36, 11, 3).createObject() == True
        assert At(36, 20, 4).createObject() == True
        assert At(36, 29, 5).createObject() == True
        assert At(36, 1, 6).createObject() == True
        assert At(36, 9, 7).createObject() == True
        assert At(37, 6, 1).createObject() == True
        assert At(37, 16, 2).createObject() == True
        assert At(37, 14, 3).createObject() == True
        assert At(37, 23, 4).createObject() == True
        assert At(37, 4, 5).createObject() == True
        assert At(37, 26, 6).createObject() == True
        assert At(37, 9, 7).createObject() == True
        assert At(37, 10, 8).createObject() == True
        assert At(38, 10, 1).createObject() == True
        assert At(38, 1, 2).createObject() == True
        assert At(38, 17, 3).createObject() == True
        assert At(38, 7, 4).createObject() == True
        assert At(38, 24, 5).createObject() == True
        assert At(39, 20, 1).createObject() == True
        assert At(39, 16, 2).createObject() == True
        assert At(39, 4, 3).createObject() == True
        assert At(39, 27, 4).createObject() == True
        assert At(39, 1, 5).createObject() == True
        assert At(39, 19, 6).createObject() == True
        assert At(40, 2, 1).createObject() == True
        assert At(40, 29, 2).createObject() == True
        assert At(40, 18, 3).createObject() == True
        assert At(40, 20, 4).createObject() == True
        assert At(40, 11, 5).createObject() == True
        assert At(40, 24, 6).createObject() == True
        assert At(40, 8, 7).createObject() == True
        assert At(40, 14, 8).createObject() == True
        assert At(40, 9, 9).createObject() == True
        assert At(40, 19, 10).createObject() == True
        assert At(41, 8, 1).createObject() == True
        assert At(41, 29, 2).createObject() == True
        assert At(41, 14, 3).createObject() == True
        assert At(41, 25, 4).createObject() == True
        assert At(41, 3, 5).createObject() == True
        assert At(42, 6, 1).createObject() == True
        assert At(42, 5, 2).createObject() == True
        assert At(42, 7, 3).createObject() == True
        assert At(42, 21, 4).createObject() == True
        assert At(42, 1, 5).createObject() == True
        assert At(42, 20, 6).createObject() == True
        assert At(42, 10, 7).createObject() == True
        assert At(42, 29, 8).createObject() == True
        assert At(42, 9, 9).createObject() == True
        assert At(43, 9, 1).createObject() == True
        assert At(43, 29, 2).createObject() == True
        assert At(43, 6, 3).createObject() == True
        assert At(43, 13, 4).createObject() == True
        assert At(43, 10, 5).createObject() == True
        assert At(43, 25, 6).createObject() == True
        assert At(43, 23, 7).createObject() == True
        assert At(43, 15, 8).createObject() == True
        assert At(43, 1, 9).createObject() == True
        assert At(43, 5, 10).createObject() == True
        assert At(44, 13, 1).createObject() == True
        assert At(44, 26, 2).createObject() == True
        assert At(44, 8, 3).createObject() == True
        assert At(44, 7, 4).createObject() == True
        assert At(44, 6, 5).createObject() == True
        assert At(44, 11, 6).createObject() == True
        assert At(44, 12, 7).createObject() == True
        assert At(44, 14, 8).createObject() == True
        assert At(44, 19, 9).createObject() == True
        assert At(44, 4, 10).createObject() == True
        assert At(45, 12, 1).createObject() == True
        assert At(45, 20, 2).createObject() == True
        assert At(45, 6, 3).createObject() == True
        assert At(45, 1, 4).createObject() == True
        assert At(45, 26, 5).createObject() == True
        assert At(45, 13, 6).createObject() == True
        assert At(45, 7, 7).createObject() == True
        assert At(45, 24, 8).createObject() == True
        assert At(46, 14, 1).createObject() == True
        assert At(46, 26, 2).createObject() == True
        assert At(46, 6, 3).createObject() == True
        assert At(46, 27, 4).createObject() == True
        assert At(46, 28, 5).createObject() == True
        assert At(46, 3, 6).createObject() == True
        assert At(47, 4, 1).createObject() == True
        assert At(47, 17, 2).createObject() == True
        assert At(47, 7, 3).createObject() == True
        assert At(47, 23, 4).createObject() == True
        assert At(47, 8, 5).createObject() == True
        assert At(47, 27, 6).createObject() == True
        assert At(47, 19, 7).createObject() == True
        assert At(47, 9, 8).createObject() == True
        assert At(47, 5, 9).createObject() == True
        assert At(48, 10, 1).createObject() == True
        assert At(48, 29, 2).createObject() == True
        assert At(48, 28, 3).createObject() == True
        assert At(48, 23, 4).createObject() == True
        assert At(48, 9, 5).createObject() == True
        assert At(48, 16, 6).createObject() == True
        assert At(48, 3, 7).createObject() == True
        assert At(49, 14, 1).createObject() == True
        assert At(49, 23, 2).createObject() == True
        assert At(49, 3, 3).createObject() == True
        assert At(49, 22, 4).createObject() == True
        assert At(49, 28, 5).createObject() == True
        assert At(50, 11, 1).createObject() == True
        assert At(50, 9, 2).createObject() == True
        assert At(50, 4, 3).createObject() == True
        assert At(50, 23, 4).createObject() == True
        assert At(50, 12, 5).createObject() == True
        assert At(50, 10, 6).createObject() == True
        assert At(50, 7, 7).createObject() == True
        assert At(50, 21, 8).createObject() == True
        assert At(50, 13, 9).createObject() == True
        assert At(51, 2, 1).createObject() == True
        assert At(51, 5, 2).createObject() == True
        assert At(51, 16, 3).createObject() == True
        assert At(51, 4, 4).createObject() == True
        assert At(51, 23, 5).createObject() == True
        assert At(51, 26, 6).createObject() == True
        assert At(51, 8, 7).createObject() == True
        assert At(51, 19, 8).createObject() == True
        assert At(52, 9, 1).createObject() == True
        assert At(52, 6, 2).createObject() == True
        assert At(52, 7, 3).createObject() == True
        assert At(52, 27, 4).createObject() == True
        assert At(52, 2, 5).createObject() == True
        assert At(52, 10, 6).createObject() == True
        assert At(52, 11, 7).createObject() == True
        assert At(53, 12, 1).createObject() == True
        assert At(53, 13, 2).createObject() == True
        assert At(53, 28, 3).createObject() == True
        assert At(53, 8, 4).createObject() == True
        assert At(53, 3, 5).createObject() == True
        assert At(53, 15, 6).createObject() == True
        assert At(53, 11, 7).createObject() == True
        assert At(54, 29, 1).createObject() == True
        assert At(54, 17, 2).createObject() == True
        assert At(54, 3, 3).createObject() == True
        assert At(54, 7, 4).createObject() == True
        assert At(54, 16, 5).createObject() == True
        assert At(54, 12, 6).createObject() == True
        assert At(54, 13, 7).createObject() == True
        assert At(54, 21, 8).createObject() == True
        assert At(55, 27, 1).createObject() == True
        assert At(55, 12, 2).createObject() == True
        assert At(55, 15, 3).createObject() == True
        assert At(55, 1, 4).createObject() == True
        assert At(55, 22, 5).createObject() == True
        assert At(56, 24, 1).createObject() == True
        assert At(56, 6, 2).createObject() == True
        assert At(56, 25, 3).createObject() == True
        assert At(56, 18, 4).createObject() == True
        assert At(56, 8, 5).createObject() == True
        assert At(56, 4, 6).createObject() == True
        assert At(56, 9, 7).createObject() == True
        assert At(56, 14, 8).createObject() == True
        assert At(56, 19, 9).createObject() == True
        assert At(57, 16, 1).createObject() == True
        assert At(57, 20, 2).createObject() == True
        assert At(57, 26, 3).createObject() == True
        assert At(57, 22, 4).createObject() == True
        assert At(57, 27, 5).createObject() == True
        assert At(57, 1, 6).createObject() == True
        assert At(58, 22, 1).createObject() == True
        assert At(58, 4, 2).createObject() == True
        assert At(58, 21, 3).createObject() == True
        assert At(58, 9, 4).createObject() == True
        assert At(58, 15, 5).createObject() == True
        assert At(58, 26, 6).createObject() == True
        assert At(58, 18, 7).createObject() == True
        assert At(58, 8, 8).createObject() == True
        assert At(58, 25, 9).createObject() == True
        assert At(59, 24, 1).createObject() == True
        assert At(59, 20, 2).createObject() == True
        assert At(59, 16, 3).createObject() == True
        assert At(59, 10, 4).createObject() == True
        assert At(59, 8, 5).createObject() == True
        assert At(59, 5, 6).createObject() == True
        assert At(59, 25, 7).createObject() == True
        assert At(60, 7, 1).createObject() == True
        assert At(60, 4, 2).createObject() == True
        assert At(60, 9, 3).createObject() == True
        assert At(60, 18, 4).createObject() == True
        assert At(60, 13, 5).createObject() == True
        assert At(60, 17, 6).createObject() == True
        assert At(60, 29, 7).createObject() == True
        assert At(61, 3, 1).createObject() == True
        assert At(61, 9, 2).createObject() == True
        assert At(61, 13, 3).createObject() == True
        assert At(61, 12, 4).createObject() == True
        assert At(61, 17, 5).createObject() == True
        assert At(62, 13, 1).createObject() == True
        assert At(62, 28, 2).createObject() == True
        assert At(62, 12, 3).createObject() == True
        assert At(62, 8, 4).createObject() == True
        assert At(62, 25, 5).createObject() == True
        assert At(62, 27, 6).createObject() == True
        assert At(62, 11, 7).createObject() == True
        assert At(62, 16, 8).createObject() == True
        assert At(63, 28, 1).createObject() == True
        assert At(63, 15, 2).createObject() == True
        assert At(63, 12, 3).createObject() == True
        assert At(63, 8, 4).createObject() == True
        assert At(63, 25, 5).createObject() == True
        assert At(63, 2, 6).createObject() == True
        assert At(63, 5, 7).createObject() == True
        assert At(63, 20, 8).createObject() == True
        assert At(63, 1, 9).createObject() == True
        assert At(63, 26, 10).createObject() == True
        assert At(64, 17, 1).createObject() == True
        assert At(64, 4, 2).createObject() == True
        assert At(64, 15, 3).createObject() == True
        assert At(64, 29, 4).createObject() == True
        assert At(64, 24, 5).createObject() == True
        assert At(64, 27, 6).createObject() == True
        assert At(64, 8, 7).createObject() == True
        assert At(64, 28, 8).createObject() == True
        assert At(64, 19, 9).createObject() == True
        assert At(65, 9, 1).createObject() == True
        assert At(65, 22, 2).createObject() == True
        assert At(65, 3, 3).createObject() == True
        assert At(65, 16, 4).createObject() == True
        assert At(65, 7, 5).createObject() == True
        assert At(65, 21, 6).createObject() == True
        assert At(65, 24, 7).createObject() == True
        assert At(65, 11, 8).createObject() == True
        assert At(66, 2, 1).createObject() == True
        assert At(66, 29, 2).createObject() == True
        assert At(66, 25, 3).createObject() == True
        assert At(66, 9, 4).createObject() == True
        assert At(66, 16, 5).createObject() == True
        assert At(66, 14, 6).createObject() == True
        assert At(66, 22, 7).createObject() == True
        assert At(66, 6, 8).createObject() == True
        assert At(66, 19, 9).createObject() == True
        assert At(66, 26, 10).createObject() == True
        assert At(67, 28, 1).createObject() == True
        assert At(67, 26, 2).createObject() == True
        assert At(67, 8, 3).createObject() == True
        assert At(67, 23, 4).createObject() == True
        assert At(67, 21, 5).createObject() == True
        assert At(67, 22, 6).createObject() == True
        assert At(67, 2, 7).createObject() == True
        assert At(67, 17, 8).createObject() == True
        assert At(68, 14, 1).createObject() == True
        assert At(68, 16, 2).createObject() == True
        assert At(68, 24, 3).createObject() == True
        assert At(68, 6, 4).createObject() == True
        assert At(68, 4, 5).createObject() == True
        assert At(68, 21, 6).createObject() == True
        assert At(68, 5, 7).createObject() == True
        assert At(68, 7, 8).createObject() == True
        assert At(69, 22, 1).createObject() == True
        assert At(69, 8, 2).createObject() == True
        assert At(69, 10, 3).createObject() == True
        assert At(69, 27, 4).createObject() == True
        assert At(69, 15, 5).createObject() == True
        assert At(69, 29, 6).createObject() == True
        assert At(70, 4, 1).createObject() == True
        assert At(70, 6, 2).createObject() == True
        assert At(70, 25, 3).createObject() == True
        assert At(70, 9, 4).createObject() == True
        assert At(70, 24, 5).createObject() == True
        assert At(70, 29, 6).createObject() == True
        assert At(70, 18, 7).createObject() == True
        assert At(70, 12, 8).createObject() == True
        assert At(70, 1, 9).createObject() == True
        assert At(71, 18, 1).createObject() == True
        assert At(71, 20, 2).createObject() == True
        assert At(71, 26, 3).createObject() == True
        assert At(71, 15, 4).createObject() == True
        assert At(71, 9, 5).createObject() == True
        assert At(71, 2, 6).createObject() == True
        assert At(71, 5, 7).createObject() == True
        assert At(71, 1, 8).createObject() == True
        assert At(71, 19, 9).createObject() == True
        assert At(71, 25, 10).createObject() == True
        assert At(72, 21, 1).createObject() == True
        assert At(72, 7, 2).createObject() == True
        assert At(72, 3, 3).createObject() == True
        assert At(72, 10, 4).createObject() == True
        assert At(72, 24, 5).createObject() == True
        assert At(72, 14, 6).createObject() == True
        assert At(72, 4, 7).createObject() == True
        assert At(72, 5, 8).createObject() == True
        assert At(72, 20, 9).createObject() == True
        assert At(73, 16, 1).createObject() == True
        assert At(73, 18, 2).createObject() == True
        assert At(73, 13, 3).createObject() == True
        assert At(73, 11, 4).createObject() == True
        assert At(73, 27, 5).createObject() == True
        assert At(73, 26, 6).createObject() == True
        assert At(73, 8, 7).createObject() == True
        assert At(74, 28, 1).createObject() == True
        assert At(74, 23, 2).createObject() == True
        assert At(74, 16, 3).createObject() == True
        assert At(74, 4, 4).createObject() == True
        assert At(74, 5, 5).createObject() == True
        assert At(75, 7, 1).createObject() == True
        assert At(75, 24, 2).createObject() == True
        assert At(75, 28, 3).createObject() == True
        assert At(75, 18, 4).createObject() == True
        assert At(75, 23, 5).createObject() == True
        assert At(75, 2, 6).createObject() == True
        assert At(76, 26, 1).createObject() == True
        assert At(76, 6, 2).createObject() == True
        assert At(76, 1, 3).createObject() == True
        assert At(76, 19, 4).createObject() == True
        assert At(76, 5, 5).createObject() == True
        assert At(77, 15, 1).createObject() == True
        assert At(77, 27, 2).createObject() == True
        assert At(77, 23, 3).createObject() == True
        assert At(77, 19, 4).createObject() == True
        assert At(77, 7, 5).createObject() == True
        assert At(78, 10, 1).createObject() == True
        assert At(78, 12, 2).createObject() == True
        assert At(78, 9, 3).createObject() == True
        assert At(78, 2, 4).createObject() == True
        assert At(78, 1, 5).createObject() == True
        assert At(78, 24, 6).createObject() == True
        assert At(78, 23, 7).createObject() == True
        assert At(78, 16, 8).createObject() == True
        assert At(79, 4, 1).createObject() == True
        assert At(79, 1, 2).createObject() == True
        assert At(79, 12, 3).createObject() == True
        assert At(79, 16, 4).createObject() == True
        assert At(79, 22, 5).createObject() == True
        assert At(80, 18, 1).createObject() == True
        assert At(80, 3, 2).createObject() == True
        assert At(80, 29, 3).createObject() == True
        assert At(80, 24, 4).createObject() == True
        assert At(80, 21, 5).createObject() == True
        assert At(80, 9, 6).createObject() == True
        assert At(81, 8, 1).createObject() == True
        assert At(81, 19, 2).createObject() == True
        assert At(81, 9, 3).createObject() == True
        assert At(81, 7, 4).createObject() == True
        assert At(81, 1, 5).createObject() == True
        assert At(82, 28, 1).createObject() == True
        assert At(82, 22, 2).createObject() == True
        assert At(82, 20, 3).createObject() == True
        assert At(82, 12, 4).createObject() == True
        assert At(82, 13, 5).createObject() == True
        assert At(82, 5, 6).createObject() == True
        assert At(82, 16, 7).createObject() == True
        assert At(82, 26, 8).createObject() == True
        assert At(83, 19, 1).createObject() == True
        assert At(83, 14, 2).createObject() == True
        assert At(83, 7, 3).createObject() == True
        assert At(83, 18, 4).createObject() == True
        assert At(83, 15, 5).createObject() == True
        assert At(83, 16, 6).createObject() == True
        assert At(83, 1, 7).createObject() == True
        assert At(83, 6, 8).createObject() == True
        assert At(83, 17, 9).createObject() == True
        assert At(84, 16, 1).createObject() == True
        assert At(84, 13, 2).createObject() == True
        assert At(84, 17, 3).createObject() == True
        assert At(84, 9, 4).createObject() == True
        assert At(84, 23, 5).createObject() == True
        assert At(84, 25, 6).createObject() == True
        assert At(84, 27, 7).createObject() == True
        assert At(84, 18, 8).createObject() == True
        assert At(84, 15, 9).createObject() == True
        assert At(85, 28, 1).createObject() == True
        assert At(85, 18, 2).createObject() == True
        assert At(85, 15, 3).createObject() == True
        assert At(85, 14, 4).createObject() == True
        assert At(85, 3, 5).createObject() == True
        assert At(85, 8, 6).createObject() == True
        assert At(85, 12, 7).createObject() == True
        assert At(86, 6, 1).createObject() == True
        assert At(86, 19, 2).createObject() == True
        assert At(86, 12, 3).createObject() == True
        assert At(86, 8, 4).createObject() == True
        assert At(86, 2, 5).createObject() == True
        assert At(86, 29, 6).createObject() == True
        assert At(86, 16, 7).createObject() == True
        assert At(86, 17, 8).createObject() == True
        assert At(86, 4, 9).createObject() == True
        assert At(87, 20, 1).createObject() == True
        assert At(87, 4, 2).createObject() == True
        assert At(87, 13, 3).createObject() == True
        assert At(87, 18, 4).createObject() == True
        assert At(87, 11, 5).createObject() == True
        assert At(87, 27, 6).createObject() == True
        assert At(87, 15, 7).createObject() == True
        assert At(87, 25, 8).createObject() == True
        assert At(87, 17, 9).createObject() == True
        assert At(88, 5, 1).createObject() == True
        assert At(88, 2, 2).createObject() == True
        assert At(88, 1, 3).createObject() == True
        assert At(88, 8, 4).createObject() == True
        assert At(88, 4, 5).createObject() == True
        assert At(89, 27, 1).createObject() == True
        assert At(89, 4, 2).createObject() == True
        assert At(89, 25, 3).createObject() == True
        assert At(89, 24, 4).createObject() == True
        assert At(89, 16, 5).createObject() == True
        assert At(89, 9, 6).createObject() == True
        assert At(89, 15, 7).createObject() == True
        assert At(89, 3, 8).createObject() == True
        assert At(89, 7, 9).createObject() == True
        assert At(90, 7, 1).createObject() == True
        assert At(90, 14, 2).createObject() == True
        assert At(90, 2, 3).createObject() == True
        assert At(90, 27, 4).createObject() == True
        assert At(90, 22, 5).createObject() == True
        assert At(90, 29, 6).createObject() == True
        assert At(91, 2, 1).createObject() == True
        assert At(91, 9, 2).createObject() == True
        assert At(91, 17, 3).createObject() == True
        assert At(91, 18, 4).createObject() == True
        assert At(91, 23, 5).createObject() == True
        assert At(91, 29, 6).createObject() == True
        assert At(91, 10, 7).createObject() == True
        assert At(92, 21, 1).createObject() == True
        assert At(92, 24, 2).createObject() == True
        assert At(92, 12, 3).createObject() == True
        assert At(92, 7, 4).createObject() == True
        assert At(92, 18, 5).createObject() == True
        assert At(92, 4, 6).createObject() == True
        assert At(93, 22, 1).createObject() == True
        assert At(93, 13, 2).createObject() == True
        assert At(93, 10, 3).createObject() == True
        assert At(93, 7, 4).createObject() == True
        assert At(93, 21, 5).createObject() == True
        assert At(93, 26, 6).createObject() == True
        assert At(93, 18, 7).createObject() == True
        assert At(93, 23, 8).createObject() == True
        assert At(93, 15, 9).createObject() == True
        assert At(93, 12, 10).createObject() == True
        assert At(94, 10, 1).createObject() == True
        assert At(94, 11, 2).createObject() == True
        assert At(94, 3, 3).createObject() == True
        assert At(94, 26, 4).createObject() == True
        assert At(94, 7, 5).createObject() == True
        assert At(94, 29, 6).createObject() == True
        assert At(94, 20, 7).createObject() == True
        assert At(94, 18, 8).createObject() == True
        assert At(94, 8, 9).createObject() == True
        assert At(94, 2, 10).createObject() == True
        assert At(95, 6, 1).createObject() == True
        assert At(95, 1, 2).createObject() == True
        assert At(95, 22, 3).createObject() == True
        assert At(95, 4, 4).createObject() == True
        assert At(95, 8, 5).createObject() == True
        assert At(95, 26, 6).createObject() == True
        assert At(95, 14, 7).createObject() == True
        assert At(95, 29, 8).createObject() == True
        assert At(95, 25, 9).createObject() == True
        assert At(96, 21, 1).createObject() == True
        assert At(96, 13, 2).createObject() == True
        assert At(96, 20, 3).createObject() == True
        assert At(96, 27, 4).createObject() == True
        assert At(96, 11, 5).createObject() == True
        assert At(96, 14, 6).createObject() == True
        assert At(97, 16, 1).createObject() == True
        assert At(97, 25, 2).createObject() == True
        assert At(97, 20, 3).createObject() == True
        assert At(97, 6, 4).createObject() == True
        assert At(97, 13, 5).createObject() == True
        assert At(97, 24, 6).createObject() == True
        assert At(98, 29, 1).createObject() == True
        assert At(98, 21, 2).createObject() == True
        assert At(98, 19, 3).createObject() == True
        assert At(98, 5, 4).createObject() == True
        assert At(98, 22, 5).createObject() == True
        assert At(98, 28, 6).createObject() == True
        assert At(98, 23, 7).createObject() == True
        assert At(98, 14, 8).createObject() == True
        assert At(99, 6, 1).createObject() == True
        assert At(99, 11, 2).createObject() == True
        assert At(99, 15, 3).createObject() == True
        assert At(99, 25, 4).createObject() == True
        assert At(99, 12, 5).createObject() == True
        assert At(99, 26, 6).createObject() == True
        assert At(99, 21, 7).createObject() == True
        assert At(100, 8, 1).createObject() == True
        assert At(100, 27, 2).createObject() == True
        assert At(100, 1, 3).createObject() == True
        assert At(100, 13, 4).createObject() == True
        assert At(100, 29, 5).createObject() == True
        assert At(100, 7, 6).createObject() == True
        assert At(101, 10, 1).createObject() == True
        assert At(101, 8, 2).createObject() == True
        assert At(101, 3, 3).createObject() == True
        assert At(101, 15, 4).createObject() == True
        assert At(101, 16, 5).createObject() == True
        assert At(101, 27, 6).createObject() == True
        assert At(101, 14, 7).createObject() == True
        assert At(101, 2, 8).createObject() == True
        assert At(102, 13, 1).createObject() == True
        assert At(102, 24, 2).createObject() == True
        assert At(102, 8, 3).createObject() == True
        assert At(102, 22, 4).createObject() == True
        assert At(102, 23, 5).createObject() == True
        assert At(103, 2, 1).createObject() == True
        assert At(103, 5, 2).createObject() == True
        assert At(103, 8, 3).createObject() == True
        assert At(103, 13, 4).createObject() == True
        assert At(103, 9, 5).createObject() == True
        assert At(103, 4, 6).createObject() == True
        assert At(104, 5, 1).createObject() == True
        assert At(104, 15, 2).createObject() == True
        assert At(104, 10, 3).createObject() == True
        assert At(104, 8, 4).createObject() == True
        assert At(104, 27, 5).createObject() == True
        assert At(104, 21, 6).createObject() == True
        assert At(104, 25, 7).createObject() == True
        assert At(104, 2, 8).createObject() == True
        assert At(104, 1, 9).createObject() == True
        assert At(104, 22, 10).createObject() == True
        assert At(105, 29, 1).createObject() == True
        assert At(105, 2, 2).createObject() == True
        assert At(105, 27, 3).createObject() == True
        assert At(105, 24, 4).createObject() == True
        assert At(105, 10, 5).createObject() == True
        assert At(105, 4, 6).createObject() == True
        assert At(105, 17, 7).createObject() == True
        assert At(106, 10, 1).createObject() == True
        assert At(106, 21, 2).createObject() == True
        assert At(106, 2, 3).createObject() == True
        assert At(106, 27, 4).createObject() == True
        assert At(106, 9, 5).createObject() == True
        assert At(106, 26, 6).createObject() == True
        assert At(107, 8, 1).createObject() == True
        assert At(107, 23, 2).createObject() == True
        assert At(107, 20, 3).createObject() == True
        assert At(107, 7, 4).createObject() == True
        assert At(107, 24, 5).createObject() == True
        assert At(107, 6, 6).createObject() == True
        assert At(107, 19, 7).createObject() == True
        assert At(107, 21, 8).createObject() == True
        assert At(107, 18, 9).createObject() == True
        assert At(108, 27, 1).createObject() == True
        assert At(108, 10, 2).createObject() == True
        assert At(108, 23, 3).createObject() == True
        assert At(108, 29, 4).createObject() == True
        assert At(108, 26, 5).createObject() == True
        assert At(108, 5, 6).createObject() == True
        assert At(108, 21, 7).createObject() == True
        assert At(108, 15, 8).createObject() == True
        assert At(108, 17, 9).createObject() == True
        assert At(108, 3, 10).createObject() == True
        assert At(109, 24, 1).createObject() == True
        assert At(109, 20, 2).createObject() == True
        assert At(109, 12, 3).createObject() == True
        assert At(109, 6, 4).createObject() == True
        assert At(109, 9, 5).createObject() == True
        assert At(109, 17, 6).createObject() == True
        assert At(109, 16, 7).createObject() == True
        assert At(109, 28, 8).createObject() == True
        assert At(109, 22, 9).createObject() == True
        assert At(110, 21, 1).createObject() == True
        assert At(110, 6, 2).createObject() == True
        assert At(110, 8, 3).createObject() == True
        assert At(110, 14, 4).createObject() == True
        assert At(110, 7, 5).createObject() == True
        assert At(110, 25, 6).createObject() == True
        assert At(110, 5, 7).createObject() == True
        assert At(110, 13, 8).createObject() == True
        assert At(110, 16, 9).createObject() == True
        assert At(110, 20, 10).createObject() == True
        assert At(111, 6, 1).createObject() == True
        assert At(111, 18, 2).createObject() == True
        assert At(111, 15, 3).createObject() == True
        assert At(111, 5, 4).createObject() == True
        assert At(111, 10, 5).createObject() == True
        assert At(111, 9, 6).createObject() == True
        assert At(111, 8, 7).createObject() == True
        assert At(111, 1, 8).createObject() == True
        assert At(112, 1, 1).createObject() == True
        assert At(112, 14, 2).createObject() == True
        assert At(112, 18, 3).createObject() == True
        assert At(112, 10, 4).createObject() == True
        assert At(112, 19, 5).createObject() == True
        assert At(112, 24, 6).createObject() == True
        assert At(112, 23, 7).createObject() == True
        assert At(112, 3, 8).createObject() == True
        assert At(113, 7, 1).createObject() == True
        assert At(113, 28, 2).createObject() == True
        assert At(113, 8, 3).createObject() == True
        assert At(113, 12, 4).createObject() == True
        assert At(113, 19, 5).createObject() == True
        assert At(113, 18, 6).createObject() == True
        assert At(113, 4, 7).createObject() == True
        assert At(113, 21, 8).createObject() == True
        assert At(113, 22, 9).createObject() == True
        assert At(113, 14, 10).createObject() == True
        assert At(114, 26, 1).createObject() == True
        assert At(114, 4, 2).createObject() == True
        assert At(114, 15, 3).createObject() == True
        assert At(114, 29, 4).createObject() == True
        assert At(114, 10, 5).createObject() == True
        assert At(114, 25, 6).createObject() == True
        assert At(114, 28, 7).createObject() == True
        assert At(114, 1, 8).createObject() == True
        assert At(115, 3, 1).createObject() == True
        assert At(115, 29, 2).createObject() == True
        assert At(115, 4, 3).createObject() == True
        assert At(115, 1, 4).createObject() == True
        assert At(115, 11, 5).createObject() == True
        assert At(115, 17, 6).createObject() == True
        assert At(115, 2, 7).createObject() == True
        assert At(116, 18, 1).createObject() == True
        assert At(116, 14, 2).createObject() == True
        assert At(116, 3, 3).createObject() == True
        assert At(116, 21, 4).createObject() == True
        assert At(116, 1, 5).createObject() == True
        assert At(116, 22, 6).createObject() == True
        assert At(116, 25, 7).createObject() == True
        assert At(116, 16, 8).createObject() == True
        assert At(117, 15, 1).createObject() == True
        assert At(117, 13, 2).createObject() == True
        assert At(117, 5, 3).createObject() == True
        assert At(117, 22, 4).createObject() == True
        assert At(117, 16, 5).createObject() == True
        assert At(117, 11, 6).createObject() == True
        assert At(117, 9, 7).createObject() == True
        assert At(117, 21, 8).createObject() == True
        assert At(117, 1, 9).createObject() == True
        assert At(117, 28, 10).createObject() == True
        assert At(118, 24, 1).createObject() == True
        assert At(118, 26, 2).createObject() == True
        assert At(118, 14, 3).createObject() == True
        assert At(118, 1, 4).createObject() == True
        assert At(118, 12, 5).createObject() == True
        assert At(118, 25, 6).createObject() == True
        assert At(118, 2, 7).createObject() == True
        assert At(119, 2, 1).createObject() == True
        assert At(119, 6, 2).createObject() == True
        assert At(119, 25, 3).createObject() == True
        assert At(119, 17, 4).createObject() == True
        assert At(119, 24, 5).createObject() == True
        assert At(120, 19, 1).createObject() == True
        assert At(120, 6, 2).createObject() == True
        assert At(120, 12, 3).createObject() == True
        assert At(120, 4, 4).createObject() == True
        assert At(120, 9, 5).createObject() == True
        assert At(121, 27, 1).createObject() == True
        assert At(121, 18, 2).createObject() == True
        assert At(121, 15, 3).createObject() == True
        assert At(121, 6, 4).createObject() == True
        assert At(121, 22, 5).createObject() == True
        assert At(121, 19, 6).createObject() == True
        assert At(121, 17, 7).createObject() == True
        assert At(122, 11, 1).createObject() == True
        assert At(122, 29, 2).createObject() == True
        assert At(122, 9, 3).createObject() == True
        assert At(122, 27, 4).createObject() == True
        assert At(122, 15, 5).createObject() == True
        assert At(122, 13, 6).createObject() == True
        assert At(123, 27, 1).createObject() == True
        assert At(123, 16, 2).createObject() == True
        assert At(123, 11, 3).createObject() == True
        assert At(123, 18, 4).createObject() == True
        assert At(123, 26, 5).createObject() == True
        assert At(123, 14, 6).createObject() == True
        assert At(123, 25, 7).createObject() == True
        assert At(123, 22, 8).createObject() == True
        assert At(123, 9, 9).createObject() == True
        assert At(123, 2, 10).createObject() == True
        assert At(124, 23, 1).createObject() == True
        assert At(124, 3, 2).createObject() == True
        assert At(124, 8, 3).createObject() == True
        assert At(124, 19, 4).createObject() == True
        assert At(124, 10, 5).createObject() == True
        assert At(125, 12, 1).createObject() == True
        assert At(125, 14, 2).createObject() == True
        assert At(125, 1, 3).createObject() == True
        assert At(125, 13, 4).createObject() == True
        assert At(125, 29, 5).createObject() == True
        assert At(125, 16, 6).createObject() == True
        assert At(126, 19, 1).createObject() == True
        assert At(126, 26, 2).createObject() == True
        assert At(126, 22, 3).createObject() == True
        assert At(126, 1, 4).createObject() == True
        assert At(126, 4, 5).createObject() == True
        assert At(126, 3, 6).createObject() == True
        assert At(126, 29, 7).createObject() == True
        assert At(126, 12, 8).createObject() == True
        assert At(126, 23, 9).createObject() == True
        assert At(127, 2, 1).createObject() == True
        assert At(127, 11, 2).createObject() == True
        assert At(127, 1, 3).createObject() == True
        assert At(127, 23, 4).createObject() == True
        assert At(127, 20, 5).createObject() == True
        assert At(127, 28, 6).createObject() == True
        assert At(127, 5, 7).createObject() == True
        assert At(128, 26, 1).createObject() == True
        assert At(128, 2, 2).createObject() == True
        assert At(128, 27, 3).createObject() == True
        assert At(128, 1, 4).createObject() == True
        assert At(128, 7, 5).createObject() == True
        assert At(128, 11, 6).createObject() == True
        assert At(128, 10, 7).createObject() == True
        assert At(128, 24, 8).createObject() == True
        assert At(128, 23, 9).createObject() == True
        assert At(128, 12, 10).createObject() == True
        assert At(129, 2, 1).createObject() == True
        assert At(129, 8, 2).createObject() == True
        assert At(129, 16, 3).createObject() == True
        assert At(129, 11, 4).createObject() == True
        assert At(129, 20, 5).createObject() == True
        assert At(129, 1, 6).createObject() == True
        assert At(129, 4, 7).createObject() == True
        assert At(130, 13, 1).createObject() == True
        assert At(130, 21, 2).createObject() == True
        assert At(130, 1, 3).createObject() == True
        assert At(130, 19, 4).createObject() == True
        assert At(130, 7, 5).createObject() == True
        assert At(130, 3, 6).createObject() == True
        assert At(130, 18, 7).createObject() == True
        assert At(130, 14, 8).createObject() == True
        assert At(131, 12, 1).createObject() == True
        assert At(131, 15, 2).createObject() == True
        assert At(131, 14, 3).createObject() == True
        assert At(131, 29, 4).createObject() == True
        assert At(131, 16, 5).createObject() == True
        assert At(131, 4, 6).createObject() == True
        assert At(131, 3, 7).createObject() == True
        assert At(131, 8, 8).createObject() == True
        assert At(131, 26, 9).createObject() == True
        assert At(132, 28, 1).createObject() == True
        assert At(132, 22, 2).createObject() == True
        assert At(132, 23, 3).createObject() == True
        assert At(132, 29, 4).createObject() == True
        assert At(132, 20, 5).createObject() == True
        assert At(132, 3, 6).createObject() == True
        assert At(132, 5, 7).createObject() == True
        assert At(132, 13, 8).createObject() == True
        assert At(132, 1, 9).createObject() == True
        assert At(133, 22, 1).createObject() == True
        assert At(133, 29, 2).createObject() == True
        assert At(133, 16, 3).createObject() == True
        assert At(133, 13, 4).createObject() == True
        assert At(133, 25, 5).createObject() == True
        assert At(133, 3, 6).createObject() == True
        assert At(133, 21, 7).createObject() == True
        assert At(133, 20, 8).createObject() == True
        assert At(134, 3, 1).createObject() == True
        assert At(134, 15, 2).createObject() == True
        assert At(134, 13, 3).createObject() == True
        assert At(134, 11, 4).createObject() == True
        assert At(134, 6, 5).createObject() == True
        assert At(134, 7, 6).createObject() == True
        assert At(135, 9, 1).createObject() == True
        assert At(135, 25, 2).createObject() == True
        assert At(135, 29, 3).createObject() == True
        assert At(135, 26, 4).createObject() == True
        assert At(135, 3, 5).createObject() == True
        assert At(135, 2, 6).createObject() == True
        assert At(135, 27, 7).createObject() == True
        assert At(135, 7, 8).createObject() == True
        assert At(135, 4, 9).createObject() == True
        assert At(135, 11, 10).createObject() == True
        assert At(136, 3, 1).createObject() == True
        assert At(136, 4, 2).createObject() == True
        assert At(136, 9, 3).createObject() == True
        assert At(136, 24, 4).createObject() == True
        assert At(136, 29, 5).createObject() == True
        assert At(137, 9, 1).createObject() == True
        assert At(137, 13, 2).createObject() == True
        assert At(137, 5, 3).createObject() == True
        assert At(137, 1, 4).createObject() == True
        assert At(137, 15, 5).createObject() == True
        assert At(137, 4, 6).createObject() == True
        assert At(137, 6, 7).createObject() == True
        assert At(138, 22, 1).createObject() == True
        assert At(138, 26, 2).createObject() == True
        assert At(138, 8, 3).createObject() == True
        assert At(138, 20, 4).createObject() == True
        assert At(138, 7, 5).createObject() == True
        assert At(139, 14, 1).createObject() == True
        assert At(139, 27, 2).createObject() == True
        assert At(139, 23, 3).createObject() == True
        assert At(139, 5, 4).createObject() == True
        assert At(139, 25, 5).createObject() == True
        assert At(139, 26, 6).createObject() == True
        assert At(139, 29, 7).createObject() == True
        assert At(140, 7, 1).createObject() == True
        assert At(140, 21, 2).createObject() == True
        assert At(140, 1, 3).createObject() == True
        assert At(140, 9, 4).createObject() == True
        assert At(140, 4, 5).createObject() == True
        assert At(141, 2, 1).createObject() == True
        assert At(141, 16, 2).createObject() == True
        assert At(141, 7, 3).createObject() == True
        assert At(141, 21, 4).createObject() == True
        assert At(141, 14, 5).createObject() == True
        assert At(141, 13, 6).createObject() == True
        assert At(141, 11, 7).createObject() == True
        assert At(142, 26, 1).createObject() == True
        assert At(142, 28, 2).createObject() == True
        assert At(142, 19, 3).createObject() == True
        assert At(142, 17, 4).createObject() == True
        assert At(142, 14, 5).createObject() == True
        assert At(142, 12, 6).createObject() == True
        assert At(142, 6, 7).createObject() == True
        assert At(142, 5, 8).createObject() == True
        assert At(142, 7, 9).createObject() == True
        assert At(142, 20, 10).createObject() == True
        assert At(143, 18, 1).createObject() == True
        assert At(143, 25, 2).createObject() == True
        assert At(143, 16, 3).createObject() == True
        assert At(143, 6, 4).createObject() == True
        assert At(143, 26, 5).createObject() == True
        assert At(144, 23, 1).createObject() == True
        assert At(144, 26, 2).createObject() == True
        assert At(144, 14, 3).createObject() == True
        assert At(144, 10, 4).createObject() == True
        assert At(144, 13, 5).createObject() == True
        assert At(144, 1, 6).createObject() == True
        assert At(144, 6, 7).createObject() == True
        assert At(145, 24, 1).createObject() == True
        assert At(145, 7, 2).createObject() == True
        assert At(145, 8, 3).createObject() == True
        assert At(145, 10, 4).createObject() == True
        assert At(145, 18, 5).createObject() == True
        assert At(145, 22, 6).createObject() == True
        assert At(145, 6, 7).createObject() == True
        assert At(146, 22, 1).createObject() == True
        assert At(146, 12, 2).createObject() == True
        assert At(146, 11, 3).createObject() == True
        assert At(146, 29, 4).createObject() == True
        assert At(146, 10, 5).createObject() == True
        assert At(146, 8, 6).createObject() == True
        assert At(147, 12, 1).createObject() == True
        assert At(147, 27, 2).createObject() == True
        assert At(147, 7, 3).createObject() == True
        assert At(147, 20, 4).createObject() == True
        assert At(147, 24, 5).createObject() == True
        assert At(147, 3, 6).createObject() == True
        assert At(147, 10, 7).createObject() == True
        assert At(147, 29, 8).createObject() == True
        assert At(147, 14, 9).createObject() == True
        assert At(148, 15, 1).createObject() == True
        assert At(148, 2, 2).createObject() == True
        assert At(148, 24, 3).createObject() == True
        assert At(148, 18, 4).createObject() == True
        assert At(148, 10, 5).createObject() == True
        assert At(148, 21, 6).createObject() == True
        assert At(148, 9, 7).createObject() == True
        assert At(148, 3, 8).createObject() == True
        assert At(148, 6, 9).createObject() == True
        assert At(149, 18, 1).createObject() == True
        assert At(149, 6, 2).createObject() == True
        assert At(149, 1, 3).createObject() == True
        assert At(149, 4, 4).createObject() == True
        assert At(149, 11, 5).createObject() == True
        assert At(149, 28, 6).createObject() == True
        assert At(149, 25, 7).createObject() == True
        assert At(149, 5, 8).createObject() == True
        assert At(149, 24, 9).createObject() == True
        assert At(149, 26, 10).createObject() == True
        assert At(150, 18, 1).createObject() == True
        assert At(150, 13, 2).createObject() == True
        assert At(150, 27, 3).createObject() == True
        assert At(150, 14, 4).createObject() == True
        assert At(150, 9, 5).createObject() == True
        assert At(150, 22, 6).createObject() == True
        assert At(150, 6, 7).createObject() == True
        assert At(150, 2, 8).createObject() == True
        assert At(150, 15, 9).createObject() == True
        

        assert Booking('MH 9 AB 8797', '28U', 1, 23, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '7L', 1, 11, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '24U', 1, 29, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '16U', 1, 39, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '26L', 1, 22, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '1L', 1, 7, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '15L', 1, 13, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '17U', 1, 15, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '11U', 1, 28, 18, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '8L', 1, 33, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '6U', 2, 34, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '8L', 2, 13, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '28U', 2, 12, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '20L', 2, 27, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '14L', 2, 8, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '11U', 2, 19, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '16U', 2, 30, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '22U', 2, 24, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '18U', 2, 6, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '27L', 2, 22, 23, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '3L', 2, 17, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '6U', 3, 30, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '26L', 3, 25, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '17U', 3, 23, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '24U', 3, 2, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '13L', 3, 30, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '19L', 3, 22, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '8L', 3, 9, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '5U', 3, 33, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '25L', 3, 22, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '29U', 3, 36, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '30U', 3, 14, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '9L', 3, 35, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '10U', 3, 16, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '1L', 3, 13, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '15L', 3, 6, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '4U', 3, 8, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '27L', 3, 5, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '7L', 3, 18, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '23U', 3, 29, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '16U', 3, 1, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '30U', 4, 30, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '18U', 4, 2, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '27L', 4, 35, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '24U', 4, 21, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '25L', 4, 33, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '17U', 4, 35, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '8L', 4, 5, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '9L', 4, 12, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '4U', 4, 27, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '20L', 4, 7, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '12U', 4, 18, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '7L', 4, 29, 17, 5).createObject() == True
        assert Booking('MH 19 AB 8198', '19L', 4, 38, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '2L', 5, 17, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 5, 24, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 5, 34, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 5, 26, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 5, 15, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '28U', 5, 27, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '1L', 5, 18, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '19L', 5, 28, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 5, 14, 23, 13).createObject() == True
        assert Booking('MH 10 AB 5575', '29U', 5, 39, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '24U', 6, 11, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '6U', 6, 19, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '26L', 6, 10, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '28U', 6, 14, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '13L', 6, 24, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '25L', 6, 24, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '21L', 6, 27, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '1L', 6, 36, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '27L', 6, 38, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '20L', 6, 39, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '9L', 6, 16, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '12U', 6, 4, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '23U', 6, 14, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '17U', 6, 30, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '14L', 6, 15, 13, 11).createObject() == True
        assert Booking('MH 16 AB 7222', '10U', 6, 23, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '28U', 7, 16, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '26L', 7, 23, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 7, 40, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '24U', 7, 37, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 7, 16, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 7, 36, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 7, 27, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '17U', 7, 11, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 7, 7, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 7, 18, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 7, 25, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 7, 32, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 7, 31, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 7, 12, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 7, 23, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 7, 29, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 7, 16, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 7, 27, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 7, 3, 6, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 7, 8, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 8, 17, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 8, 34, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '5U', 8, 7, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 8, 17, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 8, 28, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 8, 27, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 8, 23, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 8, 25, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '19L', 8, 30, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '14L', 8, 29, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 8, 27, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '28U', 8, 3, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 8, 13, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '4U', 8, 20, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '21L', 8, 39, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 8, 32, 1, 24).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 8, 3, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 9, 5, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '14L', 9, 31, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '9L', 9, 39, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '18U', 9, 19, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '28U', 9, 30, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '10U', 9, 23, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '22U', 9, 36, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '16U', 9, 5, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '4U', 9, 29, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '25L', 9, 10, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '7L', 9, 10, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '29U', 9, 25, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 9, 12, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '13L', 9, 11, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '3L', 9, 17, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '23U', 9, 19, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '17U', 9, 29, 24, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '2L', 9, 20, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '24U', 10, 9, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '13L', 10, 25, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '7L', 10, 23, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '16U', 10, 35, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '23U', 10, 5, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '25L', 10, 22, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '28U', 10, 40, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '11U', 10, 1, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '4U', 10, 5, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '20L', 10, 18, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '3L', 10, 9, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '17U', 10, 40, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '15L', 10, 26, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '6U', 10, 40, 22, 26).createObject() == True
        assert Booking('MH 14 AB 6518', '30U', 10, 17, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '3L', 11, 18, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 11, 29, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 11, 35, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 11, 26, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '23U', 11, 26, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '1L', 11, 31, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '21L', 11, 37, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 11, 15, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '13L', 11, 33, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '19L', 11, 24, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 11, 6, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 11, 23, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '5U', 11, 8, 29, 8).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 11, 20, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '19L', 12, 28, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '28U', 12, 3, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '21L', 12, 2, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '10U', 12, 29, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '6U', 12, 24, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '24U', 12, 4, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '17U', 12, 33, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '5U', 12, 31, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '14L', 12, 22, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '16U', 12, 23, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '9L', 12, 12, 7, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '7L', 12, 8, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '2L', 13, 18, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '23U', 13, 30, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '21L', 13, 3, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '14L', 13, 5, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '9L', 13, 37, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '8L', 13, 24, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '6U', 13, 26, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '15L', 13, 34, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '18U', 13, 20, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '19L', 13, 1, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '4U', 13, 7, 21, 4).createObject() == True
        assert Booking('MH 11 AB 8643', '29U', 13, 12, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '16U', 14, 17, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '8L', 14, 13, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '29U', 14, 10, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '23U', 14, 24, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '2L', 14, 15, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '11U', 14, 27, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '5U', 14, 39, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '24U', 14, 11, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '19L', 14, 24, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '28U', 14, 33, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '30U', 14, 8, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '3L', 14, 23, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '10U', 14, 7, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '9L', 14, 22, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '20L', 14, 32, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '25L', 14, 22, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '27L', 14, 5, 23, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '14L', 14, 6, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '16U', 15, 4, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '26L', 15, 14, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '10U', 15, 18, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '20L', 15, 3, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '19L', 15, 18, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '9L', 15, 16, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '28U', 15, 32, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '17U', 15, 11, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '21L', 15, 26, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '6U', 15, 4, 16, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '14L', 15, 12, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '17U', 16, 9, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '15L', 16, 2, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '18U', 16, 29, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '30U', 16, 34, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '24U', 16, 39, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '4U', 16, 1, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 16, 22, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 16, 9, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '29U', 16, 10, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '8L', 16, 19, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '10U', 16, 6, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '13L', 16, 29, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '6U', 16, 32, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '28U', 16, 38, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '22U', 16, 23, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '23U', 16, 2, 18, 28).createObject() == True
        assert Booking('MH 18 AB 7004', '26L', 16, 3, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '26L', 17, 29, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '15L', 17, 5, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '4U', 17, 17, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '17U', 17, 36, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '19L', 17, 8, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '1L', 17, 8, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '5U', 17, 9, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '22U', 17, 23, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '8L', 17, 30, 17, 3).createObject() == True
        assert Booking('MH 13 AB 9993', '27L', 17, 13, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '6U', 18, 5, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '9L', 18, 3, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '2L', 18, 6, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '16U', 18, 28, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '30U', 18, 30, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '17U', 18, 25, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '11U', 18, 19, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '25L', 18, 35, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '15L', 18, 37, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '27L', 18, 10, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '23U', 18, 21, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '4U', 18, 31, 19, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '26L', 18, 19, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '24U', 19, 10, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '16U', 19, 16, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '22U', 19, 11, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '12U', 19, 38, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '27L', 19, 21, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '1L', 19, 2, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '20L', 19, 27, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '8L', 19, 8, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '10U', 19, 2, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '4U', 19, 5, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '5U', 19, 24, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '21L', 19, 14, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '19L', 19, 8, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '15L', 20, 12, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '26L', 20, 22, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '27L', 20, 40, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '2L', 20, 31, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '11U', 20, 3, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '29U', 20, 16, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '14L', 20, 22, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '23U', 20, 3, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '4U', 20, 15, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '22U', 20, 9, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '10U', 20, 7, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '18U', 20, 10, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '17U', 20, 39, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '5U', 20, 30, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '28U', 20, 17, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '19L', 20, 25, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '9L', 20, 5, 8, 12).createObject() == True
        assert Booking('MH 11 AB 7889', '1L', 20, 37, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '19L', 21, 17, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '17U', 21, 37, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '14L', 21, 11, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '12U', 21, 16, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '7L', 21, 5, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '30U', 21, 33, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '9L', 21, 29, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '25L', 21, 10, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '1L', 21, 14, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '28U', 21, 37, 22, 6).createObject() == True
        assert Booking('MH 13 AB 9993', '27L', 21, 7, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '21L', 22, 26, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '19L', 22, 36, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '25L', 22, 17, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '6U', 22, 33, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '24U', 22, 12, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '14L', 22, 20, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '5U', 22, 7, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '15L', 22, 40, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '20L', 22, 9, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '22U', 22, 21, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '17U', 22, 20, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '10U', 22, 27, 6, 20).createObject() == True
        assert Booking('MH 14 AB 5997', '1L', 22, 31, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '27L', 23, 31, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '12U', 23, 21, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '8L', 23, 19, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '1L', 23, 2, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '26L', 23, 21, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '4U', 23, 8, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '9L', 23, 28, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '14L', 23, 8, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '30U', 23, 20, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '29U', 23, 13, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '10U', 23, 6, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '16U', 23, 35, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '21L', 23, 39, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '22U', 23, 9, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '3L', 23, 37, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '5U', 23, 14, 2, 21).createObject() == True
        assert Booking('MH 14 AB 9684', '15L', 23, 38, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 24, 12, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 24, 20, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 24, 39, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '5U', 24, 19, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 24, 3, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 24, 21, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 24, 24, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 24, 32, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 24, 12, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 24, 25, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '26L', 24, 2, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 24, 12, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 25, 24, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 25, 6, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 25, 30, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '24U', 25, 35, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 25, 9, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 25, 13, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 25, 29, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 25, 25, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 25, 3, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '7L', 25, 36, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 25, 35, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '21L', 25, 30, 9, 16).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 25, 3, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '10U', 26, 13, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '14L', 26, 27, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '29U', 26, 3, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '4U', 26, 29, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '5U', 26, 40, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '8L', 26, 23, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '11U', 26, 25, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '19L', 26, 30, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '23U', 26, 17, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '7L', 26, 26, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '27L', 26, 7, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '26L', 26, 36, 1, 11).createObject() == True
        assert Booking('MH 11 AB 8643', '1L', 26, 40, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '17U', 27, 15, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '9L', 27, 32, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '14L', 27, 3, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '16U', 27, 22, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '28U', 27, 24, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '7L', 27, 19, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '22U', 27, 20, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '6U', 27, 3, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '10U', 27, 24, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '3L', 27, 21, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '13L', 27, 20, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '5U', 27, 29, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '25L', 27, 21, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '11U', 27, 8, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '20L', 27, 31, 5, 8).createObject() == True
        assert Booking('MH 5 AB 7650', '26L', 27, 25, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '1L', 28, 14, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '15L', 28, 22, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '24U', 28, 20, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '17U', 28, 9, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '26L', 28, 15, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '30U', 28, 15, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '19L', 28, 39, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '25L', 28, 36, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '18U', 28, 37, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '20L', 28, 24, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '10U', 28, 6, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '14L', 28, 38, 23, 9).createObject() == True
        assert Booking('MH 12 AB 9096', '21L', 28, 8, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '5U', 29, 23, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '14L', 29, 15, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '21L', 29, 17, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '9L', 29, 35, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '1L', 29, 17, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '12U', 29, 7, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '27L', 29, 27, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '4U', 29, 25, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '16U', 29, 16, 18, 23).createObject() == True
        assert Booking('MH 11 AB 7989', '25L', 29, 36, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '13L', 30, 36, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '29U', 30, 14, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '30U', 30, 30, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '7L', 30, 3, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '12U', 30, 3, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '14L', 30, 35, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '17U', 30, 9, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '22U', 30, 1, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '4U', 30, 3, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '9L', 30, 22, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '16U', 30, 21, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '10U', 30, 39, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '8L', 30, 9, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '24U', 30, 11, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '19L', 30, 38, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '6U', 30, 34, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '25L', 30, 11, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '5U', 30, 18, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '15L', 30, 24, 20, 22).createObject() == True
        assert Booking('MH 11 AB 8643', '1L', 30, 35, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '2L', 31, 39, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '7L', 31, 2, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '13L', 31, 4, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '3L', 31, 11, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '18U', 31, 32, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '5U', 31, 10, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '16U', 31, 12, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '25L', 31, 11, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '26L', 31, 7, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '30U', 31, 8, 4, 28).createObject() == True
        assert Booking('MH 12 AB 9096', '24U', 31, 12, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '3L', 32, 10, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '4U', 32, 29, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '6U', 32, 20, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '8L', 32, 37, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '26L', 32, 8, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '15L', 32, 39, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '19L', 32, 27, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '25L', 32, 15, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '12U', 32, 9, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '27L', 32, 33, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '13L', 32, 17, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '30U', 32, 13, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '24U', 32, 34, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '18U', 32, 18, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '24U', 33, 4, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '29U', 33, 23, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '4U', 33, 22, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '22U', 33, 17, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '28U', 33, 6, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '23U', 33, 10, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '7L', 33, 24, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '10U', 33, 18, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '26L', 33, 6, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '5U', 33, 7, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '25L', 33, 27, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '6U', 33, 20, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '13L', 33, 25, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '18U', 33, 28, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '29U', 34, 29, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '13L', 34, 26, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '24U', 34, 22, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '3L', 34, 20, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '7L', 34, 36, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '23U', 34, 13, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '1L', 34, 38, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '15L', 34, 11, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '14L', 34, 33, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '21L', 34, 5, 19, 1).createObject() == True
        assert Booking('MH 15 AB 9478', '27L', 34, 28, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '19L', 35, 19, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '26L', 35, 40, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '14L', 35, 5, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '24U', 35, 24, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '9L', 35, 32, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '28U', 35, 40, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '5U', 35, 30, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '21L', 35, 37, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '29U', 35, 28, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '7L', 35, 23, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '15L', 35, 13, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '16U', 35, 17, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '11U', 35, 26, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '10U', 35, 13, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '18U', 35, 12, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '13L', 35, 29, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '23U', 35, 20, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '3L', 35, 16, 28, 14).createObject() == True
        assert Booking('MH 7 AB 6536', '20L', 35, 12, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '13L', 36, 36, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '6U', 36, 37, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '12U', 36, 7, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '29U', 36, 6, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '8L', 36, 26, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '16U', 36, 20, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '4U', 36, 19, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '9L', 36, 14, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '5U', 36, 5, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '3L', 36, 39, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '25L', 36, 31, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '18U', 36, 39, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '23U', 36, 10, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '21L', 36, 37, 14, 9).createObject() == True
        assert Booking('MH 11 AB 7659', '20L', 36, 14, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '2L', 37, 16, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '24U', 37, 22, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '27L', 37, 3, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '22U', 37, 14, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '20L', 37, 3, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '7L', 37, 19, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '18U', 37, 15, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '19L', 37, 16, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '13L', 37, 17, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '25L', 37, 16, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '23U', 37, 39, 6, 10).createObject() == True
        assert Booking('MH 9 AB 8797', '3L', 37, 38, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '14L', 38, 9, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 38, 13, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '10U', 38, 40, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '23U', 38, 8, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '17U', 38, 7, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 38, 13, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '22U', 38, 5, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '11U', 38, 34, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '20L', 38, 27, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '3L', 38, 2, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '12U', 38, 21, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 38, 2, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 38, 14, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '29U', 38, 14, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '28U', 38, 3, 10, 24).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 38, 15, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '3L', 39, 5, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '6U', 39, 9, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '21L', 39, 34, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '29U', 39, 7, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '5U', 39, 21, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '2L', 39, 15, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '7L', 39, 20, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '4U', 39, 21, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '17U', 39, 33, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '16U', 39, 20, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '19L', 39, 6, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '30U', 39, 31, 20, 19).createObject() == True
        assert Booking('MH 20 AB 8094', '27L', 39, 32, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 40, 12, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '5U', 40, 28, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '6U', 40, 19, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '9L', 40, 23, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '3L', 40, 31, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '7L', 40, 5, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 40, 19, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '30U', 40, 35, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '28U', 40, 23, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '20L', 40, 33, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '23U', 40, 40, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '27L', 40, 23, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '29U', 40, 3, 2, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '18U', 40, 6, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '2L', 41, 19, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '10U', 41, 17, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '4U', 41, 2, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '19L', 41, 33, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '23U', 41, 13, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '13L', 41, 1, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '5U', 41, 23, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '30U', 41, 4, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '3L', 41, 40, 8, 3).createObject() == True
        assert Booking('MH 19 AB 8198', '17U', 41, 8, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '19L', 42, 25, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '4U', 42, 37, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 42, 12, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 42, 24, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '12U', 42, 30, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '5U', 42, 2, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '3L', 42, 1, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 42, 33, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '11U', 42, 19, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 42, 34, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '15L', 42, 29, 6, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '14L', 42, 31, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 43, 26, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '4U', 43, 37, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 43, 22, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 43, 14, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 43, 37, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 43, 26, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '3L', 43, 19, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 43, 36, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 43, 29, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '5U', 43, 35, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 43, 12, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 43, 14, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '7L', 43, 21, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 43, 40, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 43, 4, 9, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 43, 5, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '6U', 44, 23, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '4U', 44, 34, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '8L', 44, 16, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '28U', 44, 14, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '3L', 44, 11, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 44, 9, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 44, 36, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 44, 32, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 44, 29, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 44, 4, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 44, 37, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '30U', 44, 9, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 44, 2, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '13L', 44, 19, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 44, 6, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '5U', 44, 34, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '11U', 44, 13, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 44, 24, 13, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 44, 31, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '23U', 45, 7, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '2L', 45, 20, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '18U', 45, 11, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '5U', 45, 26, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '20L', 45, 10, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '27L', 45, 32, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '4U', 45, 4, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '14L', 45, 29, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '9L', 45, 33, 12, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '21L', 45, 11, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '18U', 46, 7, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '29U', 46, 37, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '5U', 46, 26, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '25L', 46, 31, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '9L', 46, 32, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '11U', 46, 38, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '3L', 46, 28, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '23U', 46, 16, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '15L', 46, 9, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '16U', 46, 35, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '19L', 46, 3, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '2L', 46, 34, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '10U', 46, 7, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '28U', 46, 37, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '26L', 46, 24, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '12U', 46, 28, 14, 3).createObject() == True
        assert Booking('MH 8 AB 5155', '1L', 46, 4, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 47, 34, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '22U', 47, 34, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '23U', 47, 40, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '4U', 47, 27, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '30U', 47, 25, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 47, 39, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '5U', 47, 13, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '8L', 47, 1, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 47, 23, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '12U', 47, 13, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '16U', 47, 11, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '17U', 47, 35, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 47, 39, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '14L', 47, 11, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '20L', 47, 39, 4, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '25L', 47, 26, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '12U', 48, 35, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '9L', 48, 23, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '29U', 48, 30, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '13L', 48, 23, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '8L', 48, 14, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '24U', 48, 19, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '7L', 48, 9, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '11U', 48, 27, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '6U', 48, 24, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '2L', 48, 38, 10, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '1L', 48, 28, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 49, 39, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 49, 21, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '5U', 49, 20, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 49, 15, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '16U', 49, 1, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 49, 19, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 49, 26, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 49, 26, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '21L', 49, 17, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 49, 20, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 49, 25, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '17U', 49, 34, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 49, 24, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 49, 10, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 49, 36, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '3L', 49, 15, 14, 28).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 49, 32, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '18U', 50, 2, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 50, 39, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '10U', 50, 1, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 50, 2, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '12U', 50, 15, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '11U', 50, 39, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '6U', 50, 36, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 50, 31, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 50, 13, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '14L', 50, 5, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '17U', 50, 1, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '21L', 50, 39, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '15L', 50, 31, 11, 13).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 50, 9, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '28U', 51, 29, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '30U', 51, 29, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '24U', 51, 30, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '16U', 51, 16, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '11U', 51, 5, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '27L', 51, 15, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '12U', 51, 27, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '29U', 51, 5, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '6U', 51, 28, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '21L', 51, 18, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8932', '2L', 51, 10, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '6U', 52, 16, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 52, 33, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '22U', 52, 16, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '21L', 52, 34, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '29U', 52, 28, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '8L', 52, 14, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '24U', 52, 26, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '11U', 52, 26, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '12U', 52, 16, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 52, 22, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '25L', 52, 35, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '14L', 52, 36, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '23U', 52, 20, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '27L', 52, 22, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '10U', 52, 6, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '20L', 52, 36, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '11U', 53, 7, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '20L', 53, 7, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '7L', 53, 3, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '24U', 53, 31, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 53, 3, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '27L', 53, 20, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 53, 3, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '15L', 53, 5, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '1L', 53, 25, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '6U', 53, 16, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '25L', 53, 20, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '21L', 53, 28, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '22U', 53, 36, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '12U', 53, 14, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '3L', 53, 18, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '4U', 53, 9, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '30U', 53, 14, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '29U', 53, 14, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '9L', 53, 26, 12, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '13L', 53, 38, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '9L', 54, 16, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '19L', 54, 5, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '25L', 54, 21, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '5U', 54, 37, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '7L', 54, 35, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '15L', 54, 30, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '24U', 54, 28, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '12U', 54, 36, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '16U', 54, 13, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '23U', 54, 25, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '18U', 54, 10, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '10U', 54, 20, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '1L', 54, 14, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '17U', 54, 31, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '4U', 54, 10, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '28U', 54, 21, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '11U', 54, 29, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '29U', 54, 8, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '22U', 54, 3, 29, 21).createObject() == True
        assert Booking('MH 6 AB 5509', '2L', 54, 29, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '11U', 55, 9, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '13L', 55, 18, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '22U', 55, 36, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '1L', 55, 29, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '7L', 55, 26, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '24U', 55, 9, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '12U', 55, 4, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '19L', 55, 31, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '18U', 55, 24, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '28U', 55, 40, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '23U', 55, 28, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '26L', 55, 19, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '27L', 55, 9, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '29U', 55, 9, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '3L', 55, 27, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '10U', 55, 38, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '4U', 55, 16, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '15L', 55, 18, 27, 22).createObject() == True
        assert Booking('MH 11 AB 5703', '5U', 55, 17, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '26L', 56, 29, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '3L', 56, 35, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '24U', 56, 36, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '16U', 56, 17, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '9L', 56, 15, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '19L', 56, 36, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '14L', 56, 34, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '29U', 56, 24, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '5U', 56, 17, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '30U', 56, 38, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '13L', 56, 27, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '1L', 56, 9, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '2L', 56, 5, 24, 19).createObject() == True
        assert Booking('MH 19 AB 5367', '17U', 56, 16, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '15L', 57, 39, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '5U', 57, 17, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '27L', 57, 28, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '19L', 57, 21, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '18U', 57, 25, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '10U', 57, 15, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '12U', 57, 16, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '16U', 57, 18, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '29U', 57, 6, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '9L', 57, 40, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '30U', 57, 21, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '22U', 57, 26, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '6U', 57, 27, 16, 1).createObject() == True
        assert Booking('MH 13 AB 9993', '8L', 57, 28, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '30U', 58, 24, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '25L', 58, 17, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '12U', 58, 39, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '23U', 58, 5, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '7L', 58, 7, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '14L', 58, 30, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '16U', 58, 31, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '17U', 58, 20, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '27L', 58, 27, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '28U', 58, 31, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '2L', 58, 35, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '3L', 58, 20, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '5U', 58, 2, 22, 25).createObject() == True
        assert Booking('MH 17 AB 5987', '9L', 58, 34, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '9L', 59, 3, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '27L', 59, 26, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '18U', 59, 6, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '12U', 59, 25, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '23U', 59, 19, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '1L', 59, 1, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '24U', 59, 32, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '14L', 59, 4, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '20L', 59, 24, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '8L', 59, 12, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '30U', 59, 40, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '3L', 59, 5, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '29U', 59, 33, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '13L', 59, 26, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '10U', 59, 28, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '2L', 59, 32, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '7L', 59, 18, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '19L', 59, 20, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '21L', 59, 17, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '4U', 60, 5, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '24U', 60, 4, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '9L', 60, 1, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '11U', 60, 33, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '20L', 60, 25, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '17U', 60, 30, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '30U', 60, 30, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '2L', 60, 11, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '28U', 60, 31, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '18U', 60, 30, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '16U', 60, 20, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '25L', 60, 15, 7, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '19L', 60, 34, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '12U', 61, 38, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '22U', 61, 8, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '20L', 61, 10, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '19L', 61, 14, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '28U', 61, 18, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 61, 2, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '4U', 61, 37, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 61, 17, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '30U', 61, 15, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '14L', 61, 18, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '25L', 61, 38, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 61, 1, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 61, 15, 3, 17).createObject() == True
        assert Booking('MH 16 AB 7740', '24U', 61, 1, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '15L', 62, 7, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '11U', 62, 14, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '21L', 62, 38, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '27L', 62, 4, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '13L', 62, 1, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '2L', 62, 1, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '6U', 62, 36, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '24U', 62, 3, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '20L', 62, 40, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '8L', 62, 3, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '16U', 62, 19, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '30U', 62, 28, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '7L', 62, 39, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '14L', 62, 8, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '10U', 62, 15, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '17U', 62, 9, 13, 16).createObject() == True
        assert Booking('MH 19 AB 8932', '23U', 62, 13, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '4U', 63, 30, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '14L', 63, 24, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '1L', 63, 33, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '9L', 63, 5, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '7L', 63, 30, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '24U', 63, 33, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '12U', 63, 26, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '27L', 63, 23, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '8L', 63, 20, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '29U', 63, 28, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '28U', 63, 2, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '21L', 63, 2, 28, 26).createObject() == True
        assert Booking('MH 17 AB 8217', '3L', 63, 2, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '15L', 64, 8, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '19L', 64, 4, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '8L', 64, 4, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '12U', 64, 28, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '18U', 64, 20, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '20L', 64, 5, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '13L', 64, 18, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '29U', 64, 21, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '30U', 64, 15, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '23U', 64, 23, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '28U', 64, 1, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '7L', 64, 5, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '5U', 64, 17, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '6U', 64, 25, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '17U', 64, 33, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '11U', 64, 28, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '2L', 64, 24, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '9L', 64, 29, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '21L', 64, 32, 17, 19).createObject() == True
        assert Booking('MH 5 AB 6693', '4U', 64, 8, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '4U', 65, 13, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '21L', 65, 26, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '2L', 65, 29, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '29U', 65, 17, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '6U', 65, 17, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '14L', 65, 14, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '16U', 65, 21, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '26L', 65, 30, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '15L', 65, 14, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '9L', 65, 10, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '23U', 65, 28, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '27L', 65, 29, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '5U', 65, 39, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '10U', 65, 15, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '8L', 65, 1, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '7L', 65, 22, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '11U', 65, 39, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '18U', 65, 11, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '30U', 66, 13, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '10U', 66, 15, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '8L', 66, 3, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '7L', 66, 38, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '11U', 66, 2, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '22U', 66, 20, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '3L', 66, 26, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '2L', 66, 40, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '9L', 66, 38, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '13L', 66, 10, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '24U', 66, 39, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '18U', 66, 5, 2, 26).createObject() == True
        assert Booking('MH 19 AB 8198', '6U', 66, 11, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '24U', 67, 28, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '18U', 67, 12, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '11U', 67, 33, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '1L', 67, 10, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '16U', 67, 4, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '28U', 67, 27, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '14L', 67, 12, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '5U', 67, 17, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '20L', 67, 12, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '2L', 67, 11, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '15L', 67, 20, 28, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '22U', 67, 5, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '27L', 68, 32, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '13L', 68, 4, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 68, 35, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 68, 39, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 68, 19, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 68, 40, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '16U', 68, 30, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '4U', 68, 37, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '29U', 68, 36, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '19L', 68, 37, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '23U', 68, 9, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '14L', 68, 27, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '1L', 68, 18, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '7L', 68, 3, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '12U', 68, 7, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '17U', 68, 8, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '8L', 68, 10, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 68, 36, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 68, 38, 14, 7).createObject() == True
        assert Booking('MH 10 AB 5575', '25L', 68, 36, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '12U', 69, 38, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '8L', 69, 15, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '11U', 69, 36, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '26L', 69, 38, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '18U', 69, 21, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '16U', 69, 5, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '6U', 69, 31, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '9L', 69, 2, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '27L', 69, 28, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '23U', 69, 31, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '17U', 69, 10, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '14L', 69, 13, 22, 29).createObject() == True
        assert Booking('MH 8 AB 5155', '5U', 69, 29, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '19L', 70, 33, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '29U', 70, 18, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '1L', 70, 37, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '24U', 70, 21, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '7L', 70, 40, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '30U', 70, 18, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '12U', 70, 19, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '20L', 70, 17, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '18U', 70, 37, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '21L', 70, 33, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '15L', 70, 33, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '9L', 70, 13, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '11U', 70, 25, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '2L', 70, 17, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '22U', 70, 28, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '3L', 70, 24, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '4U', 70, 37, 4, 1).createObject() == True
        assert Booking('MH 6 AB 5509', '27L', 70, 27, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '13L', 71, 9, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '28U', 71, 18, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '21L', 71, 26, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '17U', 71, 33, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '30U', 71, 16, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '29U', 71, 25, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '20L', 71, 18, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '22U', 71, 9, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '26L', 71, 5, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '25L', 71, 28, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '27L', 71, 5, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '4U', 71, 18, 18, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '3L', 71, 5, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '7L', 72, 6, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '15L', 72, 8, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '21L', 72, 14, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '18U', 72, 27, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '1L', 72, 23, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '28U', 72, 34, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '10U', 72, 34, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '4U', 72, 15, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '6U', 72, 32, 21, 20).createObject() == True
        assert Booking('MH 12 AB 9096', '17U', 72, 3, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '15L', 73, 10, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '13L', 73, 33, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '25L', 73, 25, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '10U', 73, 33, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '23U', 73, 19, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '21L', 73, 33, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '2L', 73, 4, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '12U', 73, 25, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '16U', 73, 30, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '3L', 73, 10, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '6U', 73, 35, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '18U', 73, 35, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '28U', 73, 12, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '11U', 73, 5, 16, 8).createObject() == True
        assert Booking('MH 19 AB 5367', '19L', 73, 17, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '9L', 74, 30, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '17U', 74, 22, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '16U', 74, 34, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '1L', 74, 18, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '3L', 74, 36, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '14L', 74, 28, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '4U', 74, 12, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '6U', 74, 17, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '8L', 74, 37, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '22U', 74, 34, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '7L', 74, 18, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '15L', 74, 23, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '10U', 74, 19, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '5U', 74, 18, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '2L', 74, 37, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '19L', 74, 25, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '25L', 74, 8, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '28U', 74, 32, 28, 5).createObject() == True
        assert Booking('MH 8 AB 6980', '11U', 74, 31, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 75, 10, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '16U', 75, 2, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 75, 13, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 75, 7, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '3L', 75, 10, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 75, 15, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 75, 16, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 75, 1, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 75, 4, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 75, 40, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '21L', 75, 15, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 75, 37, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 75, 16, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 75, 28, 7, 2).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 75, 32, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '28U', 76, 29, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '8L', 76, 7, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '21L', 76, 32, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '19L', 76, 23, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '25L', 76, 9, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '20L', 76, 12, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '4U', 76, 8, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '11U', 76, 40, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '29U', 76, 33, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '14L', 76, 9, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '9L', 76, 9, 26, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '7L', 76, 25, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '10U', 77, 5, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '11U', 77, 9, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '20L', 77, 21, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '27L', 77, 18, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '15L', 77, 30, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '23U', 77, 16, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '13L', 77, 1, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '6U', 77, 15, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '3L', 77, 24, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '12U', 77, 30, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '28U', 77, 2, 15, 7).createObject() == True
        assert Booking('MH 12 AB 8578', '21L', 77, 4, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '5U', 78, 6, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '9L', 78, 33, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '11U', 78, 9, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '17U', 78, 37, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '12U', 78, 15, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '27L', 78, 19, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '3L', 78, 27, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '14L', 78, 18, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '2L', 78, 30, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '18U', 78, 36, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '23U', 78, 10, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '19L', 78, 24, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '28U', 78, 25, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '7L', 78, 20, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '20L', 78, 22, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '26L', 78, 13, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '25L', 78, 4, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '10U', 78, 7, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '29U', 78, 35, 10, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '6U', 78, 23, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '4U', 79, 36, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '1L', 79, 24, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '23U', 79, 25, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '8L', 79, 14, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '13L', 79, 35, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '29U', 79, 37, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '28U', 79, 21, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '12U', 79, 11, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '19L', 79, 31, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '15L', 79, 29, 4, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '18U', 79, 39, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 80, 35, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 80, 26, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 80, 5, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '28U', 80, 7, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 80, 15, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '8L', 80, 4, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 80, 26, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 80, 26, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 80, 8, 18, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '14L', 80, 37, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '6U', 81, 17, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '28U', 81, 9, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '4U', 81, 27, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '7L', 81, 7, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '12U', 81, 34, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '1L', 81, 30, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '9L', 81, 40, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '19L', 81, 25, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '22U', 81, 13, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '27L', 81, 15, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '29U', 81, 18, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '15L', 81, 32, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '5U', 81, 21, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '25L', 81, 40, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '13L', 81, 16, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '2L', 81, 27, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '18U', 81, 22, 8, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '11U', 81, 27, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '25L', 82, 40, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '5U', 82, 22, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '2L', 82, 17, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '20L', 82, 34, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '28U', 82, 14, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '10U', 82, 11, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '13L', 82, 20, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '18U', 82, 16, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '29U', 82, 39, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '24U', 82, 38, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '19L', 82, 5, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '17U', 82, 4, 28, 26).createObject() == True
        assert Booking('MH 14 AB 5997', '21L', 82, 2, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '1L', 83, 26, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '4U', 83, 31, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '18U', 83, 28, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '30U', 83, 8, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '22U', 83, 36, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '17U', 83, 5, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '8L', 83, 13, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '26L', 83, 30, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '3L', 83, 38, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '27L', 83, 33, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '15L', 83, 6, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '2L', 83, 10, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '20L', 83, 11, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '14L', 83, 6, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '5U', 83, 3, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '28U', 83, 17, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '13L', 83, 32, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '7L', 83, 19, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '19L', 83, 27, 19, 17).createObject() == True
        assert Booking('MH 12 AB 9096', '6U', 83, 29, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '4U', 84, 31, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '26L', 84, 23, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '17U', 84, 12, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '30U', 84, 17, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '2L', 84, 34, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '27L', 84, 22, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '21L', 84, 31, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '3L', 84, 24, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '12U', 84, 11, 16, 15).createObject() == True
        assert Booking('MH 9 AB 8797', '9L', 84, 40, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '20L', 85, 26, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '12U', 85, 26, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '19L', 85, 32, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '9L', 85, 6, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '24U', 85, 30, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '16U', 85, 37, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '25L', 85, 16, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '2L', 85, 20, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '23U', 85, 13, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '30U', 85, 21, 28, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '26L', 85, 14, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '15L', 86, 2, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '4U', 86, 8, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '11U', 86, 39, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '12U', 86, 9, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '25L', 86, 3, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '29U', 86, 9, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '7L', 86, 39, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '5U', 86, 24, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '23U', 86, 21, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '17U', 86, 31, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '2L', 86, 11, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '16U', 86, 10, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '26L', 86, 3, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '1L', 86, 35, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '19L', 86, 39, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '26L', 87, 38, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '5U', 87, 2, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '30U', 87, 40, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '2L', 87, 6, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '9L', 87, 13, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '27L', 87, 17, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '11U', 87, 4, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '4U', 87, 14, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '8L', 87, 30, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '15L', 87, 8, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '23U', 87, 2, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '24U', 87, 36, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '3L', 87, 29, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '10U', 87, 8, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6518', '29U', 87, 10, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '27L', 88, 3, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '15L', 88, 27, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '8L', 88, 1, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '25L', 88, 25, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '23U', 88, 33, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '18U', 88, 22, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '17U', 88, 1, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '9L', 88, 10, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '3L', 88, 15, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '4U', 88, 4, 5, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '28U', 88, 26, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '29U', 89, 3, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '8L', 89, 30, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '23U', 89, 15, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '11U', 89, 29, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '3L', 89, 24, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '20L', 89, 19, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '27L', 89, 13, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '26L', 89, 17, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '5U', 89, 12, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '25L', 89, 12, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '1L', 89, 19, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '30U', 89, 35, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '7L', 89, 13, 27, 7).createObject() == True
        assert Booking('MH 14 AB 9684', '16U', 89, 5, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '13L', 90, 38, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '18U', 90, 31, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '28U', 90, 8, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '23U', 90, 1, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '9L', 90, 40, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '7L', 90, 2, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '26L', 90, 36, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '21L', 90, 2, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '3L', 90, 23, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '30U', 90, 22, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '5U', 90, 9, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '24U', 90, 26, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '29U', 90, 24, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '15L', 90, 16, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '17U', 90, 23, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '12U', 90, 13, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '8L', 90, 24, 7, 29).createObject() == True
        assert Booking('MH 12 AB 5440', '27L', 90, 24, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '1L', 91, 36, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '11U', 91, 6, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '7L', 91, 1, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '19L', 91, 26, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '27L', 91, 1, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '12U', 91, 5, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '24U', 91, 30, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '4U', 91, 18, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '10U', 91, 10, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '15L', 91, 11, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '6U', 91, 29, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '13L', 91, 10, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '17U', 91, 27, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '3L', 91, 11, 2, 10).createObject() == True
        assert Booking('MH 5 AB 6693', '5U', 91, 18, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '6U', 92, 40, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '23U', 92, 16, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '30U', 92, 34, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '19L', 92, 21, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '20L', 92, 17, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '16U', 92, 4, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '26L', 92, 34, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '4U', 92, 38, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '29U', 92, 36, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '5U', 92, 34, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '14L', 92, 12, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '28U', 92, 26, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 92, 20, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '7L', 92, 16, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '17U', 92, 4, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '10U', 92, 17, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 92, 17, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '3L', 92, 8, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '24U', 92, 17, 21, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '13L', 92, 27, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '29U', 93, 30, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '19L', 93, 18, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '11U', 93, 8, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '3L', 93, 20, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '10U', 93, 37, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '1L', 93, 10, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '9L', 93, 37, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '8L', 93, 19, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '13L', 93, 26, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '6U', 93, 25, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '27L', 93, 15, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '17U', 93, 10, 22, 12).createObject() == True
        assert Booking('MH 12 AB 8578', '12U', 93, 5, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '21L', 94, 35, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 94, 1, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '1L', 94, 36, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 94, 2, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '19L', 94, 28, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '5U', 94, 16, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '25L', 94, 23, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 94, 40, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '28U', 94, 34, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '7L', 94, 14, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 94, 37, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '4U', 94, 19, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '20L', 94, 20, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '12U', 94, 27, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '29U', 94, 39, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '30U', 94, 5, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 94, 37, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '28U', 95, 30, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '12U', 95, 38, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '16U', 95, 30, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '20L', 95, 5, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '21L', 95, 40, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '30U', 95, 31, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '15L', 95, 35, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '26L', 95, 8, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '19L', 95, 8, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '24U', 95, 21, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '11U', 95, 9, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '18U', 95, 17, 6, 25).createObject() == True
        assert Booking('MH 6 AB 5509', '1L', 95, 37, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '18U', 96, 8, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '5U', 96, 16, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '7L', 96, 35, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '28U', 96, 2, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '30U', 96, 39, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '6U', 96, 16, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '2L', 96, 9, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '24U', 96, 4, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '14L', 96, 30, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '19L', 96, 35, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '9L', 96, 8, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '27L', 96, 5, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '3L', 96, 14, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '13L', 96, 21, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '22U', 96, 6, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '12U', 96, 6, 21, 14).createObject() == True
        assert Booking('MH 12 AB 7062', '21L', 96, 4, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '19L', 97, 16, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '29U', 97, 11, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '10U', 97, 17, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '17U', 97, 4, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '4U', 97, 38, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '15L', 97, 13, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '6U', 97, 24, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '5U', 97, 36, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '2L', 97, 24, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '7L', 97, 11, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '25L', 97, 29, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '1L', 97, 13, 16, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '22U', 97, 38, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '24U', 98, 19, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 98, 30, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '4U', 98, 30, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 98, 40, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '29U', 98, 37, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '23U', 98, 9, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '22U', 98, 11, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '25L', 98, 30, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '13L', 98, 21, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '15L', 98, 36, 29, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '2L', 98, 11, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '12U', 99, 28, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '18U', 99, 17, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '30U', 99, 16, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '29U', 99, 16, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '13L', 99, 39, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '21L', 99, 6, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '2L', 99, 40, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '20L', 99, 36, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '10U', 99, 12, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '16U', 99, 16, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '4U', 99, 10, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '19L', 99, 25, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '7L', 99, 3, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '26L', 99, 12, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '15L', 99, 7, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '1L', 99, 34, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '5U', 99, 22, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '11U', 99, 3, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '22U', 99, 18, 6, 21).createObject() == True
        assert Booking('MH 11 AB 7989', '23U', 99, 7, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '29U', 100, 37, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '19L', 100, 22, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '2L', 100, 40, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '24U', 100, 40, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '6U', 100, 40, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '18U', 100, 6, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '28U', 100, 26, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '11U', 100, 39, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '1L', 100, 27, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '23U', 100, 32, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '12U', 100, 13, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '30U', 100, 10, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '20L', 100, 30, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '3L', 100, 7, 8, 7).createObject() == True
        assert Booking('MH 14 AB 5997', '27L', 100, 29, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '25L', 101, 1, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '15L', 101, 40, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '14L', 101, 14, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '2L', 101, 26, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '10U', 101, 6, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '21L', 101, 16, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '24U', 101, 36, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '8L', 101, 16, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '12U', 101, 16, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '16U', 101, 32, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '18U', 101, 25, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '6U', 101, 20, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '26L', 101, 26, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '17U', 101, 25, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '28U', 101, 12, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '5U', 101, 11, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '20L', 101, 28, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '9L', 101, 28, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '1L', 101, 5, 10, 2).createObject() == True
        assert Booking('MH 13 AB 9993', '3L', 101, 29, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '2L', 102, 31, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '6U', 102, 4, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '12U', 102, 10, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '26L', 102, 32, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '21L', 102, 24, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '15L', 102, 8, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '18U', 102, 12, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '14L', 102, 40, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '8L', 102, 25, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '30U', 102, 22, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '24U', 102, 31, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '10U', 102, 22, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '17U', 102, 29, 13, 23).createObject() == True
        assert Booking('MH 8 AB 6980', '4U', 102, 22, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '4U', 103, 22, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '13L', 103, 11, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '9L', 103, 19, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '10U', 103, 29, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '16U', 103, 35, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 103, 25, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '30U', 103, 10, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '23U', 103, 9, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '8L', 103, 34, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 103, 20, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '2L', 103, 4, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '20L', 103, 27, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '7L', 103, 28, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 103, 19, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '1L', 103, 34, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '5U', 103, 28, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '14L', 103, 24, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 103, 28, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 103, 16, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '24U', 104, 18, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '21L', 104, 9, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '11U', 104, 15, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '25L', 104, 35, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '22U', 104, 25, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '18U', 104, 30, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '9L', 104, 18, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '7L', 104, 38, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '6U', 104, 29, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '13L', 104, 32, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '15L', 104, 27, 5, 22).createObject() == True
        assert Booking('MH 5 AB 6693', '14L', 104, 3, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '10U', 105, 3, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '29U', 105, 9, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '3L', 105, 34, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '8L', 105, 27, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '13L', 105, 18, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '6U', 105, 1, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '20L', 105, 1, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '16U', 105, 13, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '25L', 105, 7, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '24U', 105, 6, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '19L', 105, 37, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '1L', 105, 25, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '28U', 105, 25, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '4U', 105, 34, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '15L', 105, 15, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '27L', 105, 39, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '9L', 105, 16, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '5U', 105, 5, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '17U', 105, 1, 29, 17).createObject() == True
        assert Booking('MH 12 AB 5440', '14L', 105, 7, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '4U', 106, 2, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 106, 14, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 106, 33, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 106, 40, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 106, 26, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 106, 11, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 106, 33, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 106, 31, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 106, 12, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 106, 4, 10, 26).createObject() == True
        assert Booking('MH 17 AB 9316', '26L', 106, 12, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '19L', 107, 5, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '21L', 107, 25, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '11U', 107, 24, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '1L', 107, 30, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '6U', 107, 34, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '25L', 107, 3, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '13L', 107, 26, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '22U', 107, 18, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '17U', 107, 31, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 107, 22, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '30U', 107, 23, 8, 18).createObject() == True
        assert Booking('MH 9 AB 8308', '14L', 107, 21, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 108, 4, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 108, 39, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '18U', 108, 40, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '11U', 108, 1, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 108, 15, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '21L', 108, 1, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '30U', 108, 34, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '22U', 108, 22, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '15L', 108, 37, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 108, 8, 27, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 108, 37, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '23U', 109, 21, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '20L', 109, 14, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '10U', 109, 6, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '29U', 109, 24, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '27L', 109, 5, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '17U', 109, 19, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '28U', 109, 16, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '18U', 109, 33, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '5U', 109, 13, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '7L', 109, 30, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '11U', 109, 35, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '16U', 109, 4, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '2L', 109, 4, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '13L', 109, 11, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '21L', 109, 19, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '30U', 110, 12, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '4U', 110, 22, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '5U', 110, 7, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '8L', 110, 37, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '25L', 110, 19, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '21L', 110, 29, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '26L', 110, 24, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '11U', 110, 24, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '19L', 110, 25, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '15L', 110, 40, 21, 20).createObject() == True
        assert Booking('MH 12 AB 7062', '3L', 110, 20, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '24U', 111, 31, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '5U', 111, 5, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '26L', 111, 30, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '7L', 111, 27, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '21L', 111, 16, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '9L', 111, 6, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '2L', 111, 37, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '1L', 111, 31, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '19L', 111, 2, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '3L', 111, 25, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '20L', 111, 13, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '13L', 111, 36, 6, 1).createObject() == True
        assert Booking('MH 20 AB 8094', '10U', 111, 35, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '26L', 112, 2, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '15L', 112, 18, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '21L', 112, 40, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '13L', 112, 7, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '14L', 112, 7, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '18U', 112, 10, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '23U', 112, 31, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '9L', 112, 8, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '24U', 112, 34, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '19L', 112, 36, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '16U', 112, 8, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '27L', 112, 27, 1, 3).createObject() == True
        assert Booking('MH 14 AB 9684', '28U', 112, 30, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 113, 5, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 113, 10, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 113, 31, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '23U', 113, 35, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 113, 26, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '7L', 113, 19, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 113, 31, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '14L', 113, 28, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '4U', 113, 38, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '11U', 113, 22, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '5U', 113, 29, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '8L', 113, 38, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 113, 32, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 113, 37, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '6U', 114, 12, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '21L', 114, 17, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 114, 32, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 114, 30, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 114, 24, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 114, 11, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 114, 12, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 114, 28, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 114, 22, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 114, 31, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '3L', 114, 31, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 114, 19, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 114, 33, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '23U', 114, 36, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '4U', 114, 6, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '28U', 114, 10, 26, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 114, 39, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '1L', 115, 31, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '22U', 115, 31, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '4U', 115, 28, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '26L', 115, 8, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '6U', 115, 5, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '19L', 115, 28, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '20L', 115, 37, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '9L', 115, 26, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '25L', 115, 4, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '8L', 115, 10, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '23U', 115, 8, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '21L', 115, 25, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '28U', 115, 26, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '2L', 115, 27, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '7L', 115, 8, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '3L', 115, 34, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '16U', 115, 25, 3, 2).createObject() == True
        assert Booking('MH 14 AB 9684', '15L', 115, 35, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '28U', 116, 39, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '1L', 116, 34, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '29U', 116, 30, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '3L', 116, 30, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '22U', 116, 18, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '20L', 116, 15, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '15L', 116, 23, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '24U', 116, 40, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '18U', 116, 11, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '17U', 116, 30, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '12U', 116, 30, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '30U', 116, 17, 18, 16).createObject() == True
        assert Booking('MH 10 AB 9617', '13L', 116, 13, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '22U', 117, 24, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '1L', 117, 13, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '3L', 117, 2, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '23U', 117, 23, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '26L', 117, 11, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '20L', 117, 11, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '13L', 117, 18, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '5U', 117, 20, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '18U', 117, 3, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '10U', 117, 32, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '2L', 117, 25, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '21L', 117, 3, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '15L', 117, 14, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '29U', 117, 35, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '11U', 117, 40, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '4U', 117, 3, 15, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '28U', 117, 24, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '11U', 118, 30, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '26L', 118, 34, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '23U', 118, 11, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '16U', 118, 24, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '24U', 118, 5, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '10U', 118, 12, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '25L', 118, 38, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '29U', 118, 5, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '7L', 118, 33, 24, 2).createObject() == True
        assert Booking('MH 13 AB 5137', '3L', 118, 33, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '24U', 119, 32, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '19L', 119, 19, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '14L', 119, 21, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 119, 14, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '15L', 119, 39, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '3L', 119, 8, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '29U', 119, 23, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '5U', 119, 16, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '1L', 119, 30, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 119, 14, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '21L', 119, 5, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '2L', 119, 7, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '22U', 119, 16, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '20L', 119, 23, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '8L', 119, 18, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '17U', 119, 21, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '27L', 119, 39, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '25L', 119, 39, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '6U', 119, 26, 2, 24).createObject() == True
        assert Booking('MH 9 AB 8308', '23U', 119, 16, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '24U', 120, 23, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '16U', 120, 31, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '14L', 120, 17, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '15L', 120, 37, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '1L', 120, 38, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '21L', 120, 8, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '26L', 120, 22, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '5U', 120, 40, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '9L', 120, 11, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '4U', 120, 33, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '28U', 120, 21, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '29U', 120, 36, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '30U', 120, 35, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '10U', 120, 14, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '8L', 120, 8, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '17U', 120, 11, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '7L', 120, 36, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '12U', 120, 22, 19, 9).createObject() == True
        assert Booking('MH 19 AB 8198', '6U', 120, 9, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '22U', 121, 31, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '27L', 121, 37, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '18U', 121, 3, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '1L', 121, 2, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '9L', 121, 3, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '14L', 121, 9, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '8L', 121, 30, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '13L', 121, 5, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '12U', 121, 23, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '6U', 121, 14, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '5U', 121, 31, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '21L', 121, 32, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '2L', 121, 36, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '24U', 121, 4, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '19L', 121, 2, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '3L', 121, 24, 27, 17).createObject() == True
        assert Booking('MH 8 AB 8272', '4U', 121, 25, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '26L', 122, 24, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '11U', 122, 34, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '13L', 122, 19, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '24U', 122, 25, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '22U', 122, 17, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '12U', 122, 6, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '27L', 122, 28, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '14L', 122, 33, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '23U', 122, 14, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '15L', 122, 23, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '1L', 122, 37, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '17U', 122, 8, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '4U', 122, 39, 11, 13).createObject() == True
        assert Booking('MH 12 AB 7062', '28U', 122, 39, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '22U', 123, 34, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '17U', 123, 18, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '12U', 123, 24, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '2L', 123, 27, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '23U', 123, 11, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '11U', 123, 32, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '25L', 123, 31, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '3L', 123, 33, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '18U', 123, 38, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '19L', 123, 37, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '16U', 123, 3, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '28U', 123, 23, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '27L', 123, 25, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '29U', 123, 32, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '13L', 123, 37, 27, 2).createObject() == True
        assert Booking('MH 19 AB 8932', '15L', 123, 40, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '1L', 124, 6, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '5U', 124, 22, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '21L', 124, 37, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 124, 8, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '8L', 124, 6, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '20L', 124, 35, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '13L', 124, 17, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '25L', 124, 20, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '9L', 124, 9, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '18U', 124, 9, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '24U', 124, 2, 23, 10).createObject() == True
        assert Booking('MH 9 AB 8308', '10U', 124, 3, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '7L', 125, 14, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '9L', 125, 11, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '26L', 125, 13, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '18U', 125, 36, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '20L', 125, 32, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '27L', 125, 33, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '14L', 125, 4, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '30U', 125, 16, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '13L', 125, 36, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '23U', 125, 19, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '2L', 125, 11, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '8L', 125, 35, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '10U', 125, 6, 12, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '4U', 125, 12, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '22U', 126, 20, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '30U', 126, 4, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '4U', 126, 36, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '13L', 126, 5, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '24U', 126, 23, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '28U', 126, 16, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '27L', 126, 22, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '11U', 126, 21, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '21L', 126, 28, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '2L', 126, 21, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '5U', 126, 14, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '25L', 126, 26, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '17U', 126, 24, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '1L', 126, 22, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '16U', 126, 26, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '19L', 126, 8, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '14L', 126, 15, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '15L', 126, 19, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '10U', 126, 25, 19, 23).createObject() == True
        assert Booking('MH 8 AB 8272', '8L', 126, 21, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 127, 26, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '6U', 127, 6, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '7L', 127, 27, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '4U', 127, 17, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 127, 23, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '19L', 127, 23, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 127, 10, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '21L', 127, 6, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 127, 4, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 127, 25, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '28U', 127, 1, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '30U', 127, 40, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 127, 17, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 127, 18, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 127, 32, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 127, 15, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '14L', 127, 37, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 127, 10, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 127, 8, 2, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 127, 39, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '2L', 128, 23, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '9L', 128, 4, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '21L', 128, 13, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '7L', 128, 36, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '17U', 128, 14, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '13L', 128, 27, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '18U', 128, 6, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '26L', 128, 40, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '24U', 128, 25, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '12U', 128, 8, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '29U', 128, 28, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '14L', 128, 23, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '4U', 128, 9, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '20L', 128, 28, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '10U', 128, 8, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '23U', 128, 2, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '1L', 128, 2, 26, 12).createObject() == True
        assert Booking('MH 19 AB 9404', '11U', 128, 13, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 129, 34, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '2L', 129, 29, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '8L', 129, 40, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 129, 18, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '17U', 129, 17, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '12U', 129, 30, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 129, 39, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '16U', 129, 38, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '27L', 129, 18, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '7L', 129, 2, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '22U', 129, 23, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '6U', 129, 25, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '13L', 129, 36, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '9L', 129, 24, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 129, 6, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '23U', 129, 5, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '30U', 129, 36, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '14L', 129, 19, 2, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '1L', 129, 36, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '22U', 130, 15, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '28U', 130, 3, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '23U', 130, 15, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '8L', 130, 22, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '30U', 130, 7, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '25L', 130, 2, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '18U', 130, 24, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '3L', 130, 19, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '24U', 130, 19, 13, 14).createObject() == True
        assert Booking('MH 12 AB 5440', '9L', 130, 1, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '21L', 131, 32, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 131, 22, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 131, 4, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '30U', 131, 2, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 131, 36, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 131, 9, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '7L', 131, 10, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 131, 31, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 131, 3, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 131, 3, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 131, 22, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '3L', 131, 24, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 131, 36, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 131, 14, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '11U', 131, 28, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 131, 37, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 131, 38, 12, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '8L', 131, 10, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '28U', 132, 36, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '18U', 132, 9, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '8L', 132, 29, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '15L', 132, 27, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '10U', 132, 20, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '11U', 132, 9, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '6U', 132, 19, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '29U', 132, 25, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '16U', 132, 25, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '5U', 132, 26, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '4U', 132, 30, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '1L', 132, 9, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '21L', 132, 20, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '20L', 132, 2, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '13L', 132, 10, 28, 1).createObject() == True
        assert Booking('MH 11 AB 5703', '2L', 132, 24, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '23U', 133, 7, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '7L', 133, 2, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '9L', 133, 8, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '11U', 133, 16, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '27L', 133, 25, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '15L', 133, 17, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '16U', 133, 6, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 133, 39, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '20L', 133, 14, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '24U', 133, 12, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '19L', 133, 25, 22, 20).createObject() == True
        assert Booking('MH 9 AB 8308', '6U', 133, 29, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '28U', 134, 30, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '16U', 134, 2, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 134, 3, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 134, 21, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 134, 16, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 134, 8, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 134, 7, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 134, 20, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 134, 1, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '24U', 134, 5, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 134, 12, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 134, 34, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 134, 4, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 134, 11, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '7L', 134, 16, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 134, 4, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 134, 30, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 134, 15, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '3L', 135, 2, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '21L', 135, 24, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '5U', 135, 10, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 135, 20, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 135, 32, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '28U', 135, 39, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 135, 35, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 135, 6, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 135, 37, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 135, 2, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 135, 33, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '7L', 135, 8, 9, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '24U', 135, 7, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '13L', 136, 13, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '15L', 136, 31, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '2L', 136, 16, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '18U', 136, 21, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '6U', 136, 19, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '10U', 136, 12, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '25L', 136, 23, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '29U', 136, 14, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '5U', 136, 10, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '23U', 136, 11, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '19L', 136, 34, 3, 29).createObject() == True
        assert Booking('MH 17 AB 8217', '21L', 136, 31, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '12U', 137, 1, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '21L', 137, 38, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '19L', 137, 17, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '22U', 137, 6, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '26L', 137, 34, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '16U', 137, 33, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '2L', 137, 35, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '18U', 137, 34, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '23U', 137, 14, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '7L', 137, 34, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '14L', 137, 23, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '25L', 137, 7, 9, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '4U', 137, 13, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '2L', 138, 8, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '5U', 138, 29, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '3L', 138, 7, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '1L', 138, 13, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '6U', 138, 38, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '18U', 138, 9, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '13L', 138, 8, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '11U', 138, 12, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '16U', 138, 34, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '14L', 138, 9, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '7L', 138, 12, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '30U', 138, 3, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '28U', 138, 21, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '9L', 138, 22, 22, 7).createObject() == True
        assert Booking('MH 19 AB 9404', '22U', 138, 9, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '18U', 139, 3, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '23U', 139, 27, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '5U', 139, 26, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '6U', 139, 3, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '14L', 139, 2, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '13L', 139, 17, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '7L', 139, 10, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '10U', 139, 34, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '1L', 139, 32, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '19L', 139, 5, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '16U', 139, 10, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '4U', 139, 3, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '12U', 139, 36, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '29U', 139, 8, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '20L', 139, 19, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '22U', 139, 14, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '15L', 139, 31, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '11U', 139, 2, 14, 29).createObject() == True
        assert Booking('MH 11 AB 7989', '25L', 139, 22, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '30U', 140, 22, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '12U', 140, 19, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '24U', 140, 23, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '29U', 140, 26, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '23U', 140, 32, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '22U', 140, 15, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '7L', 140, 26, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '21L', 140, 16, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '14L', 140, 35, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '20L', 140, 26, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '4U', 140, 11, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '10U', 140, 4, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '13L', 140, 16, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '5U', 140, 18, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '17U', 140, 22, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '3L', 140, 1, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '19L', 140, 21, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '6U', 140, 20, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '11U', 140, 8, 7, 4).createObject() == True
        assert Booking('MH 9 AB 8797', '25L', 140, 21, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '17U', 141, 38, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 141, 21, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '13L', 141, 15, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '24U', 141, 39, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '5U', 141, 20, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '30U', 141, 3, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '19L', 141, 37, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '18U', 141, 30, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 141, 25, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '22U', 141, 7, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 141, 25, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '27L', 141, 3, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '6U', 141, 18, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '10U', 141, 28, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '25L', 141, 30, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '14L', 141, 27, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '23U', 141, 4, 2, 11).createObject() == True
        assert Booking('MH 16 AB 7740', '11U', 141, 22, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '24U', 142, 9, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '13L', 142, 24, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '4U', 142, 39, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '1L', 142, 30, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '11U', 142, 30, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '17U', 142, 6, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '14L', 142, 15, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '7L', 142, 24, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '27L', 142, 6, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '28U', 142, 15, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '19L', 142, 15, 26, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '30U', 142, 19, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '17U', 143, 18, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 143, 6, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '6U', 143, 6, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '2L', 143, 29, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '28U', 143, 27, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '29U', 143, 24, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 143, 18, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 143, 39, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '25L', 143, 40, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 143, 34, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '16U', 143, 30, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '22U', 143, 31, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '23U', 143, 37, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '13L', 143, 7, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '12U', 143, 25, 18, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '19L', 143, 8, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '28U', 144, 19, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '9L', 144, 39, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '27L', 144, 21, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '15L', 144, 17, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '11U', 144, 20, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '10U', 144, 17, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '5U', 144, 22, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '7L', 144, 38, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '6U', 144, 29, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '22U', 144, 23, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '25L', 144, 13, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '20L', 144, 24, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '18U', 144, 24, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '1L', 144, 39, 23, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '26L', 144, 35, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '21L', 145, 17, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '19L', 145, 19, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '17U', 145, 11, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '25L', 145, 16, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '3L', 145, 31, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '30U', 145, 17, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '4U', 145, 37, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '28U', 145, 14, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '22U', 145, 37, 24, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '20L', 145, 33, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '3L', 146, 17, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '2L', 146, 11, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '9L', 146, 28, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '6U', 146, 24, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '10U', 146, 5, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '19L', 146, 28, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '7L', 146, 2, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '11U', 146, 30, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '30U', 146, 3, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '13L', 146, 2, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '20L', 146, 17, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '8L', 146, 29, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '16U', 146, 22, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '22U', 146, 23, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '12U', 146, 37, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '15L', 146, 15, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '27L', 146, 4, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '21L', 146, 37, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '4U', 146, 33, 22, 8).createObject() == True
        assert Booking('MH 13 AB 5137', '26L', 146, 40, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '24U', 147, 26, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '9L', 147, 16, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '19L', 147, 18, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '23U', 147, 31, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '21L', 147, 25, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '13L', 147, 4, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '25L', 147, 35, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '20L', 147, 19, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '4U', 147, 8, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '30U', 147, 29, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '15L', 147, 38, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '4U', 148, 14, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '10U', 148, 21, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '13L', 148, 22, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '26L', 148, 29, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '6U', 148, 34, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '5U', 148, 11, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '19L', 148, 20, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '27L', 148, 28, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '9L', 148, 8, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '24U', 148, 17, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '8L', 148, 16, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '2L', 148, 8, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '15L', 148, 22, 15, 6).createObject() == True
        assert Booking('MH 11 AB 7889', '25L', 148, 11, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '13L', 149, 22, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '2L', 149, 40, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '1L', 149, 20, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '20L', 149, 28, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '12U', 149, 23, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '3L', 149, 32, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '9L', 149, 6, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '10U', 149, 39, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '24U', 149, 7, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '14L', 149, 1, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '15L', 149, 32, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '26L', 149, 17, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '27L', 149, 5, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '5U', 149, 9, 18, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '16U', 149, 1, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '29U', 150, 18, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '25L', 150, 38, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '17U', 150, 19, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '27L', 150, 16, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '20L', 150, 5, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 150, 5, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 150, 32, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '19L', 150, 22, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '10U', 150, 31, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '24U', 150, 29, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '16U', 150, 34, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 150, 32, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '15L', 150, 16, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '12U', 150, 7, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 150, 2, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '5U', 150, 19, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '23U', 150, 9, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '4U', 150, 7, 18, 15).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 150, 20, 18, 15).createObject() == True


def main():
    unittest.main(verbosity=2)

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        print(colored('Script needs Args :-', 'red'))
        print(colored('runtest', 'yellow'))
        print(colored('createall', 'yellow'))
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
        print(colored('createall', 'yellow'))
        print(colored('dropall', 'yellow'))
        exit()