from django.db import models

class Tutorial(models.Model):
	modalcode = models.CharField(max_length= 100,default="") 
	videoname = models.CharField(max_length= 20)
	description = models.TextField(null=True)
	videolink = models.CharField(max_length= 100)
	thumbnaillink = models.CharField(max_length= 100)

	def __str__(self):
		return self.videoname 

class Calldetail(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)

	def __str__(self):
		return self.name + " - " + self.phone
