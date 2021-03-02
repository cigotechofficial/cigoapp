from django.db import models

class Gst(models.Model):
	cgst = models.DecimalField(max_digits=6, decimal_places=1)
	sgst = models.DecimalField(max_digits=6, decimal_places=1)

class Newuserinfo(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)

	def __str__(self):
		return self.name + " - " + self.phone

class Contactus(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.name + " - " + self.phone

class Defaultimg(models.Model):
	dimage = models.ImageField(upload_to='images/', null=True, blank=True)