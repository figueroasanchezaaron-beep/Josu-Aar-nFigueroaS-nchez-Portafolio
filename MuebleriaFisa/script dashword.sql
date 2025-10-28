-- ======================================================
-- BASE DE DATOS: Mueblería FISA
-- Estructura de PostgreSQL
-- ======================================================


-- ======================================================
-- TABLA: Categorías
-- ======================================================
CREATE TABLE Categorías (
    id_categoria SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(40) NOT NULL,
    descripcion TEXT
);

-- ======================================================
-- TABLA: Proveedores
-- ======================================================
CREATE TABLE Proveedores (
    id_proveedor SERIAL PRIMARY KEY,
    nombre_empresa VARCHAR(50) NOT NULL,
    contacto VARCHAR(50),
    telefono VARCHAR(20),
    correo VARCHAR(50),
    direccion VARCHAR(100),
    ciudad VARCHAR(30)
);

-- ======================================================
-- TABLA: Empleados
-- ======================================================
CREATE TABLE Empleados (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    puesto VARCHAR(40),
    telefono VARCHAR(20),
    direccion VARCHAR(100),
    fecha_contratacion DATE,
    salario DECIMAL(10,2)
);

-- ======================================================
-- TABLA: Clientes
-- ======================================================
CREATE TABLE Clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(50),
    ciudad VARCHAR(30)
);

-- ======================================================
-- TABLA: Productos
-- ======================================================
CREATE TABLE Productos (
    id_producto SERIAL PRIMARY KEY,
    nombre_producto VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100),
    precio DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    id_categoria INT,
    id_proveedor INT,
    FOREIGN KEY (id_categoria) REFERENCES Categorías(id_categoria) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor) ON UPDATE CASCADE ON DELETE SET NULL
);

-- ======================================================
-- TABLA: Ventas
-- ======================================================
CREATE TABLE Ventas (
    id_venta SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_empleado INT NOT NULL,
    fecha_venta DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado) ON UPDATE CASCADE ON DELETE SET NULL
);

-- ======================================================
-- TABLA: Detalle_Venta
-- ======================================================
CREATE TABLE Detalle_Venta (
    id_detalle SERIAL PRIMARY KEY,
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto) ON UPDATE CASCADE ON DELETE SET NULL
);

-- ======================================================
-- TABLA: Compras
-- ======================================================
CREATE TABLE Compras (
    id_compra SERIAL PRIMARY KEY,
    id_proveedor INT NOT NULL,
    fecha_compra DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor) ON UPDATE CASCADE ON DELETE CASCADE
);

-- ======================================================
-- TABLA: Detalle_Compra
-- ======================================================
CREATE TABLE Detalle_Compra (
    id_detalle_compra SERIAL PRIMARY KEY,
    id_compra INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    costo_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) GENERATED ALWAYS AS (cantidad * costo_unitario) STORED,
    FOREIGN KEY (id_compra) REFERENCES Compras(id_compra) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto) ON UPDATE CASCADE ON DELETE SET NULL
);

-- ======================================================
-- TABLA: Pagos
-- ======================================================
CREATE TABLE Pagos (
    id_pago SERIAL PRIMARY KEY,
    id_venta INT NOT NULL,
    fecha_pago DATE NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    metodo_pago VARCHAR(20),
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta) ON UPDATE CASCADE ON DELETE CASCADE
);

-- ======================================================
-- TABLA: Envíos
-- ======================================================
CREATE TABLE Envíos (
    id_envio SERIAL PRIMARY KEY,
    id_venta INT NOT NULL,
    id_empleado INT NOT NULL,
    direccion_envio VARCHAR(100),
    fecha_envio DATE,
    estado_envio VARCHAR(20) DEFAULT 'Pendiente',
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado) ON UPDATE CASCADE ON DELETE SET NULL
);

-- ======================================================

