# Ejercicio 1
cadena = input("Ingrese una cadena de texto: ")
if cadena[0].lower() in 'aeiou':
    print("La primera letra de la primera palabra es una vocal")
else:
    print("La primera letra de la primera palabra no es una vocal")

# Ejercicio 2
numero = int(input("Ingrese un número: "))
if 10 <= abs(numero) <= 99:
    print("El número tiene dos dígitos")
else:
    print("El número no tiene dos dígitos")

# Ejercicio 3
cadena = input("Ingrese una cadena de texto: ")
primera_palabra = cadena.split()[0]
if len(primera_palabra) >= 4:
    print("La primera palabra tiene al menos cuatro letras")
else:
    print("La primera palabra no tiene al menos cuatro letras")

# Ejercicio 4
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
if numero1 % numero2 == 0:
    print("El segundo número es divisor del primero")
else:
    print("El segundo número no es divisor del primero")

# Ejercicio 5
cadena = input("Ingrese una cadena de texto: ")
if cadena.split()[0].startswith("a"):
    print("La primera palabra comienza con la letra 'a'")
else:
    print("La primera palabra no comienza con la letra 'a'")

# Ejercicio 6
numero = int(input("Ingrese un número: "))
if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("El número no es primo")
            break
    else:
        print("El número es primo")
else:
    print("El número no es primo")

# Ejercicio 7
cadena = input("Ingrese una cadena de texto: ")
primera_palabra = cadena.split()[0]
if len(primera_palabra) >= 3 and primera_palabra[2] == 'o':
    print("La primera palabra tiene la letra 'o' en la tercera posición")
else:
    print("La primera palabra no tiene la letra 'o' en la tercera posición")

# Ejercicio 8
numero = int(input("Ingrese un número: "))
if numero > 0 and numero % 2 == 0:
    print("El número es par y mayor que cero")
else:
    print("El número no es par y mayor que cero")

# Ejercicio 9
cadena = input("Ingrese una cadena de texto: ")
primera_palabra = cadena.split()[0]
if any(c.isupper() for c in primera_palabra):
    print("La primera palabra tiene al menos una letra mayúscula")
else:
    print("La primera palabra no tiene ninguna letra mayúscula")

# Ejercicio 10
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
if numero1 > numero2:
    print("El primer número es mayor")
elif numero2 > numero1:
    print("El segundo número es mayor")
else:
    print("Ambos números son iguales")

# Ejercicio 11
cadena = input("Ingrese una cadena de texto: ")
if all('e' in palabra for palabra in cadena.split()):
    print("Todas las palabras contienen la letra 'e'")
else:
    print("No todas las palabras contienen la letra 'e'")

# Ejercicio 12
numero = int(input("Ingrese un número: "))
suma = 0
i = 1
while suma < numero:
    suma += i
    i += 1
if suma == numero:
    print("El número es triangular")
else:
    print("El número no es triangular")

# Ejercicio 13
cadena = input("Ingrese una cadena de texto: ")
if all(len(palabra) > 1 and palabra[1] == 'a' for palabra in cadena.split()):
    print("Todas las palabras tienen la letra 'a' en la segunda posición")
else:
    print("No todas las palabras tienen la letra 'a' en la segunda posición")

# Ejercicio 14
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
if numero1 == 0 and numero2 == 0:
    print("Ambos números son iguales a cero")
else:
    print("Ambos números no son iguales a cero")

# Ejercicio 15
cadena = input("Ingrese una cadena de texto: ")
primera_palabra = cadena.split()[0]
if any(c.islower() for c in primera_palabra):
    print("La primera palabra tiene al menos una letra minúscula")
else:
    print("La primera palabra no tiene ninguna letra minúscula")

# Ejercicio 16
numero = int(input("Ingrese un número: "))
if numero % 3 == 0:
    print("El número es múltiplo de 3")
else:
    print("El número no es múltiplo de 3")

# Ejercicio 17
cadena = input("Ingrese una cadena de texto: ")
primera_palabra = cadena.split()[0]
if primera_palabra.endswith('i'):
    print("La primera palabra tiene la letra 'i' en la última posición")
else:
    print("La primera palabra no tiene la letra 'i' en la última posición")

# Ejercicio 18
numero = int(input("Ingrese un número: "))
suma_digitos = sum(int(digito) for digito in str(numero))
if numero % suma_digitos == 0:
    print("El número es un número de Harshad")
else:
    print("El número no es un número de Harshad")

# Ejercicio 19
cadena = input("Ingrese una cadena de texto: ")
primera_palabra = cadena.split()[0]
if len(primera_palabra) > 1 and primera_palabra[1].isupper():
    print("La primera palabra tiene al menos una letra mayúscula en la segunda posición")
else:
    print("La primera palabra no tiene una letra mayúscula en la segunda posición")

# Ejercicio 20
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
if (numero1 > 0 and numero2 > 0) or (numero1 < 0 and numero2 < 0):
    print("Ambos números son positivos o negativos")
else:
    print("Uno de los números es positivo y el otro es negativo")
