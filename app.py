print("\n\n\nSTARTED\n\n\n")


# Configure Database Connection
from app.model.database import connectDB, createAllTables
connectDB()

# Import Routes
from routes import requestRoutes

#Create All Database Tables
createAllTables()


# Import Dependencies
from flask import Flask
from flask_uuid import FlaskUUID
import os
from dotenv import load_dotenv
from datetime import timedelta
load_dotenv()


# Create App and Set Secret Key, session_lifetime
app = Flask(__name__, static_url_path="", static_folder="app/web/static", template_folder="app/web/templates")
FlaskUUID(app)
app.secret_key = os.environ['app_secret']
app.permanent_session_lifetime = timedelta(minutes= 15)
ip_address = os.environ['ip_address']


# Register Routes Blueprint
app.register_blueprint(requestRoutes)


if __name__ == "__main__":
    app.run(debug=True)


# for waitress
# def create_app():
#    return app