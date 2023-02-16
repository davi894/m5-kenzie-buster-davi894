from django.db import models
from users.models import User


class MovieChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        null=True, max_length=20, choices=MovieChoices.choices, default=MovieChoices.G
    )
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.User", related_name="user", on_delete=models.CASCADE
    )


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user_movie = models.ForeignKey(
        "users.User", related_name="user_movie_order", on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        "movies.Movie", related_name="movie_order", on_delete=models.CASCADE
    )
