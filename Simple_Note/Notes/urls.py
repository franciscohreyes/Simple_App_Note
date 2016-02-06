from django.conf.urls import patterns, include, url
from Notes.views import CreateNewNoteView

urlpatterns = [
    url(r'^AgregarNota/$', CreateNewNoteView.as_view(), name="create_new_note"),
]
