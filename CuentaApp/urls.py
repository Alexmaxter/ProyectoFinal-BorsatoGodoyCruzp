from django.conf import settings
from django.urls import path, reverse_lazy
from .views import iniciar_sesion, perfil, registro, editar_perfil, perfil_usuario, ChangePasswordView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registro/', registro, name='registro'),
    path('cerrar_sesion/', LogoutView.as_view(template_name='CuentaApp/cerrar_sesion.html'), name='cerrar_sesion'),
    path('perfil/', perfil, name='perfil'),
    path('perfil_usuario/<int:id>/', perfil_usuario, name='perfil_usuario'),
    path('perfil/editar', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar_contrasegna', ChangePasswordView.as_view(), name='cambiar_contrasegna'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]


urlpatterns += static(settings.MEDIA_ROOT, docuement_root=settings.MEDIA_ROOT,)