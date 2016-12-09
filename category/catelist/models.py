from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=50)
	parent = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'categories'
