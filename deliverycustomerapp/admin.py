from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import *
from .models import DeliveryOrder,ArchiveDeliveryOrder

class DeliveryArchiveAdmin(ImportExportModelAdmin):
	resource_class = DeliveryArchiveResource

admin.site.register(DeliveryOrder)
admin.site.register(ArchiveDeliveryOrder, DeliveryArchiveAdmin)
