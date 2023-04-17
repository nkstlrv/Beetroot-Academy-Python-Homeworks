from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("new-note/", views.NewNoteView.as_view(), name='new-note'),
    path("note/<int:pk>/", views.DetailedNoteView.as_view(), name='detailed-note'),
    path("edit/<int:pk>/", views.EditNoteView.as_view(), name='edit-note'),
    path("delete/<int:pk>/", views.DeleteNoteView.as_view(), name='edit-note'),
]