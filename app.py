print("\n\n\nSTARTED\n\n\n")
from flask import Flask, render_template, session
from model.database import connectDB, createAllTables, dropAllTables

#Establish database session
# connectDB()
# createAllTables()

# from model.session_manager import getSessionStatus, addActiveSession
import controller_owner
import controller_customer
import controller_operator

import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_url_path="", static_folder="web/static", template_folder="web/templates")
app.secret_key = os.environ['app_secret']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bookbus')
def bookbus():
    return render_template('bookbus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

@app.route('/owner', methods=['POST'])
def owner():
    return controller_owner.handleRequest()

@app.route('/customer', methods=['POST'])
def customer():
    return controller_customer.handleRequest()

@app.route('/operator', methods=['POST'])
def operator():
    return controller_operator.handleRequest()



# @app.route('/debug')
# def debug():
#     sess = addActiveSession("@siddhesh")
#     getSessionStatus(session['session-id'])
#     return f'Session : {sess}'

if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app