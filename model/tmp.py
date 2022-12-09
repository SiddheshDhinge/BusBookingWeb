print("\n\n\nSTARTED: \n\n\n")
#Establish database session
from database import connectDB, createAllTables
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

#create Database schema if not exists
createAllTables()


def main():
    o1 = Owner('Siddhesh', 'abc', 'abcd', '9879870000')
    o2 = Owner('sarvesh', 'abc', 'abcd', '9879870800')

    # print(o1.createOwner())
    # print(o2.createOwner())

    print(o1.loginOwner())

if __name__ == "__main__":
    main()