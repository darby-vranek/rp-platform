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


class CharacterDetailView(DetailView):
    model = Character


class CharacterListView(ListView):
    model = Character

    def get_queryset(self):
        return Character.objects.order_by('page_name')


class CharacterCreateView(CreateView):
    model = Character
    fields = ['page_name', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']
    template_name = 'rp/form.html'
    success_url = "/characters/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Character'
        return context


class CharacterUpdateView(UpdateView):
    model = Character
    fields = ['page_name', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # I'd eventually like to have this say "edit character name"
        context['title'] = 'Edit Character'
        return context

    def get(self, *args, **kwargs):
        self.success_url = '/characters/%s/' % kwargs['pk']
        return super().get(self)


class CharacterDeleteView(DeleteView):
    pass


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


class BioDetailView(DetailView):
    model = Bio
    context_object_name = 'character'


class BioCreateView(CreateView):
    model = Bio
    fields = ['bio_char', 'bio_verse', '_display_name', '_caption', '_desc', '_sm_icon', '_lg_icon']
    template_name = 'rp/form.html'
    success_url = '/characters/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'New Bio'
        return context


class CharacterBioCreateView(CreateView):
    model = Bio
    fields = ['bio_char', 'bio_verse', '_display_name', '_caption', '_desc', '_sm_icon', '_lg_icon']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New AU'
        return context

    def get(self, *args, **kwargs):
        self.initial = {'bio_char': Character.objects.get(pk=kwargs['pk'])}
        self.success_url = kwargs['pk']
        return super().get(self)


class VerseBioCreateView(CreateView):
    model = Bio
    fields = ['bio_char', 'bio_verse', '_display_name', '_caption', '_desc', '_sm_icon', '_lg_icon']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Verse'
        return context

    def get(self, *args, **kwargs):
        self.initial = {'bio_verse': Verse.objects.get(pk=kwargs['pk'])}
        self.success_url = '/verses/%s/' % kwargs['pk']
        return super().get(self)


class BioUpdateView(UpdateView):
    model = Bio
    fields = ['_display_name', '_caption', '_desc', '_sm_icon', '_lg_icon']
    template_name = 'rp/form.html'
    bio = None

    def get(self, *args, **kwargs):
        self.bio = Bio.objects.get(pk=kwargs['pk'])
        self.success_url = '/bios/%s/' % kwargs['pk']
        return super().get(self)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '%s: <em>%s</em>' % (self.bio.bio_char.display_name, self.bio.bio_verse.display_name)
        return context


class ThreadListView(ListView):
    model = Thread

    def get_queryset(self):
        return Thread.objects.order_by('title')


class ThreadDetailView(DetailView):
    model = Thread

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


class ImageListView(ListView):
    model = Image

    def get_queryset(self):
        return Image.objects.order_by('fc')


class ImageDetailView(DetailView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'rp/image_form.html'
    success_url = "/images/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Image'
        return context


class ImageUpdateView(UpdateView):
    model = Image
    form_class = ImageForm
    template_name = 'rp/form.html'
    success_url = '/images/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Image'
        return context

def new_image(request):
    if request.POST:
        return redirect(reverse('images'))
    return render(request, 'rp/new_image.html')


def sign_s3(request, file_name, file_type, file_format):
    s3 = boto3.client('s3')
    s3.upload_file(f"/{file_name}", 'aurora-rp', file_name)

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.



def trait_list_view(request, query):
    trait_list = Trait.objects.filter(title__iexact=query)
    return render(request, 'rp/trait_list.html', context={'trait_list': trait_list})


class CharacterTraitCreateView(CreateView):
    model = Trait
    form_class = TraitForm
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Trait'
        return context

    def get(self, *args, **kwargs):
        self.success_url = '/characters/%s/' % kwargs['char_pk']
        self.initial = {'character': Character.objects.get(pk=kwargs['char_pk'])}
        return super().get(self)


class CharacterTraitUpdateView(UpdateView):
    model = Trait
    form_class = TraitForm
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Trait'
        return context

    def get(self, *args, **kwargs):
        self.success_url = '/characters/%s/' % kwargs['char_pk']
        return super().get(self)


class CharacterTraitDeleteView(DeleteView):
    model = Trait

    def post(self, *args, **kwargs):
        self.success_url = '/characters/%s/' % kwargs['char_pk']
        return super().post(self)


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
