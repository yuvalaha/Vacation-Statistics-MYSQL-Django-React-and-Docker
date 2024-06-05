import datetime

# This class consists of two functions that compare the start date and end date of a vacation and determine whether the vacation is in the future.

class CompareDates:
    def __init__(self):
        pass
    
    @staticmethod
    # The function checks if the user entered a future vacation date  
    def is_vacation_in_the_past(vacation_start_date):
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        vacation_start_date = vacation_start_date.split("-")
        if year > int(vacation_start_date[0]):
            return False
        elif year == int(vacation_start_date[0]) and month > int(vacation_start_date[1]):
            return False
        elif year == int(vacation_start_date[0]) and month == int(vacation_start_date[1]) and day > int(vacation_start_date[2]):
            return False
        return True
        
    @staticmethod  
     # The function checks if the vacation start date is not before end date 
    def is_start_date_before_end_date(vacation_start_date, vacation_end_date):
        
        # Creating year, month and day for start date 
        start_year = vacation_start_date.split("-")[0]    
        start_month = vacation_start_date.split("-")[1]    
        start_day = vacation_start_date.split("-")[2]    
        
        # Creating year, month and day for  end date
        end_year = vacation_end_date.split("-")[0]    
        end_month = vacation_end_date.split("-")[1]    
        end_day = vacation_end_date.split("-")[2] 
        
        # Compare dates
        if end_year < start_year:
            return False
        elif end_year == start_year and end_month < start_month:
            return False
        elif end_year == start_year and end_month == start_month and end_day < start_day :
            return False
        return True