from django.contrib import admin

from pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """Модель животного для админки"""
    list_display = ('id', 'name', 'age', 'arrived', 'weight', 'height', 'special_sigh',)
    fields = ('name', 'age', 'arrived', 'weight', 'height', 'special_sigh',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'special_sigh',)
    readonly_fields = ('arrived',)

