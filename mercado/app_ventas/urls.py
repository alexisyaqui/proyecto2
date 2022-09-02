from django.urls import path
from app_ventas.views.views import CategoriaListView



urlpatterns = [
    path('categoria/lista', CategoriaListView.as_view(), name='categoria/lista'),
]
