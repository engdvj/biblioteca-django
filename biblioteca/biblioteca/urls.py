"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from core import views  # Importa todas as views da pasta core
from core.views import autor_list_create, autor_detail, categoria_list_create, categoria_detail


urlpatterns = [
    path('livros/', views.livro_list_create, name='livro-list-create'),
    path('livros/<int:pk>/', views.livro_detail, name='livro-detail'),

    path('autores/', views.autor_list_create, name='autor-list-create'),
    path('autores/<int:pk>/', views.autor_detail, name='autor-detail'),

    path('categorias/', views.categoria_list_create, name='categoria-list-create'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria-detail'),
]