-- ======================================================
-- INSERTAR 30 CLIENTES
-- ======================================================
INSERT INTO Clientes (nombre, direccion, telefono, correo, ciudad) VALUES
('Juan Pérez','Calle 1, Col. Centro','5551001000','juanperez@gmail.com','Ciudad A'),
('María López','Av. 2, Col. Norte','5551001001','marialopez@gmail.com','Ciudad B'),
('Carlos García','Calle 3, Col. Sur','5551001002','carlosgarcia@gmail.com','Ciudad A'),
('Ana Torres','Av. 4, Col. Centro','5551001003','anatorres@gmail.com','Ciudad C'),
('Luis Martínez','Calle 5, Col. Norte','5551001004','luismartinez@gmail.com','Ciudad B'),
('Sofía Hernández','Av. 6, Col. Sur','5551001005','sofiahernandez@gmail.com','Ciudad A'),
('Miguel Ramírez','Calle 7, Col. Centro','5551001006','miguelramirez@gmail.com','Ciudad C'),
('Paola Sánchez','Av. 8, Col. Norte','5551001007','paolasanchez@gmail.com','Ciudad B'),
('Fernando Díaz','Calle 9, Col. Sur','5551001008','fernandodiaz@gmail.com','Ciudad A'),
('Laura Gómez','Av. 10, Col. Centro','5551001009','lauragomez@gmail.com','Ciudad C'),
('Ricardo Morales','Calle 11, Col. Norte','5551001010','ricardomorales@gmail.com','Ciudad B'),
('Patricia Ruiz','Av. 12, Col. Sur','5551001011','patriciaruiz@gmail.com','Ciudad A'),
('Jorge Castillo','Calle 13, Col. Centro','5551001012','jorgecastillo@gmail.com','Ciudad C'),
('Mónica Vega','Av. 14, Col. Norte','5551001013','monicavega@gmail.com','Ciudad B'),
('Andrés Rojas','Calle 15, Col. Sur','5551001014','andresrojas@gmail.com','Ciudad A'),
('Verónica Jiménez','Av. 16, Col. Centro','5551001015','veronicajimenez@gmail.com','Ciudad C'),
('Diego Ortega','Calle 17, Col. Norte','5551001016','diegoortega@gmail.com','Ciudad B'),
('Carolina Molina','Av. 18, Col. Sur','5551001017','carolinamolina@gmail.com','Ciudad A'),
('Héctor Cruz','Calle 19, Col. Centro','5551001018','hectorcruz@gmail.com','Ciudad C'),
('Gabriela Torres','Av. 20, Col. Norte','5551001019','gabrielatorres@gmail.com','Ciudad B'),
('Santiago Flores','Calle 21, Col. Sur','5551001020','santiagoflores@gmail.com','Ciudad A'),
('Natalia Ruiz','Av. 22, Col. Centro','5551001021','natalia.ruiz@gmail.com','Ciudad C'),
('Julián Navarro','Calle 23, Col. Norte','5551001022','julian.navarro@gmail.com','Ciudad B'),
('Isabel Vargas','Av. 24, Col. Sur','5551001023','isabelvargas@gmail.com','Ciudad A'),
('Antonio Herrera','Calle 25, Col. Centro','5551001024','antonioherrera@gmail.com','Ciudad C'),
('Lucía Peña','Av. 26, Col. Norte','5551001025','luciapena@gmail.com','Ciudad B'),
('Ricardo Torres','Calle 27, Col. Sur','5551001026','ricardotorres@gmail.com','Ciudad A'),
('Daniela Soto','Av. 28, Col. Centro','5551001027','danielasoto@gmail.com','Ciudad C'),
('Emilio Campos','Calle 29, Col. Norte','5551001028','emiliocampos@gmail.com','Ciudad B'),
('Valeria Paredes','Av. 30, Col. Sur','5551001029','valeriaparedes@gmail.com','Ciudad A');

