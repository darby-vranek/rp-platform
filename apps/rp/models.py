from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class Model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Entity(Model):
    display_name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, default='', blank=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.display_name

    class Meta:
        abstract = True


class Character(Entity):
    page_name = models.CharField(max_length=30)
    sm_icon = models.URLField(default='', blank=True)
    lg_icon = models.URLField(default='', blank=True)
    verses = models.ManyToManyField('Verse', through='Bio', symmetrical=True, related_name='characters')

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.pk})


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['page_name', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']


class Verse(Entity):
    franchise = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('verse-detail', kwargs={'pk': self.pk})


class VerseForm(ModelForm):
    class Meta:
        model = Verse
        fields = ['display_name', 'caption', 'desc', 'franchise']


class Bio(Model):
    character = models.ForeignKey('Character', related_name='bios', on_delete=models.DO_NOTHING)
    verse = models.ForeignKey('Verse', related_name='bios', on_delete=models.DO_NOTHING)
    _display_name = models.CharField(max_length=255, default='', blank=True)
    _caption = models.CharField(max_length=255, default='', blank=True)
    _desc = models.TextField(blank=True)
    _sm_icon = models.URLField(default='', blank=True)
    _lg_icon = models.URLField(default='', blank=True)

    def display_name(self):
        if self._display_name != '':
            return self._display_name
        return self.character.display_name

    def caption(self):
        if self._caption != '':
            return self._caption
        return self.character.caption

    def desc(self):
        if self._desc != '':
            return self._desc
        return self.character.desc

    def sm_icon(self):
        if self._sm_icon != '':
            return self._sm_icon
        return self.character.sm_icon

    def lg_icon(self):
        if self._lg_icon != '':
            return self._lg_icon
        return self.character.lg_icon

    def get_absolute_url(self):
        return reverse('bio-detail', kwargs={'pk': self.pk})


class BioForm(ModelForm):
    class Meta:
        model = Bio
        fields = ['character', 'verse', '_display_name', '_caption', '_desc', '_sm_icon', '_lg_icon']


class Trait(Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.title, self.content)

    class Meta:
        abstract = True


class CharacterTrait(Trait):
    char = models.ForeignKey(Character, related_name='traits', on_delete=models.DO_NOTHING, null=True)

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.char.pk})


class VerseTrait(Trait):
    ver = models.ForeignKey(Verse, related_name='traits', on_delete=models.DO_NOTHING, null=True)


class VerseTraitForm(ModelForm):
    class Meta:
        model = VerseTrait
        fields = ['ver', 'title', 'content']


class BioTrait(Trait):
    bio = models.ForeignKey(Bio, related_name='traits', on_delete=models.DO_NOTHING, null=True)


class BioTraitForm(ModelForm):
    class Meta:
        model = BioTrait
        fields = ['bio', 'title', 'content']