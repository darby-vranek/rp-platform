from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django_summernote.widgets import SummernoteWidget
from django.core.files.storage import FileSystemStorage
from django.forms.widgets import HiddenInput, Textarea, TextInput, Select

fs = FileSystemStorage(location='media/')


class Model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(Model):
    display_name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, default='', blank=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.display_name


class Character(Profile):
    page_name = models.CharField(max_length=30)
    sm_icon = models.URLField(default='', blank=True)
    lg_icon = models.URLField(default='', blank=True)
    verses = models.ManyToManyField('Verse', through='Bio', symmetrical=True, related_name='characters')

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.pk})

    def get_threads(self):
        reps = Reply.objects.filter(character=self)
        threads = list()
        for rep in reps.all():
            if not rep.parent in threads:
                threads.append(rep.parent)
        return threads

    def last_reply(self):
        if self.replies:
            return self.replies.order_by('created').last()



class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['page_name', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']


class Verse(Profile):
    franchise = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('verse-detail', kwargs={'pk': self.pk})


class VerseForm(ModelForm):
    class Meta:
        model = Verse
        fields = ['display_name', 'caption', 'desc', 'franchise']


class Bio(Model):
    bio_char = models.ForeignKey('Character', related_name='bios', on_delete=models.DO_NOTHING)
    bio_verse = models.ForeignKey('Verse', related_name='bios', on_delete=models.DO_NOTHING)
    _display_name = models.CharField(max_length=255, default='', blank=True)
    _caption = models.CharField(max_length=255, default='', blank=True)
    _desc = models.TextField(blank=True)
    _sm_icon = models.URLField(default='', blank=True)
    _lg_icon = models.URLField(default='', blank=True)

    def get_threads(self):
        reps = Reply.objects.filter(character=self.bio_char)
        threads = list()
        for rep in reps.all():
            if rep.parent not in threads and rep.parent.verse == self.bio_verse:
                threads.append(rep.parent)
        return threads

    def display_name(self):
        if self._display_name != '':
            return self._display_name
        return self.bio_char.display_name

    def caption(self):
        if self._caption != '':
            return self._caption
        return self.bio_char.caption

    def desc(self):
        if self._desc != '':
            return self._desc
        return self.bio_char.desc

    def sm_icon(self):
        if self._sm_icon != '':
            return self._sm_icon
        return self.bio_char.sm_icon

    def lg_icon(self):
        if self._lg_icon != '':
            return self._lg_icon
        return self.bio_char.lg_icon

    def get_absolute_url(self):
        return reverse('bio-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s (%s)' % (self.bio_char.display_name, self.bio_verse.display_name)


class BioForm(ModelForm):
    class Meta:
        model = Bio
        fields = ['bio_char', 'bio_verse', '_display_name', '_caption', '_desc', '_sm_icon', '_lg_icon']


# threads & replies
class Thread(Model):
    title = models.CharField(max_length=255, default="Untitled")
    caption = models.CharField(max_length=255, default='', blank=True)
    verse = models.ForeignKey(Verse, related_name='threads', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_latest_reply_created(self):
        latest = self.replies.order_by('created').last()
        return latest.created

    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={'pk': self.pk})


class ThreadForm(ModelForm):
    model = Thread
    fields = ['title', 'caption', 'verse']


class Reply(Model):
    parent = models.ForeignKey(Thread, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    character = models.ForeignKey(Character, related_name='replies', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Reply to %s (%s)' % (self.parent.title, self.created)

    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={'pk': self.parent.pk})


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['character', 'content']
        widgets = {
            'content': SummernoteWidget()
        }


# images
class Image(Model):
    img = models.ImageField(upload_to='images', storage=fs)
    fc = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.fc

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})



class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['img', 'fc']


# about

class Trait(Model):
    character = models.ForeignKey(Character, related_name='traits', null=True, on_delete=models.DO_NOTHING, blank=True)
    verse = models.ForeignKey(Verse, related_name='traits', null=True, on_delete=models.DO_NOTHING, blank=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s' % (self.title, self.content)

    def get_absolute_url(self):
        if self.character:
            return reverse('character-detail', kwargs={'pk': self.character.pk})
        if self.verse:
            return reverse('verse-detail', kwargs={'pk': self.verse.pk})


class TraitForm(ModelForm):
    class Meta:
        model = Trait
        fields = ['character', 'verse', 'title', 'content']


#post

class Post(Model):
    title = models.CharField(max_length=255, default='Untitled', blank=True)
    verse = models.ForeignKey(Verse, related_name='posts', null=True, on_delete=models.DO_NOTHING, blank=True)
    character = models.ForeignKey(Character, related_name='posts', null=True, on_delete=models.DO_NOTHING, blank=True)
    content = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'verse', 'character', 'content']
        widgets = {
            'content': SummernoteWidget()
        }


class Script(Model):
    title = models.CharField(max_length=255, default='Untitled', blank=True)
    verse = models.ForeignKey(Verse, related_name='dialogues', null=True, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('script-detail', kwargs={'pk': self.pk})


class ScriptForm(ModelForm):
    class Meta:
        model = Script
        fields = ['title', 'verse']


class Line(Model):
    script = models.ForeignKey(Script, related_name='lines', on_delete=models.CASCADE, blank=True)
    character = models.ForeignKey(Character, related_name='lines', null=True, blank=True, on_delete=models.DO_NOTHING)
    parenthetical = models.CharField(max_length=255, default='', blank=True)
    dialogue = models.TextField(default='', blank=True)
    action = models.CharField(max_length=255, default='', blank=True)


class LineForm(ModelForm):
    class Meta:
        model = Line
        fields = ['script', 'character', 'parenthetical', 'dialogue', 'action']
        widgets = {
            'script': HiddenInput(),
            'dialogue': Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'e.g. Looking for something, Herms?'
            }),
            'action': TextInput(attrs={
                'class': 'form-control mt-3',
                'placeholder': 'e.g. She waves the blouse triumphantly at her sister.',
            }),
            'parenthetical': TextInput(attrs={
                'class': 'form-control text-right mt-3',
                'placeholder': 'e.g. giggling wickedly',
            }),
            'character': Select(attrs={
                'class': 'custom-select form-control',
            }),

        }
