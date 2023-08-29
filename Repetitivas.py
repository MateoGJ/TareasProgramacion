# Ejercicios Estructuras Repetitivas

# Escribir un programa que realice la sumatoria de los números
suma = 0
numero = int(input("Ingresa un número (-1 para salir): "))
while numero != -1:
    suma += numero
    numero = int(input("Ingresa un número (-1 para salir): "))
print("La sumatoria es:", suma)

# Realizar un algoritmo que pida números
cantidad = int(input("Ingrese la cantidad de números a introducir: "))
mayores = 0
menores = 0
iguales = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print("Números mayores a 0:", mayores)
print("Números menores a 0:", menores)
print("Números iguales a 0:", iguales)

# Algoritmo que pida caracteres e imprima "VOCAL" o "NO VOCAL"
while True:
    caracter = input("Ingresa un caracter (0 para salir): ").lower()
    if caracter == "0":
        break
    elif caracter in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")

# Algoritmo que pida números hasta que se introduzca un cero.
suma = 0
contador = 0

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador != 0:
    media = suma / contador
    print("La suma de los números es:", suma)
    print("La media de los números es:", media)
else:
    print("No se ingresaron números.")