#general
error = 'Something went wrong... Try again'
authenticationFailed = 'Something went wrong... Please login Again'
loginInRequired= 'You need to be logged In'

#user
userCreationFailed = 'This user already exists choose a different username'
userCreationSuccess = 'You have successfully created an account!'
userLoginSuccess = 'Successfully Logged In!'
userLoginFailed = 'Wrong information! Try Again...'
userLogoutSuccess = 'You have been logged Out'
userLogoutFailed = 'log out failed.... try again...'
userAccountUpdateSuccess = 'Successfully Updated account'
userAccountUpdateFailed = 'Account updation failed'
userPasswordUpdateSuccess = 'Successfully Changed Password'
userPasswordUpdateFailed = 'Password reset Failed...'

#service
busRegistrationSuccess = 'Successfully registered the bus!'
busInvalidTypeFailed = 'Invalid bus type!'
busRegistrationFailed = 'Bus registration Failed!'
cityCreationSuccess = 'Successfully created the City!'
cityCreationFailed = 'City creation Failed!'
stopCreationSuccess = 'Successfully created the stop!'
stopCreationFailed = 'Stop creation Failed!'
scheduleCreationSuccess = 'Successfully created the Schedule!'
scheduleCreationFailed = 'Schedule creation Failed!'
scheduleStopUpdationSuccess = 'Successfully Updated the Schedule Stops!'
scheduleStopUpdationFailed = 'Schedule Stop Updation Failed!'
passengerCreationSuccess = 'Successfully added Passenger!'
passengerCreationFailed = 'Passenger addition Failed!'
bookingCreationSuccess = 'Successfully completed Booking!'
bookingCreationFailed = 'Booking Failed!'
invalidStopSequenceError = 'Please Select Valid Stops'
invalidScheduleIdError = 'Please Select Valid Schedule'
tripUpdationSuccess = 'Successfully Updated Trip Status'
invalidTripStatusError = 'Updatation of Trip Status Failed!'
invalidBusError = 'Please Select Valid Bus'

#filters
enterFilter = 'Please enter required filters.'
filterNoMatch = 'There are no matching results!'
filterMatch = 'Here are some results!'
scheduleDateFailed = 'Please Enter a valid Date!'
sourceDestinatioFailed = 'Please Enter a valid Source and destination City!'


#Custom Message flashing
# NOT IMPLEMENTED
from flask import flash

def flashMessage(messageLabel):
    flash(message= messageLabel[0], category= messageLabel[1])