-- ======================================
-- INSERTAR 30 EMPLEADOS
-- ======================================
INSERT INTO Empleados (nombre, puesto, telefono, direccion, fecha_contratacion, salario) VALUES
('Luis Fernández','Vendedor','5552001000','Calle 1, Col. Centro','2022-01-10',12000.00),
('Ana Martínez','Vendedor','5552001001','Av. 2, Col. Norte','2021-05-15',11500.00),
('Carlos Gómez','Vendedor','5552001002','Calle 3, Col. Sur','2020-08-20',13000.00),
('Sofía Ramírez','Gerente','5552001003','Av. 4, Col. Centro','2019-03-12',20000.00),
('Miguel Torres','Vendedor','5552001004','Calle 5, Col. Norte','2022-06-01',12500.00),
('Laura Hernández','Vendedor','5552001005','Av. 6, Col. Sur','2021-11-05',11800.00),
('Jorge López','Vendedor','5552001006','Calle 7, Col. Centro','2020-12-22',12700.00),
('Paola Jiménez','Administrativo','5552001007','Av. 8, Col. Norte','2018-07-30',15000.00),
('Fernando Díaz','Vendedor','5552001008','Calle 9, Col. Sur','2022-03-18',12300.00),
('Verónica Ruiz','Vendedor','5552001009','Av. 10, Col. Centro','2021-09-09',11900.00),
('Ricardo Navarro','Vendedor','5552001010','Calle 11, Col. Norte','2020-05-05',12500.00),
('Isabel Castro','Vendedor','5552001011','Av. 12, Col. Sur','2019-10-20',12200.00),
('Diego Vega','Vendedor','5552001012','Calle 13, Col. Centro','2022-08-15',12100.00),
('Natalia Herrera','Vendedor','5552001013','Av. 14, Col. Norte','2021-01-10',11850.00),
('Andrés Morales','Vendedor','5552001014','Calle 15, Col. Sur','2020-02-25',12400.00),
('Mónica Peña','Vendedor','5552001015','Av. 16, Col. Centro','2019-06-12',11950.00),
('Santiago Soto','Vendedor','5552001016','Calle 17, Col. Norte','2022-09-01',12350.00),
('Paula Campos','Vendedor','5552001017','Av. 18, Col. Sur','2021-04-20',12050.00),
('Héctor Vargas','Vendedor','5552001018','Calle 19, Col. Centro','2020-11-18',12500.00),
('Gabriela Torres','Vendedor','5552001019','Av. 20, Col. Norte','2019-12-05',12150.00),
('Ricardo Flores','Vendedor','5552001020','Calle 21, Col. Sur','2022-07-07',12200.00),
('Daniela Molina','Vendedor','5552001021','Av. 22, Col. Centro','2021-02-02',12000.00),
('Emilio Rojas','Vendedor','5552001022','Calle 23, Col. Norte','2020-08-30',12450.00),
('Valeria Jiménez','Vendedor','5552001023','Av. 24, Col. Sur','2019-09-15',12300.00),
('Julián Ortega','Vendedor','5552001024','Calle 25, Col. Centro','2022-01-25',12100.00),
('Lucía Ramírez','Vendedor','5552001025','Av. 26, Col. Norte','2021-06-12',11950.00),
('Antonio Peña','Vendedor','5552001026','Calle 27, Col. Sur','2020-10-10',12400.00),
('Isabel Soto','Vendedor','5552001027','Av. 28, Col. Centro','2019-05-05',12250.00),
('Diego Campos','Vendedor','5552001028','Calle 29, Col. Norte','2022-03-03',12300.00),
('Verónica Morales','Vendedor','5552001029','Av. 30, Col. Sur','2021-07-07',12150.00);

-- ======================================
-- INSERTAR 30 CATEGORÍAS
-- ======================================
INSERT INTO Categorías (nombre_categoria, descripcion) VALUES
('Sala','Muebles para sala como sofás, sillones y mesas'),
('Comedor','Muebles para comedor, incluyendo mesas y sillas'),
('Recámara','Muebles para dormitorio, como camas y closets'),
('Oficina','Muebles de oficina como escritorios y sillas'),
('Exterior','Muebles para jardín y terraza'),
('Infantil','Muebles para habitaciones de niños'),
('Decoración','Accesorios y decoración del hogar'),
('Almacenamiento','Closets, libreros y estanterías'),
('Cocina','Muebles y accesorios de cocina'),
('Baño','Muebles y accesorios para baño'),
('Sofás','Sofás de diferentes tamaños y estilos'),
('Sillas','Sillas de comedor y oficina'),
('Mesas','Mesas para sala, comedor y oficina'),
('Camas','Camas individuales, matrimoniales y king'),
('Closets','Closets y guardarropas'),
('Estanterías','Muebles para almacenar objetos'),
('Escritorios','Escritorios para oficina o estudio'),
('Sillones','Sillones reclinables y de descanso'),
('Accesorios','Lámparas, cuadros y decoración'),
('Jardín','Muebles y accesorios de exterior'),
('Mueble TV','Muebles para televisión y entretenimiento'),
('Buffet','Buffets y aparadores'),
('Repisas','Repisas decorativas y funcionales'),
('Sillas Oficina','Sillas ergonómicas de oficina'),
('Mesas Café','Mesas pequeñas para sala'),
('Cunas','Cunas y muebles infantiles'),
('Sillas Niños','Sillas para niños'),
('Mesas Niños','Mesas para niños'),
('Zapateros','Muebles para guardar calzado'),
('Vitrinas','Vitrinas y exhibidores');

