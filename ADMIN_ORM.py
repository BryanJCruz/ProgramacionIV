#Estoy usando 'match case' disponible desde python3.10 en adelante....
import time
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text

DB_URL = "mysql+pymysql://BRYAN:CADETE4507@localhost/sgc"

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# 1:M
class Proveedores(Base):
    __tablename__ = 'PROVEEDORES'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    ubicacion = Column(String(70))
    clasificacion = Column(String(50))

    # Relación con los productos
    productos = relationship("Producto", back_populates="proveedor")

class Producto(Base):
    __tablename__ = 'PRODUCTO'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    tipo = Column(String(50))
    cantidad = Column(Integer)

    # Clave foránea que se relaciona con la tabla Proveedores
    proveedor_id = Column(Integer, ForeignKey('PROVEEDORES.id'))
    # Relación inversa con la tabla Proveedores
    proveedor = relationship("Proveedores", back_populates="productos")

    # Clave foránea que se relaciona con la tabla Distribuidores
    distribuidor_id = Column(Integer, ForeignKey('DISTRIBUIDORES.id'))
    distribuidor = relationship("Distribuidor", back_populates="productos")

class Distribuidor(Base):
    __tablename__ = 'DISTRIBUIDORES'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    ubicacion = Column(String(70))
    clasificacion = Column(String(50))
    # Relación inversa con la tabla Productos
    productos = relationship("Producto", back_populates="distribuidor")
    
def eliminar_base_datos():
    print("¡PANICO! Esta opción eliminará toda la base de datos, incluyendo tablas. ¿Estás seguro?")
    print("1. Sí")
    print("2. No")

    try:
        confirmacion = int(input("Seleccione: "))
    except ValueError:
        confirmacion = 2

    if confirmacion == 1:
        with engine.connect() as connection:
            connection.execute(text("DROP DATABASE sgc"))
        print("¡Base de datos y tablas eliminadas!")
    else:
        print("Cancelando...")
        time.sleep(0.5)

