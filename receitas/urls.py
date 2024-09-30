from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('receita/new', views.newRecipe, name='new-recipe'),
    path('receita/<int:pk>/', views.receita, name='receita-detail'),
    path('random_receita/', views.randomRecipe, name='random-receita'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('delete_receita/<int:pk>/', views.deleteRecipe, name='delete-receita'),
    path('update_receita/<int:pk>/', views.updateRecipe, name='update-receita'),
]
