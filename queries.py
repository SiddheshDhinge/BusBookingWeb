db_name = "db_bus"

sql_check_db_exists = f"select exists(SELECT * FROM pg_database where datname='{db_name}');"

sql_create_db = f"create database {db_name};"

sql_create_users_table = '''
    create table if not exists users(
        username text primary key,
        pass text not null);
        '''

sql_create_bus_table = '''
    create table if not exists bus(
        id text primary key,
        name text not null,
        dep_from text not null,
        dep_to text not null,
        dep_date date not null,
        dep_time time not null,
        total_seats integer not null,
        total_available_seats integer not null);
        '''

sql_create_passenger_table = '''
    create table if not exists passenger(
        p_id serial primary key,
        name text not null,
        gender char(1) not null,
        age integer not null,
        mobile text not null);
        '''

sql_create_ticket_table = '''
     create table if not exists ticket(
        ticket_no text primary key,
        username text,
        id text,
        p_id integer unique,
        seatno integer not null,
        foreign key(username) references users(username),
        foreign key(id) references bus(id),
        foreign key(p_id) references passenger(p_id),
        unique(id, seatno));
        '''

sql_insert_user = "insert into users values(%s, %s);"

sql_select_exists_user = "select exists(select * from users where username = %s and pass = %s);"

sql_insert_bus = "insert into bus values(%s, %s, %s, %s, %s, %s);"

sql_select_all_bus = "select * from bus;"

sql_select_from_to_bus = "select * from bus where dep_from = %s and dep_to = %s;"

sql_select_from_bus = "select * from bus where dep_from = %s;"

sql_insert_passenger = '''
    insert into passenger(name, gender, age, mobile) values(%s, %s, %s, %s);
    SELECT currval('passenger_p_id_seq');
    '''

sql_select_booked_seats = '''
    select seatno, passenger.gender from ticket, passenger
    where ticket.id = %s and passenger.p_id = ticket.p_id;
    '''

sql_select_ticket_no =  "select concat_ws('-', dep_date, id, %s) from bus where id = %s;"

sql_insert_ticket = "insert into ticket values(%s, %s, %s, %s, %s);"