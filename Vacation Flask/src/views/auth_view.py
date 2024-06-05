from flask import render_template, Blueprint, redirect, request, url_for
from facades.auth_facade import AuthFacade
from models.client_errors import ValidationError, AuthError

# Managing the entire view
auth_blueprint = Blueprint("auth_view", __name__)

# Create auth facade: 
auth_facade = AuthFacade()

# Register new user:
@auth_blueprint.route("/register", methods = ["GET", "POST"])
def register():
    try:
        if request.method == "GET":
            return render_template("register.html", new_user = {})
        auth_facade.register() 
        return redirect(url_for("vacations_view.vacations"))
    except ValidationError as err: # Check the validation error
           return render_template("register.html", error = err.message, new_user = err.model)
       
    # Register new user:
@auth_blueprint.route("/login", methods = ["GET", "POST"])   
def login():
    try:
        if request.method == "GET":
            err = request.args.get("error") 
            return render_template("login.html", error = err, credentials = {})
        auth_facade.login()
        return redirect(url_for("vacations_view.vacations"))
    except(ValidationError, AuthError) as err:
        return render_template("login.html", error = err.message, credentials=err.model)  
        
@auth_blueprint.route("/logout")
def logout():
    auth_facade.logout()
    return redirect(url_for("home_view.home"))  