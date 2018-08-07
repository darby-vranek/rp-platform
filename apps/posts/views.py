from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.rp.models import *


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'


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
    template_name = 'posts/post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'rp/form.html'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/posts/'
