from django.contrib import admin
from django.urls import path
from users.views import login,register,account,logout


app_name = 'users'

urlpatterns = [
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('account/',account,name = 'account'),
    path('logout/', logout, name='logout'),
]

