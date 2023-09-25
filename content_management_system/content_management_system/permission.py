# from rest_framework import permissions
from configurations import messages,constants
import jose
from django.http import JsonResponse
import jwt,time

# Description: This function check user is authenticate before accessing system
class UserAccessPermission:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        return self.get_response(request)
    def process_view(self, request,view_func, view_args, view_kargs):
        try:
            print(request.path)
            """ This is used to bypass the listed URL"""
            if str(request.path).strip() in ["/authentication/user_authentication/","/authentication/user_register/"]:
                print("passing")
                return None
            else:
                
                """ Decode the User token """
                jwt_token = request.headers['Authorization'].split()[1]
                decodedAccessToken = jwt.decode(jwt_token, algorithms=['HS256'], options={"verify_signature": False})
                
                """ This issue to validate the expiration time"""
                current_time = time.time()
                exp_time =  decodedAccessToken['exp']
                if current_time > exp_time:
                    print('Token has expired')
                    return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_401_UNAUTHORIZED),messages.MESSAGE:messages.UNAUTHORIZED_ACCESS}, safe=False, status=str(constants.HTTP_401_UNAUTHORIZED))
            return None
        except jose.exceptions.ExpiredSignatureError as error:
            print("Invalid Signature",error)
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_401_UNAUTHORIZED),messages.MESSAGE:messages.UNAUTHORIZED_ACCESS}, safe=False, status=str(constants.HTTP_401_UNAUTHORIZED))
        except jose.exceptions.JWTError as error:
            print(error)
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_401_UNAUTHORIZED),messages.MESSAGE:messages.UNAUTHORIZED_ACCESS}, safe=False, status=str(constants.HTTP_401_UNAUTHORIZED))
        except Exception as error:
            print(error)
            return JsonResponse({messages.STATUS_CODE: str(constants.HTTP_401_UNAUTHORIZED),messages.MESSAGE:messages.UNAUTHORIZED_ACCESS}, safe=False, status=str(constants.HTTP_401_UNAUTHORIZED))