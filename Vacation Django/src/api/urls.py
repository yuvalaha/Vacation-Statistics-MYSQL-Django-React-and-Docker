from django.urls import path
from . import views
from . import statistics_view, auth_view

urlpatterns = [
    
    # Statistics urls
    
    # GET http://localhost:8000/api/vacations_status
    path("vacations_status", statistics_view.vacations_status),
    
    # GET http://localhost:8000/api/total_likes
    path("total_likes", statistics_view.total_likes), 
    
    # GET http://localhost:8000/api/total_users
    path("total_users", statistics_view.total_users),
    
    # GET http://localhost:8000/api/destination_and_likes
    path("like_by_vacation", statistics_view.like_by_vacation), 
    
    # Auth urls
    
    # GET http://localhost:8000/api/login
    path("login", auth_view.log_in),
    
    # GET http://localhost:8000/api/logout
    path("logout", auth_view.log_out),

]
