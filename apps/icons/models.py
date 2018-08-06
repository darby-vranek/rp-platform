from django.db import models
from apps.rp.models import Model
from django.forms import ModelForm


# icon
class Icon(Model):
    fc = models.CharField(max_length=255, default='', blank=True)
    image = models.ImageField(default='admin/img/icon-unknown.svg')

    def __str__(self):
        return self.image.url


class IconForm(ModelForm):
    class Meta:
        model = Icon
        fields = '__all__'


# gallery
class Gallery(Model):
    pass


class GalleryForm(ModelForm):
    pass