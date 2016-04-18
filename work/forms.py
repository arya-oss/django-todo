from django import forms
from django.forms import widgets
from django.forms import ModelForm
from .models import todo, tags
from django.contrib.auth.models import User

class WorkAddForm(forms.ModelForm ):
    class Meta:
        model = todo
        fields = ('title', 'description', 'priority',)

class TagsForm(forms.ModelForm):
	"""form for extended auth User model"""
	class Meta:
		model = tags
		fields = ('tagname','description')