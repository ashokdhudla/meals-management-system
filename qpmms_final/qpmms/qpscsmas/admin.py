from .models import *
from django.contrib import admin


class qpusersAdmin(admin.ModelAdmin):
    list_display = ['user_id','username','email_id','date_time']
    list_filter = ['date_time']
    search_fields = ['date_time']
    class Meta:
        model = qpusers
class associative_companyAdmin(admin.ModelAdmin):
    list_display = ['company_name','company_location']
    list_filter = ['company_name']
    search_fields = ['company_location']
    class Meta:
        model = associative_company
class employee_detailsAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','rfidcardno','date_time']
    list_filter = ['first_name']
    search_fields = ['employee_id']
    class Meta:
        model = employee_details
class emp_breakfastAdmin(admin.ModelAdmin):
    list_display = ['breakfast_count','employee_id']
    list_filter = ['date_time']
    search_fields = ['employee_id']
    class Meta:
        model = emp_breakfast
class emp_lunchAdmin(admin.ModelAdmin):
    list_display = ['lunch_count','employee_id']
    list_filter = ['date_time']
    search_fields = ['employee_id']
    class Meta:
        model = emp_lunch
class emp_dinnerAdmin(admin.ModelAdmin):
    list_display = ['dinner_count','employee_id']
    list_filter = ['date_time']
    search_fields = ['employee_id']
    class Meta:
        model = emp_dinner
class emp_accommodationAdmin(admin.ModelAdmin):
    list_display = ['rfidcardno']
    list_filter = ['rfidcardno']
    search_fields =['rfidcardno']
    class  Meta:
        model = emp_accommodation
class emp_stayAdmin(admin.ModelAdmin):
    list_display = ['rfidcardno']
    list_filter = ['rfidcardno']
    search_fields = ['rfidcardno']
    class Meta:
        model = emp_stay
class device_infoAdmin(admin.ModelAdmin):
    list_display = ['device_id','device_location','Installation_Date']
    list_filter = ['device_location']
    #search_fields = ['device_id']
    class Meta:
        model = device_info
class meal_timingAdmin(admin.ModelAdmin):
    list_display = ['breakfast_start','breakfast_end','lunch_start','lunch_end','dinner_start','dinner_end']
    #list_filter['published']
    class Meta:
        model = meal_timing
class roleAdmin(admin.ModelAdmin):
    list_display = ['rolename']
    class Meta:
        model = role
class departmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']
    class Meta:
        model = department
# bhanu's admins
class emp_entryAdmin(admin.ModelAdmin):
    list_display = ['rfidcardno']
    list_filter = ['rfidcardno']
    search_fields = ['rfidcardno']
    class Meta:
        model = emp_entry
class emp_exitAdmin(admin.ModelAdmin):
    list_display = ['rfidcardno']
    list_filter = ['rfidcardno']
    search_fields = ['rfidcardno']
    class Meta:
        model = emp_exit
admin.site.register(emp_entry,emp_entryAdmin)
admin.site.register(emp_exit,emp_exitAdmin)
admin.site.register(qpusers, qpusersAdmin)
admin.site.register(employee_details, employee_detailsAdmin)
admin.site.register(associative_company, associative_companyAdmin)
admin.site.register(emp_breakfast, emp_breakfastAdmin)
admin.site.register(emp_lunch, emp_lunchAdmin)
admin.site.register(emp_dinner, emp_dinnerAdmin)
admin.site.register(emp_accommodation,emp_accommodationAdmin)
admin.site.register(device_info,device_infoAdmin)
admin.site.register(meal_timing,meal_timingAdmin)
admin.site.register(role,roleAdmin)
admin.site.register(department,departmentAdmin)
admin.site.register(emp_stay,emp_stayAdmin)