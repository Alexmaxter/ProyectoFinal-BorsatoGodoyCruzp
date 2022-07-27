from django.conf import settings
from django.urls import path
from .views import iniciar_sesion, perfil, registro, editar_perfil
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registro/', registro, name='registro'),
    path('cerrar_sesion/', LogoutView.as_view(template_name='CuentaApp/cerrar_sesion.html'), name='cerrar_sesion'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar', editar_perfil, name='editar_perfil'),
]


urlpatterns += static(settings.MEDIA_ROOT, docuement_root=settings.MEDIA_ROOT,)