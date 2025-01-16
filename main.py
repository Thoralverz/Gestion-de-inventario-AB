from registro_productos import *
from mover_productos import * 

opc = 0
while opc != 3:
        
        print("\nInventario ACME\n\n1. Registrar productos\n2. Mover productos\n0. Salir\n")
        opc = int(input("Ingrese una opcion > "))
        #time.sleep(2)
        print("\nCargando...\n")

        match opc:

            case 1:
                print("Registre los productos:")
                registrar_productos()

            case 2:
                  print("Que producto desea mover:")
                  mover_productos()

            case 0:
                print("Programa terminado, vuelva pronto")               
                break
            case _:

                print("Selecione una opcion valida!")
        