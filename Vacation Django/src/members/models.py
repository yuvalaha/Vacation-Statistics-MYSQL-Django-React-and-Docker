from django.db.models import Model, CharField, ForeignKey, AutoField, RESTRICT
from django.forms import EmailInput, ModelForm, PasswordInput



# Role form model:
class RoleModel(Model):

    role_id = AutoField(primary_key=True)

    role_name = CharField(max_length=30)

    # __str__ magic method will return role name:
    def __str__(self):
        return self.role_name

    class Meta:
        db_table = "roles"
        managed = False

# User form model:
class UserModel(Model):
    user_id = AutoField(primary_key=True)

    first_name = CharField(max_length=30)

    last_name = CharField(max_length=30)

    email = CharField(max_length=100)

    password = CharField(max_length=1000)
    
    role = ForeignKey(RoleModel, on_delete=RESTRICT)

    class Meta:
        db_table = "users"
        managed = False
        


# Login form model:
class LoginForm(ModelForm):

    class Meta:
        model = UserModel
        fields = ["email", "password"]
        widgets = {
            "email": EmailInput(attrs = {"class": "form-control", "maxlength": 100}),
            "password": PasswordInput(attrs = {"class": "form-control", "maxlength": 100}),
        }







