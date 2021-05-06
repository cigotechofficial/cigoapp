from django.db import models
from setup.models import Venue
from datetime import datetime, date


class DeliveryOrder(models.Model):
	# customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order_id = models.AutoField(primary_key=True)
	restaurant = models.ForeignKey(Venue, on_delete=models.CASCADE, default=0)
	items_json = models.CharField(max_length=5000 )
	name = models.CharField(max_length=100 ,default="name")
	phone = models.CharField(max_length=15 ,default="phone" )
	address = models.CharField(max_length=5000 ,default="address" )
	timestamp = models.DateTimeField(default=datetime.now())
	status = models.IntegerField(default=0)
	
	def __str__(self):
		return self.items_json

class ArchiveDeliveryOrder(models.Model):
	# customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order_id = models.AutoField(primary_key=True)
	restaurant = models.ForeignKey(Venue, on_delete=models.CASCADE, default=0)
	items_json = models.CharField(max_length=5000 )
	name = models.CharField(max_length=100 ,default="name")
	phone = models.CharField(max_length=15 ,default="phone" )
	address = models.CharField(max_length=5000 ,default="address" )
	timestamp = models.DateTimeField(default=datetime.now())
	status = models.IntegerField(default=0)
	
	def __str__(self):
		return self.items_json

				