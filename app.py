from flask import Flask, render_template, session
from model import session_manager
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

@app.route('/debug')
def debug():
    sess = session_manager.addActiveSession("@siddhesh")
    session_manager.getSessionStatus(session['session-id'])
    return f'Session : {sess}'

if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app