from django.urls import path
from .views import inicio, tienda
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", inicio, name='inicio'),
    path("tienda/", tienda, name='tienda'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)