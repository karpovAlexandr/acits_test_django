from django.db import models
from django.urls import reverse


class Pet(models.Model):
    """Модель животного"""
    name = models.CharField('Кличка', max_length=50)
    age = models.SmallIntegerField('Возраст')
    arrived = models.DateField('Дата прибытия в приют', auto_now_add=True)
    weight = models.FloatField('Вес')
    height = models.SmallIntegerField('Рост')
    special_sigh = models.CharField('Особые приметы', max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pets:pet_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

