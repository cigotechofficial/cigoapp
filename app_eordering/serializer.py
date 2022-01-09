from rest_framework import serializers
from datetime import datetime, date

class OrderSerializer(serializers.Serializer):
	order_id = serializers.IntegerField()
	sessionid = serializers.CharField(max_length=90, default="0")
	restaurant = serializers.CharField()
	items_json = serializers.CharField(max_length=5000)
	table_no = serializers.CharField(max_length=90, default="")
	status = serializers.IntegerField()

class VerifyOrderSerializer(serializers.Serializer):
	order_id = serializers.IntegerField()
	sessionid = serializers.CharField(max_length=90, default="0")
	items_json = serializers.CharField(max_length=5000)
	table_no = serializers.CharField(max_length=90, default="")
	totalamount = serializers.CharField(max_length=90, default="")
	status = serializers.IntegerField()
	restaurant = serializers.CharField(default=0)
	timestamp = serializers.DateTimeField(default=datetime.now())

class TableSerializer(serializers.Serializer):
	order_id = serializers.IntegerField()
	sessionid = serializers.CharField(max_length=90, default="0")
	items_json = serializers.CharField(max_length=5000)
	# table_no = serializers.CharField(max_length=90, default="")
	status = serializers.IntegerField()

class WaiterSerializer(serializers.Serializer):
	table_no_w = serializers.CharField(max_length=90, default="")
	wcall = serializers.BooleanField(default="")
	id = serializers.IntegerField()