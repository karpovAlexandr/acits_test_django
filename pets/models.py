from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Pet(models.Model):
    """Модель животного"""
    name = models.CharField('Кличка', max_length=50)
    age = models.SmallIntegerField('Возраст', validators=[MinValueValidator(0)])
    arrived = models.DateField('Дата прибытия в приют', auto_now_add=True)
    weight = models.FloatField('Вес', validators=[MinValueValidator(0)])
    height = models.SmallIntegerField('Рост', validators=[MinValueValidator(0)])
    special_sigh = models.CharField('Особые приметы', max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pets:pet_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
