db_name = "db_bus"

sql_check_db_exists = f"select exists(SELECT * FROM pg_database where datname='{db_name}');"

sql_create_db = f"create database {db_name};"

sql_create_owner_table = '''
create table if not exists Owner(
       Owner_username varchar(16) primary key,
       Owner_password char(64) not null,
       Owner_name varchar(64) not null,
       Owner_contact varchar(10) not null,
       unique(Owner_contact),
       check(Owner_contact ~* '^[0-9]{10}$')
    );
'''

sql_create_bus_table = '''
    create table if not exists Bus(
        Bus_numberPlate varchar(16) primary key,
        Bus_totalSeats int not null,
        Bus_type varchar(16) not null,
        Owner_username varchar(16) not null,
        foreign key(Owner_username) references Owner(Owner_username)
    );
'''

sql_create_customer_table = '''
    create table if not exists Customer(
        Customer_username varchar(16) primary key,
        Customer_password char(64) not null,
        Customer_name varchar(64) not null,
        Customer_contact varchar(10) not null,
        unique(Customer_contact),
        check(Customer_contact ~* '^[0-9]{10}$')
    );
'''

sql_create_passenger_table = '''
    create table if not exists Passenger(
        Passenger_id serial primary key,
        Passenger_name varchar(64) not null,
        Passenger_gender char(1) not null,
        Passenger_age int not null,
        Passenger_contact varchar(10) not null,
        Customer_username varchar(16) not null,
        check(Passenger_contact ~* '^[0-9]{10}$'),
        foreign key(Customer_username) references Customer(Customer_username)
    );
'''

sql_create_operator_table = '''
    create table if not exists Operator(
        Operator_username varchar(16) primary key,
        Operator_password char(64) not null,
        Operator_name varchar(64) not null,
        Operator_contact varchar(10) not null,
        Operator_address varchar(128) not null,
        unique(Operator_contact),
        check(Operator_contact ~* '^[0-9]{10}$')
    );
'''

sql_create_landmark_table = '''
    create table if not exists Landmark(
        Landmark_id int primary key,
        Landmark_name varchar(64) not null
    );
'''

sql_create_stop_table = '''
    create table if not exists Stop(
        Stop_id int primary key,
        Stop_name varchar(64) not null,
        Stop_address varchar(128) not null,
        Landmark_id int not null,
        foreign key(Landmark_id) references Landmark(Landmark_id)
    );
'''

sql_create_schedule_table = '''
    create table if not exists Schedule(
        Schedule_id serial primary key,
        Schedule_fromDate date not null,
        Schedule_toDate date not null,
        Schedule_departureTime time not null,
        Schedule_dropTime time not null,
        Schedule_fairFees int not null,
        Bus_numberPlate varchar(16) not null,
        Operator_username varchar(16) not null,
        foreign key(Bus_numberPlate) references Bus(Bus_numberPlate),
        foreign key(Operator_username) references Operator(Operator_username),
        check( 
            (Schedule_fromDate < Schedule_toDate) OR 
            ((Schedule_fromDate = Schedule_toDate) AND (Schedule_departureTime < Schedule_dropTime))
        )
    );
'''

sql_create_booking_table = '''
    create table if not exists Booking(
        Schedule_id int not null,
        Passenger_id int not null,
        Booking_seatNo int not null,
        primary key(Schedule_id, Passenger_id, Booking_seatNo),
        foreign key(Schedule_id) references Schedule(Schedule_id),
        foreign key(Passenger_id) references Passenger(Passenger_id)
    );
'''

sql_create_at_table = '''
    create table if not exists At(
        Schedule_id int not null,
        Stop_id int not null,
        primary key(Schedule_id, Stop_id),
        foreign key(Schedule_id) references Schedule(Schedule_id),
        foreign key(Stop_id) references Stop(Stop_id)
    );
'''

sql_insert_customer = "insert into Customer(Customer_username, Customer_password, Customer_name, Customer_contact) values(%s, %s, %s, %s);"

sql_insert_operator = "insert into Operator(Operator_username, Operator_password, Operator_name, Operator_contact, Operator_address) values(%s, %s, %s, %s, %s);"

sql_insert_passenger = '''
    insert into Passenger(Passenger_id, Passenger_name, Passenger_gender, Passenger_age, Passenger_contact, Customer_username) values(%s, %s, %s, %s, %s, %s);
    SELECT currval('passenger_p_id_seq');
    '''

sql_insert_landmark = "insert into Landmark(Landmark_id, Landmark_name) values(%s, %s);"

sql_insert_stop = "insert into Stop(Stop_id, Stop_name, Stop_address, Landmark_id) values(%s, %s, %s, %s);"

sql_insert_booking = "insert into Booking(Schedule_id, Passenger_id, Booking_seatNo) values(%s, %s, %s);"

sql_insert_bus = "insert into Bus(Bus_numberPlate, Bus_totalSeats, Bus_type, Owner_username) values(%s, %s, %s, %s);"

# here till don3
# write next a procedure

sql_select_all_bus = "select * from bus;"

sql_select_from_to_bus = "select * from bus where dep_from = %s and dep_to = %s;"

sql_select_from_bus = "select * from bus where dep_from = %s;"


sql_select_booked_seats = '''
    select seatno, passenger.gender from ticket, passenger
    where ticket.id = %s and passenger.p_id = ticket.p_id;
    '''

sql_select_ticket_no =  "select concat_ws('-', dep_date, id, %s) from bus where id = %s;"

sql_insert_ticket = "insert into ticket values(%s, %s, %s, %s, %s);"