from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


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


class Trait(Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.title, self.content)


class CharacterTrait(Trait):
    char = models.ForeignKey(Character, related_name='traits', on_delete=models.DO_NOTHING, null=True)

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.character.pk})


class CharacterTraitForm(ModelForm):
    class Meta:
        model = CharacterTrait
        fields = ['char', 'title', 'content']


class VerseTrait(Trait):
    verse = models.ForeignKey(Verse, related_name='traits', on_delete=models.DO_NOTHING, null=True)

    def get_absolute_url(self):
        return reverse('verse-detail', kwargs={'pk': self.verse.pk})


class VerseTraitForm(ModelForm):
    class Meta:
        model = VerseTrait
        fields = ['verse', 'title', 'content']


class BioTrait(Trait):
    bio = models.ForeignKey(Bio, related_name='traits', on_delete=models.DO_NOTHING, null=True)

    def get_absolute_url(self):
        return reverse('bio-detail', kwargs={'pk': self.bio.pk})


class BioTraitForm(ModelForm):
    class Meta:
        model = BioTrait
        fields = ['bio', 'title', 'content']


# threads & replies
class Thread(Model):
    title = models.CharField(max_length=255, default="Untitled")
    caption = models.CharField(max_length=255, default='', blank=True)
    verse = models.ForeignKey(Verse, related_name='threads', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

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
        fields = ['parent', 'character', 'content']
        widgets = {
            'content': SummernoteWidget()
        }