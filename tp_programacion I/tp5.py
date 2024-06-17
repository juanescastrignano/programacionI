import csv
import json
import datetime
import re

# Ejercicio 1: 
def registrar_error():
    tipo_error = input("Ingrese el tipo de error: ")
    descripcion = input("Ingrese una descripción detallada del error: ")
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("errores.txt", "a") as file:
        file.write(f"{fecha_hora} | {tipo_error} | {descripcion}\n")
    
    print("Error registrado correctamente.")

# Ejercicio 2: 
def analizar_ventas():
    ventas = {}
    
    with open("ventas.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            producto, cantidad, precio = row
            cantidad = int(cantidad)
            precio = float(precio)
            
            if producto not in ventas:
                ventas[producto] = {"cantidad": 0, "total_precio": 0}
            
            ventas[producto]["cantidad"] += cantidad
            ventas[producto]["total_precio"] += cantidad * precio
    
    producto_mayor_ventas = max(ventas, key=lambda k: ventas[k]["cantidad"])
    producto_mayor_precio_promedio = max(ventas, key=lambda k: ventas[k]["total_precio"] / ventas[k]["cantidad"])
    
    for producto, datos in ventas.items():
        print(f"{producto}: {datos['cantidad']} unidades, ${datos['total_precio']:.2f}")
    
    print(f"Producto con mayor cantidad de ventas: {producto_mayor_ventas}")
    print(f"Producto con mayor precio promedio de venta: {producto_mayor_precio_promedio}")

# Ejercicio 3: 
def actualizar_inventario():
    codigo_producto = input("Ingrese el código de producto: ")
    nueva_cantidad = input("Ingrese la nueva cantidad en inventario: ")
    
    inventario_actualizado = []
    encontrado = False
    
    with open("inventario.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == codigo_producto:
                row[2] = nueva_cantidad
                encontrado = True
            inventario_actualizado.append(row)
    
    if encontrado:
        with open("inventario.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(inventario_actualizado)
        print("Inventario actualizado correctamente.")
    else:
        print("Producto no encontrado.")

# Ejercicio 4: 
def generar_informe_gastos():
    gastos = {}
    registros = []

    with open("gastos.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            fecha, categoria, monto = row
            monto = float(monto)
            registros.append((fecha, categoria, monto))
            
            if categoria not in gastos:
                gastos[categoria] = 0
            gastos[categoria] += monto

    with open("informe_gastos.html", "w") as file:
        file.write("<html><body><h1>Informe de Gastos</h1>")
        file.write("<table border='1'><tr><th>Fecha</th><th>Categoría</th><th>Monto</th></tr>")
        for registro in registros:
            file.write(f"<tr><td>{registro[0]}</td><td>{registro[1]}</td><td>{registro[2]:.2f}</td></tr>")
        file.write("</table>")
        file.write("<h2>Total de Gastos por Categoría</h2>")
        for categoria, total in gastos.items():
            file.write(f"<p>{categoria}: ${total:.2f}</p>")
        file.write("</body></html>")

# Ejercicio 5: 
def registrar_usuario():
    nombre_completo = input("Ingrese su nombre completo: ")
    if not nombre_completo:
        print("El nombre completo no puede estar vacío.")
        return
    
    correo = input("Ingrese su correo electrónico: ")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        print("El correo electrónico no tiene un formato válido.")
        return

    contraseña = input("Ingrese su contraseña: ")
    if not (len(contraseña) >= 8 and 
            re.search(r"[a-z]", contraseña) and 
            re.search(r"[A-Z]", contraseña) and 
            re.search(r"\d", contraseña) and 
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña)):
        print("La contraseña debe tener al menos 8 caracteres, incluyendo una letra minúscula, una letra mayúscula, un número y un símbolo especial.")
        return

    usuario = {
        "nombre_completo": nombre_completo,
        "correo": correo,
        "contraseña": contraseña
    }

    try:
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        usuarios = []

    usuarios.append(usuario)

    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)

    print("Usuario registrado correctamente.")

# Ejercicio 6: 
def convertir_monedas():
    tipos_de_cambio = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 110.0,
        "GBP": 0.75
    }
    
    cantidad = float(input("Ingrese la cantidad a convertir: "))
    moneda_origen = input("Ingrese la moneda de origen (USD, EUR, JPY, GBP): ")
    moneda_destino = input("Ingrese la moneda de destino (USD, EUR, JPY, GBP): ")
    
    if moneda_origen in tipos_de_cambio and moneda_destino in tipos_de_cambio:
        cantidad_convertida = cantidad * (tipos_de_cambio[moneda_destino] / tipos_de_cambio[moneda_origen])
        print(f"{cantidad} {moneda_origen} son {cantidad_convertida:.2f} {moneda_destino}")
    else:
        print("Moneda no soportada.")

# Ejercicio 7: 
def simulacion_cajero():
    cuenta = {
        "numero": "12345678",
        "pin": "1234",
        "saldo": 1000.0
    }
    
    numero_cuenta = input("Ingrese su número de cuenta: ")
    pin = input("Ingrese su PIN: ")
    
    if numero_cuenta == cuenta["numero"] and pin == cuenta["pin"]:
        print(f"Saldo actual: ${cuenta['saldo']:.2f}")
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro <= cuenta["saldo"]:
            cuenta["saldo"] -= retiro
            print(f"Retiro exitoso. Saldo restante: ${cuenta['saldo']:.2f}")
        else:
            print("Saldo insuficiente.")
    else:
        print("Número de cuenta o PIN incorrectos.")

# Funciones 
def main():
    while True:
        print("Seleccione una opción:")
        print("1. Registro de Errores en Archivo")
        print("2. Análisis de Estadísticas de Ventas")
        print("3. Actualización de Inventario")
        print("4. Generación de Informe de Gastos")
        print("5. Validación de Datos de Usuarios")
        print("6. Conversión de Monedas")
        print("7. Simulación de Cajero Automático")
        print("0. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            registrar_error()
        elif opcion == "2":
            analizar_ventas()
        elif opcion == "3":
            actualizar_inventario()
        elif opcion == "4":
            generar_informe_gastos()
        elif opcion == "5":
            registrar_usuario()
        elif opcion == "6":
            convertir_monedas()
        elif opcion == "7":
            simulacion_cajero()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
