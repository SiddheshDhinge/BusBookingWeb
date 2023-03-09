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
        assert Owner('Chintan', 'abc1', 'CJ', '9874563210').createOwner() == True
        assert Owner('Siddhesh', 'abc2', 'SD', '0123456789').createOwner() == True
        assert Owner('Manas', 'abc3', 'MS', '7140258963').createOwner() == True
        assert Owner('Sahil', 'abc4', 'SB', '1112223330').createOwner() == True
        assert Owner('Shubham', 'abc5', 'SS', '4411336655').createOwner()== True
        assert Owner('jack123', 'J@ckp@ss', 'Jack Smith', '5555551212').createOwner() == True
        assert Owner('emmam', 'emm@p@ss', 'Emma Morris', '5555551213').createOwner() == True
        assert Owner('brianb', 'br1@np@ss', 'Brian Baker', '5555551214').createOwner() == True
        assert Owner('katherineg', 'k@thp@ss', 'Katherine Graham', '5555551215').createOwner() == True
        assert Owner('chrisd', 'chr1sp@ss', 'Chris Davis', '5555551216').createOwner() == True
        assert Owner('samuelm', 's@mp@ss', 'Samuel Mitchell', '5555551217').createOwner() == True
        assert Owner('laurar', 'l@urp@ss', 'Laura Roberts', '5555551218').createOwner() == True
        assert Owner('davids', 'd@v1dp@ss', 'David Scott', '5555551219').createOwner() == True
        assert Owner('jennifert', 'j@nnyp@ss', 'Jennifer Taylor', '5555551220').createOwner() == True
        assert Owner('michaelw', 'm1k3wp@ss', 'Michael Williams', '5555551221').createOwner() == True
        assert Owner('susanb', 'sus@np@ss', 'Susan Brown', '5555551222').createOwner() == True
        assert Owner('jamesm', 'j@m3sp@ss', 'James Miller', '5555551223').createOwner() == True
        assert Owner('lisaq', 'l1s@qp@ss', 'Lisa Quinn', '5555551224').createOwner() == True
        assert Owner('matthewr', 'm@ttp@ss', 'Matthew Reed', '5555551225').createOwner() == True
        assert Owner('nicolej', 'n1c@lp@ss', 'Nicole Jackson', '5555551226').createOwner() == True


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


        assert Operator('Manish', 'abc1', 'MB', 'L1', '4411225549').createOperator() == True
        assert Operator('Guarav', 'abc2', 'GS', 'L2', '7475869421').createOperator() == True
        assert Operator('Ketan', 'abc3', 'KM', 'L3', '1122337495').createOperator() == True
        assert Operator('Akshay', 'abc4', 'AJ', 'L4', '5566442576').createOperator() == True
        assert Operator('Lokesh', 'abc5', 'LD', 'L5', '9988743615').createOperator() == True
        assert Operator('timothyb', 'abc', 'Timothy Bennett', '1234 Main St', '5555551227').createOperator() == True
        assert Operator('rachelc', 'abc', 'Rachel Campbell', '5678 First Ave', '5555551228').createOperator() == True
        assert Operator('michaelg', 'abc', 'Michael Green', '9101 Park Dr', '5555551229').createOperator() == True
        assert Operator('jenniferl', 'abc', 'Jennifer Larson', '1212 Oak Ave', '5555551230').createOperator() == True
        assert Operator('davidm', 'abc', 'David Mason', '3434 Maple St', '5555551231').createOperator() == True
        assert Operator('sarahp', 'abc', 'Sarah Peterson', '5656 Pine Ave', '5555551232').createOperator() == True
        assert Operator('matthewr', 'abc', 'Matthew Roberts', '7878 Cedar St', '5555551233').createOperator() == True
        assert Operator('lisaq', 'abc', 'Lisa Quinn', '9090 Birch Ave', '5555551234').createOperator() == True
        assert Operator('katherinet', 'abc', 'Katherine Taylor', '1111 Willow St', '5555551235').createOperator() == True
        assert Operator('johnd', 'abc', 'John Davis', '3333 Maple Ave', '5555551236').createOperator() == True


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
        
        
        assert Booking('MH 9 AB 8797', '30U', 1, 39, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '24U', 1, 40, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '1L', 1, 2, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '26L', 1, 36, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '12U', 1, 3, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '3L', 1, 17, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '8L', 1, 31, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '21L', 1, 31, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '29U', 1, 28, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '4U', 1, 9, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '17U', 1, 16, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '5U', 1, 40, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '11U', 1, 32, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '18U', 1, 11, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '13L', 1, 29, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '23U', 1, 3, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '10U', 1, 16, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '27L', 1, 18, 1, 1).createObject() == True
        assert Booking('MH 9 AB 8797', '16U', 1, 7, 1, 1).createObject() == True
        assert Booking('MH 8 AB 6980', '17U', 2, 5, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '8L', 2, 20, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '27L', 2, 35, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '14L', 2, 12, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '5U', 2, 1, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '4U', 2, 34, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '26L', 2, 18, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '28U', 2, 33, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '19L', 2, 17, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '9L', 2, 10, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '10U', 2, 14, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '15L', 2, 6, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '7L', 2, 35, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '30U', 2, 16, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '24U', 2, 39, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '22U', 2, 10, 18, 29).createObject() == True
        assert Booking('MH 8 AB 6980', '16U', 2, 14, 18, 29).createObject() == True
        assert Booking('MH 19 AB 8198', '6U', 3, 6, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '29U', 3, 15, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '4U', 3, 5, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '14L', 3, 20, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '20L', 3, 24, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '1L', 3, 12, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '25L', 3, 17, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '24U', 3, 14, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '18U', 3, 28, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '16U', 3, 26, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '19L', 3, 18, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '12U', 3, 12, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '27L', 3, 32, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '3L', 3, 5, 23, 22).createObject() == True
        assert Booking('MH 19 AB 8198', '24U', 4, 23, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '19L', 4, 10, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '8L', 4, 25, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '2L', 4, 18, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '3L', 4, 2, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '11U', 4, 33, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '29U', 4, 29, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '14L', 4, 9, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '27L', 4, 36, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '25L', 4, 30, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '18U', 4, 11, 21, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '10U', 4, 25, 21, 16).createObject() == True
        assert Booking('MH 10 AB 5575', '7L', 5, 7, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 5, 10, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '1L', 5, 12, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '8L', 5, 6, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '13L', 5, 28, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '9L', 5, 33, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '4U', 5, 23, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '25L', 5, 9, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 5, 2, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '6U', 5, 37, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '17U', 5, 38, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '22U', 5, 20, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 5, 9, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '23U', 5, 27, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '20L', 5, 40, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '27L', 5, 7, 17, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 5, 35, 17, 5).createObject() == True
        assert Booking('MH 16 AB 7222', '22U', 6, 8, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '24U', 6, 13, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '13L', 6, 13, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '6U', 6, 13, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '23U', 6, 7, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '29U', 6, 31, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '4U', 6, 38, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '28U', 6, 40, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '27L', 6, 22, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '26L', 6, 29, 23, 13).createObject() == True
        assert Booking('MH 16 AB 7222', '9L', 6, 16, 23, 13).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 7, 17, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 7, 35, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 7, 36, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 7, 8, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '28U', 7, 19, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '4U', 7, 1, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 7, 7, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 7, 35, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 7, 21, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 7, 33, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '5U', 7, 3, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 7, 22, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 7, 31, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 7, 7, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 7, 40, 13, 11).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 7, 37, 13, 11).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 8, 24, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '23U', 8, 11, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 8, 34, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '6U', 8, 35, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '5U', 8, 8, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '30U', 8, 19, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 8, 2, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '8L', 8, 32, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '14L', 8, 39, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 8, 21, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 8, 24, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 8, 38, 6, 13).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 8, 1, 6, 13).createObject() == True
        assert Booking('MH 18 AB 7004', '26L', 9, 27, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '19L', 9, 23, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '8L', 9, 22, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '16U', 9, 5, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '4U', 9, 29, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '3L', 9, 31, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '24U', 9, 28, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '7L', 9, 2, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 9, 24, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '9L', 9, 38, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '5U', 9, 3, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 9, 40, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '17U', 9, 34, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 9, 7, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '23U', 9, 10, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '13L', 9, 9, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '25L', 9, 33, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '30U', 9, 12, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '15L', 9, 14, 1, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '14L', 9, 30, 1, 24).createObject() == True
        assert Booking('MH 14 AB 6518', '10U', 10, 6, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '17U', 10, 34, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '6U', 10, 25, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '20L', 10, 30, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '19L', 10, 33, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '25L', 10, 36, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '1L', 10, 38, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '12U', 10, 8, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '24U', 10, 35, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '5U', 10, 11, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '29U', 10, 17, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '9L', 10, 15, 24, 28).createObject() == True
        assert Booking('MH 14 AB 6518', '4U', 10, 33, 24, 28).createObject() == True
        assert Booking('MH 11 AB 9332', '8L', 11, 21, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 11, 7, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '13L', 11, 33, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 11, 5, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '19L', 11, 6, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 11, 37, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '30U', 11, 22, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '14L', 11, 31, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '3L', 11, 1, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 11, 26, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 11, 21, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '28U', 11, 30, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 11, 32, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 11, 7, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 11, 32, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 11, 20, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '7L', 11, 18, 22, 26).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 11, 35, 22, 26).createObject() == True
        assert Booking('MH 12 AB 8578', '17U', 12, 11, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '14L', 12, 22, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '4U', 12, 7, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '5U', 12, 30, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '19L', 12, 9, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '18U', 12, 19, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '2L', 12, 39, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '1L', 12, 3, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '21L', 12, 18, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '3L', 12, 1, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '16U', 12, 5, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '23U', 12, 38, 29, 8).createObject() == True
        assert Booking('MH 12 AB 8578', '28U', 12, 26, 29, 8).createObject() == True
        assert Booking('MH 11 AB 8643', '18U', 13, 27, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '15L', 13, 33, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '12U', 13, 23, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '7L', 13, 12, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '24U', 13, 32, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '9L', 13, 12, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '27L', 13, 26, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '5U', 13, 39, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '23U', 13, 1, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '13L', 13, 28, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '20L', 13, 20, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '10U', 13, 18, 7, 10).createObject() == True
        assert Booking('MH 11 AB 8643', '3L', 13, 28, 7, 10).createObject() == True
        assert Booking('MH 10 AB 9617', '8L', 14, 22, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '16U', 14, 33, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '28U', 14, 28, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '22U', 14, 22, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '19L', 14, 23, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '15L', 14, 22, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '10U', 14, 2, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '2L', 14, 3, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '25L', 14, 36, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '26L', 14, 19, 21, 4).createObject() == True
        assert Booking('MH 10 AB 9617', '21L', 14, 18, 21, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '19L', 15, 18, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '30U', 15, 4, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '11U', 15, 15, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '25L', 15, 16, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '6U', 15, 7, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '28U', 15, 7, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '8L', 15, 34, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '1L', 15, 23, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '22U', 15, 32, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '12U', 15, 26, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '2L', 15, 11, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '3L', 15, 1, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '5U', 15, 8, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '4U', 15, 18, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '14L', 15, 11, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '29U', 15, 5, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '10U', 15, 3, 23, 5).createObject() == True
        assert Booking('MH 15 AB 9478', '9L', 15, 40, 23, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '20L', 16, 9, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '26L', 16, 23, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '25L', 16, 4, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 16, 17, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 16, 36, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '28U', 16, 7, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '2L', 16, 9, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 16, 34, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '21L', 16, 30, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '16U', 16, 38, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '22U', 16, 14, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '29U', 16, 4, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '19L', 16, 22, 16, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '8L', 16, 25, 16, 5).createObject() == True
        assert Booking('MH 13 AB 9993', '23U', 17, 40, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '30U', 17, 37, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '28U', 17, 23, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '25L', 17, 1, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '6U', 17, 11, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '20L', 17, 27, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '5U', 17, 10, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '16U', 17, 32, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '26L', 17, 26, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '8L', 17, 1, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '24U', 17, 5, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '19L', 17, 27, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '12U', 17, 27, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '4U', 17, 6, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '27L', 17, 19, 18, 28).createObject() == True
        assert Booking('MH 13 AB 9993', '1L', 17, 38, 18, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '19L', 18, 37, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '2L', 18, 17, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '5U', 18, 40, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '18U', 18, 4, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '12U', 18, 2, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '27L', 18, 8, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '26L', 18, 23, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '4U', 18, 40, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '28U', 18, 22, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '1L', 18, 12, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '11U', 18, 12, 17, 3).createObject() == True
        assert Booking('MH 15 AB 9478', '29U', 18, 37, 17, 3).createObject() == True
        assert Booking('MH 11 AB 7659', '4U', 19, 6, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '30U', 19, 39, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '27L', 19, 6, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '21L', 19, 14, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '20L', 19, 6, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '12U', 19, 35, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '24U', 19, 16, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '25L', 19, 8, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '29U', 19, 16, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '22U', 19, 13, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '16U', 19, 20, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '9L', 19, 1, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7659', '7L', 19, 13, 19, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '13L', 20, 6, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '10U', 20, 28, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '29U', 20, 27, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '7L', 20, 17, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '15L', 20, 39, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '5U', 20, 38, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '1L', 20, 39, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '12U', 20, 25, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '24U', 20, 25, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '23U', 20, 2, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '3L', 20, 39, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '14L', 20, 9, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '30U', 20, 38, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '19L', 20, 16, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '28U', 20, 4, 1, 4).createObject() == True
        assert Booking('MH 11 AB 7889', '20L', 20, 11, 1, 4).createObject() == True
        assert Booking('MH 13 AB 9993', '22U', 21, 27, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '7L', 21, 30, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '28U', 21, 28, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '3L', 21, 5, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '17U', 21, 2, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '14L', 21, 25, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '21L', 21, 15, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '19L', 21, 21, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '1L', 21, 1, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '23U', 21, 20, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '10U', 21, 36, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '6U', 21, 32, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '16U', 21, 14, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '18U', 21, 17, 8, 12).createObject() == True
        assert Booking('MH 13 AB 9993', '30U', 21, 13, 8, 12).createObject() == True
        assert Booking('MH 14 AB 5997', '13L', 22, 39, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '2L', 22, 30, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '16U', 22, 6, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '3L', 22, 13, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '6U', 22, 34, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '24U', 22, 21, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '10U', 22, 40, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '19L', 22, 40, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '30U', 22, 22, 22, 6).createObject() == True
        assert Booking('MH 14 AB 5997', '18U', 22, 32, 22, 6).createObject() == True
        assert Booking('MH 14 AB 9684', '11U', 23, 13, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '16U', 23, 6, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '12U', 23, 31, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '23U', 23, 26, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '6U', 23, 23, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '30U', 23, 38, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '9L', 23, 17, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '1L', 23, 27, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '28U', 23, 12, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '17U', 23, 5, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '26L', 23, 13, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '21L', 23, 19, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '5U', 23, 36, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '3L', 23, 19, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '15L', 23, 33, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '4U', 23, 34, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '2L', 23, 30, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '27L', 23, 11, 6, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '13L', 23, 8, 6, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 24, 1, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 24, 39, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 24, 2, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 24, 15, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '26L', 24, 4, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 24, 28, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '7L', 24, 5, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '3L', 24, 25, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 24, 12, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 24, 33, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 24, 5, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 24, 38, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 24, 6, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 24, 24, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 24, 10, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '28U', 24, 5, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 24, 1, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 24, 30, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 24, 24, 2, 21).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 25, 34, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 25, 20, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '26L', 25, 25, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '7L', 25, 7, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 25, 32, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 25, 18, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '3L', 25, 40, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 25, 3, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 25, 14, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 25, 10, 20, 25).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 25, 15, 20, 25).createObject() == True
        assert Booking('MH 11 AB 8643', '22U', 26, 33, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '6U', 26, 31, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '30U', 26, 8, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '20L', 26, 9, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '14L', 26, 4, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '11U', 26, 32, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '2L', 26, 37, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '16U', 26, 34, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '7L', 26, 12, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '28U', 26, 33, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '8L', 26, 17, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '10U', 26, 25, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '9L', 26, 34, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '27L', 26, 33, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '13L', 26, 29, 9, 16).createObject() == True
        assert Booking('MH 11 AB 8643', '24U', 26, 34, 9, 16).createObject() == True
        assert Booking('MH 5 AB 7650', '24U', 27, 3, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '13L', 27, 10, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '28U', 27, 6, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '9L', 27, 6, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '5U', 27, 40, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '25L', 27, 7, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '20L', 27, 9, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '8L', 27, 5, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '18U', 27, 31, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '12U', 27, 9, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '17U', 27, 8, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '29U', 27, 26, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '4U', 27, 19, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '16U', 27, 6, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '23U', 27, 14, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '19L', 27, 38, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '1L', 27, 11, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '14L', 27, 32, 1, 11).createObject() == True
        assert Booking('MH 5 AB 7650', '27L', 27, 8, 1, 11).createObject() == True
        assert Booking('MH 12 AB 9096', '11U', 28, 10, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '10U', 28, 7, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '21L', 28, 25, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '16U', 28, 22, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '23U', 28, 7, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '15L', 28, 26, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '9L', 28, 1, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '27L', 28, 9, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '5U', 28, 13, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '17U', 28, 36, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '12U', 28, 9, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '2L', 28, 19, 5, 8).createObject() == True
        assert Booking('MH 12 AB 9096', '26L', 28, 18, 5, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '11U', 29, 8, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '4U', 29, 24, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '20L', 29, 17, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '16U', 29, 17, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '21L', 29, 27, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '24U', 29, 31, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '12U', 29, 16, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '2L', 29, 21, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '13L', 29, 26, 23, 9).createObject() == True
        assert Booking('MH 11 AB 7989', '26L', 29, 39, 23, 9).createObject() == True
        assert Booking('MH 11 AB 8643', '16U', 30, 20, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '8L', 30, 7, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '20L', 30, 36, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '13L', 30, 23, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '15L', 30, 25, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '4U', 30, 30, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '30U', 30, 17, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '27L', 30, 24, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '25L', 30, 39, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '23U', 30, 12, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '10U', 30, 14, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '18U', 30, 13, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '2L', 30, 3, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '26L', 30, 3, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '7L', 30, 28, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '12U', 30, 27, 18, 23).createObject() == True
        assert Booking('MH 11 AB 8643', '5U', 30, 15, 18, 23).createObject() == True
        assert Booking('MH 12 AB 9096', '12U', 31, 3, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '30U', 31, 16, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '10U', 31, 40, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '16U', 31, 5, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '13L', 31, 9, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '22U', 31, 9, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '28U', 31, 35, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '17U', 31, 34, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '18U', 31, 27, 20, 22).createObject() == True
        assert Booking('MH 12 AB 9096', '29U', 31, 39, 20, 22).createObject() == True
        assert Booking('MH 8 AB 6980', '20L', 32, 25, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '21L', 32, 21, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '6U', 32, 15, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '5U', 32, 2, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '10U', 32, 1, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '9L', 32, 14, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '23U', 32, 9, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '14L', 32, 1, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '13L', 32, 17, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '8L', 32, 37, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '26L', 32, 10, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '19L', 32, 16, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '12U', 32, 37, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '25L', 32, 17, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '4U', 32, 16, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '11U', 32, 13, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '7L', 32, 28, 4, 28).createObject() == True
        assert Booking('MH 8 AB 6980', '27L', 32, 2, 4, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '3L', 33, 14, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '21L', 33, 10, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '30U', 33, 19, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '29U', 33, 28, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '20L', 33, 28, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '7L', 33, 3, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '27L', 33, 33, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '8L', 33, 25, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '10U', 33, 29, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '17U', 33, 31, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '13L', 33, 35, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '19L', 33, 14, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '24U', 33, 30, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '25L', 33, 19, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '16U', 33, 29, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '28U', 33, 33, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '9L', 33, 36, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '15L', 33, 38, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '5U', 33, 7, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '1L', 33, 10, 15, 28).createObject() == True
        assert Booking('MH 15 AB 9478', '4U', 34, 1, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '20L', 34, 2, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '1L', 34, 19, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '14L', 34, 16, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '27L', 34, 29, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '7L', 34, 31, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '21L', 34, 28, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '5U', 34, 8, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '18U', 34, 6, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '12U', 34, 23, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '28U', 34, 40, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '23U', 34, 36, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '9L', 34, 14, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '11U', 34, 6, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '22U', 34, 1, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '13L', 34, 10, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '6U', 34, 4, 12, 4).createObject() == True
        assert Booking('MH 15 AB 9478', '17U', 34, 22, 12, 4).createObject() == True
        assert Booking('MH 7 AB 6536', '26L', 35, 14, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '7L', 35, 35, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '18U', 35, 39, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '14L', 35, 17, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '6U', 35, 8, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '2L', 35, 39, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '12U', 35, 35, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '19L', 35, 37, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '22U', 35, 17, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '5U', 35, 40, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '21L', 35, 19, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '24U', 35, 32, 19, 1).createObject() == True
        assert Booking('MH 7 AB 6536', '23U', 35, 12, 19, 1).createObject() == True
        assert Booking('MH 11 AB 7659', '29U', 36, 25, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '1L', 36, 21, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '11U', 36, 24, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '27L', 36, 4, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '24U', 36, 28, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '21L', 36, 4, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '3L', 36, 23, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '23U', 36, 32, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '16U', 36, 32, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '22U', 36, 9, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '17U', 36, 4, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '19L', 36, 2, 28, 14).createObject() == True
        assert Booking('MH 11 AB 7659', '4U', 36, 30, 28, 14).createObject() == True
        assert Booking('MH 9 AB 8797', '1L', 37, 2, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '2L', 37, 29, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '28U', 37, 13, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '10U', 37, 9, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '5U', 37, 23, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '14L', 37, 19, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '20L', 37, 24, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '18U', 37, 1, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '22U', 37, 6, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '23U', 37, 33, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '17U', 37, 30, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '24U', 37, 28, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '30U', 37, 13, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '27L', 37, 15, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '13L', 37, 37, 14, 9).createObject() == True
        assert Booking('MH 9 AB 8797', '9L', 37, 22, 14, 9).createObject() == True
        assert Booking('MH 16 AB 7740', '10U', 38, 30, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '30U', 38, 30, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '18U', 38, 34, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '12U', 38, 12, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '16U', 38, 1, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '4U', 38, 5, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '20L', 38, 1, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '23U', 38, 3, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 38, 25, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '13L', 38, 11, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '15L', 38, 6, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '21L', 38, 6, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '5U', 38, 4, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 38, 39, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '25L', 38, 22, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '6U', 38, 36, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 38, 3, 6, 10).createObject() == True
        assert Booking('MH 16 AB 7740', '3L', 38, 13, 6, 10).createObject() == True
        assert Booking('MH 20 AB 8094', '21L', 39, 22, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '2L', 39, 37, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '26L', 39, 34, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '24U', 39, 22, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '22U', 39, 22, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '25L', 39, 21, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '15L', 39, 12, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '8L', 39, 40, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '28U', 39, 26, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '10U', 39, 34, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '11U', 39, 37, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '16U', 39, 29, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '12U', 39, 25, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '27L', 39, 24, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '4U', 39, 7, 10, 24).createObject() == True
        assert Booking('MH 20 AB 8094', '30U', 39, 30, 10, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '23U', 40, 21, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '19L', 40, 17, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '5U', 40, 38, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '8L', 40, 39, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 40, 17, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '7L', 40, 32, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '13L', 40, 4, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '3L', 40, 13, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '10U', 40, 4, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '14L', 40, 36, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '27L', 40, 17, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '28U', 40, 31, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '9L', 40, 9, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 40, 5, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '25L', 40, 30, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '6U', 40, 2, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '4U', 40, 3, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '30U', 40, 27, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '16U', 40, 30, 20, 19).createObject() == True
        assert Booking('MH 18 AB 7004', '20L', 40, 20, 20, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '21L', 41, 14, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '1L', 41, 12, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '8L', 41, 31, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '10U', 41, 26, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '27L', 41, 3, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '26L', 41, 13, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '14L', 41, 39, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '23U', 41, 27, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '19L', 41, 2, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '17U', 41, 23, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '5U', 41, 4, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '6U', 41, 31, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '28U', 41, 10, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '15L', 41, 8, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '13L', 41, 17, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '30U', 41, 29, 2, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '3L', 41, 39, 2, 19).createObject() == True
        assert Booking('MH 16 AB 7740', '22U', 42, 32, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '16U', 42, 8, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '24U', 42, 40, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '29U', 42, 40, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '3L', 42, 25, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 42, 33, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '19L', 42, 13, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '23U', 42, 36, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '10U', 42, 22, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '15L', 42, 36, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 42, 8, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 42, 40, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '17U', 42, 21, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 42, 28, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '13L', 42, 22, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '5U', 42, 25, 8, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '21L', 42, 24, 8, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '24U', 43, 29, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 43, 33, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '4U', 43, 3, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 43, 25, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 43, 17, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 43, 28, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 43, 1, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 43, 24, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 43, 19, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 43, 2, 6, 9).createObject() == True
        assert Booking('MH 17 AB 9316', '7L', 43, 23, 6, 9).createObject() == True
        assert Booking('MH 11 AB 9332', '23U', 44, 27, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 44, 5, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 44, 7, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '8L', 44, 9, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 44, 31, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 44, 20, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 44, 16, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '30U', 44, 19, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 44, 40, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 44, 29, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '7L', 44, 15, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 44, 13, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '6U', 44, 7, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 44, 25, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '28U', 44, 24, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '1L', 44, 7, 9, 5).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 44, 3, 9, 5).createObject() == True
        assert Booking('MH 18 AB 7004', '6U', 45, 35, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '28U', 45, 5, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '26L', 45, 27, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '4U', 45, 21, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 45, 34, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '2L', 45, 20, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 45, 28, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '21L', 45, 24, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '17U', 45, 1, 13, 4).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 45, 24, 13, 4).createObject() == True
        assert Booking('MH 8 AB 5155', '1L', 46, 16, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '16U', 46, 26, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '18U', 46, 33, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '8L', 46, 7, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '7L', 46, 33, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '19L', 46, 4, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '26L', 46, 17, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '11U', 46, 7, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '23U', 46, 2, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '4U', 46, 11, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '3L', 46, 25, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '5U', 46, 31, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '12U', 46, 16, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '2L', 46, 25, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '14L', 46, 23, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '22U', 46, 2, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '30U', 46, 8, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '20L', 46, 14, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '21L', 46, 39, 12, 24).createObject() == True
        assert Booking('MH 8 AB 5155', '27L', 46, 20, 12, 24).createObject() == True
        assert Booking('MH 10 AB 5575', '17U', 47, 8, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '4U', 47, 23, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '5U', 47, 14, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '9L', 47, 20, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 47, 24, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '12U', 47, 34, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 47, 4, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '10U', 47, 30, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '16U', 47, 6, 14, 3).createObject() == True
        assert Booking('MH 10 AB 5575', '20L', 47, 39, 14, 3).createObject() == True
        assert Booking('MH 5 AB 6693', '27L', 48, 35, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '21L', 48, 24, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '18U', 48, 19, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '8L', 48, 37, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '23U', 48, 5, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '9L', 48, 28, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '6U', 48, 39, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '12U', 48, 12, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '17U', 48, 16, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '2L', 48, 30, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '13L', 48, 17, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '25L', 48, 30, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '7L', 48, 28, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '1L', 48, 18, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '11U', 48, 25, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '15L', 48, 28, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '24U', 48, 39, 4, 5).createObject() == True
        assert Booking('MH 5 AB 6693', '28U', 48, 7, 4, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 49, 17, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 49, 18, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 49, 8, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 49, 38, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 49, 26, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '16U', 49, 6, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 49, 21, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '21L', 49, 22, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 49, 6, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 49, 34, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 49, 38, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 49, 19, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '3L', 49, 23, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 49, 36, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 49, 23, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 49, 3, 10, 3).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 49, 23, 10, 3).createObject() == True
        assert Booking('MH 16 AB 7740', '27L', 50, 17, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '29U', 50, 17, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '24U', 50, 28, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '15L', 50, 5, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '13L', 50, 10, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 50, 30, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 50, 22, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '4U', 50, 40, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 50, 15, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '14L', 50, 16, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '30U', 50, 14, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '10U', 50, 35, 14, 28).createObject() == True
        assert Booking('MH 16 AB 7740', '18U', 50, 13, 14, 28).createObject() == True
        assert Booking('MH 19 AB 8932', '21L', 51, 39, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '12U', 51, 20, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '4U', 51, 38, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '17U', 51, 39, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '2L', 51, 18, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '10U', 51, 30, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '29U', 51, 32, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '28U', 51, 3, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '27L', 51, 40, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '6U', 51, 20, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '3L', 51, 4, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '23U', 51, 30, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '16U', 51, 13, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '22U', 51, 4, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '26L', 51, 38, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '7L', 51, 34, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '1L', 51, 32, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '5U', 51, 6, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '14L', 51, 15, 11, 13).createObject() == True
        assert Booking('MH 9 AB 8308', '20L', 52, 35, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '9L', 52, 36, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '5U', 52, 17, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '4U', 52, 12, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '7L', 52, 1, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '30U', 52, 14, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '27L', 52, 29, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '29U', 52, 31, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '14L', 52, 1, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '16U', 52, 30, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '12U', 52, 14, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '17U', 52, 3, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '13L', 52, 33, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 52, 16, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 52, 28, 2, 19).createObject() == True
        assert Booking('MH 9 AB 8308', '9L', 53, 35, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '2L', 53, 21, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '15L', 53, 17, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '25L', 53, 8, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 53, 34, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '10U', 53, 20, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '11U', 53, 25, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '13L', 53, 38, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '4U', 53, 15, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '18U', 53, 39, 9, 11).createObject() == True
        assert Booking('MH 9 AB 8308', '16U', 53, 31, 9, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '24U', 54, 3, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '28U', 54, 5, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '17U', 54, 17, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '13L', 54, 9, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '7L', 54, 8, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '21L', 54, 39, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '1L', 54, 23, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '14L', 54, 39, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '20L', 54, 1, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '4U', 54, 23, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '9L', 54, 1, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '6U', 54, 11, 12, 11).createObject() == True
        assert Booking('MH 6 AB 5509', '23U', 54, 8, 12, 11).createObject() == True
        assert Booking('MH 11 AB 5703', '21L', 55, 35, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '14L', 55, 22, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '18U', 55, 12, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '19L', 55, 10, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '6U', 55, 5, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '22U', 55, 14, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '9L', 55, 37, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '26L', 55, 40, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '4U', 55, 31, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '25L', 55, 25, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '5U', 55, 14, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '17U', 55, 1, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '3L', 55, 25, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '15L', 55, 5, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '28U', 55, 5, 29, 21).createObject() == True
        assert Booking('MH 11 AB 5703', '13L', 55, 13, 29, 21).createObject() == True
        assert Booking('MH 19 AB 5367', '2L', 56, 14, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '26L', 56, 30, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '30U', 56, 29, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '11U', 56, 8, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '4U', 56, 29, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '24U', 56, 9, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '15L', 56, 14, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '18U', 56, 26, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '7L', 56, 26, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '29U', 56, 14, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '22U', 56, 15, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '3L', 56, 26, 27, 22).createObject() == True
        assert Booking('MH 19 AB 5367', '5U', 56, 5, 27, 22).createObject() == True
        assert Booking('MH 13 AB 9993', '7L', 57, 31, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '13L', 57, 28, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '23U', 57, 32, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '3L', 57, 4, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '4U', 57, 25, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '30U', 57, 14, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '26L', 57, 39, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '14L', 57, 16, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '15L', 57, 35, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '10U', 57, 12, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '19L', 57, 21, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '8L', 57, 1, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '2L', 57, 17, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '25L', 57, 13, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '6U', 57, 5, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '5U', 57, 33, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '1L', 57, 32, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '22U', 57, 18, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '11U', 57, 14, 24, 19).createObject() == True
        assert Booking('MH 13 AB 9993', '20L', 57, 27, 24, 19).createObject() == True
        assert Booking('MH 17 AB 5987', '24U', 58, 27, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '5U', 58, 20, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '15L', 58, 1, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '30U', 58, 16, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '12U', 58, 34, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '6U', 58, 9, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '7L', 58, 30, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '13L', 58, 22, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '22U', 58, 25, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '11U', 58, 8, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '10U', 58, 18, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '18U', 58, 19, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '16U', 58, 20, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '29U', 58, 6, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '2L', 58, 16, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '8L', 58, 7, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '28U', 58, 9, 16, 1).createObject() == True
        assert Booking('MH 17 AB 5987', '4U', 58, 20, 16, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '7L', 59, 15, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '16U', 59, 4, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '8L', 59, 34, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '20L', 59, 15, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '27L', 59, 39, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '10U', 59, 11, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '19L', 59, 25, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '25L', 59, 39, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '6U', 59, 37, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '26L', 59, 29, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '5U', 59, 8, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '18U', 59, 3, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '1L', 59, 18, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '9L', 59, 7, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '3L', 59, 10, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '12U', 59, 12, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '21L', 59, 21, 22, 25).createObject() == True
        assert Booking('MH 16 AB 7222', '28U', 59, 26, 22, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '7L', 60, 16, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '8L', 60, 40, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '22U', 60, 36, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '9L', 60, 19, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '1L', 60, 16, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '14L', 60, 37, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '23U', 60, 9, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '16U', 60, 39, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '26L', 60, 10, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '2L', 60, 25, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '17U', 60, 36, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '5U', 60, 3, 24, 25).createObject() == True
        assert Booking('MH 11 AB 7989', '30U', 60, 18, 24, 25).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 61, 12, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 61, 17, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '16U', 61, 3, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '17U', 61, 39, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '5U', 61, 12, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '14L', 61, 31, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '3L', 61, 12, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '12U', 61, 25, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '18U', 61, 9, 7, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 61, 7, 7, 29).createObject() == True
        assert Booking('MH 19 AB 8932', '22U', 62, 20, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '13L', 62, 16, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '27L', 62, 8, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '14L', 62, 23, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '6U', 62, 19, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '23U', 62, 24, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '7L', 62, 23, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '1L', 62, 16, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '24U', 62, 9, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '19L', 62, 6, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '10U', 62, 15, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '12U', 62, 24, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '2L', 62, 7, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '9L', 62, 2, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '5U', 62, 6, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '26L', 62, 25, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '15L', 62, 19, 3, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '20L', 62, 14, 3, 17).createObject() == True
        assert Booking('MH 17 AB 8217', '25L', 63, 27, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '5U', 63, 32, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '14L', 63, 13, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '20L', 63, 23, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '28U', 63, 5, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '16U', 63, 12, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '23U', 63, 25, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '17U', 63, 34, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '3L', 63, 4, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '21L', 63, 6, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '24U', 63, 6, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '7L', 63, 22, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '18U', 63, 29, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '26L', 63, 26, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '8L', 63, 11, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '1L', 63, 34, 13, 16).createObject() == True
        assert Booking('MH 17 AB 8217', '9L', 63, 19, 13, 16).createObject() == True
        assert Booking('MH 5 AB 6693', '17U', 64, 2, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '21L', 64, 40, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '16U', 64, 1, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '25L', 64, 2, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '28U', 64, 22, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '24U', 64, 4, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '11U', 64, 25, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '2L', 64, 1, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '7L', 64, 28, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '22U', 64, 3, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '23U', 64, 24, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '18U', 64, 20, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '13L', 64, 27, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '20L', 64, 24, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '8L', 64, 1, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '4U', 64, 6, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '19L', 64, 7, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '30U', 64, 3, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '10U', 64, 32, 28, 26).createObject() == True
        assert Booking('MH 5 AB 6693', '29U', 64, 31, 28, 26).createObject() == True
        assert Booking('MH 6 AB 5509', '5U', 65, 5, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '3L', 65, 4, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '18U', 65, 13, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '8L', 65, 17, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '2L', 65, 3, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '14L', 65, 35, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '23U', 65, 22, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '30U', 65, 28, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '26L', 65, 11, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '13L', 65, 35, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '17U', 65, 11, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '12U', 65, 27, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '20L', 65, 33, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '9L', 65, 28, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '21L', 65, 14, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '22U', 65, 20, 17, 19).createObject() == True
        assert Booking('MH 6 AB 5509', '1L', 65, 35, 17, 19).createObject() == True
        assert Booking('MH 19 AB 8198', '23U', 66, 2, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '5U', 66, 37, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '16U', 66, 27, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '18U', 66, 40, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '17U', 66, 36, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '11U', 66, 20, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '4U', 66, 24, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '6U', 66, 22, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '20L', 66, 29, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '10U', 66, 19, 9, 11).createObject() == True
        assert Booking('MH 19 AB 8198', '29U', 66, 33, 9, 11).createObject() == True
        assert Booking('MH 8 AB 8272', '25L', 67, 12, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '24U', 67, 27, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '6U', 67, 3, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '15L', 67, 17, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '9L', 67, 21, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '7L', 67, 10, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '20L', 67, 18, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '22U', 67, 2, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '11U', 67, 15, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '29U', 67, 32, 2, 26).createObject() == True
        assert Booking('MH 8 AB 8272', '5U', 67, 20, 2, 26).createObject() == True
        assert Booking('MH 10 AB 5575', '21L', 68, 8, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '29U', 68, 26, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '7L', 68, 24, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '14L', 68, 34, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 68, 10, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 68, 24, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 68, 27, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '12U', 68, 28, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '4U', 68, 32, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '2L', 68, 31, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '19L', 68, 13, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '30U', 68, 21, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '10U', 68, 4, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 68, 28, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '22U', 68, 7, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 68, 26, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '13L', 68, 39, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '17U', 68, 37, 28, 17).createObject() == True
        assert Booking('MH 10 AB 5575', '1L', 68, 28, 28, 17).createObject() == True
        assert Booking('MH 8 AB 5155', '22U', 69, 38, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '8L', 69, 9, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '4U', 69, 23, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '27L', 69, 2, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '24U', 69, 3, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '11U', 69, 17, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '6U', 69, 22, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '30U', 69, 38, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '5U', 69, 34, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '9L', 69, 16, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '20L', 69, 26, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '13L', 69, 27, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '14L', 69, 16, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '28U', 69, 32, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '2L', 69, 9, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '26L', 69, 13, 14, 7).createObject() == True
        assert Booking('MH 8 AB 5155', '18U', 69, 7, 14, 7).createObject() == True
        assert Booking('MH 6 AB 5509', '18U', 70, 32, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '11U', 70, 18, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '21L', 70, 36, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '28U', 70, 4, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '12U', 70, 10, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '26L', 70, 37, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '1L', 70, 21, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '23U', 70, 12, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '3L', 70, 16, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '20L', 70, 26, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '29U', 70, 5, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '8L', 70, 27, 22, 29).createObject() == True
        assert Booking('MH 6 AB 5509', '7L', 70, 14, 22, 29).createObject() == True
        assert Booking('MH 16 AB 7222', '2L', 71, 18, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '24U', 71, 23, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '20L', 71, 9, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '12U', 71, 32, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '23U', 71, 31, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '26L', 71, 22, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '21L', 71, 19, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '15L', 71, 17, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '3L', 71, 19, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '27L', 71, 36, 4, 1).createObject() == True
        assert Booking('MH 16 AB 7222', '11U', 71, 32, 4, 1).createObject() == True
        assert Booking('MH 12 AB 9096', '15L', 72, 19, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '27L', 72, 25, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '12U', 72, 26, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '9L', 72, 7, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '11U', 72, 40, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '8L', 72, 38, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '3L', 72, 21, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '17U', 72, 12, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '1L', 72, 8, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '7L', 72, 31, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '5U', 72, 34, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '13L', 72, 17, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '23U', 72, 29, 18, 25).createObject() == True
        assert Booking('MH 12 AB 9096', '28U', 72, 26, 18, 25).createObject() == True
        assert Booking('MH 19 AB 5367', '27L', 73, 29, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '3L', 73, 6, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '26L', 73, 35, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '1L', 73, 19, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '6U', 73, 1, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '29U', 73, 9, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '5U', 73, 34, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '28U', 73, 13, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '21L', 73, 21, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '2L', 73, 24, 21, 20).createObject() == True
        assert Booking('MH 19 AB 5367', '30U', 73, 13, 21, 20).createObject() == True
        assert Booking('MH 8 AB 6980', '26L', 74, 29, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '15L', 74, 9, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '13L', 74, 26, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '29U', 74, 13, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '11U', 74, 10, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '1L', 74, 1, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '4U', 74, 6, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '25L', 74, 40, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '20L', 74, 22, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '10U', 74, 22, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '24U', 74, 39, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '27L', 74, 9, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '9L', 74, 35, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '30U', 74, 20, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '18U', 74, 8, 16, 8).createObject() == True
        assert Booking('MH 8 AB 6980', '16U', 74, 6, 16, 8).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 75, 33, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 75, 21, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '3L', 75, 9, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 75, 8, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '12U', 75, 33, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 75, 20, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '16U', 75, 37, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 75, 5, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 75, 3, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 75, 37, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 75, 12, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 75, 18, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 75, 17, 28, 5).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 75, 6, 28, 5).createObject() == True
        assert Booking('MH 10 AB 9617', '18U', 76, 33, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '30U', 76, 32, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '22U', 76, 24, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '14L', 76, 19, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '3L', 76, 19, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '25L', 76, 21, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '24U', 76, 13, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '7L', 76, 30, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '27L', 76, 28, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '15L', 76, 14, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '5U', 76, 34, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '11U', 76, 31, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '16U', 76, 6, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '29U', 76, 7, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '28U', 76, 5, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '17U', 76, 18, 7, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '9L', 76, 11, 7, 2).createObject() == True
        assert Booking('MH 12 AB 8578', '22U', 77, 27, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '20L', 77, 11, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '2L', 77, 32, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '19L', 77, 14, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '11U', 77, 4, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '6U', 77, 28, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '25L', 77, 22, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '27L', 77, 14, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '1L', 77, 1, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '16U', 77, 33, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '30U', 77, 28, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '21L', 77, 6, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '4U', 77, 8, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '8L', 77, 10, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '5U', 77, 35, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '24U', 77, 20, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '14L', 77, 3, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '9L', 77, 8, 26, 5).createObject() == True
        assert Booking('MH 12 AB 8578', '12U', 77, 20, 26, 5).createObject() == True
        assert Booking('MH 5 AB 7650', '9L', 78, 22, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '27L', 78, 23, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '29U', 78, 4, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '24U', 78, 23, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '19L', 78, 36, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '16U', 78, 8, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '11U', 78, 26, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '30U', 78, 36, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '28U', 78, 39, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '7L', 78, 6, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '2L', 78, 33, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '14L', 78, 29, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '25L', 78, 26, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '15L', 78, 22, 15, 7).createObject() == True
        assert Booking('MH 5 AB 7650', '13L', 78, 8, 15, 7).createObject() == True
        assert Booking('MH 19 AB 8198', '20L', 79, 15, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '27L', 79, 10, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '18U', 79, 20, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '26L', 79, 24, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '7L', 79, 20, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '29U', 79, 17, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '9L', 79, 28, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '19L', 79, 5, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '2L', 79, 36, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '21L', 79, 36, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '17U', 79, 40, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '15L', 79, 28, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '3L', 79, 6, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '5U', 79, 7, 10, 16).createObject() == True
        assert Booking('MH 19 AB 8198', '14L', 79, 33, 10, 16).createObject() == True
        assert Booking('MH 11 AB 9332', '1L', 80, 11, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 80, 35, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 80, 19, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 80, 25, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 80, 40, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 80, 5, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 80, 4, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '19L', 80, 17, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '3L', 80, 38, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 80, 19, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 80, 10, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '22U', 80, 37, 4, 22).createObject() == True
        assert Booking('MH 11 AB 9332', '21L', 80, 35, 4, 22).createObject() == True
        assert Booking('MH 17 AB 5987', '15L', 81, 40, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '25L', 81, 3, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '3L', 81, 30, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '11U', 81, 7, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '13L', 81, 36, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '24U', 81, 3, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '19L', 81, 5, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '7L', 81, 14, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '18U', 81, 38, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '4U', 81, 15, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '14L', 81, 9, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '21L', 81, 3, 18, 9).createObject() == True
        assert Booking('MH 17 AB 5987', '9L', 81, 3, 18, 9).createObject() == True
        assert Booking('MH 14 AB 5997', '8L', 82, 35, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '14L', 82, 28, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '19L', 82, 15, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '22U', 82, 4, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '30U', 82, 10, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '12U', 82, 17, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '28U', 82, 21, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '13L', 82, 15, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '9L', 82, 40, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '29U', 82, 10, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '26L', 82, 34, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '11U', 82, 23, 8, 1).createObject() == True
        assert Booking('MH 14 AB 5997', '10U', 82, 4, 8, 1).createObject() == True
        assert Booking('MH 12 AB 9096', '7L', 83, 3, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '1L', 83, 20, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '17U', 83, 39, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '20L', 83, 2, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '9L', 83, 9, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '28U', 83, 6, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '30U', 83, 13, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '19L', 83, 12, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '11U', 83, 7, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '6U', 83, 29, 28, 26).createObject() == True
        assert Booking('MH 12 AB 9096', '18U', 83, 33, 28, 26).createObject() == True
        assert Booking('MH 9 AB 8797', '26L', 84, 22, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '24U', 84, 10, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '10U', 84, 6, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '9L', 84, 24, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '11U', 84, 2, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '22U', 84, 5, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '8L', 84, 32, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '30U', 84, 37, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '6U', 84, 16, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '7L', 84, 26, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '21L', 84, 33, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '1L', 84, 8, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '20L', 84, 32, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '28U', 84, 25, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '3L', 84, 7, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '23U', 84, 2, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '12U', 84, 21, 19, 17).createObject() == True
        assert Booking('MH 9 AB 8797', '16U', 84, 13, 19, 17).createObject() == True
        assert Booking('MH 12 AB 8578', '19L', 85, 13, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '26L', 85, 20, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '3L', 85, 31, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '6U', 85, 40, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '29U', 85, 11, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '17U', 85, 4, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '25L', 85, 9, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '9L', 85, 28, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '5U', 85, 34, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '28U', 85, 16, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '18U', 85, 32, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '24U', 85, 24, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '27L', 85, 25, 16, 15).createObject() == True
        assert Booking('MH 12 AB 8578', '15L', 85, 12, 16, 15).createObject() == True
        assert Booking('MH 14 AB 6870', '11U', 86, 26, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '9L', 86, 20, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '27L', 86, 16, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '5U', 86, 14, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '2L', 86, 4, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '6U', 86, 29, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '19L', 86, 38, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '15L', 86, 25, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '12U', 86, 26, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '29U', 86, 14, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '14L', 86, 16, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '28U', 86, 40, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '22U', 86, 34, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '4U', 86, 28, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '17U', 86, 25, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '26L', 86, 13, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '23U', 86, 29, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6870', '18U', 86, 3, 28, 12).createObject() == True
        assert Booking('MH 14 AB 6518', '7L', 87, 8, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '20L', 87, 28, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '19L', 87, 28, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '13L', 87, 23, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '11U', 87, 34, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '12U', 87, 32, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '2L', 87, 32, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '15L', 87, 24, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '30U', 87, 28, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6518', '28U', 87, 1, 6, 4).createObject() == True
        assert Booking('MH 14 AB 6870', '22U', 88, 11, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '1L', 88, 37, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '27L', 88, 6, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '14L', 88, 3, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '10U', 88, 20, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '20L', 88, 5, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '30U', 88, 33, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '3L', 88, 11, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '19L', 88, 16, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '4U', 88, 31, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '8L', 88, 40, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '7L', 88, 17, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '9L', 88, 16, 20, 17).createObject() == True
        assert Booking('MH 14 AB 6870', '28U', 88, 14, 20, 17).createObject() == True
        assert Booking('MH 14 AB 9684', '23U', 89, 12, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '17U', 89, 28, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '22U', 89, 33, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '18U', 89, 9, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '21L', 89, 5, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '9L', 89, 31, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '3L', 89, 18, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '26L', 89, 15, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '12U', 89, 25, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '14L', 89, 9, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '25L', 89, 38, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '10U', 89, 36, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '4U', 89, 20, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '1L', 89, 40, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '19L', 89, 1, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '20L', 89, 26, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '5U', 89, 27, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '27L', 89, 13, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '13L', 89, 26, 5, 4).createObject() == True
        assert Booking('MH 14 AB 9684', '8L', 89, 12, 5, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '11U', 90, 13, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '10U', 90, 32, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '1L', 90, 4, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '7L', 90, 39, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '14L', 90, 17, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '6U', 90, 37, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '24U', 90, 13, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '4U', 90, 5, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '5U', 90, 27, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '28U', 90, 32, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '29U', 90, 25, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '27L', 90, 36, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '20L', 90, 9, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '18U', 90, 16, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '3L', 90, 13, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '15L', 90, 1, 27, 7).createObject() == True
        assert Booking('MH 12 AB 5440', '26L', 90, 30, 27, 7).createObject() == True
        assert Booking('MH 5 AB 6693', '18U', 91, 9, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '23U', 91, 14, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '3L', 91, 24, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '2L', 91, 22, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '30U', 91, 3, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '17U', 91, 21, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '19L', 91, 23, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '26L', 91, 12, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '10U', 91, 17, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '8L', 91, 36, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '16U', 91, 3, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '27L', 91, 37, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '12U', 91, 3, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '7L', 91, 21, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '14L', 91, 25, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '13L', 91, 21, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '11U', 91, 23, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '21L', 91, 28, 7, 29).createObject() == True
        assert Booking('MH 5 AB 6693', '1L', 91, 36, 7, 29).createObject() == True
        assert Booking('MH 18 AB 7004', '22U', 92, 40, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '10U', 92, 35, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '9L', 92, 5, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '19L', 92, 20, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '17U', 92, 8, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '20L', 92, 17, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '5U', 92, 36, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '8L', 92, 38, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 92, 2, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 92, 31, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '7L', 92, 13, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '13L', 92, 7, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '3L', 92, 6, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '29U', 92, 6, 2, 10).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 92, 12, 2, 10).createObject() == True
        assert Booking('MH 12 AB 8578', '10U', 93, 10, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '2L', 93, 38, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '26L', 93, 34, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '9L', 93, 35, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '23U', 93, 22, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '8L', 93, 33, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '7L', 93, 40, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '1L', 93, 6, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '6U', 93, 23, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '5U', 93, 2, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '15L', 93, 33, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '3L', 93, 10, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '27L', 93, 7, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '29U', 93, 35, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '25L', 93, 1, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '20L', 93, 14, 21, 4).createObject() == True
        assert Booking('MH 12 AB 8578', '19L', 93, 14, 21, 4).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 94, 20, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '27L', 94, 24, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '12U', 94, 39, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '25L', 94, 27, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '14L', 94, 27, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 94, 23, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '5U', 94, 4, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '22U', 94, 40, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '28U', 94, 34, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '16U', 94, 23, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 94, 15, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 94, 16, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '29U', 94, 24, 22, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 94, 32, 22, 12).createObject() == True
        assert Booking('MH 6 AB 5509', '4U', 95, 14, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '28U', 95, 13, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '30U', 95, 21, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '13L', 95, 37, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '9L', 95, 25, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '19L', 95, 17, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '29U', 95, 21, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '10U', 95, 11, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '6U', 95, 37, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '5U', 95, 10, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '25L', 95, 40, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '20L', 95, 12, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '18U', 95, 35, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '8L', 95, 5, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '24U', 95, 24, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '12U', 95, 16, 10, 2).createObject() == True
        assert Booking('MH 6 AB 5509', '27L', 95, 17, 10, 2).createObject() == True
        assert Booking('MH 12 AB 7062', '17U', 96, 34, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '23U', 96, 9, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '30U', 96, 10, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '16U', 96, 25, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '20L', 96, 34, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '15L', 96, 29, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '6U', 96, 31, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '8L', 96, 40, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '21L', 96, 39, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '26L', 96, 13, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '7L', 96, 28, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '27L', 96, 8, 6, 25).createObject() == True
        assert Booking('MH 12 AB 7062', '11U', 96, 33, 6, 25).createObject() == True
        assert Booking('MH 8 AB 8272', '7L', 97, 13, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '22U', 97, 8, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '26L', 97, 11, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '19L', 97, 25, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '14L', 97, 34, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '6U', 97, 25, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '1L', 97, 32, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '20L', 97, 23, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '29U', 97, 26, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '23U', 97, 25, 21, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '15L', 97, 36, 21, 14).createObject() == True
        assert Booking('MH 18 AB 7004', '1L', 98, 26, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '27L', 98, 35, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '28U', 98, 13, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '15L', 98, 31, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '10U', 98, 3, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '22U', 98, 7, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '26L', 98, 34, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '17U', 98, 33, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '12U', 98, 20, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '3L', 98, 10, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '30U', 98, 1, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '11U', 98, 33, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '24U', 98, 27, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '29U', 98, 11, 16, 24).createObject() == True
        assert Booking('MH 18 AB 7004', '21L', 98, 24, 16, 24).createObject() == True
        assert Booking('MH 11 AB 7989', '15L', 99, 13, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '6U', 99, 12, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '24U', 99, 4, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '5U', 99, 4, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '12U', 99, 13, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '17U', 99, 29, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '14L', 99, 32, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '7L', 99, 31, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '16U', 99, 34, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '19L', 99, 10, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '2L', 99, 39, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '30U', 99, 2, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '3L', 99, 3, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '20L', 99, 28, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '1L', 99, 4, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '9L', 99, 11, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '10U', 99, 3, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '28U', 99, 35, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '26L', 99, 20, 29, 14).createObject() == True
        assert Booking('MH 11 AB 7989', '4U', 99, 4, 29, 14).createObject() == True
        assert Booking('MH 14 AB 5997', '5U', 100, 28, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '17U', 100, 40, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '18U', 100, 31, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '26L', 100, 24, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '13L', 100, 2, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '11U', 100, 4, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '23U', 100, 3, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '25L', 100, 32, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '24U', 100, 13, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '3L', 100, 14, 6, 21).createObject() == True
        assert Booking('MH 14 AB 5997', '16U', 100, 8, 6, 21).createObject() == True
        assert Booking('MH 13 AB 9993', '8L', 101, 39, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '27L', 101, 32, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '24U', 101, 35, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '9L', 101, 6, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '28U', 101, 39, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '1L', 101, 11, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '16U', 101, 30, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '2L', 101, 11, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '26L', 101, 7, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '12U', 101, 2, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '14L', 101, 23, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '17U', 101, 6, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '4U', 101, 31, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '22U', 101, 7, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '19L', 101, 8, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '3L', 101, 25, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '13L', 101, 32, 8, 7).createObject() == True
        assert Booking('MH 13 AB 9993', '30U', 101, 29, 8, 7).createObject() == True
        assert Booking('MH 8 AB 6980', '6U', 102, 20, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '28U', 102, 31, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '19L', 102, 4, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '27L', 102, 5, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '7L', 102, 10, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '25L', 102, 2, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '11U', 102, 18, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '12U', 102, 22, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '29U', 102, 31, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '18U', 102, 21, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '16U', 102, 17, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '14L', 102, 15, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '8L', 102, 6, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '22U', 102, 35, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '21L', 102, 16, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '30U', 102, 33, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '1L', 102, 3, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '5U', 102, 30, 10, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '13L', 102, 21, 10, 2).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 103, 34, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '6U', 103, 3, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '10U', 103, 16, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 103, 34, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '2L', 103, 32, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '7L', 103, 37, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '29U', 103, 23, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '19L', 103, 16, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '23U', 103, 40, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 103, 32, 13, 23).createObject() == True
        assert Booking('MH 10 AB 5575', '28U', 103, 25, 13, 23).createObject() == True
        assert Booking('MH 5 AB 6693', '14L', 104, 28, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '26L', 104, 11, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '20L', 104, 33, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '23U', 104, 10, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '30U', 104, 17, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '11U', 104, 27, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '15L', 104, 11, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '24U', 104, 34, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '25L', 104, 5, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '8L', 104, 35, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '13L', 104, 31, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '7L', 104, 26, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '21L', 104, 24, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '17U', 104, 20, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '9L', 104, 14, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '28U', 104, 15, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '10U', 104, 35, 2, 4).createObject() == True
        assert Booking('MH 5 AB 6693', '19L', 104, 21, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '28U', 105, 3, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '2L', 105, 18, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '29U', 105, 15, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '9L', 105, 25, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '15L', 105, 2, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '19L', 105, 1, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '21L', 105, 11, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '8L', 105, 32, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '23U', 105, 13, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '30U', 105, 14, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '13L', 105, 4, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '20L', 105, 39, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '22U', 105, 32, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '17U', 105, 27, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '18U', 105, 22, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '25L', 105, 38, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '3L', 105, 2, 5, 22).createObject() == True
        assert Booking('MH 12 AB 5440', '16U', 105, 7, 5, 22).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 106, 33, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 106, 17, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '24U', 106, 12, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '4U', 106, 16, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '28U', 106, 1, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 106, 6, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 106, 37, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '21L', 106, 9, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 106, 38, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 106, 7, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 106, 13, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 106, 20, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 106, 17, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 106, 15, 29, 17).createObject() == True
        assert Booking('MH 17 AB 9316', '26L', 106, 27, 29, 17).createObject() == True
        assert Booking('MH 9 AB 8308', '2L', 107, 38, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '14L', 107, 5, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 107, 14, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 107, 40, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '23U', 107, 6, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '13L', 107, 17, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '22U', 107, 34, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '19L', 107, 3, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '5U', 107, 4, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '27L', 107, 25, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '4U', 107, 10, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '6U', 107, 10, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '7L', 107, 28, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '20L', 107, 35, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '3L', 107, 12, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '1L', 107, 15, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '8L', 107, 36, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '18U', 107, 11, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '30U', 107, 18, 10, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '10U', 107, 39, 10, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '11U', 108, 3, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '4U', 108, 13, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '29U', 108, 17, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '8L', 108, 29, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '20L', 108, 31, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '19L', 108, 34, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '5U', 108, 8, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '25L', 108, 9, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '16U', 108, 3, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '6U', 108, 10, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 108, 40, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 108, 34, 8, 18).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 108, 34, 8, 18).createObject() == True
        assert Booking('MH 12 AB 7062', '13L', 109, 21, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '26L', 109, 24, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '20L', 109, 21, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '7L', 109, 17, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '16U', 109, 11, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '1L', 109, 17, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '3L', 109, 16, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '18U', 109, 26, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '4U', 109, 22, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '22U', 109, 35, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '28U', 109, 18, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '6U', 109, 17, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '2L', 109, 5, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '21L', 109, 7, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '24U', 109, 13, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '10U', 109, 24, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '25L', 109, 28, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '15L', 109, 16, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '12U', 109, 10, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '30U', 109, 17, 27, 3).createObject() == True
        assert Booking('MH 12 AB 7062', '6U', 110, 23, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '19L', 110, 4, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '29U', 110, 17, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '13L', 110, 24, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '3L', 110, 35, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '2L', 110, 31, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '18U', 110, 16, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '26L', 110, 30, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '12U', 110, 5, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '23U', 110, 3, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '16U', 110, 5, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '5U', 110, 7, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '4U', 110, 6, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '14L', 110, 14, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '20L', 110, 7, 24, 22).createObject() == True
        assert Booking('MH 12 AB 7062', '21L', 110, 8, 24, 22).createObject() == True
        assert Booking('MH 20 AB 8094', '21L', 111, 28, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '22U', 111, 40, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '23U', 111, 11, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '26L', 111, 12, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '17U', 111, 24, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '6U', 111, 35, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '1L', 111, 19, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '16U', 111, 13, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '15L', 111, 11, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '30U', 111, 5, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '7L', 111, 32, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '11U', 111, 1, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '25L', 111, 23, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '14L', 111, 11, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '10U', 111, 13, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '19L', 111, 6, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '29U', 111, 30, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '8L', 111, 23, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '18U', 111, 27, 21, 20).createObject() == True
        assert Booking('MH 20 AB 8094', '5U', 111, 7, 21, 20).createObject() == True
        assert Booking('MH 14 AB 9684', '27L', 112, 8, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '22U', 112, 27, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '16U', 112, 20, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '14L', 112, 28, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '15L', 112, 31, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '5U', 112, 22, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '12U', 112, 27, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '20L', 112, 28, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '30U', 112, 4, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '17U', 112, 29, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '4U', 112, 7, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '9L', 112, 5, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '28U', 112, 4, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '2L', 112, 1, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '3L', 112, 7, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '29U', 112, 38, 6, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '25L', 112, 3, 6, 1).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 113, 31, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 113, 22, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '26L', 113, 5, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '23U', 113, 20, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '11U', 113, 15, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 113, 19, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '21L', 113, 22, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '13L', 113, 30, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '8L', 113, 15, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '28U', 113, 14, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 113, 20, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '6U', 113, 8, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 113, 21, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 113, 14, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 113, 22, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '30U', 113, 5, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '4U', 113, 15, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 113, 28, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '1L', 113, 13, 1, 3).createObject() == True
        assert Booking('MH 11 AB 9332', '19L', 114, 32, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '13L', 114, 32, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 114, 4, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 114, 17, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '21L', 114, 12, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '15L', 114, 20, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '30U', 114, 19, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '9L', 114, 17, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 114, 16, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '4U', 114, 11, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 114, 24, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '20L', 114, 40, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 114, 29, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 114, 34, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 114, 11, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '5U', 114, 38, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '14L', 114, 10, 7, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '11U', 114, 7, 7, 14).createObject() == True
        assert Booking('MH 14 AB 9684', '2L', 115, 25, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '8L', 115, 9, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '28U', 115, 33, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '13L', 115, 37, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '23U', 115, 7, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '12U', 115, 32, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '21L', 115, 37, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '17U', 115, 35, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '15L', 115, 20, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '9L', 115, 24, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '1L', 115, 3, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '24U', 115, 4, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '30U', 115, 22, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '4U', 115, 15, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '20L', 115, 7, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '5U', 115, 22, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '22U', 115, 27, 26, 1).createObject() == True
        assert Booking('MH 14 AB 9684', '16U', 115, 8, 26, 1).createObject() == True
        assert Booking('MH 10 AB 9617', '16U', 116, 7, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '2L', 116, 21, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '12U', 116, 29, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '20L', 116, 15, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '30U', 116, 4, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '18U', 116, 36, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '28U', 116, 1, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '19L', 116, 33, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '15L', 116, 30, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '24U', 116, 14, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '5U', 116, 5, 3, 2).createObject() == True
        assert Booking('MH 10 AB 9617', '8L', 116, 20, 3, 2).createObject() == True
        assert Booking('MH 8 AB 6980', '22U', 117, 17, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '6U', 117, 5, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '10U', 117, 9, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '28U', 117, 29, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '19L', 117, 12, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '9L', 117, 7, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '30U', 117, 28, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '14L', 117, 3, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '20L', 117, 12, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '7L', 117, 34, 18, 16).createObject() == True
        assert Booking('MH 8 AB 6980', '3L', 117, 5, 18, 16).createObject() == True
        assert Booking('MH 13 AB 5137', '7L', 118, 21, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '9L', 118, 29, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '24U', 118, 1, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '27L', 118, 37, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '10U', 118, 15, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '4U', 118, 5, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '12U', 118, 11, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '8L', 118, 16, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '28U', 118, 25, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '21L', 118, 32, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '26L', 118, 26, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '29U', 118, 22, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '20L', 118, 38, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '25L', 118, 1, 15, 28).createObject() == True
        assert Booking('MH 13 AB 5137', '11U', 118, 8, 15, 28).createObject() == True
        assert Booking('MH 9 AB 8308', '15L', 119, 14, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '18U', 119, 15, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '29U', 119, 31, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '3L', 119, 19, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '17U', 119, 34, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '13L', 119, 16, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '24U', 119, 11, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '30U', 119, 39, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '27L', 119, 36, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '4U', 119, 10, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '6U', 119, 17, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '9L', 119, 37, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '5U', 119, 25, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '22U', 119, 12, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '21L', 119, 26, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '8L', 119, 16, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '19L', 119, 26, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '1L', 119, 22, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '12U', 119, 39, 24, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 119, 40, 24, 2).createObject() == True
        assert Booking('MH 19 AB 8198', '3L', 120, 40, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '16U', 120, 1, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '10U', 120, 3, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '29U', 120, 25, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '30U', 120, 23, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '28U', 120, 38, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '13L', 120, 32, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '4U', 120, 26, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '11U', 120, 40, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '25L', 120, 18, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '9L', 120, 25, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '7L', 120, 4, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '22U', 120, 37, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '5U', 120, 19, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '23U', 120, 22, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '24U', 120, 35, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '12U', 120, 20, 2, 24).createObject() == True
        assert Booking('MH 19 AB 8198', '1L', 120, 4, 2, 24).createObject() == True
        assert Booking('MH 8 AB 8272', '9L', 121, 30, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '30U', 121, 22, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '25L', 121, 1, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '16U', 121, 1, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '11U', 121, 4, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '5U', 121, 7, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '14L', 121, 4, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '19L', 121, 4, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '18U', 121, 7, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '26L', 121, 15, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '10U', 121, 15, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '20L', 121, 21, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '7L', 121, 15, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '21L', 121, 14, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '4U', 121, 35, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '3L', 121, 33, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '17U', 121, 5, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '28U', 121, 25, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '2L', 121, 17, 19, 9).createObject() == True
        assert Booking('MH 8 AB 8272', '8L', 121, 30, 19, 9).createObject() == True
        assert Booking('MH 12 AB 7062', '22U', 122, 4, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '27L', 122, 30, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '15L', 122, 30, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '29U', 122, 14, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '21L', 122, 27, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '16U', 122, 15, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '11U', 122, 24, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '24U', 122, 23, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '1L', 122, 8, 27, 17).createObject() == True
        assert Booking('MH 12 AB 7062', '13L', 122, 14, 27, 17).createObject() == True
        assert Booking('MH 19 AB 8932', '2L', 123, 9, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '14L', 123, 11, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '23U', 123, 37, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '9L', 123, 21, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '21L', 123, 29, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '11U', 123, 33, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '3L', 123, 15, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '5U', 123, 34, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '22U', 123, 5, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '18U', 123, 35, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '8L', 123, 12, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '24U', 123, 36, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '16U', 123, 24, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '15L', 123, 34, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '6U', 123, 12, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '1L', 123, 30, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '25L', 123, 22, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '26L', 123, 17, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '30U', 123, 6, 11, 13).createObject() == True
        assert Booking('MH 19 AB 8932', '10U', 123, 9, 11, 13).createObject() == True
        assert Booking('MH 9 AB 8308', '4U', 124, 40, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '13L', 124, 21, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 124, 28, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '16U', 124, 29, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '19L', 124, 5, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 124, 23, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '18U', 124, 10, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '15L', 124, 36, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '1L', 124, 17, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '2L', 124, 11, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '25L', 124, 2, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '29U', 124, 23, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '3L', 124, 31, 27, 2).createObject() == True
        assert Booking('MH 9 AB 8308', '22U', 124, 37, 27, 2).createObject() == True
        assert Booking('MH 17 AB 8217', '24U', 125, 32, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '26L', 125, 21, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '5U', 125, 10, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '7L', 125, 19, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '21L', 125, 17, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '18U', 125, 16, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '3L', 125, 34, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '25L', 125, 4, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '15L', 125, 3, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '16U', 125, 14, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '14L', 125, 23, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '2L', 125, 40, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '13L', 125, 11, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '20L', 125, 1, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '6U', 125, 36, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '23U', 125, 23, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '1L', 125, 25, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '17U', 125, 2, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '27L', 125, 26, 23, 10).createObject() == True
        assert Booking('MH 17 AB 8217', '22U', 125, 24, 23, 10).createObject() == True
        assert Booking('MH 8 AB 8272', '19L', 126, 35, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '12U', 126, 20, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '26L', 126, 22, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '15L', 126, 4, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '24U', 126, 21, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '17U', 126, 39, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '25L', 126, 11, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '20L', 126, 8, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '3L', 126, 39, 12, 16).createObject() == True
        assert Booking('MH 8 AB 8272', '10U', 126, 17, 12, 16).createObject() == True
        assert Booking('MH 11 AB 9332', '3L', 127, 20, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 127, 34, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '5U', 127, 11, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 127, 10, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 127, 40, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '25L', 127, 12, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '11U', 127, 7, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 127, 21, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '4U', 127, 20, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 127, 36, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '23U', 127, 21, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '19L', 127, 29, 19, 23).createObject() == True
        assert Booking('MH 11 AB 9332', '10U', 127, 31, 19, 23).createObject() == True
        assert Booking('MH 19 AB 9404', '27L', 128, 31, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '17U', 128, 36, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '3L', 128, 4, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '25L', 128, 9, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '6U', 128, 26, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '24U', 128, 34, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '23U', 128, 30, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '13L', 128, 29, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '22U', 128, 27, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '21L', 128, 2, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '15L', 128, 33, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '16U', 128, 26, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '10U', 128, 38, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '18U', 128, 16, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '11U', 128, 10, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '26L', 128, 15, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '20L', 128, 21, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '19L', 128, 34, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '28U', 128, 7, 2, 5).createObject() == True
        assert Booking('MH 19 AB 9404', '8L', 128, 32, 2, 5).createObject() == True
        assert Booking('MH 10 AB 5575', '15L', 129, 39, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '20L', 129, 18, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '27L', 129, 34, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 129, 21, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 129, 35, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '30U', 129, 9, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '7L', 129, 12, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '10U', 129, 9, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '29U', 129, 26, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '25L', 129, 13, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 129, 38, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '6U', 129, 2, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '28U', 129, 32, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '5U', 129, 17, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 129, 9, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '23U', 129, 27, 26, 12).createObject() == True
        assert Booking('MH 10 AB 5575', '9L', 129, 35, 26, 12).createObject() == True
        assert Booking('MH 12 AB 5440', '17U', 130, 20, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '30U', 130, 21, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '21L', 130, 38, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '18U', 130, 18, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '13L', 130, 4, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '28U', 130, 31, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '9L', 130, 2, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '25L', 130, 39, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '6U', 130, 15, 2, 4).createObject() == True
        assert Booking('MH 12 AB 5440', '20L', 130, 20, 2, 4).createObject() == True
        assert Booking('MH 11 AB 9332', '7L', 131, 24, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '2L', 131, 40, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '3L', 131, 33, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '29U', 131, 21, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '1L', 131, 11, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '27L', 131, 17, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '12U', 131, 27, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '18U', 131, 14, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '16U', 131, 13, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '6U', 131, 14, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '24U', 131, 8, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '17U', 131, 34, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '23U', 131, 24, 13, 14).createObject() == True
        assert Booking('MH 11 AB 9332', '14L', 131, 36, 13, 14).createObject() == True
        assert Booking('MH 11 AB 5703', '10U', 132, 8, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '29U', 132, 8, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '28U', 132, 21, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '26L', 132, 24, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '15L', 132, 1, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '23U', 132, 37, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '7L', 132, 14, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '13L', 132, 39, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '27L', 132, 34, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '20L', 132, 23, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '25L', 132, 19, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '11U', 132, 7, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '4U', 132, 27, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '17U', 132, 22, 12, 26).createObject() == True
        assert Booking('MH 11 AB 5703', '9L', 132, 5, 12, 26).createObject() == True
        assert Booking('MH 9 AB 8308', '28U', 133, 26, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '12U', 133, 10, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '29U', 133, 7, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '19L', 133, 3, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '20L', 133, 12, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '18U', 133, 3, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '23U', 133, 18, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '26L', 133, 1, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '9L', 133, 30, 28, 1).createObject() == True
        assert Booking('MH 9 AB 8308', '10U', 133, 3, 28, 1).createObject() == True
        assert Booking('MH 17 AB 9316', '16U', 134, 15, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '7L', 134, 26, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 134, 21, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 134, 4, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '22U', 134, 37, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 134, 33, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '1L', 134, 16, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 134, 16, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '27L', 134, 38, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 134, 23, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 134, 39, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 134, 19, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 134, 16, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '28U', 134, 20, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 134, 27, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 134, 28, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 134, 40, 22, 20).createObject() == True
        assert Booking('MH 17 AB 9316', '5U', 135, 30, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '20L', 135, 31, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '8L', 135, 26, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '11U', 135, 19, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '15L', 135, 6, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '29U', 135, 36, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '9L', 135, 7, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '6U', 135, 4, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '18U', 135, 26, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '10U', 135, 26, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '2L', 135, 26, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '25L', 135, 27, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '14L', 135, 38, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '30U', 135, 27, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '23U', 135, 32, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '26L', 135, 5, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '4U', 135, 39, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '19L', 135, 4, 3, 7).createObject() == True
        assert Booking('MH 17 AB 9316', '13L', 135, 25, 3, 7).createObject() == True
        assert Booking('MH 17 AB 8217', '11U', 136, 10, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '5U', 136, 6, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '1L', 136, 39, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '7L', 136, 14, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '20L', 136, 32, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '13L', 136, 26, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '3L', 136, 15, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '14L', 136, 31, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '10U', 136, 37, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '26L', 136, 36, 9, 11).createObject() == True
        assert Booking('MH 17 AB 8217', '23U', 136, 12, 9, 11).createObject() == True
        assert Booking('MH 17 AB 5692', '1L', 137, 4, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '18U', 137, 5, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '30U', 137, 28, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '17U', 137, 16, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '19L', 137, 3, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '29U', 137, 30, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '12U', 137, 8, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '27L', 137, 22, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '9L', 137, 29, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '8L', 137, 10, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '16U', 137, 39, 3, 29).createObject() == True
        assert Booking('MH 17 AB 5692', '6U', 137, 34, 3, 29).createObject() == True
        assert Booking('MH 19 AB 9404', '21L', 138, 33, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '22U', 138, 16, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '14L', 138, 27, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '28U', 138, 32, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '3L', 138, 26, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '9L', 138, 32, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '23U', 138, 11, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '5U', 138, 6, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '19L', 138, 26, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '27L', 138, 17, 9, 6).createObject() == True
        assert Booking('MH 19 AB 9404', '8L', 138, 12, 9, 6).createObject() == True
        assert Booking('MH 11 AB 7989', '5U', 139, 26, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '8L', 139, 21, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '3L', 139, 38, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '6U', 139, 14, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '20L', 139, 32, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '26L', 139, 5, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '21L', 139, 15, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '17U', 139, 1, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '27L', 139, 21, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '30U', 139, 40, 22, 7).createObject() == True
        assert Booking('MH 11 AB 7989', '2L', 139, 36, 22, 7).createObject() == True
        assert Booking('MH 9 AB 8797', '6U', 140, 24, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '24U', 140, 29, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '27L', 140, 13, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '28U', 140, 36, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '20L', 140, 32, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '9L', 140, 10, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '4U', 140, 38, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '29U', 140, 21, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '11U', 140, 7, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '17U', 140, 26, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '7L', 140, 39, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '13L', 140, 1, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '18U', 140, 17, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '1L', 140, 39, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '22U', 140, 5, 14, 29).createObject() == True
        assert Booking('MH 9 AB 8797', '16U', 140, 28, 14, 29).createObject() == True
        assert Booking('MH 16 AB 7740', '18U', 141, 14, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 141, 3, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '19L', 141, 6, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '26L', 141, 35, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '6U', 141, 11, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 141, 15, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '5U', 141, 15, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '16U', 141, 33, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '13L', 141, 32, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 141, 22, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '12U', 141, 32, 7, 4).createObject() == True
        assert Booking('MH 16 AB 7740', '25L', 141, 1, 7, 4).createObject() == True
        assert Booking('MH 19 AB 5367', '1L', 142, 1, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '22U', 142, 37, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '2L', 142, 23, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '26L', 142, 34, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '7L', 142, 34, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '25L', 142, 10, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '11U', 142, 5, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '23U', 142, 8, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '8L', 142, 37, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '6U', 142, 9, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '13L', 142, 11, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '12U', 142, 25, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '30U', 142, 29, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '19L', 142, 7, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '20L', 142, 22, 2, 11).createObject() == True
        assert Booking('MH 19 AB 5367', '17U', 142, 36, 2, 11).createObject() == True
        assert Booking('MH 10 AB 5575', '26L', 143, 9, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '6U', 143, 33, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '8L', 143, 18, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '2L', 143, 12, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '18U', 143, 32, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '9L', 143, 13, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '25L', 143, 15, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '3L', 143, 14, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '19L', 143, 29, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '16U', 143, 5, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '11U', 143, 19, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '17U', 143, 14, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '27L', 143, 2, 26, 20).createObject() == True
        assert Booking('MH 10 AB 5575', '24U', 143, 21, 26, 20).createObject() == True
        assert Booking('MH 11 AB 7889', '9L', 144, 7, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '22U', 144, 19, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '4U', 144, 16, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '7L', 144, 39, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '23U', 144, 19, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '1L', 144, 9, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '13L', 144, 26, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '24U', 144, 13, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '19L', 144, 23, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '12U', 144, 25, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '20L', 144, 37, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '28U', 144, 11, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '8L', 144, 26, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '18U', 144, 39, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '16U', 144, 16, 18, 26).createObject() == True
        assert Booking('MH 11 AB 7889', '25L', 144, 36, 18, 26).createObject() == True
        assert Booking('MH 17 AB 5692', '7L', 145, 36, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '22U', 145, 18, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '28U', 145, 10, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '1L', 145, 26, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '6U', 145, 15, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '16U', 145, 6, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '24U', 145, 33, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '25L', 145, 30, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '5U', 145, 9, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '29U', 145, 11, 23, 6).createObject() == True
        assert Booking('MH 17 AB 5692', '27L', 145, 38, 23, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '3L', 146, 38, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '9L', 146, 34, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '8L', 146, 2, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '25L', 146, 28, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '6U', 146, 38, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '5U', 146, 37, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '29U', 146, 37, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '19L', 146, 30, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '22U', 146, 34, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '7L', 146, 18, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '24U', 146, 2, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '27L', 146, 6, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '30U', 146, 30, 24, 6).createObject() == True
        assert Booking('MH 13 AB 5137', '1L', 146, 19, 24, 6).createObject() == True
        assert Booking('MH 11 AB 7989', '20L', 147, 9, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '2L', 147, 28, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '24U', 147, 16, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '22U', 147, 13, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '18U', 147, 40, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '19L', 147, 36, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '11U', 147, 27, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '25L', 147, 2, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '16U', 147, 30, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '14L', 147, 22, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '5U', 147, 6, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '6U', 147, 4, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '12U', 147, 39, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '8L', 147, 32, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '30U', 147, 3, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '23U', 147, 13, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '10U', 147, 28, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '1L', 147, 19, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '17U', 147, 34, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7989', '7L', 147, 17, 22, 8).createObject() == True
        assert Booking('MH 11 AB 7889', '4U', 148, 32, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '29U', 148, 21, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '15L', 148, 2, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '6U', 148, 27, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '27L', 148, 11, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '3L', 148, 6, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '22U', 148, 9, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '13L', 148, 40, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '28U', 148, 31, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '9L', 148, 39, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '5U', 148, 38, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '12U', 148, 40, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '30U', 148, 23, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '25L', 148, 34, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '8L', 148, 1, 12, 14).createObject() == True
        assert Booking('MH 11 AB 7889', '21L', 148, 14, 12, 14).createObject() == True
        assert Booking('MH 8 AB 8272', '9L', 149, 6, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '16U', 149, 5, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '5U', 149, 9, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '12U', 149, 19, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '25L', 149, 38, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '26L', 149, 10, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '20L', 149, 11, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '6U', 149, 29, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '7L', 149, 27, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '18U', 149, 19, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '2L', 149, 20, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '8L', 149, 6, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '3L', 149, 16, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '11U', 149, 30, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '27L', 149, 18, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '15L', 149, 5, 15, 6).createObject() == True
        assert Booking('MH 8 AB 8272', '28U', 149, 2, 15, 6).createObject() == True
        assert Booking('MH 16 AB 7740', '25L', 150, 40, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '28U', 150, 40, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '22U', 150, 22, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '7L', 150, 9, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '13L', 150, 35, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '1L', 150, 3, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '23U', 150, 30, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '18U', 150, 1, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '10U', 150, 5, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '11U', 150, 3, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '9L', 150, 35, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '19L', 150, 35, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '2L', 150, 37, 18, 26).createObject() == True
        assert Booking('MH 16 AB 7740', '17U', 150, 13, 18, 26).createObject() == True


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