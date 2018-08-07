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


class TraitCreateView(CreateView):
    model = Trait
    form_class = TraitForm
    template_name = 'rp/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Trait'
        return context


def trait_list_view(request, query):
    trait_list = Trait.objects.filter(title__iexact=query)
    return render(request, 'rp/trait_list.html', context={'trait_list': trait_list})