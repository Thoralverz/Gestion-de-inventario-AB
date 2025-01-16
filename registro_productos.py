from json import *
from datetime import date, datetime 



productos_registrados = {}

def fecha():
    fecha = date.today()
    hora = datetime.now()
    hora_personalizada = hora.strftime("%H:%M")
    hora_actual = f"El producto se agrego: {fecha} // a la(s): {hora_personalizada}"
    return hora_actual

def registrar_productos():
 

    codigo = input("\nCodigo del producto > ")
    nombre_producto = input("\nNombre del producto > ")
    provedor = input("\nProvedor > ")
    saldo = 0

    registrados = {
        "Fecha" : fecha(),
        "Codigo del Producto" : codigo,
        "Nombre del producto" : nombre_producto,
        "Provedor del producto" : provedor,
        "Cantidad" : saldo
    }
    
    productos_registrados[codigo] = registrados

    with open("Productos registrados/productos.json", "a") as archivo:
        datos = dumps(registrados)
        archivo.write(f"\n{datos}")
        archivo.close()

        print("\nProducto agregado:\n")

        for llave, valor in registrados.items():
            print(f"{llave}: {valor}")
    