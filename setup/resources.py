from import_export import resources
from .models import Menu

class ItemAdminResource(resources.ModelResource):

    class Meta:
        model   =   Menu
        exclude = ('id',)
        import_id_fields = ('product_id',)



