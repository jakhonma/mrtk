from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from main.utils import directory_path, code_generator


class Poster(models.Model):
    objects = models.Manager()
    image = models.ImageField(upload_to=directory_path, blank=True, null=True)

    def clean(self):
        MAX_SIZE = 1024*1024
        MIN_SIZE = 1024
        image_size = self.image.size
        width, height = self.image.width, self.image.height
        if image_size >= MAX_SIZE:
            raise ValidationError("1 Mbdan kichikroq rasm kiriting")
        if image_size < MIN_SIZE:
            raise ValidationError("1 Kbdan katta rasm kiriting")
        if width > height:
            raise ValidationError("Poster uchun o'lcham notug'ri(160X230)")
        return self

    def __str__(self):
        return f"poster -> {self.pk}"


class Information(models.Model):
    class Colors(models.TextChoices):
        COLOURED = 'coloured', 'coloured'
        WRITE_BLACK = 'write-black', 'write-black'

    class Material(models.TextChoices):
        ETHER = 'ether', 'ether'
        PRIMARY = 'primary', 'primary'

    employee = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True, blank=True)
    fond = models.ForeignKey('helper.Fond', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('helper.Category', on_delete=models.SET_NULL, null=True, blank=True)
    mtv = models.ManyToManyField('helper.Mtv', related_name='mtv', blank=True)
    region = models.ManyToManyField('helper.Region', related_name='region', blank=True)
    language = models.ManyToManyField('helper.Language', related_name='language', blank=True)
    format = models.ManyToManyField('helper.Format', related_name='format', blank=True)
    poster = models.OneToOneField(Poster, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, db_index=True)
    mtv_index = models.CharField(max_length=100)
    location_on_server = models.CharField(max_length=250)
    color = models.CharField(max_length=12, choices=Colors.choices, default=Colors.COLOURED)
    material = models.CharField(max_length=10, choices=Material.choices, default=Material.ETHER)
    duration = models.TimeField(blank=True, null=True)
    year = models.PositiveIntegerField(null=True, blank=True, validators=[
        MinValueValidator(1920, message="Yilni tug'ri kiriting?"),
        MaxValueValidator(int(date.today().year), message="Yilni tug'ri kiriting?")
    ])
    month = models.PositiveIntegerField(null=True, blank=True, validators=[
        MinValueValidator(1, message="Oyni tug'ri kiriting?"),
        MaxValueValidator(12, message="Oyni tug'ri kiriting?")
    ])
    day = models.PositiveIntegerField(null=True, blank=True, validators=[
        MinValueValidator(1, message="Kunni tug'ri kiriting?"),
        MaxValueValidator(31, message="Kunni tug'ri kiriting?")
    ])
    single_code = models.PositiveBigIntegerField(default=code_generator(), editable=False)
    restoration = models.BooleanField(default=False)
    confidential = models.BooleanField(default=False)
    brief_data = models.TextField(null=True, blank=True, db_index=True)
    summary = models.TextField(null=True, blank=True, db_index=True)
    is_serial = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    # def clean(self):
    #     if not self.is_serial:
    #         raise ValidationError("Qism qushish mumkin emas")

    def __str__(self):
        return self.title


class Cadre(models.Model):
    objects = models.Manager()
    image = models.ImageField(upload_to=directory_path)
    information = models.ForeignKey('main.Information', on_delete=models.CASCADE, related_name='information')

    def __str__(self):
        return f'video_cadre - {self.pk}'


class Serial(models.Model):
    objects = models.Manager()
    information = models.ForeignKey('main.Information', on_delete=models.CASCADE, related_name='seraial')
    part = models.PositiveSmallIntegerField(null=True, blank=True)
    duration = models.TimeField()

    def __str__(self):
        return self.information.title
