from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db.models import Q
import sys,os,json
from configurations import messages,constants
from .serializer import *
from authentication.views.common_method import *

"""
    METHOD: insert_content
    DESCRIPTION: This is used to insert the user content
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
@csrf_exempt
def insert_content(request):
    try:
        if request.method == constants.POST:
            user_request = request if type(request) is dict else json.loads(request.body)
            insert_content = UserContentSerializer(data=user_request)
            if not insert_content.is_valid():
                print("user_register",insert_content.errors)
                return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 
            new_user_register = insert_content.save()
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_200_OK), messages.MESSAGE: messages.SUCCESSFULLY_RESPONSE}, safe=False,status=constants.HTTP_200_OK) 
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_405_METHOD_NOT_ALLOWED), messages.MESSAGE: messages.METHOD_NOT_ALLOWED}, safe=False,status=constants.HTTP_405_METHOD_NOT_ALLOWED) 
    except Exception as error:
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 

"""
    METHOD: get_content
    DESCRIPTION: This is used to print the exception
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
@csrf_exempt
def get_content(request):
    try:
        if request.method == constants.GET:
            user_request = request if type(request) is dict else json.loads(request.body)
            query = Q()
            if 'title' in user_request:
                query &= Q(title=user_request['title'])
            if 'body' in user_request:
                query &= Q(title=user_request['title'])
            if 'summary' in user_request:
                query &= Q(title=user_request['summary'])
            if 'document' in user_request:
                query &= Q(title=user_request['title'])
            if 'categories' in user_request:
                query &= Q(title=user_request['title'])
            if not any([query]):
                content_details_object = ContentDetails.objects.all().values()
            else:
                content_details_object = ContentDetails.objects.filter(query).values()
            if not list(content_details_object):
                return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_200_OK), messages.MESSAGE: messages.NO_DATA_FOUND,"data":list(content_details_object)}, safe=False,status=constants.HTTP_200_OK) 
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_200_OK), messages.MESSAGE: messages.SUCCESSFULLY_RESPONSE,"data":list(content_details_object)}, safe=False,status=constants.HTTP_200_OK) 
    except Exception as error:
        print_error("str",error)
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 

"""
    METHOD: update_content
    DESCRIPTION: This is used to update the content
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
@csrf_exempt
def update_content(request):
    try:
        user_request = request if type(request) is dict else json.loads(request.body)
        user_id,content_id,creator_id= user_request['user_id'],user_request['content_id'],user_request['creator_id']
        
        """ To get the user role with respect to user id"""
        user_role = get_user_role(user_id)
        if user_role != constants.ADMIN_ROLE or user_id != creator_id:
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_401_UNAUTHORIZED),messages.MESSAGE:messages.UNAUTHORIZED_ACCESS}, safe=False, status=str(constants.HTTP_401_UNAUTHORIZED))
        
        is_content_exist = ContentDetails.objects.filter(content_id=content_id).first()
        if not is_content_exist:
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_404_NOT_FOUND), messages.MESSAGE: messages.NO_DATA_FOUND}, safe=False,status=constants.HTTP_404_NOT_FOUND) 
        
        update_serializer = UpdateUserContentSerializer(is_content_exist, data=user_request)
        if not update_serializer.is_valid():
            print("update_serializer",update_serializer.errors)
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 
        update_serializer.save()
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_200_OK), messages.MESSAGE: messages.SUCCESSFULLY_RESPONSE}, safe=False,status=constants.HTTP_200_OK) 
    except Exception as error:
        print_error(str(request.path),error)
        return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_500_INTERNAL_SERVER_ERROR), messages.MESSAGE: messages.INTERVAL_REQUEST_BODY}, safe=False,status=constants.HTTP_400_BAD_REQUEST) 

"""
    METHOD: print_error
    DESCRIPTION: This is used to print error logs
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
def print_error(func_name,error=''):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{func_name} : {str(error)}", " in ", fname, " at ", exc_tb.tb_lineno)