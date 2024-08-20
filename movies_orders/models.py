from django.db import models
from movies.models import Movie
from users.models import User


class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)