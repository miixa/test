from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user (models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=75)
  organization = models.CharField(max_length=75)

class Subject (models.Model):
  title = models.CharField(max_length=200)
  
class Theme (models.Model):
  title = models.CharField(max_length=200)
  subject = models.ForeignKey(Subject)

class Question (models.Model):
  title = models.CharField(max_length=400)
  subject = models.ForeignKey(Subject)
  theme = models.ForeignKey(Theme)
  
class Answer (models.Model):
  title = models.CharField(max_length=400)
  question = models.ForeignKey(Question)
  subject = models.ForeignKey(Subject)
  theme = models.ForeignKey(Theme)
