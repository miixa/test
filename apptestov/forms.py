from django.forms import ModelForm
from models import *

class ThemeForm (ModelForm):
    class Meta():
        model = Theme
