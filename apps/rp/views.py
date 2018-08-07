from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
import os
import boto3
import json


def index(request):
    return render(request, 'rp/base.html')


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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Verse'
        return context

    def get(self, *args, **kwargs):
        self.success_url = '/verses/%s/' % kwargs['pk']
        return super().get(self)


class VerseTraitCreateView(CreateView):
    model = Trait
    form_class = TraitForm
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Trait for %s' % Verse.objects.get(pk=kwargs['pk']).display_name
        return context

    def get(self, *args, **kwargs):
        self.success_url = '/verses/%s/' % kwargs['pk']
        self.initial = {'verse': Verse.objects.get(pk=kwargs['pk'])}
        return super().get(self)


class VerseTraitUpdateView(UpdateView):
    model = Trait
    form_class = TraitForm
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.success_url = '/verses/%s/' % kwargs['pk']
        context['title'] = 'Edit Trait'
        return context


class VerseTraitDeleteView(DeleteView):
    pass


class TraitCreateView(CreateView):
    model = Trait
    form_class = TraitForm
    template_name = 'rp/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Trait'
        return context


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Post'
        return context


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'rp/form.html'


def trait_list_view(request, query):
    trait_list = Trait.objects.filter(title__iexact=query)
    return render(request, 'rp/trait_list.html', context={'trait_list': trait_list})