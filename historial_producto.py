from registro_productos import *
from productos_en_bodega import *
from retirar_productos import *


def historial():

    producto_historial = input("codigo del producto que desea revisar el historial")

    for producto in productos_registrados:
        if producto["Codigo del Producto"] == producto_historial:
            archivos_leidos = open(f"Movimientos registrados/Movimientos{producto_historial}.csv", "r")
            print("TUS MOVIMIENTOS")
            print(archivos_leidos.read())