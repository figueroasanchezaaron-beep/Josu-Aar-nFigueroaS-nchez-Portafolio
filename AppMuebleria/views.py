from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Categoria, Producto, Cliente, Proveedor, Empleado,
    Venta, DetalleVenta, Compra, DetalleCompra, Pago, Envio
)
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum

def inicio(request):
    total_productos = Producto.objects.count()
    total_clientes = Cliente.objects.count()
    total_proveedores = Proveedor.objects.count()
    total_empleados = Empleado.objects.count()

    total_ventas = Venta.objects.count()
    venta_acumulada = Venta.objects.aggregate(Sum("total"))["total__sum"] or 0

    return render(request, "dashboard.html", {
        "total_productos": total_productos,
        "total_clientes": total_clientes,
        "total_proveedores": total_proveedores,
        "total_empleados": total_empleados,
        "total_ventas": total_ventas,
        "venta_acumulada": venta_acumulada,
    })




# ======================================================
#  CATEGORÍAS
# ======================================================

def categorias_lista(request):
    q = request.GET.get("q")
    if q:
        categorias = Categoria.objects.filter(nombre_categoria__icontains=q)
    else:
        categorias = Categoria.objects.all()
    return render(request, "categorias/lista.html", {"categorias": categorias})



def categorias_crear(request):
    if request.method == "POST":
        Categoria.objects.create(
            nombre_categoria=request.POST["nombre_categoria"],
            descripcion=request.POST.get("descripcion")
        )
        return redirect("categorias_lista")
    return render(request, "categorias/crear.html")


def categorias_editar(request, id):
    categoria = get_object_or_404(Categoria, id_categoria=id)

    if request.method == "POST":
        categoria.nombre_categoria = request.POST["nombre_categoria"]
        categoria.descripcion = request.POST.get("descripcion")
        categoria.save()
        return redirect("categorias_lista")

    return render(request, "categorias/editar.html", {"categoria": categoria})


def categorias_eliminar(request, id):
    categoria = get_object_or_404(Categoria, id_categoria=id)
    categoria.delete()
    return redirect("categorias_lista")


# ======================================================
#  PRODUCTOS
# ======================================================

from django.db.models import Q

def productos_lista(request):
    q = request.GET.get("q")
    categoria = request.GET.get("categoria")
    proveedor = request.GET.get("proveedor")
    min_precio = request.GET.get("min_precio")
    max_precio = request.GET.get("max_precio")

    productos = Producto.objects.all()

    if q:
        productos = productos.filter(
            Q(nombre_producto__icontains=q) |
            Q(descripcion__icontains=q)
        )

    if categoria:
        productos = productos.filter(categoria_id=categoria)

    if proveedor:
        productos = productos.filter(proveedor_id=proveedor)

    if min_precio:
        productos = productos.filter(precio__gte=min_precio)

    if max_precio:
        productos = productos.filter(precio__lte=max_precio)

    return render(request, "productos/lista.html", {
        "productos": productos,
        "categorias": Categoria.objects.all(),
        "proveedores": Proveedor.objects.all()
    })




def productos_crear(request):
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    if request.method == "POST":
        Producto.objects.create(
            nombre_producto=request.POST["nombre_producto"],
            descripcion=request.POST.get("descripcion"),
            precio=request.POST["precio"],
            stock=request.POST["stock"],
            categoria_id=request.POST["id_categoria"],
            proveedor_id=request.POST["id_proveedor"],
        )
        return redirect("productos_lista")

    return render(request, "productos/crear.html",
                  {"categorias": categorias, "proveedores": proveedores})


