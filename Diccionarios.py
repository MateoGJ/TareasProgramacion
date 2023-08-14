import random

# -------------------------------------------------- Ejercicio Diccionarios -------------------------------------------------

# Crear diccionario con DNI como claves y nombres como valores
familia_diccionario = {
    "123456784": "Padre",
    "234567894": "Madre",
    "345678905": "Hermano",
    "456789015": "Hermana"
}

# Añadir datos de familia ampliada
familia_diccionario.update({
    "567890124": "Abuelo",
    "678901234": "Abuela",
    "789014366": "Tia",
    "423012345": "Tio"
})

# Crear diccionario con claves autogeneradas y números de teléfono
telefonos = {}

# Generar claves aleatorias y asignar números de teléfono
for _ in range(3):
    clave = str(random.randint(10000000, 99999999))
    telefono = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    telefonos[clave] = telefono

# Mostrar el diccionario de teléfonos
print("Diccionario de Teléfonos:", telefonos)