while True:
    print("\n====SGC=====")
    print("1. Eliminar")
    print("2. Crear")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Salir")
    print("0. Crear Base de Datos")
    try:
        opcion = int(input("\nOpcion: "))
    except:
        opcion = 1000

    if opcion == 1:
        print("\t\t\tEliminar")
        print("\n 1- Poveedor")
        print("\n 2- Distribuidor")
        print("\n 3- Producto")
        try:
            option = int(input("\nOpcion: "))
        except:
            option = 0
        match option:
            case 1:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_proveedor = session.query(Proveedores).filter_by(id=identificador).first()

                if selected_proveedor is not None:
                    print("DATOS ALMACENADOS: " + selected_proveedor.name + ", " + str(
                        selected_proveedor.clasificacion) + ", " + str(selected_proveedor.ubicacion))
                    print("\n\t Desea eliminarlo ? ")
                    print("1-SI")
                    print("2-NO")
                    try:
                        op=int(input("Seleccione : "))
                    except:
                        op = 2
                    match op:
                        case 1:
                            session.delete(selected_proveedor)
                            session.commit()
                            print("Proveedor eliminado")
                        case 2:
                            print("Cancelando...")
                            time.sleep(0.5)
                else:
                    print(f"No se encontró un proveedor con el ID : '{identificador}'.")
            case 2:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_distribuidor = session.query(Distribuidor).filter_by(id=identificador).first()

                if selected_distribuidor is not None:
                    print("DATOS ALMACENADOS: " + selected_distribuidor.name + ", " + str(
                        selected_distribuidor.clasificacion) + ", " + str(selected_distribuidor.ubicacion))
                    print("\n\t Desea eliminarlo ? ")
                    print("1-SI")
                    print("2-NO")
                    try:
                        op = int(input("Seleccione : "))
                    except:
                        op = 2
                    match op:
                        case 1:
                            session.delete(selected_distribuidor)
                            session.commit()
                            print("Proveedor eliminado")
                        case 2:
                            print("Cancelando...")
                            time.sleep(0.5)
                else:
                    print(f"No se encontró un Distribuidor con el ID : '{identificador}'.")
            case 3:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_PRODUCT = session.query(Producto).filter_by(id=identificador).first()

                if selected_PRODUCT is not None:
                    print("DATOS ALMACENADOS: " + selected_PRODUCT.name + ", " + str(
                        selected_PRODUCT.tipo) + ", " + str(selected_PRODUCT.cantidad) + ", DIS_ID: " + str(
                        selected_PRODUCT.distribuidor_id) + ", PROV_ID: " + str(selected_PRODUCT.proveedor_id))
                    print("\n\t Desea eliminarlo ? ")
                    print("1-SI")
                    print("2-NO")
                    try:
                        op = int(input("Seleccione : "))
                    except:
                        op = 2
                    match op:
                        case 1:
                            session.delete(selected_PRODUCT)
                            session.commit()
                            print("Proveedor eliminado")
                        case 2:
                            print("Cancelando...")
                            time.sleep(0.5)
                else:
                    print(f"No se encontró un Producto con el ID :  '{identificador}'.")
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
                print("\t\t\tCrear producto")
                nombre = input("Ingrese el nombre del producto : ")
                clase = input("Ingrese el tipo del producto :  ")
                suma = int(input("Ingrese la cantidad del producto : "))
                pro_id = int(input("Ingrese ID del proveedor asignado : "))
                Dis_id = int(input("Ingrese ID del distribuidor asignado : "))
                proveedor_existente = session.query(Proveedores).filter(Proveedores.id == pro_id).first()
                # Verifica si el ID del distribuidor existe en la base de datos
                distribuidor_existente = session.query(Distribuidor).filter(Distribuidor.id == Dis_id).first()

                if proveedor_existente and distribuidor_existente:
                    nuevo_producto = Producto(name=nombre, tipo=clase, cantidad=suma, proveedor_id=pro_id,
                                              distribuidor_id=Dis_id)
                    session.add(nuevo_producto)
                    session.commit()
                else:
                    print("La ID del proveedor o distribuidor no existe en la base de datos")

            elif opcion == 2:
                print("Crear proveedor")
                nombre = input("\n Ingrese el nombre del Proveedor : ")
                lugar = input("Ingrese la ubicación : ")
                tipo = input("Clasificación del producto : ")
                nuevo_proveedor = Proveedores(name=nombre, ubicacion=lugar, clasificacion=tipo)
                session.add(nuevo_proveedor)
                session.commit()
            elif opcion == 3:
                print("Crear distribuidor")
                nombre = input("Ingrese el nombre Del Distribuidor : ")
                lugar = input("Ubicacion : ")
                clase = input("Clasificación o tipo del producto : ")
                nuevo_distribuidor = Distribuidor(name=nombre,ubicacion=lugar,clasificacion=clase)
                session.add(nuevo_distribuidor)
                session.commit()
            elif opcion == 4:
                print("Regresando al menú principal...")
                time.sleep(2)
                break
    elif opcion == 3:
        print("\t\t\tLUPA")
        print("\n 1- Poveedor")
        print("\n 2- Distribuidor")
        print("\n 3- Producto")
        try:
            option = int(input("\nOpcion: "))
        except:
            option = 0
        match option:
            case 1:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_proveedor = session.query(Proveedores).filter_by(id=identificador).first()

                if selected_proveedor is not None:
                    print("DATOS ALMACENADOS: " + selected_proveedor.name + ", " + str(
                        selected_proveedor.clasificacion) + ", " + str(selected_proveedor.ubicacion))
                else:
                    print(f"No se encontró un proveedor con el ID : '{identificador}'.")
            case 2:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_distribuidor = session.query(Distribuidor).filter_by(id=identificador).first()

                if selected_distribuidor is not None:
                    print("DATOS ALMACENADOS: " + selected_distribuidor.name + ", " + str(
                        selected_distribuidor.clasificacion) + ", " + str(selected_distribuidor.ubicacion))
                else:
                    print(f"No se encontró un Distribuidor con el ID : '{identificador}'.")
            case 3:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_PRODUCT = session.query(Producto).filter_by(id=identificador).first()

                if selected_PRODUCT is not None:
                    print("DATOS ALMACENADOS: " + selected_PRODUCT.name + ", " + str(
                        selected_PRODUCT.tipo) + ", " + str(selected_PRODUCT.cantidad) + ", DIS_ID: " + str(
                        selected_PRODUCT.distribuidor_id) + ", PROV_ID: " + str(selected_PRODUCT.proveedor_id))
                else:
                    print(f"No se encontró un Producto con el ID :  '{identificador}'.")

    elif opcion == 4:
        print("\t\t\tActualizar")
        print("\n 1- Poveedor")
        print("\n 2- Distribuidor")
        print("\n 3- Producto")
        try:
            option = int(input("\nOpcion: "))
        except:
            option = 0
        match option:
            case 1:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_proveedor = session.query(Proveedores).filter_by(id=identificador).first()
                if selected_proveedor is not None:
                    print("DATO seleccionado: " + selected_proveedor.name + ", " + str(
                        selected_proveedor.clasificacion) + ", " + str(selected_proveedor.ubicacion))
                    while True:
                        print("DESEA ACTUALIZAR TODO ? ")
                        print("1-SI")
                        print("2-NO")
                        print("0-SALIR")
                        try:
                            opcion = int(input("Selecciones una opcion : "))
                        except:
                            print("Opcion no disponible")
                            time.sleep(0.5)
                            print("Regresando.....")
                            opcion = 0
                        match opcion:
                            case 1:
                                nuevo_nom = input("Ingrese el nuevo nombre : ")
                                nueva_ubi = input("Ingrese la nueva Ubicacion : ")
                                nueva_cla = input("Ingrese la nueva clasificacion : ")
                                selected_proveedor.name = nuevo_nom
                                selected_proveedor.ubicacion = nueva_ubi
                                selected_proveedor.clasificacion = nueva_cla
                                session.commit()
                            case 2:
                                print("\t\t Editar")
                                print(" 1-Nombre")
                                print(" 2-Ubicacion")
                                print(" 3-clasificaion")
                                try:
                                    pop = int(input("Seleccione una opcion : "))
                                except:
                                    pop = 0
                                match pop:
                                    case 1:
                                        nuevo_nom = input("Ingrese el nuevo nombre : ")
                                        selected_proveedor.name = nuevo_nom
                                        session.commit()
                                    case 2:
                                        nueva_ubi = input("Ingrese la nueva Ubicacion : ")
                                        selected_proveedor.ubicacion = nueva_ubi
                                        session.commit()
                                    case 3:
                                        nueva_cla = input("Ingrese la nueva clasificacion : ")
                                        selected_proveedor.clasificacion = nueva_cla
                                        session.commit()
                                    case 0:
                                        print("Regresando....")
                            case 0:
                                break
                else:
                    print(f"No se encontró un proveedor con el ID:  '{identificador}'.")
            case 2:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_distribuidor = session.query(Distribuidor).filter_by(id=identificador).first()
                if selected_distribuidor is not None:
                    print("DATO seleccionado: " + selected_distribuidor.name + ", " + str(
                        selected_distribuidor.clasificacion) + ", " + str(selected_distribuidor.ubicacion))
                    while True:
                        print("DESEA ACTUALIZAR TODO ? ")
                        print("1-SI")
                        print("2-NO")
                        print("0-SALIR")
                        try:
                            opcion = int(input("Selecciones una opcion : "))
                        except:
                            print("Opcion no disponible")
                            time.sleep(0.5)
                            print("Regresando.....")
                            opcion = 0
                        match opcion:
                            case 1:
                                nuevo_nom = input("Ingrese el nuevo nombre : ")
                                nueva_ubi = input("Ingrese la nueva Ubicacion : ")
                                nueva_cla = input("Ingrese la nueva clasificacion : ")
                                selected_distribuidor.name = nuevo_nom
                                selected_distribuidor.ubicacion = nueva_ubi
                                selected_distribuidor.clasificacion = nueva_cla
                                session.commit()
                            case 2:
                                print("\t\t Editar")
                                print(" 1-Nombre")
                                print(" 2-Ubicacion")
                                print(" 3-clasificaion")
                                try:
                                    pop = int(input("Seleccione una opcion : "))
                                except:
                                    pop = 0
                                match pop:
                                    case 1:
                                        nuevo_nom = input("Ingrese el nuevo nombre : ")
                                        selected_distribuidor.name = nuevo_nom
                                        session.commit()
                                    case 2:
                                        nueva_ubi = input("Ingrese la nueva Ubicacion : ")
                                        selected_distribuidor.ubicacion = nueva_ubi
                                        session.commit()
                                    case 3:
                                        nueva_cla = input("Ingrese la nueva clasificacion : ")
                                        selected_distribuidor.clasificacion = nueva_cla
                                        session.commit()
                                    case 0:
                                        print("Regresando....")
                            case 0:
                                break
                else:
                    print(f"No se encontró un Distribuidor con el ID :  '{identificador}'.")
            case 3:
                try:
                    identificador = int(input("Búsqueda por ID : "))
                except:
                    identificador = 0
                selected_PRODUCT = session.query(Producto).filter_by(id=identificador).first()
                if selected_PRODUCT is not None:
                    print("DATO seleccionado: " + selected_PRODUCT.name + ", " + str(
                        selected_PRODUCT.tipo) + ", " + str(selected_PRODUCT.cantidad)+ ", DIS_ID: " + str(selected_PRODUCT.distribuidor_id)+ ", PROV_ID: " + str(selected_PRODUCT.proveedor_id))
                    while True:
                        print("DESEA ACTUALIZAR TODO ? ")
                        print("1-SI")
                        print("2-NO")
                        print("0-SALIR")
                        try:
                            opcion = int(input("Selecciones una opcion : "))
                        except:
                            print("Opcion no disponible")
                            time.sleep(0.5)
                            print("Regresando.....")
                            opcion = 0
                        match opcion:
                            case 1:
                                nuevo_nom = input("Ingrese el nuevo nombre : ")
                                nueva_tip = input("Ingrese la nueva clase o tipo : ")
                                nueva_can = int(input("Ingrese nueva cantidad : "))
                                nueva_proid = int(input("Ingrese la ID Del proveedor encargado : "))
                                nueva_disid = int(input("Ingrese la ID del Disdtribuidor encargado : "))
                                selected_PRODUCT.name = nuevo_nom
                                selected_PRODUCT.tipo = nueva_tip
                                selected_PRODUCT.cantidad = nueva_can
                                selected_PRODUCT.proveedor_id = nueva_proid
                                selected_PRODUCT.distribuidor_id = nueva_disid
                            case 2:
                                print("\t\t Editar")
                                print(" 1-Nombre")
                                print(" 2-Tipo")
                                print(" 3-Cantidad")
                                print(" 4-Proveedor")
                                print(" 5- Distribuidor")
                                print(" 0-SALIR")
                                try:
                                    pop = int(input("Seleccione una opcion : "))
                                except:
                                    pop = 0
                                match pop:
                                    case 1:
                                        nuevo_nom = input("Ingrese el nuevo nombre : ")
                                        selected_PRODUCT.name = nuevo_nom
                                        session.commit()
                                    case 2:
                                        nueva_tip = input("Ingrese la nueva clase o tipo : ")
                                        selected_PRODUCT.tipo = nueva_tip
                                        session.commit()
                                    case 3:
                                        nueva_can = int(input("Ingrese nueva cantidad : "))
                                        selected_PRODUCT.cantidad = nueva_can
                                        session.commit()
                                    case 4:
                                        nueva_proid = int(input("Ingrese la ID Del proveedor encargado : "))
                                        selected_PRODUCT.proveedor_id = nueva_proid
                                    case 5:
                                        nueva_disid = int(input("Ingrese la ID del Disdtribuidor encargado : "))
                                        selected_PRODUCT.distribuidor_id = nueva_disid
                                    case 0:
                                        print("Regresando....")
                            case 0:
                                break
                else:
                    print(f"No se encontró ningun Producto con el ID :  '{identificador}'.")
    elif opcion == 5:
        print("Saliendo")
        time.sleep(2)
        break
    elif opcion == 0:
        Base.metadata.create_all(engine)
 
       
        
        
        
        
        