def productos_editar(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    if request.method == "POST":
        producto.nombre_producto = request.POST["nombre_producto"]
        producto.descripcion = request.POST.get("descripcion")
        producto.precio = request.POST["precio"]
        producto.stock = request.POST["stock"]
        producto.categoria_id = request.POST["id_categoria"]
        producto.proveedor_id = request.POST["id_proveedor"]
        producto.save()
        return redirect("productos_lista")

    return render(request, "productos/editar.html",
                  {"producto": producto, "categorias": categorias, "proveedores": proveedores})


def productos_detalle(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    return render(request, "productos/detalle.html", {"producto": producto})


def productos_eliminar(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    producto.delete()
    return redirect("productos_lista")


# ======================================================
#  CLIENTES
# ======================================================

def clientes_lista(request):
    q = request.GET.get("q")
    ciudad = request.GET.get("ciudad")

    clientes = Cliente.objects.all()

    if q:
        clientes = clientes.filter(Q(nombre__icontains=q) | Q(correo__icontains=q))

    if ciudad:
        clientes = clientes.filter(ciudad__icontains=ciudad)

    return render(request, "clientes/lista.html", {"clientes": clientes})




def clientes_crear(request):
    if request.method == "POST":
        Cliente.objects.create(
            nombre=request.POST["nombre"],
            direccion=request.POST.get("direccion"),
            telefono=request.POST.get("telefono"),
            correo=request.POST.get("correo"),
            ciudad=request.POST.get("ciudad"),
        )
        return redirect("clientes_lista")
    return render(request, "clientes/crear.html")


def clientes_editar(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)

    if request.method == "POST":
        cliente.nombre = request.POST["nombre"]
        cliente.direccion = request.POST.get("direccion")
        cliente.telefono = request.POST.get("telefono")
        cliente.correo = request.POST.get("correo")
        cliente.ciudad = request.POST.get("ciudad")
        cliente.save()
        return redirect("clientes_lista")

    return render(request, "clientes/editar.html", {"cliente": cliente})


def clientes_detalle(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    return render(request, "clientes/detalle.html", {"cliente": cliente})


def clientes_eliminar(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    cliente.delete()
    return redirect("clientes_lista")


# ======================================================
#  PROVEEDORES
# ======================================================

def proveedores_lista(request):
    q = request.GET.get("q")
    if q:
        proveedores = Proveedor.objects.filter(
            Q(nombre_empresa__icontains=q) |
            Q(contacto__icontains=q) |
            Q(ciudad__icontains=q)
        )
    else:
        proveedores = Proveedor.objects.all()
    return render(request, "proveedores/lista.html", {"proveedores": proveedores})



def proveedores_crear(request):
    if request.method == "POST":
        Proveedor.objects.create(
            nombre_empresa=request.POST["nombre_empresa"],
            contacto=request.POST.get("contacto"),
            telefono=request.POST.get("telefono"),
            correo=request.POST.get("correo"),
            direccion=request.POST.get("direccion"),
            ciudad=request.POST.get("ciudad"),
        )
        return redirect("proveedores_lista")

    return render(request, "proveedores/crear.html")


def proveedores_editar(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)

    if request.method == "POST":
        proveedor.nombre_empresa = request.POST["nombre_empresa"]
        proveedor.contacto = request.POST.get("contacto")
        proveedor.telefono = request.POST.get("telefono")
        proveedor.correo = request.POST.get("correo")
        proveedor.direccion = request.POST.get("direccion")
        proveedor.ciudad = request.POST.get("ciudad")
        proveedor.save()

        return redirect("proveedores_lista")

    return render(request, "proveedores/editar.html", {"proveedor": proveedor})


def proveedores_detalle(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    return render(request, "proveedores/detalle.html", {"proveedor": proveedor})


def proveedores_eliminar(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    proveedor.delete()
    return redirect("proveedores_lista")


# ======================================================
#  EMPLEADOS
# ======================================================

def empleados_lista(request):
    q = request.GET.get("q")
    puesto = request.GET.get("puesto")

    empleados = Empleado.objects.all()

    if q:
        empleados = empleados.filter(nombre__icontains=q)

    if puesto:
        empleados = empleados.filter(puesto__icontains=puesto)

    return render(request, "empleados/lista.html", {"empleados": empleados})




def empleados_crear(request):
    if request.method == "POST":
        Empleado.objects.create(
            nombre=request.POST["nombre"],
            puesto=request.POST.get("puesto"),
            telefono=request.POST.get("telefono"),
            direccion=request.POST.get("direccion"),
            fecha_contratacion=request.POST.get("fecha_contratacion"),
            salario=request.POST.get("salario"),
        )
        return redirect("empleados_lista")
    return render(request, "empleados/crear.html")


def empleados_editar(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)

    if request.method == "POST":
        empleado.nombre = request.POST["nombre"]
        empleado.puesto = request.POST.get("puesto")
        empleado.telefono = request.POST.get("telefono")
        empleado.direccion = request.POST.get("direccion")
        empleado.fecha_contratacion = request.POST.get("fecha_contratacion")
        empleado.salario = request.POST.get("salario")
        empleado.save()
        return redirect("empleados_lista")

    return render(request, "empleados/editar.html", {"empleado": empleado})


def empleados_detalle(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    return render(request, "empleados/detalle.html", {"empleado": empleado})


def empleados_eliminar(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    empleado.delete()
    return redirect("empleados_lista")


# ======================================================
#  VENTAS
# ======================================================

def ventas_lista(request):
    q = request.GET.get("q")
    desde = request.GET.get("desde")
    hasta = request.GET.get("hasta")

    ventas = Venta.objects.all()

    if q:
        ventas = ventas.filter(
            Q(cliente__nombre__icontains=q) |
            Q(empleado__nombre__icontains=q)
        )

    if desde:
        ventas = ventas.filter(fecha_venta__gte=desde)

    if hasta:
        ventas = ventas.filter(fecha_venta__lte=hasta)

    return render(request, "ventas/lista.html", {"ventas": ventas})




def ventas_crear(request):
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()

    if request.method == "POST":
        Venta.objects.create(
            cliente_id=request.POST["id_cliente"],
            empleado_id=request.POST["id_empleado"],
            fecha_venta=request.POST["fecha_venta"],
            total=request.POST["total"],
        )
        return redirect("ventas_lista")

    return render(request, "ventas/crear.html", {"clientes": clientes, "empleados": empleados})


def ventas_editar(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()

    if request.method == "POST":
        venta.cliente_id = request.POST["id_cliente"]
        venta.empleado_id = request.POST["id_empleado"]
        venta.fecha_venta = request.POST["fecha_venta"]
        venta.total = request.POST["total"]
        venta.save()
        return redirect("ventas_lista")

    return render(request, "ventas/editar.html",
                  {"venta": venta, "clientes": clientes, "empleados": empleados})


def ventas_detalle(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    detalles = DetalleVenta.objects.filter(venta_id=id)
    return render(request, "ventas/detalle.html", {"venta": venta, "detalles": detalles})


def ventas_eliminar(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    venta.delete()
    return redirect("ventas_lista")


# ======================================================
#  DETALLE DE VENTA
# ======================================================

def detalle_venta_lista(request, id_venta):
    venta = get_object_or_404(Venta, id_venta=id_venta)
    detalles = DetalleVenta.objects.filter(venta_id=id_venta)
    productos = Producto.objects.all()
    return render(request, "detalle_venta/lista.html",
                  {"venta": venta, "detalles": detalles, "productos": productos})


def detalle_venta_agregar(request, id_venta):
    venta = get_object_or_404(Venta, id_venta=id_venta)
    productos = Producto.objects.all()

    if request.method == "POST":
        DetalleVenta.objects.create(
            venta_id=id_venta,
            producto_id=request.POST["id_producto"],
            cantidad=request.POST["cantidad"],
            precio_unitario=request.POST["precio_unitario"],
        )
        return redirect(reverse("detalle_venta_lista", args=[id_venta]))

    return render(request, "detalle_venta/agregar.html",
                  {"venta": venta, "productos": productos})


def detalle_venta_editar(request, id_detalle):
    detalle = get_object_or_404(DetalleVenta, id_detalle=id_detalle)
    productos = Producto.objects.all()

    if request.method == "POST":
        detalle.producto_id = request.POST["id_producto"]
        detalle.cantidad = request.POST["cantidad"]
        detalle.precio_unitario = request.POST["precio_unitario"]
        detalle.save()

        return redirect(reverse("detalle_venta_lista", args=[detalle.venta_id]))

    return render(request, "detalle_venta/editar.html",
                  {"detalle": detalle, "productos": productos})


def detalle_venta_eliminar(request, id_detalle):
    detalle = get_object_or_404(DetalleVenta, id_detalle=id_detalle)
    venta_id = detalle.venta_id
    detalle.delete()
    return redirect(reverse("detalle_venta_lista", args=[venta_id]))


# ======================================================
#  COMPRAS
# ======================================================

def compras_lista(request):
    q = request.GET.get("q")
    proveedor = request.GET.get("proveedor")
    fecha = request.GET.get("fecha")

    compras = Compra.objects.all()

    if q:
        compras = compras.filter(proveedor__nombre_empresa__icontains=q)

    if proveedor:
        compras = compras.filter(proveedor_id=proveedor)

    if fecha:
        compras = compras.filter(fecha_compra=fecha)

    return render(request, "compras/lista.html", {
        "compras": compras,
        "proveedores": Proveedor.objects.all()
    })




def compras_crear(request):
    proveedores = Proveedor.objects.all()

    if request.method == "POST":
        Compra.objects.create(
            proveedor_id=request.POST["id_proveedor"],
            fecha_compra=request.POST["fecha_compra"],
            total=request.POST["total"],
        )
        return redirect("compras_lista")

    return render(request, "compras/crear.html", {"proveedores": proveedores})


def compras_editar(request, id):
    compra = get_object_or_404(Compra, id_compra=id)
    proveedores = Proveedor.objects.all()

    if request.method == "POST":
        compra.proveedor_id = request.POST["id_proveedor"]
        compra.fecha_compra = request.POST["fecha_compra"]
        compra.total = request.POST["total"]
        compra.save()
        return redirect("compras_lista")

    return render(request, "compras/editar.html",
                  {"compra": compra, "proveedores": proveedores})


def compras_detalle(request, id):
    compra = get_object_or_404(Compra, id_compra=id)
    detalles = DetalleCompra.objects.filter(compra_id=id)
    return render(request, "compras/detalle.html", {"compra": compra, "detalles": detalles})


def compras_eliminar(request, id):
    compra = get_object_or_404(Compra, id_compra=id)
    compra.delete()
    return redirect("compras_lista")


# ======================================================
#  DETALLE DE COMPRA
# ======================================================

def detalle_compra_lista(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra)
    detalles = DetalleCompra.objects.filter(compra_id=id_compra)
    productos = Producto.objects.all()

    return render(request, "detalle_compra/lista.html",
                  {"compra": compra, "detalles": detalles, "productos": productos})


def detalle_compra_agregar(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra)
    productos = Producto.objects.all()

    if request.method == "POST":
        DetalleCompra.objects.create(
            compra_id=id_compra,
            producto_id=request.POST["id_producto"],
            cantidad=request.POST["cantidad"],
            costo_unitario=request.POST["costo_unitario"]
        )
        return redirect(reverse("detalle_compra_lista", args=[id_compra]))

    return render(request, "detalle_compra/agregar.html",
                  {"compra": compra, "productos": productos})


def detalle_compra_editar(request, id_detalle_compra):
    detalle = get_object_or_404(DetalleCompra, id_detalle_compra=id_detalle_compra)
    productos = Producto.objects.all()

    if request.method == "POST":
        detalle.producto_id = request.POST["id_producto"]
        detalle.cantidad = request.POST["cantidad"]
        detalle.costo_unitario = request.POST["costo_unitario"]
        detalle.save()

        return redirect(reverse("detalle_compra_lista", args=[detalle.compra_id]))

    return render(request, "detalle_compra/editar.html",
                  {"detalle": detalle, "productos": productos})


def detalle_compra_eliminar(request, id_detalle_compra):
    detalle = get_object_or_404(DetalleCompra, id_detalle_compra=id_detalle_compra)
    compra_id = detalle.compra_id
    detalle.delete()
    return redirect(reverse("detalle_compra_lista", args=[compra_id]))


# ======================================================
#  PAGOS
# ======================================================

def pagos_lista(request):
    pagos = Pago.objects.select_related("venta").all()
    return render(request, "pagos/lista.html", {"pagos": pagos})


def pagos_crear(request):
    ventas = Venta.objects.all()

    if request.method == "POST":
        Pago.objects.create(
            venta_id=request.POST["id_venta"],
            fecha_pago=request.POST["fecha_pago"],
            monto=request.POST["monto"],
            metodo_pago=request.POST.get("metodo_pago")
        )
        return redirect("pagos_lista")

    return render(request, "pagos/crear.html", {"ventas": ventas})


def pagos_editar(request, id):
    pago = get_object_or_404(Pago, id_pago=id)
    ventas = Venta.objects.all()

    if request.method == "POST":
        pago.venta_id = request.POST["id_venta"]
        pago.fecha_pago = request.POST["fecha_pago"]
        pago.monto = request.POST["monto"]
        pago.metodo_pago = request.POST.get("metodo_pago")
        pago.save()
        return redirect("pagos_lista")

    return render(request, "pagos/editar.html", {"pago": pago, "ventas": ventas})


def pagos_detalle(request, id):
    pago = get_object_or_404(Pago, id_pago=id)
    return render(request, "pagos/detalle.html", {"pago": pago})


def pagos_eliminar(request, id):
    pago = get_object_or_404(Pago, id_pago=id)
    pago.delete()
    return redirect("pagos_lista")


# ======================================================
#  ENVIOS
# ======================================================

def envios_lista(request):
    envios = Envio.objects.select_related("venta", "empleado").all()
    return render(request, "envios/lista.html", {"envios": envios})


def envios_crear(request):
    ventas = Venta.objects.all()
    empleados = Empleado.objects.all()

    if request.method == "POST":
        Envio.objects.create(
            venta_id=request.POST["id_venta"],
            empleado_id=request.POST["id_empleado"],
            direccion_envio=request.POST.get("direccion_envio"),
            fecha_envio=request.POST.get("fecha_envio"),
            estado_envio=request.POST.get("estado_envio"),
        )
        return redirect("envios_lista")

    return render(request, "envios/crear.html",
                  {"ventas": ventas, "empleados": empleados})


def envios_editar(request, id):
    envio = get_object_or_404(Envio, id_envio=id)
    ventas = Venta.objects.all()
    empleados = Empleado.objects.all()

    if request.method == "POST":
        envio.venta_id = request.POST["id_venta"]
        envio.empleado_id = request.POST["id_empleado"]
        envio.direccion_envio = request.POST.get("direccion_envio")
        envio.fecha_envio = request.POST.get("fecha_envio")
        envio.estado_envio = request.POST.get("estado_envio")
        envio.save()
        return redirect("envios_lista")

    return render(request, "envios/editar.html",
                  {"envio": envio, "ventas": ventas, "empleados": empleados})


def envios_detalle(request, id):
    envio = get_object_or_404(Envio, id_envio=id)
    return render(request, "envios/detalle.html", {"envio": envio})


def envios_eliminar(request, id):
    envio = get_object_or_404(Envio, id_envio=id)
    envio.delete()
    return redirect("envios_lista")
