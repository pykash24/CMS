from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db.models import Q


"""
    METHOD: employee_authentication
    DESCRIPTION: To authenticate the employees using employee outlook and 
    AUTHOR: Vikas Tomar
    Date: 06/04/2023
"""