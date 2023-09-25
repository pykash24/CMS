from django.urls import path
from . import views

urlpatterns = [
    path('user_register/',views.user_register,name="user_register"),
    path('user_authentication/',views.user_authentication,name="user_authentication"),
]

