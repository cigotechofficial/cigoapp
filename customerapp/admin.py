from django.contrib import admin
from .models import Customer,Order,ArchiveOrder,Waiter,Feedback,CustomerAuthentication,VerifyOrder

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(VerifyOrder)
admin.site.register(ArchiveOrder)
admin.site.register(Waiter)
admin.site.register(Feedback)
admin.site.register(CustomerAuthentication)
