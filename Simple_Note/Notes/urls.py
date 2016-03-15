from django.conf.urls import patterns, include, url
from Notes.views import CreateNewNoteView, EditNoteView

urlpatterns = [
    url(r'^AgregarNota/$', CreateNewNoteView.as_view(), name="create_new_note"),
    url(r'^EditarNota/(?P<pk>\d+)/$', EditNoteView.as_view(), name="edit_note"),
]
