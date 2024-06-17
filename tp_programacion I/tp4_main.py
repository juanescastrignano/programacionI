from funciones import (
    suma_dos_numeros, area_del_circulo, add_all_nums,
    convert_celsius_to_fahrenheit, check_temporada, calcular_pendiente,
    solve_quadratic_eqn, print_list, lista_inversa, capitalize_list_items,
    add_item, remove_item, sum_of_numbers, suma_de_impares, suma_de_pares,
    calcular_area_cuadrado, calcular_perimetro_cuadrado, calcular_area_circulo,
    calcular_perimetro_circulo
)

# Ejercicio 1
resultado = suma_dos_numeros(3, 5)
print("La suma de los dos números es:", resultado)

# Ejercicio 2
radio = 5
area = area_del_circulo(radio)
print("El área del círculo es:", area)

# Ejercicio 3
resultado = add_all_nums(1, 2, 3, 4)
print("La suma de todos los números es:", resultado)
resultado_no_valido = add_all_nums(1, 'a', 3)
print("Resultado con elemento no numérico:", resultado_no_valido)

# Ejercicio 4
celsius = 30
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print(f"{celsius}°C es igual a {fahrenheit}°F")

# Ejercicio 5
mes = "Marzo"
estacion = check_temporada(mes)
print("La estación del año es:", estacion)

# Ejercicio 6
x1, y1 = 1, 2
x2, y2 = 3, 4
pendiente = calcular_pendiente(x1, y1, x2, y2)
print("La pendiente de la línea es:", pendiente)

# Ejercicio 7
a, b, c = 1, -3, 2
soluciones = solve_quadratic_eqn(a, b, c)
print("Las soluciones de la ecuación cuadrática son:", soluciones)

# Ejercicio 8
lista = [1, 2, 3, 4, 5]
print_list(lista)

# Ejercicio 9
lista = [1, 2, 3, 4, 5]
print("Lista inversa:", lista_inversa(lista))

# Ejercicio 10
lista = ["hola", "mundo"]
print("Lista en mayúsculas:", capitalize_list_items(lista))

# Ejercicio 11
food_staff = ['Papa', 'Tomate', 'Mango', 'Yogurt']
print("Lista actualizada:", add_item(food_staff, 'Carne'))

# Ejercicio 12
food_staff = ['Papa', 'Tomate', 'Mango', 'Yogurt']
print("Lista actualizada:", remove_item(food_staff, 'Mango'))

# Ejercicio 13
print("Suma de números hasta 5:", sum_of_numbers(5))

# Ejercicio 14
print("Suma de impares hasta 5:", suma_de_impares(5))

# Ejercicio 15
print("Suma de pares hasta 5:", suma_de_pares(5))

# Cálculo de figuras geométricas
# Cálculo para un cuadrado
lado_cuadrado = 5
area_cuadrado = calcular_area_cuadrado(lado_cuadrado)
perimetro_cuadrado = calcular_perimetro_cuadrado(lado_cuadrado)
print(f"Área del cuadrado: {area_cuadrado:.2f}")
print(f"Perímetro del cuadrado: {perimetro_cuadrado:.2f}")

# Cálculo para un círculo
radio_circulo = 3
area_circulo = calcular_area_circulo(radio_circulo)
perimetro_circulo = calcular_perimetro_circulo(radio_circulo)
print(f"Área del círculo: {area_circulo:.2f}")
print(f"Perímetro del círculo: {perimetro_circulo:.2f}")
