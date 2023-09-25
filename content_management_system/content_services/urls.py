from django.urls import path
from . import views

urlpatterns = [
    path('insert_content/',views.insert_content,name="insert_content"),
    path('get_content/',views.get_content,name="get_content"),
    path('update_content/',views.update_content,name="update_content"),
]

