import psycopg2
import json
from secret import db_username
from secret import db_password
from queries import sql_check_db_exists
from queries import sql_create_db
from queries import sql_create_users_table
from queries import sql_create_bus_table
from queries import sql_create_passenger_table
from queries import sql_create_ticket_table
from queries import sql_insert_user
from queries import sql_select_exists_user
from queries import sql_select_all_bus
from queries import sql_select_from_to_bus
from queries import sql_select_from_bus
from queries import sql_insert_passenger
from queries import sql_select_booked_seats
from queries import sql_select_ticket_no
from queries import sql_insert_ticket

# connection
con = None
# cursor
cur = None

# create db and table if not exists
def create_template_schema():
    con = psycopg2.connect(dbname='postgres', user=db_username, host='localhost', password=db_password)
    con.autocommit = True
    cur = con.cursor()

    cur.execute(sql_check_db_exists)
    if(cur.fetchone()[0] == False):
        cur.execute(sql_create_db)

    cur.close()
    con.close()

    con = psycopg2.connect(dbname='db_bus', user=db_username, host='localhost', password=db_password)
    cur = con.cursor()

    cur.execute(sql_create_users_table)
    cur.execute(sql_create_bus_table)
    cur.execute(sql_create_passenger_table)
    cur.execute(sql_create_ticket_table)

    con.commit()
    cur.close()
    con.close()

# configure con and cur global objects
def configure():
    create_template_schema()
    global con, cur
    con = psycopg2.connect(dbname='db_bus', user=db_username, host='localhost', password=db_password)
    cur = con.cursor()

# create a user
def create_user(user_username, user_password):
    cur.execute(sql_insert_user, (user_username, user_password))
    con.commit()

# returns true for success login else false
def login(user_username, user_password):
    cur.execute(sql_select_exists_user, (user_username, user_password))
    if(cur.fetchone()[0] == True):
        return True
    return False

# returns all bus info
def getAllBus():
    cur.execute(sql_select_all_bus)
    return json.dumps(cur.fetchall(), default=str)

# returns specific bus info with bus_dep_from and bus_dep_to where bus_dep_to could be none
def getSpecificBus(bus_dep_from, bus_dep_to = None):
    if bus_dep_to is None:
        cur.execute(sql_select_from_bus, (bus_dep_from,))
    else:
        cur.execute(sql_select_from_to_bus, (bus_dep_from, bus_dep_to))
        
    return json.dumps(cur.fetchall(), default=str)

# adds a passenger
def addPassenger(passenger_name, passenger_gender, passenger_age, passenger_mobile):
    cur.execute(sql_insert_passenger, (passenger_name, passenger_gender, passenger_age, passenger_mobile))
    con.commit()
    return cur.fetchone()[0]

# returns all booked seatno and gender of the booked seat's passenger of a specific bus
def getBookedSeats(bus_id):
    cur.execute(sql_select_booked_seats, (bus_id,))
    return json.dumps(cur.fetchall(), default=str)

# returns the ticket number in format YYYY-MM-DD-BUSID-SEATNO
def createTicketNo(bus_id, ticket_seatno):
    cur.execute(sql_select_ticket_no, (ticket_seatno, bus_id))
    return str(cur.fetchone()[0])

# not checked yet
def bookTicket(users_username, users_password, passenger_name, passenger_gender, passenger_age, passenger_mobile, bus_id, seatno):
    if not login(users_username, users_password):
        return "USER ERROR"

    passger_p_id = addPassenger(passenger_name, passenger_gender, passenger_age, passenger_mobile)
    ticket_ticket_no = createTicketNo(bus_id, seatno)
    cur.execute(sql_insert_ticket, (ticket_ticket_no, users_username, bus_id, passger_p_id, seatno))
    con.commit()


def main():
    configure()
    # create_user('sid', 'aaa')
    # print(login('sida', 'asaasa44'))
    # print(getSpecificBus('pune'))
    # print(getSpecificBus('pune', 'dhule'))
    # addPassenger('sumit', 'm', 20, '815142425555')
    # addPassenger('siddhesh', 'm', 20, '815142425555')
    # print(addPassenger('sanjay', 'f', 20, '815142425555'))
    # print(getBookedSeats('id1'))
    # print(createTicketNo('id2', 22))
    print(bookTicket('sid', 'aaa', 'sid', 'm', 20, '8888888', 'id2', 22))

if __name__ == "__main__":
    main()