-- ======================================
-- INSERTAR 30 PROVEEDORES
-- ======================================
INSERT INTO Proveedores (nombre_empresa, contacto, telefono, correo, direccion, ciudad) VALUES
('Muebles Modernos','Carlos Vega','5553001000','carlosvega@proveedor.com','Calle 1, Ciudad A','Ciudad A'),
('Hogar Feliz','Ana Morales','5553001001','anam@proveedor.com','Av. 2, Ciudad B','Ciudad B'),
('DecorArte','Luis Pérez','5553001002','luisp@proveedor.com','Calle 3, Ciudad C','Ciudad C'),
('Muebles Express','María Torres','5553001003','mariatorres@proveedor.com','Av. 4, Ciudad A','Ciudad A'),
('Confort Muebles','Jorge Sánchez','5553001004','jorges@proveedor.com','Calle 5, Ciudad B','Ciudad B'),
('Estilo y Hogar','Paola Ruiz','5553001005','paolaruiz@proveedor.com','Av. 6, Ciudad C','Ciudad C'),
('Muebles Plus','Ricardo Díaz','5553001006','ricardod@proveedor.com','Calle 7, Ciudad A','Ciudad A'),
('Ambiente Hogareño','Laura Gómez','5553001007','laurag@proveedor.com','Av. 8, Ciudad B','Ciudad B'),
('Casa Ideal','Diego Ramírez','5553001008','diegor@proveedor.com','Calle 9, Ciudad C','Ciudad C'),
('Decoración Total','Sofía Torres','5553001009','sofiat@proveedor.com','Av. 10, Ciudad A','Ciudad A'),
('Muebles ABC','Miguel López','5553001010','miguell@proveedor.com','Calle 11, Ciudad B','Ciudad B'),
('Hogar Contemporáneo','Valeria Pérez','5553001011','valeriap@proveedor.com','Av. 12, Ciudad C','Ciudad C'),
('Muebles Elite','Fernando Díaz','5553001012','fernandod@proveedor.com','Calle 13, Ciudad A','Ciudad A'),
('Decoraciones Modernas','Natalia Gómez','5553001013','nataliag@proveedor.com','Av. 14, Ciudad B','Ciudad B'),
('Confort Plus','Héctor Morales','5553001014','hectorm@proveedor.com','Calle 15, Ciudad C','Ciudad C'),
('Muebles y Diseño','Carolina Ruiz','5553001015','carolinar@proveedor.com','Av. 16, Ciudad A','Ciudad A'),
('Ambientes Únicos','Julián Herrera','5553001016','julianh@proveedor.com','Calle 17, Ciudad B','Ciudad B'),
('Decor Hogareño','Isabel Castro','5553001017','isabelc@proveedor.com','Av. 18, Ciudad C','Ciudad C'),
('Estilo Confort','Diego Flores','5553001018','diegof@proveedor.com','Calle 19, Ciudad A','Ciudad A'),
('Muebles Integrales','Paula Torres','5553001019','paulat@proveedor.com','Av. 20, Ciudad B','Ciudad B'),
('DecorArte Plus','Emilio Pérez','5553001020','emiliop@proveedor.com','Calle 21, Ciudad C','Ciudad C'),
('Casa Moderna','Lucía Rojas','5553001021','luciar@proveedor.com','Av. 22, Ciudad A','Ciudad A'),
('Muebles y Más','Antonio Jiménez','5553001022','antonioj@proveedor.com','Calle 23, Ciudad B','Ciudad B'),
('Hogar y Estilo','Gabriela Soto','5553001023','gabrielas@proveedor.com','Av. 24, Ciudad C','Ciudad C'),
('Muebles Total','Ricardo Molina','5553001024','ricardom@proveedor.com','Calle 25, Ciudad A','Ciudad A'),
('Decoración y Confort','Natalia Torres','5553001025','nataliat@proveedor.com','Av. 26, Ciudad B','Ciudad B'),
('Ambientes Modernos','Andrés Ramírez','5553001026','andresr@proveedor.com','Calle 27, Ciudad C','Ciudad C'),
('Muebles Contempo','Verónica Díaz','5553001027','veronicad@proveedor.com','Av. 28, Ciudad A','Ciudad A'),
('Estilo y Confort','Diego Herrera','5553001028','diegoh@proveedor.com','Calle 29, Ciudad B','Ciudad B'),
('Decor Hogar','Sofía Morales','5553001029','sofiam@proveedor.com','Av. 30, Ciudad C','Ciudad C');

