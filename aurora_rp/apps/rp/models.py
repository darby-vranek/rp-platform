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

    class Meta:
        abstract = True


class Character(Entity):
    page_name = models.CharField(max_length=30)
    sm_icon = models.URLField(default='', blank=True)
    lg_icon = models.URLField(default='', blank=True)

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.pk})


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['page_name', 'display_name', 'caption', 'desc', 'sm_icon', 'lg_icon']
