from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('profile/', views.profile, name='profile'),  # Adjust as needed for profile page

]