-- ======================================
-- INSERTAR 30 PRODUCTOS
-- ======================================
INSERT INTO Productos (nombre_producto, descripcion, precio, stock, id_categoria, id_proveedor) VALUES
('Sofá Moderno','Sofá de 3 plazas color gris',8000.00,10,1,1),
('Mesa de Comedor','Mesa de madera para 6 personas',4500.00,15,2,2),
('Cama Matrimonial','Cama con cabecera de madera',7000.00,12,3,3),
('Escritorio Oficina','Escritorio de madera con cajones',3000.00,20,4,4),
('Silla de Oficina','Silla ergonómica giratoria',1500.00,25,4,5),
('Sillón Reclinable','Sillón reclinable color marrón',5000.00,8,1,6),
('Mesa de Centro','Mesa pequeña de sala',1200.00,30,13,7),
('Closet 3 Puertas','Closet de madera blanca',6000.00,10,15,8),
('Cuna Infantil','Cuna para bebé con barandillas',3500.00,15,26,9),
('Sofá Cama','Sofá cama doble funcional',7500.00,5,11,10),
('Mesa Café','Mesa pequeña de madera',800.00,20,25,11),
('Librero Estantes','Estantería de madera',2500.00,12,16,12),
('Cama Individual','Cama individual con colchón',4500.00,10,14,13),
('Silla Comedor','Silla de comedor color negro',600.00,30,12,14),
('Buffet Sala','Buffet de madera para sala',3000.00,8,22,15),
('Vitrina Cristal','Vitrina de madera y cristal',4000.00,7,30,16),
('Escritorio Estudio','Escritorio de estudio compacto',2200.00,15,17,17),
('Sillón Lounge','Sillón lounge moderno',4800.00,10,18,18),
('Mesa Cocina','Mesa pequeña para cocina',1000.00,25,9,19),
('Estantería Oficina','Estantería metálica para oficina',2000.00,20,16,20),
('Cama King Size','Cama king size con cabecera',9000.00,5,14,21),
('Silla Niños','Silla infantil de madera',400.00,30,27,22),
('Mesa Niños','Mesa infantil de madera',700.00,20,28,23),
('Zapatero','Mueble para calzado',1500.00,15,29,24),
('Lámpara Decorativa','Lámpara moderna de pie',1200.00,25,19,25),
('Sofá 2 Plazas','Sofá de 2 plazas color beige',7000.00,8,11,26),
('Mesa Redonda','Mesa redonda para comedor',3500.00,10,2,27),
('Cama Infantil','Cama para niños color blanco',4000.00,12,26,28),
('Silla Oficina Ergónomica','Silla ergonómica negra',1800.00,20,24,29),
('Escritorio Ejecutivo','Escritorio ejecutivo de madera',5000.00,7,17,30);

-- ======================================
-- INSERTAR 30 VENTAS
-- ======================================
INSERT INTO Ventas (id_cliente, id_empleado, fecha_venta, total) VALUES
(1,1,'2025-01-05',8000.00),
(2,2,'2025-01-06',4500.00),
(3,3,'2025-01-07',7000.00),
(4,4,'2025-01-08',3000.00),
(5,5,'2025-01-09',1500.00),
(6,6,'2025-01-10',5000.00),
(7,7,'2025-01-11',1200.00),
(8,8,'2025-01-12',6000.00),
(9,9,'2025-01-13',3500.00),
(10,10,'2025-01-14',7500.00),
(11,11,'2025-01-15',800.00),
(12,12,'2025-01-16',2500.00),
(13,13,'2025-01-17',4500.00),
(14,14,'2025-01-18',600.00),
(15,15,'2025-01-19',3000.00),
(16,16,'2025-01-20',4000.00),
(17,17,'2025-01-21',2200.00),
(18,18,'2025-01-22',4800.00),
(19,19,'2025-01-23',1000.00),
(20,20,'2025-01-24',2000.00),
(21,21,'2025-01-25',9000.00),
(22,22,'2025-01-26',400.00),
(23,23,'2025-01-27',700.00),
(24,24,'2025-01-28',1500.00),
(25,25,'2025-01-29',1200.00),
(26,26,'2025-01-30',7000.00),
(27,27,'2025-01-31',3500.00),
(28,28,'2025-02-01',4000.00),
(29,29,'2025-02-02',1800.00),
(30,30,'2025-02-03',5000.00);

