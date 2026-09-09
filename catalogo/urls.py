from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("herramientas/", views.listado_herramientas, name="herramientas"),
    path("herramientas/<int:id>/", views.detalle_herramienta, name="detalle_herramienta"),
    path("login/", views.login_view, name="login"),
    path("carrito/agregar/<int:id>/", views.agregar_carrito, name="agregar_carrito"),
    path("carrito/", views.ver_carrito, name="ver_carrito"),
    path("carrito/eliminar/<int:id>/", views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path("carrito/cancelar/", views.cancelar_compra, name="cancelar_compra"),
    path("carrito/confirmar/", views.confirmar_compra, name="confirmar_compra"),
]

