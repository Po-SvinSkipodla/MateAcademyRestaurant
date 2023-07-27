from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)
    email = models.EmailField("email address", blank=True, unique=True)

    class Meta:
        verbose_name_plural = "cooks"


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    dish_type = models.ForeignKey(
        to=DishType, related_name="dish", on_delete=models.DO_NOTHING
    )
    cooks = models.ManyToManyField(to=Cook, related_name="dish")
