from django.urls import path
from user import apis

urlpatterns = [
    path('send-otp/', apis.SendOTPapi.as_view(), name= "sendOTP"),
    path('verify-otp/', apis.VerifyOTPapi.as_view(), name="verifyOTP"),
]
