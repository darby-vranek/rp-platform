from django.db import models
from django.forms import ModelForm


class Model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Entity(Model):
    class Meta:
        abstract = True


class Character(Entity):
    pass


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        # fields =


class Verse(Entity):
    pass


class VerseForm(ModelForm):
    pass


class Bio(Model):
    pass


class BioForm(ModelForm):
    pass