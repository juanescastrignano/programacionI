# Ejercicio 1
dia = int(input("Ingrese un número del 1 al 7 que represente el día de la semana: "))
dias = {1: "Domingo", 2: "Lunes", 3: "Martes", 4: "Miércoles", 5: "Jueves", 6: "Viernes", 7: "Sábado"}
if dia in dias:
    print("El día de la semana es:", dias[dia])
else:
    print("Número inválido, por favor ingrese un número del 1 al 7.")

# Ejercicio 2
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
numeros = [numero1, numero2, numero3]
numeros.sort()
print("Los números ordenados de menor a mayor son:", numeros)

# Ejercicio 3
lado1 = float(input("Ingrese la medida del primer lado del triángulo: "))
lado2 = float(input("Ingrese la medida del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la medida del tercer lado del triángulo: "))
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("El triángulo es escaleno")
else:
    print("El triángulo es isósceles")

# Ejercicio 4
salario = float(input("Ingrese el salario mensual del trabajador: "))
antiguedad = int(input("Ingrese la antigüedad del trabajador en años: "))
if antiguedad < 1:
    plus = salario * 0.05
elif 1 <= antiguedad < 2:
    plus = salario * 0.07
elif 2 <= antiguedad < 5:
    plus = salario * 0.10
elif 5 <= antiguedad < 10:
    plus = salario * 0.15
else:
    plus = salario * 0.20
print("El plus anual del trabajador es:", plus)
