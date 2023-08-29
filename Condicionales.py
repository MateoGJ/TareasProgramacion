# Ejercicios Estructuras Condicionales

# Pedirle al usuario que ingrese un número
numero = int(input("Ingresa un número: "))
if numero == 10:
    print("¡Usted ha ganado el sorteo!")
elif numero < 10:
    print("¡Faltó un poco, sigue participando!")
else:
    print("¡Te pasaste, sigue participando!")

# Pedirle al usuario que ingrese un día de la semana
dia = input("Ingresa un día de la semana: ").lower()
if dia == "lunes":
    print("Hoy es lunes, ánimo!")
elif dia == "viernes":
    print("¡Por fin es viernes!")
elif dia == "sabado" or dia == "domingo":
    print("Es fin de semana, disfruta!")
elif dia == "martes" or dia == "miercoles" or dia == "jueves":
    print("Vas a mitad de semana, ¡a trabajar!")
else:
    print("No es un dia que reconozca")

# Escribir un programa que solicite al usuario una letra
letra = input("Ingresa una letra: ").lower()
if letra in 'aeiou':
    print("Es vocal")
else:
    print("Es una consonante")