from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("herramientas/", views.listado_herramientas, name="herramientas"),
    path("herramientas/<int:id>/", views.detalle_herramienta, name="detalle_herramienta"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]