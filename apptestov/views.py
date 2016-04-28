# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from . import forms
from apptestov.models import Subject, Theme, Lesson

# Create your views here.

def SubjectsView (request):
    args = {}
    args['subjects'] = Subject.objects.all()
    return  render_to_response('subjects.html',args)

def ThemesView (request,url_subject_id):
    args = {}
    args['themes'] = Theme.objects.filter(subject_id=url_subject_id)
    return render_to_response('themes.html',args)

def LessonsView (request,url_theme_id):
    args = {}
    args['lessons'] = Lesson.objects.filter(theme_id=url_theme_id)
    return render_to_response('lessons.html',args)

