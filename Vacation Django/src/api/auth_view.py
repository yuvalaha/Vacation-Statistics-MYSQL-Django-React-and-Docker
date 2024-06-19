from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import UserSerializer
from members.models import  UserModel
from utils.cyber import Cyber


# Login Route
@api_view(["POST"])
def log_in(request):
    try:
        # Get email and password from the back
        if request.method == "POST":
            email = request.data.get("email")
            password = request.data.get("password")
        
        # Try to find if user exist in the database
        user = UserModel.objects.filter(email=email).first()
        request.session["is_logged-in"] = True
        # If the user exist
        if user:
            # Get the hashed password from the data base
            stored_password = user.password 
            
            # Hash the provided password with salt
            hashed_text = Cyber.hash_func(password)
            
            # Check whether the hashed version of the user entered password matches the hashed password stored in the database.
            if stored_password == hashed_text:
                # Login
                serializer = UserSerializer(user)
                
                # Set session data to mark user as logged in
                request.session["is_logged-in"] = True
                return Response({"user": serializer.data, "success": "Login successful, welcome admin."}, status=status.HTTP_200_OK)
            else:
                json = {"error": "incorrect email or password."}
                return Response(json, status=status.HTTP_401_UNAUTHORIZED)
        else:
            json = {"error": "incorrect email or password."}
            return Response(json, status=status.HTTP_401_UNAUTHORIZED)
            
                
    except Exception as err:
        
        json = { "error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Logout Route
@api_view(["DELETE"])
def log_out(request):
    try:
        request.session.flush()
        json = {"You logged out": " Have a nice day! "}
        return Response(json, status.HTTP_200_OK)
    except Exception as err:
        json = {"error": str(err)}
        return Response(json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)