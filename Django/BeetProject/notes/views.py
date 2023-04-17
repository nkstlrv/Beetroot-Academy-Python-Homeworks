from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NewNoteForm, EditNoteForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Note
    template_name = 'notes/index.html'


class NewNoteView(CreateView):
    form_class = NewNoteForm
    model = Note
    template_name = 'notes/new_note.html'
    success_url = reverse_lazy('home')


class DetailedNoteView(DetailView):
    model = Note
    template_name = 'notes/note.html'


class EditNoteView(UpdateView):
    form_class = EditNoteForm
    model = Note
    template_name = 'notes/edit_note.html'
    success_url = reverse_lazy('home')


class DeleteNoteView(DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('home')