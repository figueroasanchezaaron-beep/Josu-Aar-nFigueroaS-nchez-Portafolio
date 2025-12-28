from django.contrib import admin
from .models import (
    Categoria, Proveedor, Empleado, Cliente,
    Producto, Venta, DetalleVenta,
    Compra, DetalleCompra, Pago, Envio
)

# -----------------------------
#   MODELOS BÁSICOS
# -----------------------------

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre_categoria', 'descripcion')
    search_fields = ('nombre_categoria',)
    ordering = ('id_categoria',)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre_empresa', 'contacto', 'telefono', 'ciudad')
    search_fields = ('nombre_empresa', 'contacto')
    list_filter = ('ciudad',)
    ordering = ('id_proveedor',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'puesto', 'telefono', 'fecha_contratacion', 'salario')
    search_fields = ('nombre', 'puesto')
    list_filter = ('puesto', 'fecha_contratacion')
    ordering = ('id_empleado',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'telefono', 'correo', 'ciudad')
    search_fields = ('nombre', 'correo')
    list_filter = ('ciudad',)
    ordering = ('id_cliente',)


# -----------------------------
#   PRODUCTOS
# -----------------------------

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id_producto', 'nombre_producto', 'precio', 'stock',
        'categoria', 'proveedor'
    )
    search_fields = ('nombre_producto',)
    list_filter = ('categoria', 'proveedor')
    ordering = ('id_producto',)


# -----------------------------
#   VENTAS Y DETALLES
# -----------------------------

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'cliente', 'empleado', 'fecha_venta', 'total')
    search_fields = ('cliente__nombre', 'empleado__nombre')
    list_filter = ('fecha_venta', 'empleado')
    ordering = ('id_venta',)
    inlines = [DetalleVentaInline]


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    search_fields = ('venta__id_venta', 'producto__nombre_producto')
    list_filter = ('producto',)
    ordering = ('id_detalle',)


# -----------------------------
#   COMPRAS Y DETALLES
# -----------------------------

class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id_compra', 'proveedor', 'fecha_compra', 'total')
    search_fields = ('proveedor__nombre_empresa',)
    list_filter = ('fecha_compra',)
    ordering = ('id_compra',)
    inlines = [DetalleCompraInline]


@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_compra', 'compra', 'producto', 'cantidad', 'costo_unitario', 'subtotal')
    search_fields = ('producto__nombre_producto',)
    list_filter = ('producto',)
    ordering = ('id_detalle_compra',)


# -----------------------------
#   PAGOS
# -----------------------------

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'venta', 'fecha_pago', 'monto', 'metodo_pago')
    search_fields = ('venta__id_venta',)
    list_filter = ('metodo_pago', 'fecha_pago')
    ordering = ('id_pago',)


# -----------------------------
#   ENVIOS
# -----------------------------

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    list_display = (
        'id_envio', 'venta', 'empleado',
        'direccion_envio', 'fecha_envio', 'estado_envio'
    )
    search_fields = ('venta__id_venta', 'empleado__nombre')
    list_filter = ('estado_envio', 'fecha_envio')
    ordering = ('id_envio',)
