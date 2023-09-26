import os,sys
from authentication.models import *
from datetime import timedelta
import datetime,jwt,time
from configurations import constants, messages
import re
import json


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
    
"""
    METHOD: get_user_role
    DESCRIPTION: This is used to get the user role
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
def get_user_role(user_id):
    try:
        if user_details := UserDetails.objects.filter(user_id=user_id).first():
            return user_details.user_role
        return False
    except Exception as error:
        print_error("get_user_role", error)
        return False
    
"""
    METHOD: generate_token
    DESCRIPTION: This is used to generate the user token
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
def generate_token(request):
    try:
        expiry_time = datetime.datetime.now()+timedelta(minutes=constants.TOKEN_EXPIRY)
        return jwt.encode(
            {"app_id": constants.APP_ID, "exp": expiry_time},
            constants.SECRET_KEY,
            algorithm="HS256",
        )
    except Exception as error:
        print(error)
        return False

"""
    METHOD: is_valid_email
    DESCRIPTION: This is used to validate the email
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

"""
    METHOD: is_valid_password
    DESCRIPTION: This is used to validate the password
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

"""
    METHOD: validate_user_registration
    DESCRIPTION: This is used to user registration field
    AUTHOR: Vikas Tomar
    Date: 25/09/2023
"""
def validate_user_registration(request):
    try:
        user_request = request if type(request) is dict else json.loads(request.body)

        """ To check the email id valid or not"""
        if not is_valid_email(user_request['email']):
            return  messages.INCORRECT_EMAIL 

        """ To check the password valid or not"""
        if not is_valid_password(user_request['password']):
            return messages.INCORRECT_PASSWORD

        """To Check is email is already exist """
        if is_email_exist := UserDetails.objects.filter(
            email=user_request['email']
        ).first():
            return messages.EMAIL_ALREADY_EXIST
        
        """ To validate the user pincode """
        if len(str(user_request['pincode'])) > 6:
            return messages.INVALID_PINCODE
        return False
    except Exception as error:
        return False
        