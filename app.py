print("\n\n\nSTARTED\n\n\n")
from flask import Flask, render_template, session, flash, request, jsonify, redirect
from app.model.database import connectDB, createAllTables, dropAllTables
from datetime import timedelta
# Establish database session
connectDB()
createAllTables()
# from model.session_manager import getSessionStatus, addActiveSession
from app.controller_owner import ControllerOwner
from app import controller_customer, label
from app.controller_operator import ControllerOperator


import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_url_path="", static_folder="app/web/static", template_folder="app/web/templates")
app.secret_key = os.environ['app_secret']
app.permanent_session_lifetime = timedelta(minutes= 5)

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
    return ControllerOwner().handleRequest()

@app.route('/customer', methods=['POST'])
def customer():
    return controller_customer.handleRequest()

@app.route('/operator', methods=['POST'])
def operator():
    return ControllerOperator().handleRequest()

@app.route('/loginOwner', methods=['GET', 'POST'])
def loginOwner():
    if(request.method == 'POST'):
        controllerObj = ControllerOwner()
        controllerObj.handleLogin()
        if(controllerObj.response_data[label.success] == False):
            flash(controllerObj.response_data[label.details])    
            return render_template('loginOwner.html', 
                username = label.username,
                password = label.password
            )
        else:
            flash(controllerObj.response_data[label.details])
            session.permanent = True
            return redirect('/')

    else:
        return render_template('loginOwner.html', 
            username = label.username,
            password = label.password
        )


@app.route('/logoutOwner', methods=['GET'])
def logoutOwner():
    controllerObj = ControllerOwner()
    controllerObj.handleLogout()
    if(controllerObj.response_data[label.success] == True):
        flash(controllerObj.response_data[label.details])
        return render_template('loginOwner.html',
            username = label.username,
            password = label.password
        )
    else:
        flash(controllerObj.response_data[label.details])
    
@app.route('/debug')
def debug():
    # flash('YES OWNER!!!')
    # getSessionStatus(session[model.label.])
    return f'Session : '

if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app