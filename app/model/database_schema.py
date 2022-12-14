import psycopg2
import os
from queries import sql_create_db
from queries import sql_check_db_exists
from queries import sql_create_operator_table
from queries import sql_create_bus_table
from queries import sql_create_passenger_table
from queries import sql_create_customer_table
from queries import sql_create_owner_table
from queries import sql_create_landmark_table
from queries import sql_create_stop_table
from queries import sql_create_schedule_table
from queries import sql_create_booking_table
from queries import sql_create_at_table
from dotenv import load_dotenv
load_dotenv()

db_username = os.getenv('db_username')
db_password = os.getenv('db_password')

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

    cur.execute(sql_create_owner_table)
    cur.execute(sql_create_bus_table)
    cur.execute(sql_create_customer_table)
    cur.execute(sql_create_passenger_table)
    cur.execute(sql_create_operator_table)
    cur.execute(sql_create_landmark_table)
    cur.execute(sql_create_stop_table)
    cur.execute(sql_create_schedule_table)
    cur.execute(sql_create_booking_table)
    cur.execute(sql_create_at_table)

    con.commit()
    cur.close()
    con.close()