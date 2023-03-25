success = 'request-status'
service = 'service-id'
session = 'user-session-id'
details = 'detail-information'

username = 'user-username'
accessType = 'access-type'
name_labels = 'label'
role = 'role'

# begin deprecated
# password = 'user-password'
# name = 'user-person-name'
# contact = 'user-contact-no'
# end

owner_username = 'owner-username'
owner_old_password = 'owner-old-password'
owner_password = 'owner-password'
owner_agencyName = 'owner-agency-name'
owner_contact = 'owner-contact'
owner_all_label = {
    'username' : owner_username,
    'old-password' : owner_old_password,
    'password' : owner_password,
    'name' : owner_agencyName,
    'contact' : owner_contact,
}

operator_username = 'operator-username'
operator_old_password = 'operator-old-password'
operator_password = 'operator-password'
operator_name = 'operator-name'
operator_contact = 'operator-contact'
operator_all_label = {
    'username' : operator_username,
    'old-password' : operator_old_password,
    'password' : operator_password,
    'name' : operator_name,
    'contact' : operator_contact,
}

customer_username = 'customer-username'
customer_old_password = 'customer-old-password'
customer_password = 'customer-password'
customer_name = 'customer-name'
customer_contact = 'customer-contact'
customer_all_label = {
    'username' : customer_username,
    'old-password' : owner_old_password,
    'password' : customer_password,
    'name' : customer_name,
    'contact' : customer_contact,
}


bus_numberPlate = 'bus-number-plate'
bus_busType = 'bus-type'
bus_totalFloors = 'bus-total-floors'
bus_floorRows = 'bus-floor-rows'
bus_floorColumns = 'bus-floor-columns'
bus_walkingGapRow = 'bus-walking-gap-row'
bus_typeSleep = 'SLEEP'
bus_typeSeat = 'SEAT'

seat_seatNo = 'seat-no'
seat_is_enabled = 'seat-is-enabled'

city_id = 'city-id'
city_name = 'city-name'

stop_id = 'stop-id'
stop_name = 'stop-name'
stop_address = 'stop-address'

at_sequence = 'at-sequence'

schedule_id = 'schedule-id'
schedule_fromDate = 'schedule-from-date'
schedule_toDate = 'schedule-to-date'
schedule_departureTime = 'schedule-departure-time'
schedule_dropTime = 'schedule-drop-time'
schedule_fromCity = 'schedule-from-city-id'
schedule_toCity = 'schedule-to-city-id'
schedule_fairFees = 'schedule-fair-fees'
schedule_isComplete = 'schedule-is-complete'

booking_id = 'booking-id'
booking_fromStopId = 'booking-from-stop-id'
booking_toStopId = 'booking-to-stop-id'

passenger_id = 'passenger-id'
passenger_name = 'passenger-name'
passenger_gender = 'passenger-gender'
passenger_age = 'passenger-age'
passenger_contact = 'passenger-contact'

options = 'options'
nav_btn = 'nav-btn'
btn_login_signup = ('signUp', 'logIn')
btn_signup = ('signUp')
btn_login = ('logIn')
btn_logout = ('logOut')
ip = 'ip'

data = 'data'
search = 'search'

filterSortPrice = 'filter-sort-price'
filterFromCity = 'filter-from-city'
filterToCity = 'filter-to-city'
filterTimeBlock = 'filter-time-block'
filterBusType = 'filter-bus-type'
filterDate = 'filter-date'
filterTripStatus = 'filter-trip-status'

timeBlockMorning = 'time-morning'
timeBlockNoon = 'time-noon'
timeBlockEvening = 'time-evening'
timeBlockNight = 'time-night'