from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, db_column='id_categoria')
    nombre_categoria = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Categorias'

    def __str__(self):
        return self.nombre_categoria


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True, db_column='id_proveedor')
    nombre_empresa = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'Proveedores'

    def __str__(self):
        return self.nombre_empresa


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True, db_column='id_empleado')
    nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=40, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2,
                                  null=True, blank=True)

    class Meta:
        db_table = 'Empleados'

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, db_column='id_cliente')
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True)
    ciudad = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'Clientes'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, db_column='id_producto')
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    # FK a Categorias(id_categoria) ON DELETE SET NULL
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        db_column='id_categoria',
        null=True,
        blank=True,
        related_name='productos'
    )

    # FK a Proveedores(id_proveedor) ON DELETE SET NULL
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.SET_NULL,
        db_column='id_proveedor',
        null=True,
        blank=True,
        related_name='productos'
    )

    class Meta:
        db_table = 'Productos'

    def __str__(self):
        return self.nombre_producto


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True, db_column='id_venta')

    # FK Clientes(id_cliente) ON DELETE CASCADE
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        db_column='id_cliente',
        related_name='ventas'
    )

    # FK Empleados(id_empleado) ON DELETE SET NULL
    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        db_column='id_empleado',
        null=True,
        blank=True,
        related_name='ventas'
    )

    fecha_venta = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Ventas'

    def __str__(self):
        return f"Venta #{self.id_venta} - {self.cliente.nombre}"


class DetalleVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True, db_column='id_detalle')

    # FK Ventas(id_venta) ON DELETE CASCADE
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        db_column='id_venta',
        related_name='detalles'
    )

    # FK Productos(id_producto) ON DELETE SET NULL
    producto = models.ForeignKey(
        Producto,
        on_delete=models.SET_NULL,
        db_column='id_producto',
        null=True,
        blank=True,
        related_name='detalles_venta'
    )

    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    # Campo generado en BD: subtotal = cantidad * precio_unitario
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )

    class Meta:
        db_table = 'Detalle_Venta'

    def __str__(self):
        return f"Detalle #{self.id_detalle} - Venta #{self.venta.id_venta}"


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True, db_column='id_compra')

    # FK Proveedores(id_proveedor) ON DELETE CASCADE
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        db_column='id_proveedor',
        related_name='compras'
    )

    fecha_compra = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Compras'

    def __str__(self):
        return f"Compra #{self.id_compra} - {self.proveedor.nombre_empresa}"


class DetalleCompra(models.Model):
    id_detalle_compra = models.AutoField(
        primary_key=True,
        db_column='id_detalle_compra'
    )

    # FK Compras(id_compra) ON DELETE CASCADE
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        db_column='id_compra',
        related_name='detalles'
    )

    # FK Productos(id_producto) ON DELETE SET NULL
    producto = models.ForeignKey(
        Producto,
        on_delete=models.SET_NULL,
        db_column='id_producto',
        null=True,
        blank=True,
        related_name='detalles_compra'
    )

    cantidad = models.IntegerField()
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    # Campo generado en BD: subtotal = cantidad * costo_unitario
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )

    class Meta:
        db_table = 'Detalle_Compra'

    def __str__(self):
        return f"Det.Compra #{self.id_detalle_compra} - Compra #{self.compra.id_compra}"


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True, db_column='id_pago')

    # FK Ventas(id_venta) ON DELETE CASCADE
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        db_column='id_venta',
        related_name='pagos'
    )

    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'Pagos'

    def __str__(self):
        return f"Pago #{self.id_pago} - Venta #{self.venta.id_venta}"


class Envio(models.Model):
    id_envio = models.AutoField(primary_key=True, db_column='id_envio')

    # FK Ventas(id_venta) ON DELETE CASCADE
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        db_column='id_venta',
        related_name='envios'
    )

    # FK Empleados(id_empleado) ON DELETE SET NULL
    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        db_column='id_empleado',
        null=True,
        blank=True,
        related_name='envios'
    )

    direccion_envio = models.CharField(max_length=100, null=True, blank=True)
    fecha_envio = models.DateField(null=True, blank=True)
    estado_envio = models.CharField(max_length=20, default='Pendiente')

    class Meta:
        db_table = 'Envios'

    def __str__(self):
        return f"Envío #{self.id_envio} - Venta #{self.venta.id_venta}"
