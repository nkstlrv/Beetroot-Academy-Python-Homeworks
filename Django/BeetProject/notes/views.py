from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note


class HomeView(ListView):
    model = Note
    template_name = 'notes/index.html'