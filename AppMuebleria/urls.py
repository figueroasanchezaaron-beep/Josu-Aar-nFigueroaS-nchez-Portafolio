from django.urls import path
from . import views
from .views import inicio


urlpatterns = [
path('', inicio, name="inicio"),


    # --------------------
    # CATEGORÍAS
    # --------------------
    path('categorias/', views.categorias_lista, name='categorias_lista'),
    path('categorias/crear/', views.categorias_crear, name='categorias_crear'),
    path('categorias/editar/<int:id>/', views.categorias_editar, name='categorias_editar'),
    path('categorias/eliminar/<int:id>/', views.categorias_eliminar, name='categorias_eliminar'),

    # --------------------
    # PRODUCTOS
    # --------------------
    path('productos/', views.productos_lista, name='productos_lista'),
    path('productos/crear/', views.productos_crear, name='productos_crear'),
    path('productos/editar/<int:id>/', views.productos_editar, name='productos_editar'),
    path('productos/eliminar/<int:id>/', views.productos_eliminar, name='productos_eliminar'),
    path('productos/detalle/<int:id>/', views.productos_detalle, name='productos_detalle'),

    # --------------------
    # CLIENTES
    # --------------------
    path('clientes/', views.clientes_lista, name='clientes_lista'),
    path('clientes/crear/', views.clientes_crear, name='clientes_crear'),
    path('clientes/editar/<int:id>/', views.clientes_editar, name='clientes_editar'),
    path('clientes/eliminar/<int:id>/', views.clientes_eliminar, name='clientes_eliminar'),
    path('clientes/detalle/<int:id>/', views.clientes_detalle, name='clientes_detalle'),

    # --------------------
    # PROVEEDORES
    # --------------------
    path('proveedores/', views.proveedores_lista, name='proveedores_lista'),
    path('proveedores/crear/', views.proveedores_crear, name='proveedores_crear'),
    path('proveedores/editar/<int:id>/', views.proveedores_editar, name='proveedores_editar'),
    path('proveedores/eliminar/<int:id>/', views.proveedores_eliminar, name='proveedores_eliminar'),
    path('proveedores/detalle/<int:id>/', views.proveedores_detalle, name='proveedores_detalle'),

    # --------------------
    # EMPLEADOS
    # --------------------
    path('empleados/', views.empleados_lista, name='empleados_lista'),
    path('empleados/crear/', views.empleados_crear, name='empleados_crear'),
    path('empleados/editar/<int:id>/', views.empleados_editar, name='empleados_editar'),
    path('empleados/eliminar/<int:id>/', views.empleados_eliminar, name='empleados_eliminar'),
    path('empleados/detalle/<int:id>/', views.empleados_detalle, name='empleados_detalle'),

    # --------------------
    # VENTAS
    # --------------------
    path('ventas/', views.ventas_lista, name='ventas_lista'),
    path('ventas/crear/', views.ventas_crear, name='ventas_crear'),
    path('ventas/editar/<int:id>/', views.ventas_editar, name='ventas_editar'),
    path('ventas/eliminar/<int:id>/', views.ventas_eliminar, name='ventas_eliminar'),
    path('ventas/detalle/<int:id>/', views.ventas_detalle, name='ventas_detalle'),

    # --------------------
    # DETALLE DE VENTA
    # --------------------
    path('detalle_venta/<int:id_venta>/', views.detalle_venta_lista, name='detalle_venta_lista'),
    path('detalle_venta/agregar/<int:id_venta>/', views.detalle_venta_agregar, name='detalle_venta_agregar'),
    path('detalle_venta/editar/<int:id_detalle>/', views.detalle_venta_editar, name='detalle_venta_editar'),
    path('detalle_venta/eliminar/<int:id_detalle>/', views.detalle_venta_eliminar, name='detalle_venta_eliminar'),

    # --------------------
    # COMPRAS
    # --------------------
    path('compras/', views.compras_lista, name='compras_lista'),
    path('compras/crear/', views.compras_crear, name='compras_crear'),
    path('compras/editar/<int:id>/', views.compras_editar, name='compras_editar'),
    path('compras/eliminar/<int:id>/', views.compras_eliminar, name='compras_eliminar'),
    path('compras/detalle/<int:id>/', views.compras_detalle, name='compras_detalle'),

    # --------------------
    # DETALLE DE COMPRA
    # --------------------
    path('detalle_compra/<int:id_compra>/', views.detalle_compra_lista, name='detalle_compra_lista'),
    path('detalle_compra/agregar/<int:id_compra>/', views.detalle_compra_agregar, name='detalle_compra_agregar'),
    path('detalle_compra/editar/<int:id_detalle_compra>/', views.detalle_compra_editar, name='detalle_compra_editar'),
    path('detalle_compra/eliminar/<int:id_detalle_compra>/', views.detalle_compra_eliminar, name='detalle_compra_eliminar'),

    # --------------------
    # PAGOS
    # --------------------
    path('pagos/', views.pagos_lista, name='pagos_lista'),
    path('pagos/crear/', views.pagos_crear, name='pagos_crear'),
    path('pagos/editar/<int:id>/', views.pagos_editar, name='pagos_editar'),
    path('pagos/eliminar/<int:id>/', views.pagos_eliminar, name='pagos_eliminar'),
    path('pagos/detalle/<int:id>/', views.pagos_detalle, name='pagos_detalle'),

    # --------------------
    # ENVIOS
    # --------------------
    path('envios/', views.envios_lista, name='envios_lista'),
    path('envios/crear/', views.envios_crear, name='envios_crear'),
    path('envios/editar/<int:id>/', views.envios_editar, name='envios_editar'),
    path('envios/eliminar/<int:id>/', views.envios_eliminar, name='envios_eliminar'),
    path('envios/detalle/<int:id>/', views.envios_detalle, name='envios_detalle'),
]
