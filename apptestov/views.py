from django.shortcuts import render
from . import forms
# Create your views here.

def Theme (request):
    args = {}
    args['form'] = forms.ThemeForm
    return  render(request,'apptestov.html',args)

