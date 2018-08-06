from django.db import models
from apps.rp.models import Model
from django.forms import ModelForm


# face claim
class FaceClaim(Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FaceClaimForm(ModelForm):
    class Meta:
        model = FaceClaim
        fields = '__all__'


# icon
class Icon(Model):
    name = models.CharField(max_length=255)
    fc = models.ForeignKey('FaceClaim', related_name='icons', null=True, blank=True, on_delete=models.DO_NOTHING)
    image = models.ImageField(default='admin/img/icon-unknown.svg')
    title = models.CharField(max_length=255, default='untitled', blank=True)

    def __str__(self):
        return f'Icon name: {self.name}\nFC: {self.fc}\nTitle: {self.title}'


class IconForm(ModelForm):
    class Meta:
        model = Icon
        fields = '__all__'


# gallery
class Gallery(Model):
    pass


class GalleryForm(ModelForm):
    pass