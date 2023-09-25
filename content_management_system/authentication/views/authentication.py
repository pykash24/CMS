from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db.models import Q
import sys,os,json
from configurations import messages,constants
from .serializer import *

"""
    METHOD: sign_up_send_otp
    DESCRIPTION: 
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
@csrf_exempt
def user_register(request):
    try:
        if request.method == constants.POST:
            user_request = request if type(request) is dict else json.loads(request.body)
            user_request['user_role'] = constants.USERS
            is_user_registration_valid = UserRegistrationSerializer(data=user_request)
            if not is_user_registration_valid.is_valid():
                print("user_register",is_user_registration_valid.errors)
                return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 
            new_user_register = is_user_registration_valid.save()
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_200_OK), messages.MESSAGE: messages.SUCCESSFULLY_RESPONSE}, safe=False,status=constants.HTTP_200_OK) 
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_405_METHOD_NOT_ALLOWED), messages.MESSAGE: messages.METHOD_NOT_ALLOWED}, safe=False,status=constants.HTTP_405_METHOD_NOT_ALLOWED) 
    except Exception as error:
        print_error(str(request.path),error)
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 

@csrf_exempt
def update_user_details(request):
    try:
        user_request = request if type(request) is dict else json.loads(request.body)
        
    except Exception as error:
        print_error(str(request.path),error)
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 

def print_error(func_name,error=''):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{func_name} : {str(error)}", " in ", fname, " at ", exc_tb.tb_lineno)