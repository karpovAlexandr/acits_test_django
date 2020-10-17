from django.urls import path
from pets_rest_api import views


app_name = 'pets_rest'

urlpatterns = [
    path('pets/', views.ListPets.as_view(), name='pets_list_api'),
    path('pets/pet/add/', views.CreatePet.as_view(), name='pet_create'),
    path('pets/pet/<int:pk>/', views.DetailPet.as_view(), name='pet_detail_api'),
    path('pets/pet/<int:pk>/update/', views.UpdatePet.as_view(), name='pet_update_api'),
    path('pets/pet/<int:pk>/delete/', views.DeletePet.as_view(), name='pet_delete_api'),
]
