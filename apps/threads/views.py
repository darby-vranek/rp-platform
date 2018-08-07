from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.rp.models import *


# Create your views here.
class ThreadListView(ListView):
    model = Thread
    template_name = 'threads/thread_list.html'

    def get_queryset(self):
        return Thread.objects.order_by('title')


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'threads/thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplyForm()
        return context


class ThreadCreateView(CreateView):
    model = Thread
    fields = ['title', 'caption', 'verse']
    template_name = 'rp/form.html'
    success_url = "/threads/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Thread'
        return context


class ThreadUpdateView(UpdateView):
    model = Thread
    fields = ['title', 'caption', 'verse']
    template_name = 'rp/form.html'
    success_url = "/threads/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Thread'
        return context

    def post(self, request, *args, **kwargs):
        self.success_url = '/threads/%s/' % kwargs['pk']
        return super().post(self)


class ThreadDeleteView(DeleteView):
    pass


class ReplyCreateView(CreateView):
    model = Reply
    fields = ['parent', 'character', 'content']
    template_name = 'rp/form.html'
    success_url = "/threads/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reply to Thread'
        return context

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.success_url = '/threads/%s/' % pk
        return super().post(self)


class ReplyUpdateView(UpdateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Reply'
        return context

    def get(self, request, *args, **kwargs):
        self.success_url = '/threads/%s/' % kwargs['thread_pk']
        return super().get(self)


class ReplyDeleteView(DeleteView):
    model = Reply

    def post(self, request, *args, **kwargs):
        self.success_url = '/threads/%s/' % kwargs['thread_pk']
        return super().post(self)