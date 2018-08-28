from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import *


class IconCreateView(CreateView):
    model = Icon
    form_class = IconForm
    template_name = 'rp/form.html'
    success_url = reverse_lazy('icons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['icons'] = Icon.objects.all()
        context['title'] = 'New Icon'
        return context


class IconListView(ListView):
    model = Icon

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fcs'] = FaceClaim.objects.distinct()
        context['fc_form'] = FaceClaimForm()
        return context


class IconUpdateView(UpdateView):
    model = Icon
    form_class = IconForm
    template_name = 'icons/icon_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Icon'
        return context

    def get(self, request, *args, **kwargs):
        icon = Icon.objects.get(pk=kwargs['pk'])
        return super().get(self)


class IconDeleteView(DeleteView):
    model = Icon
    success_url = "/icons/"


class FaceClaimDetailView(DetailView):
    model = FaceClaim
    template_name = 'icons/fc_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IconForm()
        return context


def create_faceclaim(request):
    post = request.POST
    fc = FaceClaim(name=post['name'])
    fc.save()
    return redirect(f"/icons/fc/{fc.pk}/")
