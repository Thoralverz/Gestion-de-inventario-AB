from registro_productos import *
from productos_en_bodega import *
from retirar_productos import *


def buscar():

    producto_buscar = input("DIgite el codigo del producto que desea buscar: ")

    for producto in productos_registrados:
        if producto["Codigo del Producto"] == producto_buscar:
            print(productos_registrados)
        else:
            print("Producto no regitrado")

