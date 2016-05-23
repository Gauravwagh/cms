from django.utils.translation import ugettext_lazy as _
from django.db import models


class Whatever(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

FOOD_TYPE = (
    ("Lunch", _("Lunch")),
    ("Dinner", _("Dinner")),
)

class Employee(models.Model):
	employee_id 	= models.CharField(max_length=200, null=True, blank=True)
	employee_name	= models.CharField(max_length=200, null=True, blank=True)
	email			= models.EmailField(null=True, blank=True)
	contact_number	= models.BigIntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.employee_id + " -  " + self.employee_name

class Food(models.Model):
	employee 		= models.ForeignKey(Employee, null=True, blank=True)
	type			= models.CharField(choices=FOOD_TYPE,max_length=200, null=True, blank=True)
	avail_datetime	= models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.employee.employee_id


class FoodAll(models.Model):
	employee 		= models.ForeignKey(Employee, null=True, blank=True)
	type			= models.CharField(choices=FOOD_TYPE,max_length=200, null=True, blank=True)
	avail_datetime	= models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.employee.employee_id