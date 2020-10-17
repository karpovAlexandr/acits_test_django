from rest_framework import serializers

from pets.models import Pet


class PetListSerializer(serializers.ModelSerializer):
    """Список животных"""

    class Meta:
        model = Pet
        fields = ('name', 'special_sigh',)


class PetDetailSerializer(serializers.ModelSerializer):
    """Вывод животного по id"""

    class Meta:
        model = Pet
        fields = '__all__'


class PetCreateSerializer(serializers.ModelSerializer):
    """Добавление животного в БД"""

    class Meta:
        model = Pet
        fields = '__all__'


class PetUpdateSerializer(serializers.ModelSerializer):
    """Редактирование животного в БД"""

    class Meta:
        model = Pet
        fields = '__all__'


class PetDeleteSerializer(serializers.ModelSerializer):
    """Удаление животного из БД"""

    class Meta:
        model = Pet
        fields = '__all__'
