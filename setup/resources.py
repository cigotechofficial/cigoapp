from import_export import resources
from .models import Menu, CustomItem

class ItemAdminResource(resources.ModelResource):

    class Meta:
        model   =   Menu
        exclude = ('id',)
        import_id_fields = ('product_id',)

class CustomiseAdminResource(resources.ModelResource):

    class Meta:
        model   =   CustomItem
        exclude = ('id',)
        import_id_fields = ('customitem_id',)



