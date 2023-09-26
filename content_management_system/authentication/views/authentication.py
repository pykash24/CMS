from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db.models import Q
import sys,os,json
from configurations import messages,constants
from .serializer import *
from .common_method import *

"""
    METHOD: user_register
    DESCRIPTION: This is used to user register.
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
@csrf_exempt
def user_register(request):
    try:
        if request.method == constants.POST:
            user_request = request if type(request) is dict else json.loads(request.body)
            
            """ To check the user request is valid as email, password validations."""
            is_exist_request_valid = validate_user_registration(request)
            if bool(is_exist_request_valid):
                return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: is_exist_request_valid}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 
            user_request['user_role'] = constants.USERS_ROLE
            
            """ To call the UserRegistrationSerializer serializer"""
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

"""
    METHOD: user_authentication
    DESCRIPTION: This is used to user authentication
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
@csrf_exempt
def user_authentication(request):
    try:
        user_request = request if type(request) is dict else json.loads(request.body)
        is_user_valid = UserDetails.objects.filter(is_deleted=constants.BOOLEAN_FALSE,password=user_request['password'],email= user_request['email']).first()
        if not is_user_valid:
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 
        
        """ This is used to generate user token """
        user_token = generate_token(request)
        if not user_token:
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 
        data = {
            "user_role":is_user_valid.user_role,
            "user_id":is_user_valid.user_id,
            "token": user_token
        }
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_200_OK), messages.MESSAGE: messages.NO_DATA_FOUND,"data":data}, safe=False,status=constants.HTTP_200_OK) 
    except Exception as error:
        print_error(str(request.path),error)
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 
    
"""
    METHOD: print_error
    DESCRIPTION: This is used to print the exception
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
def print_error(func_name,error=''):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{func_name} : {str(error)}", " in ", fname, " at ", exc_tb.tb_lineno)
    
    