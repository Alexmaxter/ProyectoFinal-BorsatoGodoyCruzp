from django.urls import path
from .views import inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", inicio, name='inicio'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)