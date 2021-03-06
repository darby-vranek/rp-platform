"""aurora_rp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
    path('', include('apps.rp.urls')),
    path('icons/', include('apps.icons.urls')),
    path('scripts/', include('apps.scripts.urls')),
    path('threads/', include('apps.threads.urls')),
    path('characters/', include('apps.characters.urls')),
    path('verses/', include('apps.verses.urls')),
    path('posts/', include('apps.posts.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
