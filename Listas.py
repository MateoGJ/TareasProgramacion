
# -------------------------------------------------- Ejercicios Listas -------------------------------------------------

# Crear listas
familia = ["Leonardo García", "Mariana Juarez", "Baltazar García", "Magdalena García", "Claudio Cinecio", "Cristina Pugliese"]
temperaturas = [25, 26, 27, 28, 28, 27, 26, 25, 24, 23, 22, 21, 20, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 30, 29, 28, 27, 26, 25, 24, 23]
ciudades = ["Nueva Zelanda", "Japón", "Italia", "Estados Unidos"]
eventos = [("2023-01-15", "Cumpleaños"), ("2023-04-22", "Graduación")]

# Ordenar listas
familia.sort()
temperaturas.sort()

# Agregar temperaturas del siguiente mes
temperaturas_siguiente_mes = [24, 25, 26, 26, 27, 28, 28, 27, 26, 25, 24, 23, 22, 21, 20, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 30, 29, 28, 27, 26, 25]
temperaturas.extend(temperaturas_siguiente_mes)

# Quitar abuelos de la lista de familia
familia.remove("Claudio Cinecio")
familia.remove("Cristina Pugliese")

# Quitar ciudad menos linda de la lista de ciudades
ciudades.remove("Italia")

# Mostrar todas las listas
print("Lista de Familia:", familia)
print("Lista de Temperaturas:", temperaturas)
print("Lista de Ciudades:", ciudades)
print("Lista de Eventos:", eventos)

