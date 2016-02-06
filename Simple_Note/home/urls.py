# encoding:utf-8
from django.conf.urls import url
from home.views import ListNotesView

urlpatterns = [
    url(r'^index/$', ListNotesView.as_view(), name='index'),
]
