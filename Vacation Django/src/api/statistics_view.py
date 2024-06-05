from all_vacations.models import LikesModel, AllVacationsModel 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from members.models import  UserModel
from django.db.models import  Count


# Route for returning past, on going and future vacations
@api_view(["GET"])
def vacations_status(request):
    try:
        # Check if the user logged in
        if ("is_logged-in" in request.session) == False: 
            json = {"error": "You are not logged in."}
            return Response(json, status.HTTP_401_UNAUTHORIZED)
    
        # Get the current date
        today = datetime.now().date()
        
        # Get past vacation using filter - lt=> less than
        past_vacations = AllVacationsModel.objects.filter(vacation_end_date__lt = today)
        
        # Get on going vacation using filter - gte=> greater than or equal, lt=> less than
        on_going_vacations = AllVacationsModel.objects.filter(vacation_start_date__lte = today, vacation_end_date__gte = today)

        # Get future vacations using filter - gt=> greater than or equal
        future_vacations = AllVacationsModel.objects.filter(vacation_start_date__gt=today)
        
        # Sum the the total past, future and on going vacations
        total_past_vacations = past_vacations.count()
        total_on_going_vacations = on_going_vacations.count()
        total_future_vacations = future_vacations.count()

        # Dictionary of vacation status
        vacations_data = {
            "past_vacations":  total_past_vacations,
            "on_going_vacations":  total_on_going_vacations,
            "future_vacations": total_future_vacations
        }
        
        # Send the json data
        return Response(vacations_data)
        
    # Handling with error
    except Exception as err:
        json = {"error": str(err)}
        return Response(json, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Route for returning total likes
@api_view(["GET"])
def total_likes(request):
    try:

        # Check if the user logged in
        if ("is_logged-in" in request.session) == False: 
            json = {"error": "You are not logged in."}
            return Response(json, status.HTTP_401_UNAUTHORIZED)
        # Get all the likes exist in the system 
        all_likes = LikesModel.objects.all().count()
        
        total_likes_data = {
            "total_likes": all_likes
        }
        
        return Response(total_likes_data)
    
    except Exception as err:
        json = {"error": str(err)}
        return(Response(json, status.HTTP_500_INTERNAL_SERVER_ERROR))
    
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Route for returning total users
@api_view(["GET"])    
def total_users(request):
    try:
        # Check if the user logged in
        if ("is_logged-in" in request.session) == False: 
            json = {"error": "You are not logged in."}
            return Response(json, status.HTTP_401_UNAUTHORIZED)
        
        # Get the number of users in the system
        all_users = UserModel.objects.all().count()
        total_users = {
            "total_users" : all_users
        }
        return Response(total_users)
    
    except Exception as err:
        json = {"error": str(err)}
        return(Response(json, status.HTTP_500_INTERNAL_SERVER_ERROR))
   
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Route for returning an array containing objects of the distribution of likes according to vacation destinations
@api_view(["GET"])
def like_by_vacation(request):
    try:
        # Check if the user logged in
        if ("is_logged-in" in request.session) == False: 
            json = {"error": "You are not logged in."}
            return Response(json, status.HTTP_401_UNAUTHORIZED)
        
        # Get every country with the sum of likes
        all_destinations = AllVacationsModel.objects.values_list('country__country_name', flat=True).distinct() # flat = true means getting regular list with values_list and not list of tuples
        # country - foreign key inside vacations table, country_name - inside the foreign table
        # distinct - ensures that only unique country names are retrieved from the queryset of vacation denies duplicates countries   
        
        
        # Get the likes distribution based on vacation destinations
        likes_distribution = LikesModel.objects.values('vacation__country__country_name').annotate(total_likes=Count('vacation_id')).order_by('vacation__country__country_name')
        # annotate let us perform functions like Sum/Count, in this case i sum the total likes for every vacation

        # Create a dictionary to store likes for each destination
        likes_according_to_destination = {}

        # Insert data to likes_according_to_destination
        for destination in all_destinations:
            likes_info = likes_distribution.filter(vacation__country__country_name=destination).first()
            # It's used to get the first item that matches the specific country name in the queryset of likes
            
            # Insert the likes into total likes
            total_likes = likes_info['total_likes'] if likes_info else 0
            
            # Insert the likes into likes_according_to_destination 
            likes_according_to_destination[destination] = total_likes

        # Transform the dictionary into the desired structure
        likes_according_to_destination = [{'destination': destination, 'likes': likes} for destination, likes in likes_according_to_destination.items()]

        return Response(likes_according_to_destination)

    # Exceptions
    except Exception as err:
        json = {"error": str(err)}
        return Response(json, status.HTTP_500_INTERNAL_SERVER_ERROR)
