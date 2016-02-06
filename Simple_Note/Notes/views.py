from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from Notes.models import Cat_estatus, Cat_notas
from Notes.forms import *


class CreateNewNoteView(CreateView):
	model = Cat_notas
	form_class = CreateNewNoteForm
	success_url = reverse_lazy("create_new_note")
	template_name = "new_note_form.html"

	def form_valid(self, form):
		# fecha = form.cleaned_data["fecha_creacion"]
		form.instance.cat_estatus_id = 1
		# form.instance.fecha_creacion = fecha
		messages.success(self.request, "Haz agregado una nueva nota a tu lista")
		return super(CreateNewNoteView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateNewNoteView, self).get_context_data(**kwargs)
		return context

