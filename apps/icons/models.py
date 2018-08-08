from django.db import models
from apps.rp.models import Model
from django.forms import ModelForm


# face claim
class FaceClaim(Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# icon
class Icon(Model):
    fc_model = models.ForeignKey(FaceClaim, related_name='icons', on_delete=models.DO_NOTHING, null=True, blank=True)
    image = models.ImageField(default='admin/img/icon-unknown.svg')
    tags = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.image.url

    def get_tags(self):
        return [f'#{tag}' for tag in self.tags.split(',')]


class IconForm(ModelForm):
    class Meta:
        model = Icon
        fields = '__all__'


