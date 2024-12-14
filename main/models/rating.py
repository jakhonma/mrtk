from django.db import models
from authentication.models import User
from main.models import Information
from django.core.validators import MinValueValidator, MaxValueValidator


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.ForeignKey(Information, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(
        # validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'information')
