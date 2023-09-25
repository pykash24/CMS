from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db.models import Q
import sys,os,json
from configurations import messages,constants
from .serializer import *

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
        
        
def print_error(func_name,error=''):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"{func_name} : {str(error)}", " in ", fname, " at ", exc_tb.tb_lineno)