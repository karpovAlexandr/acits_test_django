import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from softdelete.models import SoftDeleteObject


class Shelter(models.Model):
    """Модель приюта"""
    title = models.CharField('Название приюта', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Приют'
        verbose_name_plural = 'Приюты'


class Profile(models.Model):
    """Модель пользователя с привязкой к приюту"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shelter = models.ForeignKey(Shelter, related_name='user_shelter', verbose_name='Приют', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Pet(SoftDeleteObject, models.Model):
    """Модель животного"""
    name = models.CharField('Кличка', max_length=50)
    birth_date = models.DateField('Дата рождения', default=datetime.date.today())
    arrived = models.DateField('Дата прибытия в приют', default=datetime.date.today())
    weight = models.FloatField('Вес', validators=[MinValueValidator(0)])
    height = models.SmallIntegerField('Рост', validators=[MinValueValidator(0)])
    special_sigh = models.CharField('Особые приметы', max_length=255, blank=True)
    shelter = models.ForeignKey(Shelter, related_name='pet_shelter', verbose_name='Приют', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pets:pet_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.arrived < datetime.date.today() or self.birth_date < datetime.date.today():
            raise ValidationError("The dates cannot be in the past!")

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
