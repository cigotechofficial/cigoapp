from django.contrib import admin
from django.contrib.admin import AdminSite, ModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import *
from .models import Venue, Employee, Menu



class ItemAdmin(ImportExportModelAdmin):
	resource_class = ItemAdminResource
	list_display=('venuename','product_name','category')
	list_filter=['venuename','category']


admin.site.register(Venue)
admin.site.register(Employee)
admin.site.register(Menu, ItemAdmin)

