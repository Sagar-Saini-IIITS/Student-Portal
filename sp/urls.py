"""sp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),
path('',include('home.urls')),
    path('clubs/', include('clubs.urls')),
    path('lfitems/', include('lfitems.urls')),
    path('notes/', include('notes.urls')),
    path('cne/', include('cne.urls')),
    path('exams/', include('exams.urls')),
    path('fee/', include('fee.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)