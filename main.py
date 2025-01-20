from registro_productos import *
from productos_en_bodega import * 
from retirar_productos import *
from buscar_producto import *
from historial_producto import *

while True:
        
        print("\nInventario ACME\n\n1. Registrar productos\n2. Mover productos\n3. Retirar productos\n4. Bucar producto\n5. Historial del producto\n0. Salir\n")
        opc = int(input("Ingrese una opcion > "))
        #time.sleep(2)
        print("\nCargando...\n")

        match opc:

            case 1:
                print("Registre los productos:")
                registrar_productos()

            case 2:
                print("En que bodega va a registrar el producto:")
                bodegas()
            
            case 3:
                print("Que producto desea retirar")
                retiros()

            case 4:
                print("Buscar productos")
                buscar()

            case 5:
                  print("Que producto desea ver el historia")
                  historial()
            case 0:
                print("Programa terminado, vuelva pronto")               
                break
             
            case _:
                print("Selecione una opcion valida!")
                