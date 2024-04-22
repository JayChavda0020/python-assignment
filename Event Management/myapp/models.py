from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	mobile = models.PositiveIntegerField()
	message = models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	fname = models.CharField(max_length = 100)
	lname = models.CharField(max_length = 100)
	email = models.EmailField()
	mobile = models.PositiveIntegerField()
	password = models.CharField(max_length = 100)
	profile_picture = models.ImageField(upload_to = "profile_picture/", default="profile_picture/d.jpg")
	usertype = models.CharField(max_length = 100, default = "user")

	def __str__(self):
		return self.fname+" "+self.lname

class Events(models.Model):
	manager = models.ForeignKey(User, on_delete = models.CASCADE)
	event_name = models.CharField(max_length = 100)
	event_date = models.CharField(max_length = 100)
	event_time = models.CharField(max_length = 100)
	Event_Venue = models.TextField()
	event_picture = models.ImageField(upload_to = "event_picture/")
	event_price = models.PositiveIntegerField()

	def __str__(self):
		return self.manager.fname+"-"+self.event_name