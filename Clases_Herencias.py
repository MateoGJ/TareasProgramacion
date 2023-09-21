from enum import Enum

class Curso:
    def __init__(self, id_curso, categoria, fecha_de_comienzo, titulo, descripcion, 
                 objetivos, programa, costo, duracion_en_meses, foto, estado="disponible"):
        self.id_curso = id_curso
        self.categoria = categoria
        self.fecha_de_comienzo = fecha_de_comienzo
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracion_en_meses = duracion_en_meses
        self.foto = foto
        self.estado = estado

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase:
    def __init__(self, fecha, titulo, contenido, URLDrive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.URLDrive = URLDrive

class Usuario:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, 
                 codigo_postal, provincia, telefono_celular, email, estado="Activo"):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.estado = estado

class UsuarioFinal(Usuario):
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, 
                 codigo_postal, provincia, telefono_celular, email, nombre_usuario, contrasena):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, 
                 codigo_postal, provincia, telefono_celular, email)
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

class Docente(Usuario):
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, 
                 codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, 
                 codigo_postal, provincia, telefono_celular, email)
        self.clases_asignadas = []

class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

class Rol:
    def __init__(self, nombre):
        self.nombre = nombre

class MedioPago:
    def __init__(self, nombre):
        self.nombre = nombre

class TarjetaDebito(MedioPago):
    def __init__(self, nombre, numero, fecha_vencimiento):
        super().__init__(nombre)
        self.numero = numero
        self.fecha_vencimiento = fecha_vencimiento

class Transferencia(MedioPago):
    def __init__(self, nombre, datos_bancarios):
        super().__init__(nombre)
        self.datos_bancarios = datos_bancarios

class TarjetaCredito(MedioPago):
    def __init__(self, nombre, numero, fecha_vencimiento, codigo_seguridad):
        super().__init__(nombre)
        self.numero = numero
        self.fecha_vencimiento = fecha_vencimiento
        self.codigo_seguridad = codigo_seguridad

class Compra:
    def __init__(self, id_compra, id_carrito_compra, id_medios_pago, id_usuario, fecha, monto_total):
        self.id_compra = id_compra
        self.id_carrito_compra = id_carrito_compra
        self.id_medios_pago = id_medios_pago
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto_total = monto_total

class MedioContacto:
    def __init__(self, id_medio_contacto, fecha, email, telefono, direccion, nombre):
        self.id_medio_contacto = id_medio_contacto
        self.fecha = fecha
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.nombre = nombre

class TiposMedioContacto(MedioContacto, Enum):
    WhatsApp = 1
    CorreoElectronico = 2
    CallCenter = 3
    ReferidoInterno = 4

