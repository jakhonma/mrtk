from django.db import models


class AbstractClass(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Department(AbstractClass):
    pass


class Fond(AbstractClass):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='fonds')


class Category(AbstractClass):
    fond = models.ForeignKey(Fond, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)


class Mtv(AbstractClass):
    pass


class Region(AbstractClass):
    pass


class Language(AbstractClass):
    pass


class Format(AbstractClass):
    pass
