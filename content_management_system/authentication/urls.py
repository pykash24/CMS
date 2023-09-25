from django.urls import path
from . import views

urlpatterns = [
    path('user_register/',views.user_register,name="user_register"),
    path('update_user_details/',views.update_user_details,name = "update_user_details")
]

