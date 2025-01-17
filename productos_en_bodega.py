from registro_productos import *
from json import *
from csv import reader, writer, DictReader, DictWriter

def mover_productos():
    producto_mover = input("Codigo del producto: ")

    for producto in productos_registrados:
        if producto["Codigo del Producto"] == producto_mover:
            cantidad = float(input("Ingrese la cantidad de productos nuevos: "))
            producto["Cantidad"] += cantidad
            print(f"Producto agregado con exito! \nProducto actualizado: {producto["Nombre del producto"]}")

            with open(f"Productos registrados/productos.json", "w") as archivo:
                dump(productos_registrados, archivo, indent=4)  
            
            movimientos = [
                ["Movimiento exitoso : Producto agregado" ],
                [f"hora : {fecha()}"]
                [f"Codigo : {producto_mover}" ],
                [f"cantidad : {cantidad}" ],
                
            ]
                
            archivo = open(f"Productos registrados/ Movimientos{producto_mover}.csv", "a")

            with archivo:
                archivo = writer(archivo)
                archivo.writerows(movimientos)
            
        else:
            print("El producto no esta registrado...")