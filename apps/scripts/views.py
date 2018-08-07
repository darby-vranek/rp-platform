from apps.rp.models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ScriptCreateView(CreateView):
    model = Script
    form_class = ScriptForm
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Script'
        return context


class ScriptDetailView(DetailView):
    model = Script
    template_name = 'scripts/script_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['line_form'] = get_lineform_for_script_detail()
        return context

    def get(self, request, *args, **kwargs):
        self.initial = {'script': Script.objects.get(pk=kwargs['pk'])}
        self.success_url = reverse('script-detail', kwargs={'pk':kwargs['pk']})
        return super().get(self)


def get_lineform_for_script_detail():
    line_form = LineForm()
    return line_form


class ScriptListView(ListView):
    model = Script
    template_name = 'scripts/script_list.html'


class LineCreateView(CreateView):
    model = Line
    form_class = LineForm
    template_name = 'rp/form.html'
    success_url = "/scripts/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.success_url = '/scripts/%s/' % pk
        return super().post(self)
