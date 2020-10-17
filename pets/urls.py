from django.urls import path
from pets import views


app_name = 'pets'

urlpatterns = [
    path('', views.PetListView.as_view(), name='home'),
    path('pet/<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('pet/add/', views.PetCreateView.as_view(), name='pet_create'),
    path('pet/<int:pk>/update', views.PetUpdateView.as_view(), name='pet_update'),
    path('pet/<int:pk>/delete', views.PetDeleteView.as_view(), name='pet_delete'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogOutView.as_view(), name='logout'),
]
