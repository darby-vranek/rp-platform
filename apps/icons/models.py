from django.db import models
from apps.rp.models import Model
from django import forms
from django.forms import ModelForm
from django.urls import reverse


# face claim
class FaceClaim(Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_all_tags(self):
        tags = list()
        for icon in self.icons.all():
            for tag in icon.get_tags():
                if not tag in tags:
                    tags.append(tag);
        tags.sort()
        return tags


class FaceClaimForm(ModelForm):
    class Meta:
        model = FaceClaim
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'height': '80px'})
        }


# icon
class Icon(Model):
    fc_model = models.ForeignKey(FaceClaim, related_name='icons', on_delete=models.DO_NOTHING, null=True, blank=True)
    image = models.ImageField(default='admin/img/icon-unknown.svg')
    tags = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.image.url

    def get_tags(self):
        return [tag.strip() for tag in self.tags.split(',') if len(tag) > 0]

    def get_absolute_url(self):
        return reverse('faceclaim-detail', kwargs={'pk': self.fc_model.pk})


class IconForm(ModelForm):
    class Meta:
        model = Icon
        fields = '__all__'


class CreateIconForm(ModelForm):
    class Meta:
        model = Icon
        fields = ['image', 'tags']
        widgets = {
            'tags': forms.TextInput(attrs={
                'class': 'tagsinput form-control',
                'data-role': 'tagsinput',
                'data-color': 'primary',
                'placeholder': 'add tag'
            }),
            'image': forms.ClearableFileInput(attrs={
                'multiple': True
            })

        }

class UploadIconForm(forms.Form):
    file = forms.FileField()