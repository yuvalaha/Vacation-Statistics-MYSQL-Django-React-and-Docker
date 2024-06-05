from utils.dal import *
from models.user_model import *

class AuthLogic:
    # Constructor function creating Dal object
    def __init__(self):
        self.dal = Dal()

    # Creating new user
    def add_user(self, user):
        sql = "INSERT INTO users (first_name, last_name, email, password, role_id) VALUES (%s, %s, %s, %s, %s)"
        params = (user.first_name, user.last_name, user.email, user.password, 2)
        last_inserted_id = self.dal.insert(sql, params)
        return last_inserted_id
    
    # Get user by email and password
    def get_user_by_email_and_password(self, email, password):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        params= (email , password)    
        user = self.dal.get_scalar(sql, params)  
        return user
      
    # Check if email exist  
    def is_email_exists_in_data(self, email):
        params = (email,)
        # result get 1 if the email exists else 0
        result = self.dal.execute_stored_procedure("is_email_exist", params)[0]["email_exists"]
        if result == 1:
            return True
        return False

    # Check if index exist
    def is_user_index_exist(self, user_id):
        sql = "SELECT CASE WHEN EXISTS(SELECT 1 FROM users WHERE user_id = %s) THEN 1 ELSE 0 END AS IndexExists;"
        params = (user_id, )
        return self.dal.get_scalar(sql, params)['IndexExists']
  
    # Close resources 
    def close(self):
        self.dal.close()
        
    # Enabling "with" keyword usage:
    def __enter__(self):
        return self

    # Disposing when exiting "with" block:
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()