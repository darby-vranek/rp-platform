from django.shortcuts import render
from django.views.generic.edit import CreateView
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
        icons = Icon.objects.all()
        context['icons'] = icons
        return context

class IconListView(ListView):
    model = Icon
