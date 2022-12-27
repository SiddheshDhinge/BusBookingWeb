success = 'request-status'
service = 'service-id'
session = 'user-session-id'
details = 'detail-information'

username = 'user-username'
accessType = 'access-type'
name_labels = 'label'
role = 'role'

# begin deprecated
password = 'user-password'
name = 'user-person-name'
contact = 'user-contact-no'
# end

owner_username = 'owner-username'
owner_password = 'owner-password'
owner_name = 'owner-name'
owner_contact = 'owner-contact'
owner_all_label = {
    'username' : owner_username,
    'password' : owner_password,
    'name' : owner_name,
    'contact' : owner_contact,
}

operator_username = 'operator-username'
operator_password = 'operator-password'
operator_name = 'operator-name'
operator_contact = 'operator-contact'
operator_address = 'operator-address'
operator_all_label = {
    'username' : operator_username,
    'password' : operator_password,
    'name' : operator_name,
    'contact' : operator_contact,
    'address' : operator_address,
}

customer_username = 'customer-username'
customer_password = 'customer-password'
customer_name = 'customer-name'
customer_contact = 'customer-contact'
customer_all_label = {
    'username' : customer_username,
    'password' : customer_password,
    'name' : customer_name,
    'contact' : customer_contact,
}


bus_numberPlate = 'bus-number-plate'
bus_totalSeats = 'bus-total-seats'
bus_busType = 'bus-type'
bus_typeSleep = 'SLEEP'
bus_typeSeat = 'SEAT'

city_id = 'city-id'
city_name = 'city-name'

stop_id = 'stop-id'
stop_name = 'stop-name'
stop_address = 'stop-address'

schedule_id = 'schedule-id'
schedule_fromDate = 'schedule-from-date'
schedule_toDate = 'schedule-to-date'
schedule_departureTime = 'schedule-departure-time'
schedule_dropTime = 'schedule-drop-time'
schedule_fromCity = 'schedule-from-city-id'
schedule_toCity = 'schedule-to-city-id'
schedule_fairFees = 'schedule-fair-fees'
schedule_numberPlate = 'schedule-number-plate'

passenger_id = 'passenger-id'
passenger_name = 'passenger-name'
passenger_gender = 'passenger-gender'
passenger_age = 'passenger-age'
passenger_contact = 'passenger-contact'

booking_seatNo = 'booking-seat-no'

options = 'options'
nav_btn = 'nav-btn'
btn_login_signup = ('signUp', 'logIn')
btn_signup = ('signUp')
btn_login = ('logIn')
btn_logout = ('logOut')

data = 'data'
search = 'search'

filterSortPrice = 'filter-sort-price'
filterFromCity = 'filter-from-city'
filterToCity = 'filter-to-city'
filterTimeBlock = 'filter-time-block'
filterBusType = 'filter-bus-type'
filterDate = 'filter-date'

timeBlockMorning = 'time-morning'
timeBlockNoon = 'time-noon'
timeBlockEvening = 'time-evening'
timeBlockNight = 'time-night'