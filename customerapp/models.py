from django.db import models
from allauth.socialaccount.models import SocialAccount
from setup.models import Venue
from datetime import datetime, date

AVAIL_CHOICE=(
	('active','active'),
	('inactive','inactive'),
	)

class Customer(models.Model):
	customerid = models.ForeignKey(SocialAccount, on_delete=models.CASCADE)
	status = models.CharField(max_length=10, choices=AVAIL_CHOICE, default="inactive")
	lastrestaurant = models.ForeignKey(Venue, on_delete=models.CASCADE)
	tablenochoosed = models.IntegerField(default=0)

	# def __str__(self):
	# 	return self.customerid


class Order(models.Model):
	# customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order_id = models.AutoField(primary_key=True)
	sessionid = models.CharField(max_length=90, default="0")
	restaurant = models.ForeignKey(Venue, on_delete=models.CASCADE, default=0)
	table_no = models.CharField(max_length=90, default="")
	items_json = models.CharField(max_length=5000 )
	status = models.IntegerField()
	timestamp = models.DateTimeField(default=datetime.now())
	
	def __str__(self):
		return self.items_json

class VerifyOrder(models.Model):
	# customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order_id = models.AutoField(primary_key=True)
	sessionid = models.CharField(max_length=90, default="0")
	totalamount = models.CharField(max_length=1000 )
	restaurant = models.ForeignKey(Venue, on_delete=models.CASCADE, default=0)
	# table_no = models.CharField(max_length=90, default="")
	items_json = models.CharField(max_length=5000 )
	status = models.IntegerField(default=0)
	timestamp = models.DateTimeField(default=datetime.now())
	
	def __str__(self):
		return self.totalamount

class ArchiveOrder(models.Model):
	# customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order_id = models.AutoField(primary_key=True)
	sessionid = models.CharField(max_length=90, default="0")
	restaurant = models.ForeignKey(Venue, on_delete=models.CASCADE, default=0)
	table_no = models.CharField(max_length=90, default="")
	items_json = models.CharField(max_length=5000 )
	status = models.IntegerField()
	timestamp = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.items_json

class Feedback(models.Model):
	# customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order_id = models.AutoField(primary_key=True)
	restaurant = models.ForeignKey(Venue, on_delete=models.CASCADE, default=0)
	happiness = models.CharField(max_length=1000 )
	feedbacktext = models.TextField()
	timestamp = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.happiness


class Waiter(models.Model):
	table_no_w = models.CharField(max_length=90, default="")
	wcall = models.BooleanField(default=True)

	def __str__(self):
		return self.table_no_w



class CustomerAuthentication(models.Model):
	restaurant = models.ForeignKey(Venue, on_delete=models.CASCADE, default=0)
	table_no = models.IntegerField()
	hashcode = models.CharField(max_length=1000)



	
				