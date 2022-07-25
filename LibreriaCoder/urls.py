from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acerca_de/', include('AcercaDeApp.urls')),
    path('blog/', include('BlogApp.urls')),
    path('contacto/', include('ContactoApp.urls')),
    path('', include('LibreriaCoderApp.urls')),
]
