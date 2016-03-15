__author__ = 'developer'
# -*- encoding: utf-8 -*-
from django.forms.widgets import *
from django import forms
from Notes.models import Cat_estatus, Cat_notas


class CreateNewNoteForm(forms.ModelForm):

	class Meta:
		model = Cat_notas
		widgets = {
			'titulo': TextInput(attrs={'class': '', 'placeholder': 'Welcome'}),
			'descripcion': TextInput(attrs={'class': '', 'placeholder': 'Welcome'}),
			# 'fecha_creacion': TextInput(attrs={'class': 'datepicker', 'placeholder': '06-02-2016'}),
		}
		exclude = ['slug', 'cat_estatus', 'fecha_creacion', 'fecha_edicion']


class EditNoteForm(forms.ModelForm):

	class Meta:
		model = Cat_notas
		widgets = {
			'titulo': TextInput(attrs={'class': '', 'placeholder': 'Welcome'}),
			'descripcion': TextInput(attrs={'class': '', 'placeholder': 'Welcome'}),
		}
		exclude = ['slug', 'cat_estatus', 'fecha_creacion', 'fecha_edicion']
