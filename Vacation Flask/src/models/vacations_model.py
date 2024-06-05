from utils.compare_dates import CompareDates


# Vacations Model
class VacationsModel:

    # Constructor function
    def __init__(self, vacation_id, country_id, description, vacation_start_date, vacation_end_date, price, vacation_image):

        self.vacation_id = vacation_id
        self.country_id = country_id
        self.description = description
        self.vacation_start_date = vacation_start_date
        self.vacation_end_date = vacation_end_date
        self.price = price
        self.vacation_image = vacation_image

    # Display vacations data
    def display(self):
        print(f"Vacation ID: {self.vacation_id}\nCountry ID: {self.country_id}\nVacation Description: {self.description}\nVacation start date: {self.vacation_start_date}\nVacation end date: {self.vacation_end_date}\nPrice: ${self.price}\nVacation image: {self.vacation_image}")
        
        
    # The function converts vacation dictionary to vacation model:
    @staticmethod
    def vacation_dictionary_to_vacation_model(vacation_dictionary):
        vacation_model = VacationsModel(vacation_dictionary["vacation_id"], vacation_dictionary["country_id"], vacation_dictionary["description"], 
                  vacation_dictionary["vacation_start_date"], vacation_dictionary["vacation_end_date"],vacation_dictionary["price"], vacation_dictionary["vacation_image"])
        return vacation_model
        
    # The function converts list of vacations dictionary to list of vacations models:
    @staticmethod
    def vacation_dictionaries_to_vacations_model(list_of_vacations_dictionary):
        vacations = []
        for vacation in list_of_vacations_dictionary:
            new_vacation = VacationsModel.vacation_dictionary_to_vacation_model(vacation)
            vacations.append(new_vacation)
        return vacations    
    
   # Validating a new vacation insert:
    def validate_insert(self):
       if not self.country_id: return "Missing country."
       if not self.description: return "Missing description."
       if not self.vacation_start_date: return "Missing vacation start date."
       if not self.vacation_end_date: return "Missing vacation end date."
       if not self.price: return "Missing price."
       if not self.vacation_image: return "Missing vacation image."
       if int(self.price) > 10000 or int(self.price) < 0: return "The vacation price cannot exceed $10,000 and should not be negative."
       if not CompareDates.is_vacation_in_the_past(self.vacation_start_date): return "Vacation start date cannot be in the past."
       if not CompareDates.is_start_date_before_end_date(self.vacation_start_date, self.vacation_end_date): return "Vacation start date cannot be after the vacation end date."
   
   # Validating vacation update:
    def validate_update(self):
       if not self.country_id: return "Missing country."
       if not self.description: return "Missing description."
       if not self.vacation_start_date: return "Missing vacation start date."
       if not self.vacation_end_date: return "Missing vacation end date."
       if not self.price: return "Missing price."
       if int(self.price) > 10000 or int(self.price) < 0: return "The vacation price cannot exceed $10,000 and should not be negative."
       if not CompareDates.is_start_date_before_end_date(self.vacation_start_date, self.vacation_end_date): return "Vacation start date cannot be after the vacation end date."
   
   
   
