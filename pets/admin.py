from django.contrib import admin

from pets.models import Pet, Profile, Shelter

admin.site.register(Profile)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """Модель животного для админки"""
    list_display = ('id', 'name', 'arrived', 'shelter', 'special_sigh',)
    fields = ('name', 'birth_date', 'arrived', 'weight', 'height', 'special_sigh', 'shelter', 'deleted_at')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'special_sigh',)
    readonly_fields = ('arrived', 'deleted_at')


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    fields = ('title',)
    list_display_links = ('id', 'title',)
