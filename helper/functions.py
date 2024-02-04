import math
import string
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import *
from master.models import *

import random
import re




#---------------------ERROR MESSAGE FUNCION
def error_message_function(errors):
    """
    return error message when serializer is not valid 
    :param errors:error object
    :returns: string
    """
    for key,values in errors.items():
        error = [value [:] for value in values]
        err = ' '.join(map(str,error))
        return err
  


#--------------------general Functions


class ResponseHandling:
    def failure_response_message(detail,result):
        """
        error message for failure
        :param detail: message to show in detail
        :param result : message or result to show
        :returns: dictionary
        """
        return {'detail' : detail, 'result' : result}

    def success_response_message(detail,result):
        """
        success message for Success
        :param detail: message to show in detail
        :param result : message or result to show
        :returns: dictionary
        """
        return {'detail' : detail, 'result' : result}
 


    