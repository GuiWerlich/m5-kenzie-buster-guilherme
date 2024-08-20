from django.db import models
from users.models import User


class CategoryRating(models.TextChoices):
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    NC_17 = 'NC-17'


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, null=True, default="")
    rating = models.CharField(
        max_length=20,
        choices=CategoryRating.choices,
        default=CategoryRating.G
    )
    synopsis = models.TextField(null=True, blank=True, default="")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='movies')