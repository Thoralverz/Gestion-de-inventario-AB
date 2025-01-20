from registro_productos import *
from productos_en_bodega import*
from json import *
from csv import reader, writer, DictReader, DictWriter

def retiros():

    producto_retirar = input("Codigo del producto: ")

    for producto in productos_registrados:
        if producto["Codigo del Producto"] == producto_retirar:
            cantidad = float(input("Ingrese la cantidad de productos a retirar: "))
            if cantidad > producto["Cantidad"]:
                print("Productos insuficientes, revise los almacenes")
            elif cantidad <= producto["Cantidad"]:
                producto["Cantidad"] -= cantidad
                print(f"Producto fue retirado con exito! \nProducto actualizado: {producto["Nombre del producto"]}")

            with open(f"Productos registrados/productos.json", "w") as archivo:
                dump(productos_registrados, archivo, indent=4)  

            movimientos = [
                ["Movimiento exitoso : Producto rerirado" ],
                [f"Codigo : {producto_retirar}" ],
                [f"cantidad : {cantidad}" ],
                [f"bodega : {mover_productos}"],
                [f"hora : {fecha()}"],
                ["///////////////////////////////////////"]    
            ]

            
            archivo = open(f"Movimientos registrados/ Movimientos{producto_retirar}.csv", "a")
            with archivo:
                archivo = writer(archivo)
                archivo.writerows(movimientos)

        else:
            print("El producto no esta registrado...")