-- ======================================
-- INSERTAR 30 DETALLE_VENTA
-- ======================================
INSERT INTO Detalle_Venta (id_venta, id_producto, cantidad, precio_unitario) VALUES
(1,1,1,8000.00),(2,2,1,4500.00),(3,3,1,7000.00),(4,4,1,3000.00),(5,5,1,1500.00),
(6,6,1,5000.00),(7,7,1,1200.00),(8,8,1,6000.00),(9,9,1,3500.00),(10,10,1,7500.00),
(11,11,1,800.00),(12,12,1,2500.00),(13,13,1,4500.00),(14,14,1,600.00),(15,15,1,3000.00),
(16,16,1,4000.00),(17,17,1,2200.00),(18,18,1,4800.00),(19,19,1,1000.00),(20,20,1,2000.00),
(21,21,1,9000.00),(22,22,1,400.00),(23,23,1,700.00),(24,24,1,1500.00),(25,25,1,1200.00),
(26,26,1,7000.00),(27,27,1,3500.00),(28,28,1,4000.00),(29,29,1,1800.00),(30,30,1,5000.00);

-- ======================================
-- INSERTAR 30 COMPRAS
-- ======================================
INSERT INTO Compras (id_proveedor, fecha_compra, total) VALUES
(1,'2025-01-02',50000.00),(2,'2025-01-03',60000.00),(3,'2025-01-04',45000.00),(4,'2025-01-05',30000.00),
(5,'2025-01-06',20000.00),(6,'2025-01-07',40000.00),(7,'2025-01-08',35000.00),(8,'2025-01-09',42000.00),
(9,'2025-01-10',37000.00),(10,'2025-01-11',50000.00),(11,'2025-01-12',25000.00),(12,'2025-01-13',33000.00),
(13,'2025-01-14',48000.00),(14,'2025-01-15',27000.00),(15,'2025-01-16',36000.00),(16,'2025-01-17',45000.00),
(17,'2025-01-18',22000.00),(18,'2025-01-19',39000.00),(19,'2025-01-20',41000.00),(20,'2025-01-21',30000.00),
(21,'2025-01-22',55000.00),(22,'2025-01-23',38000.00),(23,'2025-01-24',34000.00),(24,'2025-01-25',37000.00),
(25,'2025-01-26',29000.00),(26,'2025-01-27',46000.00),(27,'2025-01-28',42000.00),(28,'2025-01-29',35000.00),
(29,'2025-01-30',31000.00),(30,'2025-01-31',40000.00);

-- ======================================
-- INSERTAR 30 DETALLE_COMPRA
-- ======================================
INSERT INTO Detalle_Compra (id_compra, id_producto, cantidad, costo_unitario) VALUES
(1,1,5,7000.00),(2,2,10,4000.00),(3,3,6,6500.00),(4,4,8,2800.00),(5,5,12,1400.00),
(6,6,3,4500.00),(7,7,15,1000.00),(8,8,5,5500.00),(9,9,10,3000.00),(10,10,4,7000.00),
(11,11,12,700.00),(12,12,10,2200.00),(13,13,5,4200.00),(14,14,10,550.00),(15,15,3,2800.00),
(16,16,2,3800.00),(17,17,6,2000.00),(18,18,5,4500.00),(19,19,10,900.00),(20,20,8,1800.00),
(21,21,3,8000.00),(22,22,10,350.00),(23,23,5,650.00),(24,24,4,1200.00),(25,25,7,1000.00),
(26,26,2,6500.00),(27,27,4,3000.00),(28,28,3,3500.00),(29,29,5,1500.00),(30,30,2,4500.00);

