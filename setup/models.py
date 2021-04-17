from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):	
	venueid = models.AutoField(primary_key=True)
	venuename = models.CharField(max_length=50)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	notables = models.IntegerField(default=0)

	def __str__(self):
		return self.venuename

 
class Employee(models.Model):
	employeeid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	ph = models.CharField(max_length=12)
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE)	
	role = models.CharField(max_length=20, default=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
 
	def __str__(self):
		return self.name + " from " + self.venue.venuename


AVAIL_CHOICE=(
	('ava','Available'),
	('not','Not Available'),
	)

class Menu(models.Model):
	product_id=models.AutoField(primary_key=True)
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
	product_name=models.CharField(max_length=50)
	category=models.CharField(max_length=50, null=True)
	description=models.CharField(max_length=300, null=True)
	price=models.IntegerField(default=0)
	# showtype 0 means old and 1 means new
	showtype=models.BooleanField(default=1) 

	availability=models.CharField(max_length=3,choices=AVAIL_CHOICE,default="ava")
	image = models.ImageField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.product_name

