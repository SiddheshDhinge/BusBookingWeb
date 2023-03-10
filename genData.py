import random
import test
from app.model.complex_operations import ComplexOperation

own = ['Chintan', 'Siddhesh', 'Manas', 'Sahil', 'Shubham', 'jack123', 'emmam', 'brianb', 'katherineg', 'chrisd', 'samuelm', 'laurar', 'davids', 'jennifert', 'michaelw', 'susanb', 'jamesm', 'lisaq', 'matthewr', 'nicolej']
oper = ['Manish', 'Guarav', 'Ketan', 'Akshay', 'Lokesh', 'timothyb', 'rachelc', 'michaelg', 'jenniferl', 'davidm', 'sarahp', 'matthewr', 'lisaq', 'katherinet', 'johnd']
number = ['MH 8 AB 8272', 'MH 12 AB 9096', 'MH 9 AB 8797', 'MH 11 AB 9332', 'MH 14 AB 6870', 'MH 5 AB 6693', 'MH 11 AB 5703', 'MH 11 AB 7989', 'MH 5 AB 7650', 'MH 19 AB 9404', 'MH 19 AB 5367', 'MH 11 AB 8643', 'MH 12 AB 5440', 'MH 17 AB 8217', 'MH 6 AB 5509', 'MH 19 AB 8932', 'MH 12 AB 8578', 'MH 17 AB 5987', 'MH 13 AB 5137', 'MH 12 AB 7062', 'MH 17 AB 5692', 'MH 18 AB 7004', 'MH 14 AB 9684', 'MH 14 AB 6518', 'MH 13 AB 9993', 'MH 8 AB 6980', 'MH 10 AB 9617', 'MH 17 AB 9316', 'MH 19 AB 8198', 'MH 11 AB 7659', 'MH 9 AB 8308', 'MH 20 AB 8094', 'MH 16 AB 7222', 'MH 16 AB 7740', 'MH 14 AB 5997', 'MH 15 AB 9478', 'MH 7 AB 6536', 'MH 8 AB 5155', 'MH 10 AB 5575', 'MH 11 AB 7889']
typ = ['SLEEP', 'SEAT']
seatNos = ['1L', '2L', '3L', '4U', '5U', '6U', '7L', '8L', '9L', '10U', '11U', '12U', '13L', '14L', '15L', '16U', '17U', '18U', '19L', '20L', '21L', '22U', '23U', '24U', '25L', '26L', '27L', '28U', '29U', '30U']
scheduleBuses = ['MH 9 AB 8797', 'MH 8 AB 6980', 'MH 19 AB 8198', 'MH 19 AB 8198', 'MH 10 AB 5575', 'MH 16 AB 7222', 'MH 17 AB 9316', 'MH 11 AB 9332', 'MH 18 AB 7004', 'MH 14 AB 6518', 'MH 11 AB 9332', 'MH 12 AB 8578', 'MH 11 AB 8643', 'MH 10 AB 9617', 'MH 15 AB 9478', 'MH 18 AB 7004', 'MH 13 AB 9993', 'MH 15 AB 9478', 'MH 11 AB 7659', 'MH 11 AB 7889', 'MH 13 AB 9993', 'MH 14 AB 5997', 'MH 14 AB 9684', 'MH 17 AB 9316', 'MH 17 AB 9316', 'MH 11 AB 8643', 'MH 5 AB 7650', 'MH 12 AB 9096', 'MH 11 AB 7989', 'MH 11 AB 8643', 'MH 12 AB 9096', 'MH 8 AB 6980', 'MH 15 AB 9478', 'MH 15 AB 9478', 'MH 7 AB 6536', 'MH 11 AB 7659', 'MH 9 AB 8797', 'MH 16 AB 7740', 'MH 20 AB 8094', 'MH 18 AB 7004', 'MH 19 AB 8198', 'MH 16 AB 7740', 'MH 17 AB 9316', 'MH 11 AB 9332', 'MH 18 AB 7004', 'MH 8 AB 5155', 'MH 10 AB 5575', 'MH 5 AB 6693', 'MH 17 AB 9316', 'MH 16 AB 7740', 'MH 19 AB 8932', 'MH 9 AB 8308', 'MH 9 AB 8308', 'MH 6 AB 5509', 'MH 11 AB 5703', 'MH 19 AB 5367', 'MH 13 AB 9993', 'MH 17 AB 5987', 'MH 16 AB 7222', 'MH 11 AB 7989', 'MH 16 AB 7740', 'MH 19 AB 8932', 'MH 17 AB 8217', 'MH 5 AB 6693', 'MH 6 AB 5509', 'MH 19 AB 8198', 'MH 8 AB 8272', 'MH 10 AB 5575', 'MH 8 AB 5155', 'MH 6 AB 5509', 'MH 16 AB 7222', 'MH 12 AB 9096', 'MH 19 AB 5367', 'MH 8 AB 6980', 'MH 17 AB 9316', 'MH 10 AB 9617', 'MH 12 AB 8578', 'MH 5 AB 7650', 'MH 19 AB 8198', 'MH 11 AB 9332', 'MH 17 AB 5987', 'MH 14 AB 5997', 'MH 12 AB 9096', 'MH 9 AB 8797', 'MH 12 AB 8578', 'MH 14 AB 6870', 'MH 14 AB 6518', 'MH 14 AB 6870', 'MH 14 AB 9684', 'MH 12 AB 5440', 'MH 5 AB 6693', 'MH 18 AB 7004', 'MH 12 AB 8578', 'MH 10 AB 5575', 'MH 6 AB 5509', 'MH 12 AB 7062', 'MH 8 AB 8272', 'MH 18 AB 7004', 'MH 11 AB 7989', 'MH 14 AB 5997', 'MH 13 AB 9993', 'MH 8 AB 6980', 'MH 10 AB 5575', 'MH 5 AB 6693', 'MH 12 AB 5440', 'MH 17 AB 9316', 'MH 9 AB 8308', 'MH 16 AB 7740', 'MH 12 AB 7062', 'MH 12 AB 7062', 'MH 20 AB 8094', 'MH 14 AB 9684', 'MH 11 AB 9332', 'MH 11 AB 9332', 'MH 14 AB 9684', 'MH 10 AB 9617', 'MH 8 AB 6980', 'MH 13 AB 5137', 'MH 9 AB 8308', 'MH 19 AB 8198', 'MH 8 AB 8272', 'MH 12 AB 7062', 'MH 19 AB 8932', 'MH 9 AB 8308', 'MH 17 AB 8217', 'MH 8 AB 8272', 'MH 11 AB 9332', 'MH 19 AB 9404', 'MH 10 AB 5575', 'MH 12 AB 5440', 'MH 11 AB 9332', 'MH 11 AB 5703', 'MH 9 AB 8308', 'MH 17 AB 9316', 'MH 17 AB 9316', 'MH 17 AB 8217', 'MH 17 AB 5692', 'MH 19 AB 9404', 'MH 11 AB 7989', 'MH 9 AB 8797', 'MH 16 AB 7740', 'MH 19 AB 5367', 'MH 10 AB 5575', 'MH 11 AB 7889', 'MH 17 AB 5692', 'MH 13 AB 5137', 'MH 11 AB 7989', 'MH 11 AB 7889', 'MH 8 AB 8272', 'MH 16 AB 7740']

