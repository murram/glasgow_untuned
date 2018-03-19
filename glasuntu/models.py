from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VenuePage(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=200, default = "")
	address = models.CharField(max_length=200, default = "")
	picture = models.CharField(max_length=400, default = "")
	website = models.CharField(max_length=200, default = "")
	info = models.CharField(max_length=1000, default = "")
	genre = models.CharField(max_length=200, default = "")
	def __str__(self):
		return self.name

class ArtistPage(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=200)
	info = models.CharField(max_length=1000, default = "")
	picture = models.CharField(max_length=400, default = "")
	website = models.CharField(max_length=200, default = "")
	genre = models.CharField(max_length=200, default = "")
	def __str__(self):
		return self.name
		
class Genre(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name
		
class Gig(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	venue = models.ForeignKey(VenuePage, default = "")
	def __str__(self):
		return self.name
		
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	#override __unicode__()
	def __str__(self):
		return self.user.username