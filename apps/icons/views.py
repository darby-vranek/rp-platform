from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from django.urls import reverse_lazy

from .models import *


class IconCreateView(CreateView):
    model = Icon
    form_class = IconForm
    template_name = 'icons/icon_form.html'
    success_url = reverse_lazy('icons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['icons'] = Icon.objects.all()
        return context


class IconListView(ListView):
    model = Icon

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fcs'] = FaceClaim.objects.distinct()
        return context


class IconUpdateView(UpdateView):
    model = Icon
    form_class = IconForm
    template_name = 'icons/icon_form.html'
    success_url = '/icons/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Icon'
        return context

    def get(self, request, *args, **kwargs):
        icon = Icon.objects.get(pk=kwargs['pk'])
        self.success_url = '/icons/fc/%s/' % icon.fc_model.pk
        return super().get(self)


class IconDeleteView(DeleteView):
    model = Icon
    success_url = "/icons/"


class FaceClaimDetailView(DetailView):
    model = FaceClaim
    template_name = 'icons/fc_detail.html'
