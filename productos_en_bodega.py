from registro_productos import *
from json import *
from csv import reader, writer, DictReader, DictWriter

centro =[] 
norte =[]
oriente =[]

def bodegas():
        
        while True:
            
            print("\nBodegas\n1. Bodega norte\n2. Bodega centro\n3. Bodega oriente\n4. Salir")
            opc = int(input("\nIngrese una opción:\n "))
            print("\ncargando...\n")
            
            match opc:
                case 1:
                    print("Mover producto a bodega")
                    mover_productos("norte")
                case 2: 
                    print("Mover producto a bodega")
                    mover_productos("centro")
                case 3:
                    print("Mover producto a bodega")
                    mover_productos("oriente")
                case 4:
                    print("Programa terminado...")
                    break
                case _:
                    print("Seleccione una opcion valida..")

def mover_productos(tipo):

    producto_mover = input("Codigo del producto: ")
    for producto in productos_registrados:
        if producto["Codigo del Producto"] == producto_mover:
            cantidad = float(input("Ingrese la cantidad de productos nuevos: "))
            producto["Cantidad"] += cantidad
            print(f"Producto agregado con exito! \nProducto actualizado: {producto["Nombre del producto"]}")

            with open(f"Productos registrados/productos.json", "w") as archivo:
                dump(productos_registrados, archivo, indent=4)
            
            movimientos = [
                ["Movimiento exitoso : Producto agregado"],
                [f"Codigo : {producto_mover}"],
                [f"cantidad : {cantidad}"],
                [f"bodega : {tipo}"],
                [f"hora : {fecha()}"],
                ["///////////////////////////////////////"],
            ]
                    
            archivo = open(f"Movimientos registrados/ Movimientos{producto_mover}.csv", "a")
            with archivo:
                archivo = writer(archivo)
                archivo.writerows(movimientos)
            

        else:
            print("El producto no esta registrado...")