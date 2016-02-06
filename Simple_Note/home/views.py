# encoding:utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from Notes.models import Cat_estatus, Cat_notas


class ListNotesView(ListView):
	model = Cat_notas
	template_name = "index.html"
	queryset = Cat_notas.objects.filter(cat_estatus__nombre="ACTIVO").order_by('id')

	def get_filter(self, queryset):
		search = self.get_search()
		if search:
			queryset = queryset.filter(
				Q(nombre__icontains=search)
			)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ListNotesView, self).get_context_data(**kwargs)
		return context