def pad(num):
    if(num < 10):
        return f'0{num}'
    return num
    
def randomPad(a, b):
    return pad(random.randint(a, b))

# for _ in range(40):
#     # Bus
#     numberPlate = number[_] # f'MH {random.randint(5, 20)} AB {random.randint(5000, 9999)}'
#     busType = typ[random.randint(0, 1)]
#     totalFloors = 2
#     floorRows = 3
#     floorColumns = 5
#     walkingGapRow = random.randint(1, 2)
#     ownerUsername = own[random.randint(0, len(own) -1)]
#     data = (numberPlate, busType, totalFloors, floorRows, floorColumns, walkingGapRow, ownerUsername )

#     print(data)


# for numberPlate in number:
#     # Seat
#     for _ in range(30):
#         # Seat
#         seatNo = seatNos[_] # str(_) + ('L', 'U')[random.randint(0, 1)]
#         isEnabled = (False, True)[random.randint(0, 1)]
#         data = (numberPlate, seatNo, isEnabled)

#         print(data)


# for scheduleId, numberPlate in enumerate(scheduleBuses):
#     # Booking
#     totalBookings = random.randint(10, 20)
#     tmpSeatNos = random.sample(seatNos, totalBookings)
#     availableStops = ComplexOperation().getSchedulesStop(scheduleId= int(scheduleId +1))
#     for _ in range(0, totalBookings):
#         seatNo = tmpSeatNos[_]
#         passengerId = random.randint(1, 40)
#         fromStopId = 1 if (len(availableStops) == 0) else availableStops[0]['stop']['stop-id']
#         toStopId = 1 if (len(availableStops) == 0) else availableStops[-1]['stop']['stop-id']
#         data = (numberPlate, seatNo, scheduleId +1, passengerId, fromStopId, toStopId)

#         print(data)


# for _ in range(1, 151):
#     # Schedule
#     frmM = 12 #random.randint(1, 11)
#     frmD = random.randint(20, 30)
#     toD = frmD +1
#     fromDate = f'2022-{pad(frmM)}-{pad(frmD)}'
#     toDate = f'2022-{pad(frmM)}-{pad(toD)}'
#     departureTime = f'{randomPad(0, 23)}:{randomPad(0, 59)}:{randomPad(0, 59)}'
#     dropTime = f'{randomPad(0, 23)}:{randomPad(0, 59)}:{randomPad(0, 59)}'
#     fairFees = random.randint(1000, 10000)
#     fromCity = random.randint(1, 5)
#     toCity = random.randint(1, 5)
#     numberPlate = number[random.randint(0, len(number) -1)]
#     operatorUsername = oper[random.randint(0, len(oper) -1)]

#     data = (fromDate, toDate, departureTime, dropTime, fairFees, fromCity, toCity, numberPlate, operatorUsername)

#     print(data)
    
    # # At
    # seq = 1
    # for __ in random.sample(range(1, 30), random.randint(5, 10)):
    #     print(f'{_}, {__}, {seq}')
    #     seq += 1




# Schedule(fromDate: str, toDate: str, departureTime: str, dropTime: str, fairFees: int, fromCity: int, toCity: int, numberPlate: str, username: str)
# assert Schedule('2019-12-01', '2019-12-31', '08:00:00', '11:00:00', 5000, 1, 6, 'MH 12 AB 1234', 'Manish').createObject() == True


# Make random trip complete
# for scheduleId in (random.sample(range(1, 153), 70)):
#     ComplexOperation().updateTripStatus(scheduleId= scheduleId)