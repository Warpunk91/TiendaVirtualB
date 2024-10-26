"""
URL configuration for tiendavirtual project.

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

from django.contrib import admin
from django.urls import path
from productos.views import ProductoDetailView, ProductoListCreateView
from tiendas.views import TiendaDetailView, TiendaListCreateView
from usuarios.views import LoginView, RegistroUsuarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistroUsuarioView.as_view(), name='usuario'),
    path('tiendas/', TiendaListCreateView.as_view(), name='tiendaCreate'),
    path('tiendas/<int:pk>/', TiendaDetailView.as_view(), name='tiendaDetail'),
    path('productos/', ProductoListCreateView.as_view(), name='productoCreate'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='productoDetail'),
]   