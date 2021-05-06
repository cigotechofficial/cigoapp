from rest_framework import serializers
from datetime import datetime, date

class DeliveryOrderSerializer(serializers.Serializer):
	order_id = serializers.IntegerField()
	restaurant = serializers.CharField()
	items_json = serializers.CharField(max_length=5000)
	name = serializers.CharField(max_length=90, default="")
	phone = serializers.CharField(max_length=90, default="")
	address = serializers.CharField(max_length=90, default="")
	status = serializers.IntegerField( default=0)


