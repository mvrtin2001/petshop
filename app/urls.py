from django.urls import path
from .views import home, contacto , galeria, añadir_producto, agrupar_productos, editar_producto, eliminar_producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('añadir-producto/', añadir_producto , name="añadir_producto"),
    path('agrupar-productos/', agrupar_productos, name="agrupar_productos"),
    path('editar-producto/<id>/', editar_producto, name="editar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    
]
