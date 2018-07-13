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


class Bio(Entity):
    character = models.ForeignKey(Character, related_name='bios', on_delete=models.DO_NOTHING)
    verse = models.ForeignKey(Verse, related_name='bios', on_delete=models.DO_NOTHING)
    sm_icon = models.URLField(default='', blank=True)
    lg_icon = models.URLField(default='', blank=True)

    def get_absolute_url(self):
        return reverse('bio-detail', kwargs={'pk': self.pk})


class BioForm(ModelForm):
    model = Bio
    fields = ['character', 'verse', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']