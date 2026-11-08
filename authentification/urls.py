from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import signup
urlpatterns = [

    path("" , LoginView.as_view(), name='login'),
    path("logout/" , LogoutView.as_view(), name='logout'),
    path('signup/' , signup.as_view() ,name= "signup"),



]