from django.contrib import admin
from cms.models import Whatever, Employee, Food, FoodAll

# admin.site.register(Whatever)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('employee', 'type', 'avail_datetime')
    search_fields = ('avail_datetime','employee__employee_name')


class FoodAllAdmin(admin.ModelAdmin):
    list_display = ('employee', 'type', 'avail_datetime')
    search_fields = ('avail_datetime','employee__employee_name')

admin.site.register(Employee)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodAll, FoodAllAdmin)