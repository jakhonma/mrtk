from django.utils import timezone
from uuid import uuid4


def code_generator() -> int:
    """Tasodifiy sonlar generatsiya qiladi"""
    return int(str(uuid4().int)[:10])


def directory_path(instance: str, filename: str):
    day = timezone.now()
    class_name = instance.__class__.__name__
    lst = filename.split('.')
    return f"{class_name}/{day.year}/{day.month}/{day.day}/{uuid4()}.{lst[-1]}"


def delete_media(file_name):
    from django.conf import settings
    import os
    paths = settings.MEDIA_ROOT
    os.remove(os.path.join(paths, file_name))


def add_many_to_many(obj, obj_list):
    """Informationga (mtv, region, language, format) larni qushish"""
    for item in obj_list:
        obj.add(item)


def edit_many_to_many(obj, obj_list):
    """Informationga (mtv, region, language, format) larni o'zgartirish"""
    if obj_list is not None:
        obj.set(obj_list)
