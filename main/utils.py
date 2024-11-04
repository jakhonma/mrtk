from django.utils import timezone
from uuid import uuid4


def code_generator() -> int:
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
