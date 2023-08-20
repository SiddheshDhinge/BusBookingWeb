print("\n\n\nSTARTED\n\n\n")

# Import Dependencies
from waitress import serve
from flask import Flask
from flask_uuid import FlaskUUID
import os
from dotenv import load_dotenv
from datetime import timedelta

# Load Environments
load_dotenv() # Load .env file
# Load environment specific file
if os.getenv("DEBUG") == "True":
    load_dotenv(".dev.env")
else:
    load_dotenv(".prod.env")

# Configure Database Connection
from app.model.database import connectDB, createAllTables
connectDB()

# Import Routes
from routes import requestRoutes

#Create All Database Tables
createAllTables()


# Create App and Set Secret Key, session_lifetime
app = Flask(__name__, static_url_path="", static_folder="app/web/static", template_folder="app/web/templates")
FlaskUUID(app)
app.secret_key = os.environ['app_secret']
app.permanent_session_lifetime = timedelta(minutes= 15)


# Register Routes Blueprint
app.register_blueprint(requestRoutes)


if __name__ == "__main__":
    if os.getenv("DEBUG") == "True":
        app.run(debug=True)
    else:
        serve(app, host='0.0.0.0', port=8080)