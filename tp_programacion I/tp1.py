# Ejercicio 1
nombre = input("Ingrese su nombre: ")
print(nombre)

# Ejercicio 2
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# Ejercicio 3
numero = float(input("Ingrese un número: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")

# Ejercicio 4
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
if numero1 > numero2:
    print("El primer número es mayor")
elif numero2 > numero1:
    print("El segundo número es mayor")
else:
    print("Ambos números son iguales")

# Ejercicio 5
cadena = input("Ingrese una cadena de texto: ")
print("Longitud de la cadena:", len(cadena))

# Ejercicio 6
cadena = input("Ingrese una cadena de texto: ")
if "a" in cadena:
    print("La cadena contiene la letra 'a'")
else:
    print("La cadena no contiene la letra 'a'")

# Ejercicio 7
cadena = input("Ingrese una cadena de texto: ")
if cadena.startswith("h"):
    print("La cadena comienza con la letra 'h'")
else:
    print("La cadena no comienza con la letra 'h'")

# Ejercicio 8
cadena = input("Ingrese una cadena de texto: ")
if cadena == cadena[::-1]:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")

# Ejercicio 9
cadena = input("Ingrese una cadena de texto: ")
print(cadena.upper())

# Ejercicio 10
cadena = input("Ingrese una cadena de texto: ")
print(cadena.lower())
