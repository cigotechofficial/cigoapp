from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import *
from .models import Venue, Employee, Menu



class ItemAdmin(ImportExportModelAdmin):
	resource_class = ItemAdminResource

admin.site.register(Venue)
admin.site.register(Employee)
admin.site.register(Menu, ItemAdmin)

