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
    template_name = 'rp/form.html'
    success_url = "/characters/"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'New Character'
        return context


class CharacterUpdateView(UpdateView):
    model = Character
    fields = ['page_name', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # I'd eventually like to have this say "edit character name"
        context['title'] = 'Edit Character'
        return context


class CharacterDeleteView(DeleteView):
    pass


class VerseDetailView(DetailView):
    model = Verse


class VerseListView(ListView):
    model = Character

    def get_queryset(self):
        return Verse.objects.order_by('franchise')


class VerseCreateView(CreateView):
    model = Verse
    fields = ['display_name', 'franchise', 'caption', 'desc']
    template_name = 'rp/form.html'
    success_url = '/verses/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Verse'
        return context


class VerseUpdateView(UpdateView):
    model = Verse
    fields = ['display_name', 'franchise', 'caption', 'desc']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Edit Verse'
        return context


class BioDetailView(DetailView):
    model = Bio


class BioCreateView(CreateView):
    model = Bio
    fields = ['character', 'verse', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']
    template_name = 'rp/form.html'
    success_url = '/characters/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'New Bio'
        return context


class BioUpdateView(UpdateView):
    model = Bio
    fields = ['character', 'verse', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Edit Bio'
        return context


class CharacterTraitCreateView(CreateView):
    model = CharacterTrait
    fields = ['char', 'title', 'content']
    template_name='rp/form.html'
    success_url = '/characters/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'New Character Trait'
        return context


class CharacterTraitUpdateView(UpdateView):
    model = CharacterTrait
    fields = ['title', 'content']
    template_name = 'rp/form.html'
    success_url = '/characters/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Edit Trait'
        return context
