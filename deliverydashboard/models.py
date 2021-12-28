from django.db import models
from setup.models import Venue


class Discount(models.Model):
	restaurant = models.ForeignKey(Venue, on_delete=models.CASCADE, default=0)
	discount = models.IntegerField(default=0)
	
	def __int__(self):
		return self.discount
