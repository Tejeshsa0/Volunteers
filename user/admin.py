from django.contrib import admin
from user.models import *

#------------------------------------MODEL ADMINS--------------------------------------------
class OtpVerificationDataAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['id', 'mobile', 'otp', 'flag_verified', 'count']
    list_filter = ['flag_verified', 'count']
    readonly_fields = ['created', 'modified']
    search_fields = ['mobile']



#-------------------------------ADMIN REGISTRATION---------------------------------------------------------
admin.site.register(OtpVerificationData, OtpVerificationDataAdmin)
