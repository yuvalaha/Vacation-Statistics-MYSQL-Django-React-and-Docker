from flask import Flask, render_template, request
from utils.app_config import AppConfig
from views.home_view import home_blueprint
from views.auth_view import auth_blueprint
from views.vacations_view import vacations_blueprint
from views.about_view import about_blueprint
from views.reviews_view import reviews_blueprint
from views.join_us_view import join_us_blueprint
from utils.logger import Logger
from logging import getLogger, ERROR

# Creating Flask server:
app = Flask(__name__)

# Create session secret key:
app.secret_key = AppConfig.session_secret_key

# Registering all routes:
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(vacations_blueprint)
app.register_blueprint(reviews_blueprint)
app.register_blueprint(join_us_blueprint)

# 404 errors
@app.errorhandler(404)
def page_not_found(error): 
    return render_template("404.html")

# Catch any unhandled errors
@app.errorhandler(Exception)
def catch_all_errors(error):
    print(error) 
    Logger.log(error)
    error_message = error if AppConfig.is_development else "Some error occurred, please try again."
    return render_template("500.html", error = error_message)

# Quiet console (werkzeug = ארגז כלים): 
getLogger("werkzeug").setLevel(ERROR)

# Display website address on terminal:
print("Listening on http://localhost:5000")