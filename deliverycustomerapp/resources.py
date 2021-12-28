from import_export import resources
from .models import ArchiveDeliveryOrder

class DeliveryArchiveResource(resources.ModelResource):

    class Meta:
        model   =   ArchiveDeliveryOrder
        exclude = ('id',)
        import_id_fields = ('order_id',)



