from rest_framework import serializers

class CustomItemSerializer(serializers.Serializer):
	customitem_id = serializers.CharField()
	product_id = serializers.CharField()
	customitemname = serializers.CharField(default="customitemname", max_length=50)
	customitemprice = serializers.IntegerField(default=0)