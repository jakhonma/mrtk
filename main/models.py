from django.db import models


class Poster(models.Model):
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.image.name


class Information(models.Model):
    class Colors(models.TextChoices):
        COLOURED = 'coloured', 'coloured'
        WRITE_BLACK = 'write-black', 'write-black'

    class Material(models.TextChoices):
        ETHER = 'ether', 'ether'
        PRIMARY = 'primary', 'primary'

    category = models.ForeignKey('helper.Category', on_delete=models.SET_NULL, null=True, blank=True)
    mtv = models.ManyToManyField('helper.Mtv', related_name='mtv', blank=True)
    region = models.ManyToManyField('helper.Region', related_name='region', blank=True)
    language = models.ManyToManyField('helper.Language', related_name='language', blank=True)
    format = models.ManyToManyField('helper.Format', related_name='format', blank=True)
    poster = models.OneToOneField(Poster, on_delete=models.SET_NULL, null=True, blank=True)

