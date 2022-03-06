from django.contrib import admin
from django.contrib.admin import AdminSite, ModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import *
from .models import Venue, Employee, Menu, CustomItem



class ItemAdmin(ImportExportModelAdmin):
	resource_class = ItemAdminResource
	list_display=('venuename','product_name','category')
	list_filter=['venuename','category']


class CustomiseAdmin(ImportExportModelAdmin):
	resource_class = CustomiseAdminResource
	list_display=('product_id','customitemname','customitemprice')
	list_filter=['product_id','customitemname']


admin.site.register(Venue)
admin.site.register(Employee)
admin.site.register(CustomItem, CustomiseAdmin)
admin.site.register(Menu, ItemAdmin)


