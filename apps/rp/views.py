from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *


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


class CharacterTraitCreateView(CreateView):
    model = CharacterTrait
    fields = ['char', 'title', 'content']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Character Trait'
        return context

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        self.success_url = '/characters/%s/' % pk
        self.initial = {'char': Character.objects.get(pk=pk)}
        return super().get(self)


class CharacterTraitUpdateView(UpdateView):
    model = CharacterTrait
    fields = ['title', 'content']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Trait'
        return context


class CharacterTraitDeleteView(DeleteView):
    model = CharacterTrait
    success_url = '/characters/'


class BioTraitCreateView(CreateView):
    model = BioTrait
    fields = ['bio', 'title', 'content']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Bio Trait'
        return context

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        self.success_url = '/bios/%s/' % pk
        self.initial = {'bio': Bio.objects.get(pk=pk)}
        return super().get(self)


class BioTraitUpdateView(UpdateView):
    model = BioTrait
    fields = ['title', 'content']
    template_name = 'rp/form.html'
    success_url = '/characters/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Trait'
        return context


class BioTraitDeleteView(DeleteView):
    model = BioTrait
    success_url = '/characters/'


class VerseTraitCreateView(CreateView):
    model = VerseTrait
    fields = ['verse', 'title', 'content']
    template_name = 'rp/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Verse Trait'
        return context

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        self.initial = {'verse': Verse.objects.get(pk=pk)}
        return super().get(self)


class VerseTraitUpdateView(UpdateView):
    model = VerseTrait
    fields = ['title', 'content']
    template_name = 'rp/form.html'
    success_url = '/verses/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Trait'
        return context


class VerseTraitDeleteView(DeleteView):
    model = VerseTrait
    success_url = '/verses/'


class TraitUpdateView(UpdateView):
    model = Trait
    fields = ['title', 'content']
    template_name = 'rp/form.html'
    success_url = '/verses/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Trait'
        return context


class TraitDeleteView(DeleteView):
    model = Trait
    success_url = '/'


class ThreadListView(ListView):
    model = Thread

    def get_queryset(self):
        return Thread.objects.order_by('-created')


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