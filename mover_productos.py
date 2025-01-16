from registro_productos import *
from datetime import date, datetime

   
def fecha():
    fecha = date.today()
    hora = datetime.now()
    hora_personalizada = hora.strftime("%H:%M")
    hora_actual = f"El producto se agrego: {fecha} // a la(s): {hora_personalizada}"
    return hora_actual

def mover_productos():
 
    codigo = input("\nCodigo del producto > ")
    
    if codigo in productos_registrados:
        cantidad = float(input("\nCuantos productos llegaron > "))
        productos_registrados[codigo]["Cantidad"] += cantidad
        bodega = input(print(f"\nA que bodega desea mover el producto\n1. Norte\n2. Centro\n3. Oriente"))
        print(f"\nProducto actualizado con exito: \n")

    productos_registrados[codigo] = codigo
    
    with open("Productos registrados/bodega norte.json", "w") as codigo:
        datos = dumps(codigo)
        codigo.write(f"\n{datos}")
        codigo.close()

        print("\nProducto agregado:\n")

    for llave, valor in registrar_productos.items():
            print(f"{llave}: {valor}")
    
