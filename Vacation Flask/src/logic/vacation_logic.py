from utils.dal import *
from models.vacations_model import *
from utils.image_handler import ImageHandler


class VacationLogic:
    # Constructor function creating Dal object
    def __init__(self):
        self.dal = Dal()

    # Get one vacation

    def get_one_vacation(self, vacation_id):
        sql = "SELECT * FROM all_vacations WHERE vacation_id = %s"
        params = (vacation_id, )
        vacation = self.dal.get_scalar(sql, params)
        return vacation

    # Add new vacation

    def add_vacation(self, vacation):
        image_name = ImageHandler.save_image(vacation.vacation_image)
        sql = "INSERT INTO all_vacations (country_id, description, vacation_start_date, vacation_end_date, price, vacation_image) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (vacation.country_id, vacation.description, vacation.vacation_start_date,
                  vacation.vacation_end_date, vacation.price, image_name)
        last_inserted_id = self.dal.insert(sql, params)
        return last_inserted_id

    # Get all vacations and in addition country_name
    def get_all_vacations_with_country_name(self):
        sql = "SELECT all_vacations.*, countries.country_name FROM all_vacations JOIN countries ON all_vacations.country_id = countries.country_id ORDER BY `all_vacations`.`vacation_start_date`"
        table = self.dal.get_table(sql)
        return table

    # Update vacation

    def update_vacation(self, vacation):
        old_image_name = self.__get_old_image_name(vacation.vacation_id)
        image_name = ImageHandler.update_image(
            old_image_name, vacation.vacation_image)
        sql = "UPDATE all_vacations SET country_id = %s, description = %s, vacation_start_date = %s, vacation_end_date = %s, price = %s, vacation_image = %s WHERE vacation_id = %s"
        params = (vacation.country_id, vacation.description, vacation.vacation_start_date,
                  vacation.vacation_end_date, vacation.price, image_name, vacation.vacation_id)
        row_count = self.dal.update(sql, params)
        return row_count

    # Delete vacation
    def delete_vacation(self, vacation_id):
            image_name = self.__get_old_image_name(vacation_id)
            ImageHandler.delete_image(image_name)

            sql = "DELETE FROM all_vacations WHERE vacation_id = %s"
            params = (vacation_id,)
            row_count = self.dal.delete(sql, params)

            sql_update = "UPDATE all_vacations SET vacation_id = vacation_id - 1 WHERE vacation_id > %s"
            self.dal.update(sql_update, (vacation_id,))
            # sql_update_likes = "UPDATE likes SET vacation_id = vacation_id - 1 WHERE vacation_id > %s"
            # self.dal.update(sql_update_likes, (vacation_id,))

            # Update the new vacations table id 
            update_sql = "ALTER TABLE all_vacations AUTO_INCREMENT = %s" 
            last_vacation_index = self.get_max_vacation_index()
            self.dal.update(update_sql, (last_vacation_index + 1,))

            return row_count

    # Get current image name
    def __get_old_image_name(self, vacation_id):
        sql = "SELECT vacation_image FROM all_vacations WHERE vacation_id=%s"
        result = self.dal.get_scalar(sql, (vacation_id, ))
        return result["vacation_image"]

    # Add like
    def add_like(self, user_id, vacation_id):
        sql = "INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)"
        params = (user_id, vacation_id)
        last_inserted_id = self.dal.insert(sql, params)
        return last_inserted_id

    # Delete like
    def delete_like(self, user_id, vacation_id):
        sql = "DELETE FROM likes WHERE user_id = %s AND vacation_id = %s"
        params = (user_id, vacation_id)
        row_count = self.dal.delete(sql, params)
        return row_count

    # Check if index exist
    def is_vacation_index_exist(self, vacation_id):
        sql = "SELECT CASE WHEN EXISTS(SELECT 1 FROM all_vacations WHERE vacation_id = %s) THEN 1 ELSE 0 END AS IndexExists"
        params = (vacation_id, )
        return self.dal.get_scalar(sql, params)['IndexExists']

    # Check if specific user already liked specific vacation
    def is_user_liked_same_vacation(self, user_id, vacation_id):
        sql = "SELECT CASE WHEN EXISTS (SELECT 1 FROM likes WHERE user_id = %s AND vacation_id = %s) THEN 1 ELSE 0 END AS RowExists"
        params = (user_id, vacation_id)
        return self.dal.get_scalar(sql, params)['RowExists']

    # Return the number of likes of every vacation
    def how_many_likes_for_every_vacation(self):
        sql = "SELECT all_vacations.vacation_id, COUNT(likes.user_id) AS total_likes FROM all_vacations LEFT JOIN likes ON all_vacations.vacation_id = likes.vacation_id GROUP BY all_vacations.vacation_id"
        return self.dal.get_table(sql)

    # Return the maximum index of vacation table
    def get_max_vacation_index(self):
        sql = "SELECT MAX(vacation_id) AS max_index FROM all_vacations;"
        return self.dal.get_scalar(sql)["max_index"]

    # Get Countries id and names
    def get_countries(self):
        sql = "SELECT * FROM countries"
        return self.dal.get_table(sql)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Additional content to my website(4 different possibilities of vacations ):
    def get_special_locations(self):
        sql = "SELECT all_vacations.*, countries.country_name FROM all_vacations JOIN countries ON all_vacations.country_id = countries.country_id WHERE all_vacations.country_id = 1 OR all_vacations.country_id = 7 OR all_vacations.country_id = 8 OR all_vacations.country_id = 9 OR all_vacations.country_id = 11 OR all_vacations.country_id = 13 OR all_vacations.country_id = 14 ORDER BY `all_vacations`.`vacation_start_date`"
        return self.dal.get_table(sql)
    
    def get_special_food(self):
        sql = "SELECT all_vacations.*, countries.country_name FROM all_vacations JOIN countries ON all_vacations.country_id = countries.country_id WHERE all_vacations.country_id = 1 OR all_vacations.country_id = 5 OR all_vacations.country_id = 10 ORDER BY `all_vacations`.`vacation_start_date`"
        return self.dal.get_table(sql)
    
    def get_winter_vacations(self):
        sql = "SELECT all_vacations.*, countries.country_name FROM all_vacations JOIN countries ON all_vacations.country_id = countries.country_id WHERE (MONTH(vacation_start_date) = 12 OR MONTH(vacation_start_date) = 1 OR MONTH(vacation_start_date) = 2) AND all_vacations.country_id != 9 ORDER BY `all_vacations`.`vacation_start_date`;"
        return self.dal.get_table(sql)
        
    def get_summer_vacations(self):  
       sql = "SELECT all_vacations.*, countries.country_name FROM all_vacations JOIN countries ON all_vacations.country_id = countries.country_id WHERE MONTH(vacation_start_date) = 6 OR MONTH(vacation_start_date) = 7 OR MONTH(vacation_start_date) = 8  ORDER BY `all_vacations`.`vacation_start_date`"
       return self.dal.get_table(sql)
          

    # Close resources

    def close(self):
        self.dal.close()
