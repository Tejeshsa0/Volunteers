from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from helper import keys
from user.managers import UserManager
from master.models import MasterBlockData, MasterDistrictData

#OTP model
class OtpVerificationData(models.Model):
    mobile = models.CharField(max_length=10)
    otp = models.CharField(max_length=6, null= True, blank= True)
    flag_verified = models.BooleanField(default= False)
    count = models.IntegerField(default=0, help_text="Count of OTP sent")

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.mobile)+ "'s OTPs"
    
    class Meta:
        verbose_name = 'OTP manager'
        verbose_name_plural = 'OTP manager'


#User model
class User(AbstractBaseUser, PermissionsMixin):
    mobile = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)


    objects = UserManager()
    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.mobile


class UserData(models.Model):

    class UserType(models.Choices):
        ADMIN = keys.ADMIN
        BC = keys.BC
        DC = keys.DC
        VOLUNTEER = keys.VOLUNTEER

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teammate')
    type = models.CharField(max_length=30, choices=UserType.choices, default=keys.ADMIN)
    user_unique_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50, null=True, blank=True)
    mothers_name = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile/images/%y/%b/')
    address = models.CharField(max_length=80, null=True, blank=True)
    pincode = models.CharField(max_length=6, null=True, blank=True)
    block = models.ForeignKey(MasterBlockData, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(MasterDistrictData, on_delete=models.SET_NULL, null=True, blank=True)
    flag_course_done = models.BooleanField(default=False)
    flag_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name



