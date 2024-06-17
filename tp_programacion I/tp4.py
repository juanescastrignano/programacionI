def suma_dos_numeros(a, b):
    return a + b

def area_del_circulo(radio):
    return 3.141592653589793 * radio ** 2

def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números."

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def check_temporada(mes):
    if mes in ['Diciembre', 'Enero', 'Febrero']:
        return 'Invierno'
    elif mes in ['Marzo', 'Abril', 'Mayo']:
        return 'Primavera'
    elif mes in ['Junio', 'Julio', 'Agosto']:
        return 'Verano'
    elif mes in ['Septiembre', 'Octubre', 'Noviembre']:
        return 'Otoño'
    else:
        return 'Mes inválido'

def calcular_pendiente(x1, y1, x2, y2):
    if x1 == x2:
        return "Pendiente indefinida (división por cero)."
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No tiene soluciones reales"

def print_list(lst):
    for item in lst:
        print(item)

def lista_inversa(lst):
    return lst[::-1]

def capitalize_list_items(lst):
    return [item.upper() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(1, n + 1))

def suma_de_impares(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

def suma_de_pares(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_perimetro_cuadrado(lado):
    return 4 * lado

def calcular_area_circulo(radio):
    return 3.141592653589793 * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * 3.141592653589793 * radio
