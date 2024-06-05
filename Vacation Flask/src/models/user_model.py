
from validate_email_address import validate_email
from models.role_model import RoleModel

# User Model
class UserModel:

    # Constructor function
    def __init__(self, user_id, first_name, last_name, email, password, role_id):

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id

    # Display user data
    def display(self):
        print(f"User ID: {self.user_id}, First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}, Password: {self.password}, Role: {self.role_id}")
    
        
        
    # The function converts user dictionary to user model:
    @staticmethod
    def user_dictionary_to_user_model(user_dictionary):
        user_model = UserModel(user_dictionary["user_id"], user_dictionary["first_name"], user_dictionary["last_name"], 
                  user_dictionary["email"], user_dictionary["password"],user_dictionary["role_id"])
        return user_model
        
    # The function converts list of users dictionary to list of users models:
    @staticmethod
    def users_dictionaries_to_users_model(list_of_users_dictionary):
        users = []
        for user in list_of_users_dictionary:
            new_user = UserModel.user_dictionary_to_user_model(user)
            users.append(new_user)
        return users    
    
        
    # Validating a new user registration:
    def validate_insert(self):
        if not self.first_name: return "Missing first name."
        if not self.last_name: return "Missing last name."
        if not self.email: return "Missing email."
        if not self.password: return "Missing password."
        if not self.role_id: return "Missing role id."
        if len(self.first_name) < 2 or len(self.first_name) > 30: return "First name length must be 2 to 30 characters."
        if len(self.last_name) < 2 or len(self.last_name) > 30: return "Last name length must be 2 to 30 characters."
        if len(self.email) < 5 or len(self.email) > 100: return "Email length must be 5 to 100 characters."
        if len(self.password) < 4 or len(self.password) > 60: return "Password must be a minimum of 4 characters and maximum 60 characters."
        if not validate_email(self.email): return "Email is not valid"
        if self.role_id != RoleModel.Admin.value and  self.role_id != RoleModel.User.value: return "Role must be admin or user" 
        return None # Return none if there aren't ant validation error
    
    
    
    
    
    
    
    
    # # Email Getter function
    # @property
    # def email(self):
    #     return self.__email
    

    # # Email Setter function - Check if the email that the user entered is valid
    # @email.setter
    # def email(self, email):
    #     if not is_email_valid(email):
    #         raise ValueError ("You entered wrong email address")
    #     self.__email = email
        
        
    # # Password Getter function
    # @property
    # def password(self):
    #     return self.__password
    
    
    # # Password Setter function - Check if the password that the user entered is valid
    # @password.setter
    # def password(self, password):
    #     if len(password) < 4 :
    #         raise ValueError ("Your password should include at least 4 letters")
    #     self.__password = password