-- ======================================
-- INSERTAR 30 PAGOS
-- ======================================
INSERT INTO Pagos (id_venta, fecha_pago, monto, metodo_pago) VALUES
(1,'2025-01-06',8000.00,'Tarjeta'),
(2,'2025-01-07',4500.00,'Efectivo'),
(3,'2025-01-08',7000.00,'Transferencia'),
(4,'2025-01-09',3000.00,'Efectivo'),
(5,'2025-01-10',1500.00,'Tarjeta'),
(6,'2025-01-11',5000.00,'Efectivo'),
(7,'2025-01-12',1200.00,'Transferencia'),
(8,'2025-01-13',6000.00,'Tarjeta'),
(9,'2025-01-14',3500.00,'Efectivo'),
(10,'2025-01-15',7500.00,'Tarjeta'),
(11,'2025-01-16',800.00,'Efectivo'),
(12,'2025-01-17',2500.00,'Transferencia'),
(13,'2025-01-18',4500.00,'Tarjeta'),
(14,'2025-01-19',600.00,'Efectivo'),
(15,'2025-01-20',3000.00,'Tarjeta'),
(16,'2025-01-21',4000.00,'Efectivo'),
(17,'2025-01-22',2200.00,'Transferencia'),
(18,'2025-01-23',4800.00,'Tarjeta'),
(19,'2025-01-24',1000.00,'Efectivo'),
(20,'2025-01-25',2000.00,'Tarjeta'),
(21,'2025-01-26',9000.00,'Transferencia'),
(22,'2025-01-27',400.00,'Efectivo'),
(23,'2025-01-28',700.00,'Tarjeta'),
(24,'2025-01-29',1500.00,'Efectivo'),
(25,'2025-01-30',1200.00,'Tarjeta'),
(26,'2025-01-31',7000.00,'Transferencia'),
(27,'2025-02-01',3500.00,'Efectivo'),
(28,'2025-02-02',4000.00,'Tarjeta'),
(29,'2025-02-03',1800.00,'Efectivo'),
(30,'2025-02-04',5000.00,'Transferencia');

-- ======================================
-- INSERTAR 30 ENVÍOS
-- ======================================
INSERT INTO Envíos (id_venta, id_empleado, direccion_envio, fecha_envio, estado_envio) VALUES
(1,1,'Calle 1, Col. Centro','2025-01-06','Entregado'),
(2,2,'Av. 2, Col. Norte','2025-01-07','Entregado'),
(3,3,'Calle 3, Col. Sur','2025-01-08','Entregado'),
(4,4,'Av. 4, Col. Centro','2025-01-09','Entregado'),
(5,5,'Calle 5, Col. Norte','2025-01-10','Pendiente'),
(6,6,'Av. 6, Col. Sur','2025-01-11','En camino'),
(7,7,'Calle 7, Col. Centro','2025-01-12','Entregado'),
(8,8,'Av. 8, Col. Norte','2025-01-13','Pendiente'),
(9,9,'Calle 9, Col. Sur','2025-01-14','En camino'),
(10,10,'Av. 10, Col. Centro','2025-01-15','Entregado'),
(11,11,'Calle 11, Col. Norte','2025-01-16','Entregado'),
(12,12,'Av. 12, Col. Sur','2025-01-17','Pendiente'),
(13,13,'Calle 13, Col. Centro','2025-01-18','En camino'),
(14,14,'Av. 14, Col. Norte','2025-01-19','Entregado'),
(15,15,'Calle 15, Col. Sur','2025-01-20','Entregado'),
(16,16,'Av. 16, Col. Centro','2025-01-21','Pendiente'),
(17,17,'Calle 17, Col. Norte','2025-01-22','En camino'),
(18,18,'Av. 18, Col. Sur','2025-01-23','Entregado'),
(19,19,'Calle 19, Col. Centro','2025-01-24','Pendiente'),
(20,20,'Av. 20, Col. Norte','2025-01-25','Entregado'),
(21,21,'Calle 21, Col. Sur','2025-01-26','En camino'),
(22,22,'Av. 22, Col. Centro','2025-01-27','Pendiente'),
(23,23,'Calle 23, Col. Norte','2025-01-28','Entregado'),
(24,24,'Av. 24, Col. Sur','2025-01-29','En camino'),
(25,25,'Calle 25, Col. Centro','2025-01-30','Pendiente'),
(26,26,'Av. 26, Col. Norte','2025-01-31','Entregado'),
(27,27,'Calle 27, Col. Sur','2025-02-01','En camino'),
(28,28,'Av. 28, Col. Centro','2025-02-02','Pendiente'),
(29,29,'Calle 29, Col. Norte','2025-02-03','Entregado'),
(30,30,'Av. 30, Col. Sur','2025-02-04','En camino');


SELECT *FROM Clientes

SELECT 
    SUM(od.cantidad * od.precio_unitario) AS Ingresos_Netos,
    AVG(T.Valor_Neto_Order) AS Valor_promedio_orden
