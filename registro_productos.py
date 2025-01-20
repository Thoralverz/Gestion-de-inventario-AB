from json import *
from datetime import date, datetime 



productos_registrados = []
registrados = {}

def fecha():
    fecha = date.today()
    hora = datetime.now()
    hora_personalizada = hora.strftime("%H:%M")
    hora_actual = f"El producto se actualizo: {fecha} // a la(s): {hora_personalizada}"
    return hora_actual

def registrar_productos():
    global registrados
    codigo = input("\nCodigo del producto > ")
    nombre_producto = input("\nNombre del producto > ")
    provedor = input("\nProvedor > ")
    stock = 0
    
    registrados = {
        "Fecha" : fecha(),
        "Codigo del Producto" : codigo,
        "Nombre del producto" : nombre_producto,
        "Proveedor del producto" : provedor,
        "Cantidad" : stock,
    }
    
    productos_registrados.append(registrados)

    with open("Productos registrados/productos.json", "w") as archivo:
        datos = dumps(productos_registrados, indent=4)
        archivo.write(f"\n{datos}")

        print("\nProducto agregado:\n")

        for llave, valor in registrados.items():
            print(f"{llave} : {valor}")