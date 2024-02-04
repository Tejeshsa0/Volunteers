from django.contrib import admin

#--------------------------- MODEL ADMINS ---------------------------------------
class MasterDistrictDataAdmin(admin.ModelAdmin):
    list_display=['id', 'district']