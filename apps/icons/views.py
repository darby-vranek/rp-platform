from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
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
    success_url = reverse_lazy('icons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Icon'
        return context


class IconDeleteView(DeleteView):
    model = Icon
    success_url = "/icons/"


def IconFcList(request, name):
    name = ' '.join(name.split('-'))
    return render(request, 'icons/fc_detail.html', context={
        'icon_list': Icon.objects.filter(fc_model__name__icontains=name),
        'fc_name': name
    })
