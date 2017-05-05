# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 

from django.template import defaultfilters



# Create your models here.
ESTADO = (
	('b', 'Borrador'),
	('p', 'Publicado'),
	)

class Category(models.Model):
	name = models.CharField(max_length = 100, db_index= True)


	def __unicode__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	category = models.ManyToManyField(Category)
	title = models.CharField(max_length = 200)
	body = models.TextField()
	status = models.CharField(max_length = 1, choices = ESTADO)


	def __unicode__(self):
		return self.title





class Comment(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	post = models.ManyToManyField(Post)
	title = models.CharField(max_length = 200)
	body = models.TextField()

	def __unicode__(self):
		return self.title	
