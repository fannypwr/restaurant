from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    prepared = models.DurationField()
    price = models.FloatField()
    is_vege = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return f'<Dish {self.name}>'


class Menu(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    dishes = models.ManyToManyField(Dish, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Menu {self.name}>'
