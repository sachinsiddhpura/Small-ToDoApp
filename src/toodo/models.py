from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length=120)

	class Meta:
		verbose_name = ("Category")
		verbose_name_plural = ("Categories")

	def __str__(self):
		return self.name

class Todo(models.Model):
	title	=models.CharField(max_length=120)
	content	=models.TextField(blank=True)
	created	=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	due_date=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	category=models.ForeignKey(Category,default=None)
	contact_number=models.IntegerField(blank=True,null=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.title