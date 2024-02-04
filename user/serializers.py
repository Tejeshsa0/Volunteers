from rest_framework import serializers
from helper import keys, utils, messages
from django.core.validators import RegexValidator

from user.models import OtpVerificationData



class SendOTPSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(max_length = 10, required = True, validators = [utils.mobile_regex], error_messages = {keys.MAX_LENGTH : messages.UPTO_10_DIGIT, keys.REQUIRED : messages.REQUIRED_MOBILE })

    class Meta:
        model = OtpVerificationData
        fields = ["mobile"]


class VerifyOTPSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(max_length = 10, required = True, validators = [utils.mobile_regex], error_messages = {keys.MAX_LENGTH : messages.UPTO_10_DIGIT, keys.REQUIRED : messages.REQUIRED_MOBILE})

    class Meta:
        model = OtpVerificationData
        fields = ("mobile","otp")