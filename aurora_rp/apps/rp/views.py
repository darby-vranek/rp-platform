from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import *


class CharacterDetailView(DetailView):
    model = Character


class CharacterListView(ListView):
    model = Character

    def get_queryset(self):
        return Character.objects.order_by('page_name')


class CharacterCreateView(CreateView):
    model = Character
    fields = ['page_name', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']
    template = 'rp/character_form.html'
    success_url = "/characters/"


class CharacterUpdateView(UpdateView):
    model = Character
    fields = ['page_name', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']
    template = 'rp/character_form.html'


class CharacterDeleteView(DeleteView):
    pass
