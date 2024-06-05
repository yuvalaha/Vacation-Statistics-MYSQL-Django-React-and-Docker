from django.db.models import Model, CharField, IntegerField, ForeignKey, RESTRICT, DateField, AutoField
from datetime import datetime
from members.models import UserModel

# Countries Model
class CountriesModel(Model):
    
    country_id = AutoField(primary_key=True)
    
    country_name = CharField(max_length = 30)
    
    # __str__ magic method will return country name:
    def __str__(self):
        return self.country_name
    
    # Metadata
    class Meta:
        db_table = "countries"
        managed = False

# ----------------------------------------------------------------------------------------------------

# Vacations Model
class AllVacationsModel(Model):
    
    vacation_id = AutoField(primary_key=True)

    country = ForeignKey(CountriesModel, on_delete=RESTRICT)
    
    description = CharField(max_length = 1000)
    
    vacation_start_date = DateField(default = datetime.now)
    
    vacation_end_date = DateField(default = datetime.now)
    
    price = IntegerField()
    
    vacation_image = CharField(max_length = 1000)
    
    # Metadata
    class Meta:
        db_table = "all_vacations"
        managed = False
        
# ----------------------------------------------------------------------
    
# Likes Model
class LikesModel(Model):
    
    user = ForeignKey(UserModel,  primary_key=True, on_delete= RESTRICT)
    
    vacation = ForeignKey(AllVacationsModel, on_delete= RESTRICT)
    
    # Metadata
    class Meta:
        db_table = "likes" 
        managed=False
        unique_together = (("user_id", "vacation_id"),)

             
