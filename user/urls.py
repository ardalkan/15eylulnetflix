from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    path('profiles/',profiles, name='profiles'),
    path('create/', create, name='create'),
    path('hesap/',hesap,name='hesap'),
    path('update/',update,name='update'),
    path('reset/',reset,name='reset'),
    path('delete/',userDelete,name="delete")
]