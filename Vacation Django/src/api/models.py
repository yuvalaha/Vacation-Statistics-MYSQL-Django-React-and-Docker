from rest_framework.serializers import ModelSerializer
from members.models import UserModel


# Class to convert Login into json
class LoginSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["email", "password"]
       
# Class to convert user into json
class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
       
