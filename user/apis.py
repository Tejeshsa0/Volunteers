
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
#----APP IMPORTS
from helper import keys, messages, utils
from user.serializers import SendOTPSerializer, VerifyOTPSerializer
from user.views import UserFunctions
from helper.functions import ResponseHandling, error_message_function


class SendOTPapi(generics.GenericAPIView):
    """
    API to send OTP to mobile

    HEAD PARAM: None
    PATH PARAM: None
    QUERYSTRING PARAM: None
    API RESPONSE: String
    """
    serializer_class = SendOTPSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        count = 0
        print('----------------------------------------------------------')
        serializer = self.get_serializer(data= request.data)
        if not serializer.is_valid(raise_exception = False):
            error = serializer.errors
            err = error_message_function(error)
            return Response(ResponseHandling.failure_response_message(err, {}), status= utils.status400)
        
        print('----------------------------------------------------------')
        mobile = str(request.data[keys.MOBILE])

        print('----------------------------------------------------------')
        # new_otp = generate_otp()
        new_otp = 123456
        
        #----------Send OTP to User Mobile-------------------------------------
        is_mobile_in_OTPmodel = UserFunctions.check_mobile_in_OTPmodel(mobile)
        
        #If mobile already in otp model -> get_count
        if is_mobile_in_OTPmodel.exists():
            count=UserFunctions.get_count(mobile)
        else:
            serializer.save()    #else save in otp model

        #Id count limit reached give erroe
        if count<3:
            UserFunctions.update_otp(mobile,new_otp,count)
        else:
            return Response(ResponseHandling.failure_response_message(messages.ONLY_3_RESEND,{}), status= utils.status400)
        
        return Response(ResponseHandling.success_response_message(messages.OTP_SUCCESSFULLY_SENT, {}), status= utils.status200)
    

class VerifyOTPapi(generics.GenericAPIView):
    """
    API to verify a particular OTP

    HEAD PARAM: None
    PATH PARAM: None
    QUERYSTRING PARAM: None
    API RESPONSE: String
    """

    serializer_class = VerifyOTPSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if not serializer.is_valid(raise_exception = False):
            error = serializer.errors
            err = error_message_function(error)
            return Response(ResponseHandling.failure_response_message(err, {}), status = utils.status400)
        
        mobile = request.data[keys.MOBILE]
        entered_otp = request.data[keys.OTP]

        otp_queryset = UserFunctions.check_mobile_in_OTPmodel(mobile)
        user_queryset = UserFunctions.check_mobile_in_UserModel(mobile)
        
        #if otp_verification instance does not exists raise errors
        if not otp_queryset.exists():
            return Response(ResponseHandling.failure_response_message(messages.USER_NOT_FOUND, {}), status= utils.status404)
        
        #collect the stored OTP and match with entered OTP
        otp_object = otp_queryset.first()
        stored_otp = otp_object.otp

        if not int(stored_otp) == int(entered_otp):
            return Response(ResponseHandling.failure_response_message(messages.OTP_DID_NOT_MATCH,{}), status= utils.status400)
        
        # UserFunctions.mark_verified(mobile)
        # if is_mobile_in_UserModel.exists():
        #     is_user = True
        #     User= is_mobile_in_UserModel.first()
        #     refresh_token = RefreshToken.for_user(User)
        #     access_token = refresh_token.access_token
        #     is_user_in_preferences = LoanFunctions.check_user_in_preferences(User)
        #     if is_user_in_preferences:
        #         details_required = False
        #     else:
        #         details_required = True

        #     response = {
        #         "is_user ": is_user,
        #         "details_required" : details_required,
        #         "token" :{
        #             "access_token": str(access_token), 
        #             "refresh_token": str(refresh_token)
        #         }
        #     }       
        #     otp_object.delete()
        #    return Response(ResponseHandling.success_response_message(messages.OTP_IS_VALID,response), status= utils.status200)
        return Response(ResponseHandling.success_response_message(messages.OTP_IS_VALID,{"is_user" : False}), status= utils.status200)
       

# class CreateUserapi(generics.CreateAPIView):
#     """
#     Api to create User and Customer in respective models

#     HEAD PARAM: None
#     PATH PARAM: None
#     QUERYSTRING PARAM: search
#     REQUEST BODY : city, mobile
#     API RESPONSE: String( token )
#     """

#     serializer_class = CustomerSerializer
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data= request.data)
#         if not serializer.is_valid(raise_exception = False):
#             error = serializer.errors
#             err = error_message_function(error)
#             return Response(ResponseHandling.failure_response_message(err, {}), status = utils.status400)
        
#         mobile = request.data.get(keys.MOBILE)
        
#         otp_user= UserFunctions.check_mobile_in_OTPmodel(mobile)
#         if otp_user.exists():
#             otp_user= otp_user.first()
#         else:
#             return Response(ResponseHandling.failure_response_message(messages.USER_NOT_FOUND, {}), status= utils.status404)
#         if not otp_user.verified==True:
#             return Response(ResponseHandling.failure_response_message(messages.UNAUTHORISED_USER, {}), status= utils.status403)
 
#         state_id = request.data[keys.STATE]
#         city_id = request.data[keys.CITY]
#         city = MasterFunctions.check_state_has_city(state_id, city_id)

#         user= UserModel.objects.create(mobile= mobile)
#         serializer.save(user = user, city = city)
#         otp_user.delete()

#         refresh_token = RefreshToken.for_user(user)
#         access_token = refresh_token.access_token

#         token= {"access_token": str(access_token), "refresh_token": str(refresh_token)}

#         return Response(ResponseHandling.success_response_message(messages.USER_CREATED, token), status=utils.status201)

     