from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.rp.models import *


class CharacterDetailView(DetailView):
    model = Character
    template_name = 'characters/character_detail.html'


class CharacterListView(ListView):
    model = Character
    template_name = 'characters/character_list.html'

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


class BioDetailView(DetailView):
    model = Bio
    template_name = 'characters/bio_detail.html'
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