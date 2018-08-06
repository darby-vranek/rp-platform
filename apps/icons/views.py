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
        context['icons'] = Icon.objects.all()
        return context


class IconListView(ListView):
    model = Icon

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['distinct'] = Icon.objects.order_by('fc').distinct('fc').exclude(fc__iexact='')
        return context


def IconFcList(request, name):
    name = ' '.join(name.split('-'))
    return render(request, 'icons/icon_list.html', context={
        'distinct': Icon.objects.order_by('fc').distinct('fc').exclude(fc__iexact=''),
        'icon_list': Icon.objects.filter(fc__icontains=name),
    })

