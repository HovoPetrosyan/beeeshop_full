from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from full_ecommerce_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
