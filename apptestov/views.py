# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from . import forms
from apptestov.models import Subject, Theme

# Create your views here.

def SubjectView (request):
    args = {}
    args['subjects'] = Subject.objects.all()
    return  render_to_response('subject.html',args)

def ThemesView (request,theme_id):
    args = {}
    args['themes'] = Theme.objects.get(id=theme_id)
    return render_to_response('themes.html',args)


