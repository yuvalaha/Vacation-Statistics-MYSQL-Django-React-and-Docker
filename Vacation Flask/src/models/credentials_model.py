from validate_email_address import validate_email
class CredentialsModel:

    # Ctor function
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    # Credentials validation
    def validate(self): 
        if not self.email: return "Missing email."
        if not self.password: return "Missing password."
        if len(self.email) < 5 or len(self.email) > 100: return "Email length must be 5 to 100 characters."
        if len(self.password) < 4 or len(self.password) > 60: return "Password must be a minimum of 4 characters and maximum 60 characters."
        if not validate_email(self.email): return "Email not valid."
        return None # Return none if there aren't ant validation error