"""
URL configuration for WebQueCocinar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views as core_views
from recetario import views as recetario_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD:WebQueCocinar/urls.py
    path('', views.index, name='index'),
    path('receta.html', views.receta, name='receta'),
    path('nosotros.html', views.nosotros, name='nosotros'),
    path('', views.contacto, name='contacto'),
=======
    path('', recetario_views.index, name='index'),
    path('receta.html/', core_views.receta, name='receta'),
    path('nosotros/', core_views.nosotros, name='nosotros'),
    path('contacto/', core_views.contacto, name='contacto'),
>>>>>>> origin/main:urls.py
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    