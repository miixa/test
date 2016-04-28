from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user (models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=75)
  organization = models.CharField(max_length=75)
  def __unicode__(self):
    return self.first_name

class Subject (models.Model):
  title = models.CharField(max_length=200)
  user = models.ForeignKey(user)
  def __unicode__(self):
    return self.title
  
class Theme (models.Model):
  class Meta:
    db_table = 'Theme'
  title = models.CharField(max_length=200)
  subject = models.ForeignKey(Subject)
  user = models.ForeignKey(user)
  def __unicode__(self):
    return self.title

class Lesson (models.Model):
  class Meta:
    db_table = 'Lesson'
  title = models.CharField(max_length=200)
  subject = models.ForeignKey(Subject)
  theme = models.ForeignKey(Theme)
  user = models.ForeignKey(user)
  def __unicode__(self):
    return self.title

class Question (models.Model):
  title = models.CharField(max_length=400)
  subject = models.ForeignKey(Subject)
  theme = models.ForeignKey(Theme)
  user = models.ForeignKey(user)
  lesson = models.ForeignKey(Lesson)
  def __unicode__(self):
    return self.title
  
class Answer (models.Model):
  title = models.CharField(max_length=400)
  question = models.ForeignKey(Question)
  subject = models.ForeignKey(Subject)
  theme = models.ForeignKey(Theme)
  user = models.ForeignKey(user)
  lesson = models.ForeignKey(Lesson)
  def __unicode__(self):
    return self.title