FROM Detalle_Venta od
INNER JOIN (
    SELECT id_venta, SUM(cantidad * precio_unitario) AS Valor_Neto_Order
    FROM Detalle_Venta
    GROUP BY id_venta
) T ON od.id_venta = T.id_venta;

SELECT 
    SUM(od.cantidad * od.precio_unitario) AS ingresos_netos_totales,
    AVG(T.Valor_Neto_Order) AS valor_promedio_ordenx
FROM Detalle_Venta od
INNER JOIN (
    SELECT id_venta, SUM(cantidad * precio_unitario) AS Valor_Neto_Order
    FROM Detalle_Venta
    GROUP BY id_venta
) T ON od.id_venta = T.id_venta;


SELECT 
    c.nombre_categoria,
    SUM(dv.cantidad * dv.precio_unitario) AS ingresos_categoria
FROM Detalle_Venta dv
INNER JOIN Productos p ON dv.id_producto = p.id_producto
INNER JOIN Categorías c ON p.id_categoria = c.id_categoria
GROUP BY c.nombre_categoria
ORDER BY ingresos_categoria DESC;

SELECT 
    p.nombre_producto,
    SUM(dv.cantidad) AS unidades_vendidas
FROM Detalle_Venta dv
INNER JOIN Productos p ON dv.id_producto = p.id_producto
GROUP BY p.nombre_producto
ORDER BY unidades_vendidas DESC;

SELECT 
    e.nombre AS empleado,
    SUM(dv.cantidad * dv.precio_unitario) AS ingresos_empleado
FROM Detalle_Venta dv
INNER JOIN Ventas v ON dv.id_venta = v.id_venta
INNER JOIN Empleados e ON v.id_empleado = e.id_empleado
GROUP BY e.nombre
ORDER BY ingresos_empleado DESC;

SELECT 
    nombre_producto,
    stock
FROM Productos
WHERE stock <= 5
ORDER BY stock ASC;

SELECT 
    pr.nombre_empresa AS proveedor,
    SUM(dc.cantidad * dc.costo_unitario) AS total_compras
FROM Detalle_Compra dc
INNER JOIN Compras c ON dc.id_compra = c.id_compra
INNER JOIN Proveedores pr ON c.id_proveedor = pr.id_proveedor
GROUP BY pr.nombre_empresa
ORDER BY total_compras DESC
limit 7;

SELECT 
    e.id_envio,
    e.direccion_envio,
    em.nombre AS empleado,
    e.estado_envio
FROM Envíos e
INNER JOIN Empleados em ON e.id_empleado = em.id_empleado
WHERE e.estado_envio IN ('Pendiente', 'En camino')
ORDER BY e.estado_envio;

SELECT 
    v.id_venta,
    SUM(p.monto) AS pagos_realizados,
    v.total AS total_venta,
    v.total - SUM(p.monto) AS saldo_pendiente
FROM Pagos p
INNER JOIN Ventas v ON p.id_venta = v.id_venta
GROUP BY v.id_venta
ORDER BY saldo_pendiente DESC;

SELECT 
    c.nombre AS cliente,
    COUNT(v.id_venta) AS compras_realizadas
FROM Ventas v
INNER JOIN Clientes c ON v.id_cliente = c.id_cliente
GROUP BY c.nombre
ORDER BY compras_realizadas DESC;

SELECT 
    c.nombre AS cliente,
    SUM(dv.cantidad * dv.precio_unitario) AS ingresos_cliente
FROM Ventas v
INNER JOIN Detalle_Venta dv ON v.id_venta = dv.id_venta
INNER JOIN Clientes c ON v.id_cliente = c.id_cliente
GROUP BY c.nombre
ORDER BY ingresos_cliente DESC;

SELECT 
    cl.ciudad,
    SUM(dv.cantidad * dv.precio_unitario) AS ingresos_ciudad
FROM Detalle_Venta dv
INNER JOIN Ventas v ON dv.id_venta = v.id_venta
INNER JOIN Clientes cl ON v.id_cliente = cl.id_cliente
GROUP BY cl.ciudad
ORDER BY ingresos_ciudad DESC;

SELECT 
    c.nombre_categoria,
    SUM(dv.cantidad * dv.precio_unitario) AS ingresos_categoria
FROM Detalle_Venta dv
INNER JOIN Productos p ON dv.id_producto = p.id_producto
INNER JOIN Categorías c ON p.id_categoria = c.id_categoria
GROUP BY c.nombre_categoria
ORDER BY ingresos_categoria DESC;










