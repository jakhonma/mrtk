from django.core.exceptions import ValidationError
from django.db import models


class AbstractClass(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Department(AbstractClass):
    pass


class Fond(AbstractClass):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='fonds')

    def __str__(self):
        return f"{self.name} {self.department.name}"


class Category(AbstractClass):
    fond = models.ForeignKey(Fond, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def clean(self):
        if self.fond is not None and self.parent is not None:
            raise ValidationError("Fond va Parent qushish mumkin emas")
        if self.parent is None and self.fond is None:
            raise ValidationError("Fond or Parent is None")
        if self.parent is not None and self.parent.name == self.name:
            raise ValidationError("Parent name mustn't be same")

    def __str__(self):
        return f"{self.name} -> {self.fond}"


class Mtv(AbstractClass):
    pass


class Region(AbstractClass):
    pass


class Language(AbstractClass):
    pass


class Format(AbstractClass):
    pass
