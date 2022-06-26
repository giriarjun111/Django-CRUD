from django.contrib import admin
from .models import Employee, Position, Contact

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('fullname', 'position')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
admin.site.register(Contact)
