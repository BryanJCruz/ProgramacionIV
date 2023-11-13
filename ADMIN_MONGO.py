import time
from pymongo import MongoClient

# Conectar a la base de datos MongoDB
client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sgc"]

# Colecciones
proveedores = db["proveedores"]
productos = db["productos"]
distribuidores = db["distribuidores"]



# obtiene ID
def obtener_siguiente_id():
    # Encuentra el último _id en la colección y agrega 1
    ultimo_distribuidor = distribuidores.find_one(sort=[("_id", -1)])
    if ultimo_distribuidor:
        siguiente_id = ultimo_distribuidor["_id"] + 1
    else:
        siguiente_id = 1  # Si la colección está vacía, inicia en 1
    return siguiente_id
def obtener_siguiente_id_proveedor():
    # Encuentra el último _id en la colección y agrega 1
    ultimo_proveedor = proveedores.find_one(sort=[("_id", -1)])
    if ultimo_proveedor:
        siguiente_id = ultimo_proveedor["_id"] + 1
    else:
        siguiente_id = 1  # Si la colección está vacía, inicia en 1
    return siguiente_id
def obtener_siguiente_id_producto():
    # Encuentra el último _id en la colección y agrega 1
    ultimo_producto = productos.find_one(sort=[("_id", -1)])
    if ultimo_producto:
        siguiente_id = ultimo_producto["_id"] + 1
    else:
        siguiente_id = 1  # Si la colección está vacía, inicia en 1
    return siguiente_id
# FUNCIONES PARA AGREGAR  A BDD
def agregar_distribuidor(name, ubicacion, clasificacion):
    _id = obtener_siguiente_id()
    nuevo_distribuidor = {
        "_id": _id,
        "name": name,
        "ubicacion": ubicacion,
        "clasificacion": clasificacion
    }
    distribuidores.insert_one(nuevo_distribuidor)
    print("Distribuidor agregado con éxito.")

def agregar_proveedor(name, ubicacion, clasificacion):
    _id = obtener_siguiente_id_proveedor()
    nuevo_proveedor = {
        "_id": _id,
        "name": name,
        "ubicacion": ubicacion,
        "clasificacion": clasificacion
    }
    proveedores.insert_one(nuevo_proveedor)
    print("Proveedor agregado con éxito.")
def agregar_producto(name, tipo, cantidad):
    _id = obtener_siguiente_id_producto()
    nuevo_producto = {
        "_id": _id,
        "name": name,
        "tipo": tipo,
        "cantidad": cantidad
    }
    productos.insert_one(nuevo_producto)
    print("Producto agregado con éxito.")
    
# Eliminar

# FUNCIONES PARA ELIMINAR DE LA BDD
def eliminar_distribuidor(distribuidor_id):
    result = distribuidores.delete_one({"_id": distribuidor_id})
    if result.deleted_count > 0:
        print(f"Distribuidor con ID {distribuidor_id} eliminado con éxito.")
    else:
        print(f"No se encontró un distribuidor con ID {distribuidor_id}.")

def eliminar_proveedor(proveedor_id):
    result = proveedores.delete_one({"_id": proveedor_id})
    if result.deleted_count > 0:
        print(f"Proveedor con ID {proveedor_id} eliminado con éxito.")
    else:
        print(f"No se encontró un proveedor con ID {proveedor_id}.")

def eliminar_producto(producto_id):
    result = productos.delete_one({"_id": producto_id})
    if result.deleted_count > 0:
        print(f"Producto con ID {producto_id} eliminado con éxito.")
    else:
        print(f"No se encontró un producto con ID {producto_id}.")


#MENU
while True:
    print("\n====SGC=====")
    print("1. Eliminar")
    print("2. Crear")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Salir")
    print("0. Crear Base de Datos")
    print("999. PANICO")

    try:
        opcion = int(input("\nOpcion: "))
    except:
        opcion = 1000

    if opcion == 1:
        print("\t\tEliminar")
        print("\n 1- Eliminar Proveedor \n 2- Eliminar Producto \n 3- Eliminar Distribuidor ")
        try:
            op=int(input("Seleccion : "))
        except:
            op = 0
        if op == 0 :
            print("opcion no disponible..")
            pass
        elif op == 1:
            id=int(input("Ingrese la ID del Proveedor : "))
            print("Eliminando...")
            time.sleep(1)
            eliminar_proveedor(id)
        elif op == 2:
            id=int(input("Ingrese la ID del Producto : "))
            print("Eliminando...")
            time.sleep(1)
            eliminar_producto(id)
        elif op == 3:
            id=int(input("Ingrese la ID del Distribuidor : "))
            print("Eliminando...")
            time.sleep(1)
            eliminar_distribuidor(id)
    elif opcion == 2:
        print("\n\t\t CREAR")
        while True:
            print("\n1. Crear producto")
            print("2. Crear proveedor")
            print("3. Crear distribuidor")
            print("4. Regresar al menú principal")
            try:
                opcion = int(input("\nOpcion: "))
            except:
                opcion = 0
            if opcion == 1:
                print("Crear Producto")
                nombre = input("Nombre del Producto: ")
                tipo = input("Tipo de Producto : ")
                cantidad = int(input("Cantidad : "))
                agregar_producto(nombre, tipo, cantidad)
            elif opcion == 2:
                print("Crear proveedor")
                nombre = input("Nombre del distribuidor: ")
                ubicacion = input("Ubicación del distribuidor: ")
                clasificacion = input("Clasificación del distribuidor: ")
                agregar_proveedor(nombre, ubicacion, clasificacion)
            elif opcion == 3:
                nombre = input("Nombre del distribuidor: ")
                ubicacion = input("Ubicación del distribuidor: ")
                clasificacion = input("Clasificación del distribuidor: ")
                agregar_distribuidor(nombre, ubicacion, clasificacion)
            elif opcion == 4:
                print("Regresando al menú principal...")
                time.sleep(2)
                break
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        break
    elif opcion == 0:
        pass
    elif opcion == 999:
        print("PANICO")

