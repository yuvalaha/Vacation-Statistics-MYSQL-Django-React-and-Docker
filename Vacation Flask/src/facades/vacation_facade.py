from logic.vacation_logic import VacationLogic
from logic.auth_logic import AuthLogic
from utils.compare_dates import CompareDates
from models.vacations_model import VacationsModel
from flask import request, session
from models.client_errors import ValidationError, ResourceNotFoundError, AuthError

class VacationFacade:
    
    
    
    # Constructor function creating VacationLogic object and CompareDates object
    def __init__(self):        
        self.vacation_logic = VacationLogic()
        self.compare_dates = CompareDates()
        self.user_logic = AuthLogic()

    # Get all vacations
    def get_all_vacations(self):
        vacations = self.vacation_logic.get_all_vacations_with_country_name()
        return vacations
    
    # Get one vacation
    def get_one_vacation(self, vacation_id):
        vacation = self.vacation_logic.get_one_vacation(vacation_id)
        if not vacation: raise ResourceNotFoundError(vacation_id)
        return vacation

    # Creating new vacation
    def add_new_vacation(self):
        country_id = request.form.get("country_id")
        description = request.form.get("description")
        vacation_start_date = request.form.get("vacation_start_date")
        vacation_end_date = request.form.get("vacation_end_date")
        price = request.form.get("price")
        vacation_image = request.files["vacation_image"]
        new_vacation = VacationsModel(None, country_id, description, vacation_start_date, vacation_end_date, price, vacation_image)       
        error = new_vacation.validate_insert()
        if error: raise ValidationError(error, new_vacation)
        self.vacation_logic.add_vacation(new_vacation)

    # Add like for vacation
    def add_like_for_vacation(self, user_id, vacation_id):  
        self.vacation_logic.add_like(user_id, vacation_id)
        
        
    # Update vacation
    def update_vacation(self):
        vacation_id = request.form.get("vacation_id")
        country_id = request.form.get("country_id")
        description = request.form.get("description")
        vacation_start_date = request.form.get("vacation_start_date")
        vacation_end_date = request.form.get("vacation_end_date")
        price = request.form.get("price")
        vacation_image = request.files["vacation_image"]
        updated_vacation = VacationsModel(vacation_id, country_id, description, vacation_start_date, vacation_end_date, price, vacation_image)       
        error = updated_vacation.validate_update()
        if error: raise ValidationError(error, updated_vacation)
        self.vacation_logic.update_vacation(updated_vacation)


     
    # Delete vacation 
    def delete_vacation(self, vacation_id):
        self.vacation_logic.delete_vacation(vacation_id)
        
        
     # Check if user exist
    def is_vacation_exist(self, vacation_index):
        return self.vacation_logic.is_vacation_index_exist(vacation_index)
    
    # Check if user liked specific vacation
    def is_user_already_liked_same_vacation(self, user_id, vacation_id):
        is_liked = self.vacation_logic.is_user_liked_same_vacation(user_id, vacation_id)
        return is_liked
            

    # Check the number of likes according of every vacation
    def how_many_likes_for_vacation(self):
        likes = self.vacation_logic.how_many_likes_for_every_vacation()
        return likes
    
    # Remove like
    def delete_like_for_vacation(self, user_id,vacation_id):
        self.vacation_logic.delete_like(user_id, vacation_id)
    
    # Return all the possible countries for vacation
    def get_countries_name(self):
        return self.vacation_logic.get_countries()   

    # Get all vacations with like status 
    def get_vacations_with_like_status(self, user_id):
        vacations = self.get_all_vacations()  
        vacation_like_status = {}
        for vacation in vacations:
            like_status = self.is_user_already_liked_same_vacation(user_id, vacation.get('vacation_id'))
            vacation_like_status[vacation.get('vacation_id')] = like_status
        return vacation_like_status



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # Get special vacations 
    def special_locations(self):
        special_locations = self.vacation_logic.get_special_locations()
        return special_locations
    
    # Get culinary vacations
    def culinary_locations(self):
        culinary_locations = self.vacation_logic.get_special_food()
        return culinary_locations
    
    # Get winter vacations
    def winter_vacations(self):
        winter_vacations = self.vacation_logic.get_winter_vacations()
        return winter_vacations
    
    # Get summer vacations
    def summer_vacations(self):
        summer_vacations = self.vacation_logic.get_summer_vacations()
        return summer_vacations

    # Close resources 
    def close(self):
        self.vacation_logic.close()
        
    # Enabling "with" keyword usage:
    def __enter__(self):
        return self

    # Disposing when exiting "with" block:
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()


