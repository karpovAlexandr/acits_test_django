from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Shelter(models.Model):
    title = models.CharField('Название приюта', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Приют'
        verbose_name_plural = 'Приюты'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shelter = models.ForeignKey(Shelter, related_name='user_shelter', verbose_name='Приют', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Pet(models.Model):
    """Модель животного"""
    name = models.CharField('Кличка', max_length=50)
    age = models.SmallIntegerField('Возраст', validators=[MinValueValidator(0)])
    arrived = models.DateField('Дата прибытия в приют', auto_now_add=True)
    weight = models.FloatField('Вес', validators=[MinValueValidator(0)])
    height = models.SmallIntegerField('Рост', validators=[MinValueValidator(0)])
    special_sigh = models.CharField('Особые приметы', max_length=255, blank=True)
    shelter = models.ForeignKey(Shelter, related_name='pet_shelter', verbose_name='Приют', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pets:pet_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
