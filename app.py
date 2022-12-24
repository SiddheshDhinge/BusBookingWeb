print("\n\n\nSTARTED\n\n\n")
from flask import Flask, render_template, session, flash, request, jsonify, redirect
from app.model.database import connectDB, createAllTables, dropAllTables
from datetime import timedelta
# Establish database session
connectDB()
createAllTables()
# from model.session_manager import getSessionStatus, addActiveSession
from app import label, label_reason
from app.controller_owner import ControllerOwner
from app.controller_operator import ControllerOperator
from app.controller_customer import ControllerCustomer


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
    return ControllerCustomer().handleRequest()

@app.route('/operator', methods=['POST'])
def operator():
    return ControllerOperator().handleRequest()

@app.route('/login/<role>', methods=['GET', 'POST'])
def login(role):
    if(role == 'owner'):
        return ControllerOwner().handleLogin()
    elif(role == 'operator'):
        return ControllerOperator().handleLogin()
    elif(role == 'customer'):
        return ControllerCustomer().handleLogin()
    else:
        return '404'
    if(request.method == 'POST'):
        controllerObj = ControllerOwner()
        controllerObj.handleLogin()
        flash(controllerObj.response_data[label.details])    

        if(controllerObj.response_data[label.success] == True):
            session.permanent = True
            return redirect('/')
        else:
            return render_template('login.html', 
                username = label.username,
                password = label.password,
                toUrl = 'loginOwner'
            )

    else:
        return render_template('login.html', 
            username = label.username,
            password = label.password,
            toUrl = 'loginOwner'
        )


@app.route('/logoutOwner', methods=['GET'])
def logoutOwner():
    controllerObj = ControllerOwner()
    controllerObj.handleLogout()
    flash(controllerObj.response_data[label.details])
    if(controllerObj.response_data[label.success] == True):
        return render_template('login.html',
            username = label.username,
            password = label.password,
            toUrl = 'loginOwner'
        )
    else:
        pass


@app.route('/loginOperator', methods=['GET', 'POST'])
def loginOperator():
    if(request.method == 'POST'):
        controllerObj = ControllerOperator()
        controllerObj.handleLogin()
        flash(controllerObj.response_data[label.details])    

        if(controllerObj.response_data[label.success] == True):
            session.permanent = True
            return redirect('/')
        else:
            return render_template('login.html', 
                username = label.username,
                password = label.password,
                toUrl = 'loginOperator'
            )

    else:
        return render_template('login.html', 
            username = label.username,
            password = label.password,
            toUrl = 'loginOperator'
        )


@app.route('/logoutOperator', methods=['GET'])
def logoutOperator():
    controllerObj = ControllerOperator()
    controllerObj.handleLogout()
    flash(controllerObj.response_data[label.details])
    if(controllerObj.response_data[label.success] == True):
        return render_template('login.html',
            username = label.username,
            password = label.password,
            toUrl = 'loginOperator'
        )
    else:
        pass

@app.route('/viewSchedules')
def viewSchedules():
    controllerObj = ControllerOperator()
    controllerObj.handleViewSchedule()
    return render_template('table.html', response_data= controllerObj.response_data)

@app.route('/debug')
def debug():
    # flash('YES OWNER!!!')
    # getSessionStatus(session[model.label.])
    return f'Session : '

@app.route('/layout')
def lay1():
    flash(label_reason.loginInRequired)
    return render_template('layout.html')

if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app