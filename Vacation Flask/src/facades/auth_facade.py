from flask import request, session
from logic.auth_logic import *
from utils.cyber import Cyber
from models.role_model import RoleModel
from models.client_errors import ValidationError, AuthError
from models.credentials_model import CredentialsModel
class AuthFacade:

    # Constructor function creating user logic object
    def __init__(self):
        self.logic = AuthLogic()

    # Register new user to the system
    def register(self):
        
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        role_id = RoleModel.User.value
        new_user = UserModel(None, first_name, last_name, email, password, role_id) # Building new user
        error = new_user.validate_insert() 
        if error: raise ValidationError(error, new_user) # Check for validation errors
        # Check if the email is already exist in the system
        if self.logic.is_email_exists_in_data(new_user.email): raise ValidationError("Your email already exist.", new_user)
        new_user.password = Cyber.hash(new_user.password) # Hashing the password
        self.logic.add_user(new_user) # Add the new user into the system
        new_user = self.logic.get_user_by_email_and_password(new_user.email, new_user.password) # Get the dictionary new_user from database
        del new_user["password"] # Remove passwords from session.
        session["user"] = new_user # Save the user inside the session dictionary.


    # Login existing user
    def login(self):
        email = request.form.get("email")
        password = request.form.get("password")
        credentials = CredentialsModel(email, password) # Building new user credentials
        error = credentials.validate()
        if error: raise ValidationError(error, credentials) # Check for validation errors
        hashed_password = Cyber.hash(credentials.password) # Hashing the password
        user = self.logic.get_user_by_email_and_password(
            credentials.email, hashed_password) # Get the dictionary user from database

        if not user: raise AuthError("Incorrect email or password", credentials) # Check if user exists
        del user["password"] # Remove passwords from session.
        session["user"] = user # Save the user inside the session dictionary.

    # Logout:
    def logout(self):
        session.clear() # Clear session for logout.


    # Block non logged in users: 
    def block_anonymous(self):
        user = session.get("user")
        if not user:
            raise AuthError("You are not logged in.")    
    
    
    # Block non admin users:
    def block_non_admin(self):
        user = session.get("user")
        if not user:
            raise AuthError("You are not logged in.")    
        if user["role_id"] != RoleModel.Admin.value:
            raise AuthError("You are not authorized.")
        

    
    
    # Close resources
    def close(self):
        self.logic.close()

    # Enabling "with" keyword usage:
    def __enter__(self):
        return self

    # Disposing when exiting "with" block:
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()
        
        
        
    # # Check if user exist
    # def is_user_exist(self, user_index):
    #     return self.logic.is_user_index_exist(user_index)
    
    