from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Brother(models.Model):
	STATUS = (
		('A', 'Active'),
		('P', 'PLEDGE'),
		('G', 'Alumni')
		)

	brother_id = models.CharField(max_length = 30, primary_key=True)
	first_n = models.CharField(max_length = 20)
	last_n = models.CharField(max_length = 20)
	status = models.CharField(max_length = 1, choices= STATUS, required = False)
	def __str__ (self):
		output = self.first_n + " " + self.last_n
		return output

	#status: Either Active or Pledge
class Guest(models.Model):
	GENDER = (
		('M', 'Male'),
		('F', 'Female')
		)

	first_n = models.CharField(max_length = 30)
	last_n = models.CharField(max_length= 30)
	gender = models.CharField(max_length=1, choices=GENDER)
	blacklisted = models.BooleanField(default=False, required = False)
	host = models.ManyToManyField(Brother)
	def __str__ (self):
		return self.first_n + " " + self.last_n



# class Invite(models.Model):
# 	host = models.ForeignKey(Brother, on_delete=models.CASCADE)
# 	guest = models.ForeignKey(Guest, on_delete = models.CASCADE)
