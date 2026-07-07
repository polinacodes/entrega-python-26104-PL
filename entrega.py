# from colorama import init, Fore

# init(autoreset=True)

# stock = [
#     {"nombre": "Lapicera Azul", "categoria": "Escritura", "precio": 150},
#     {"nombre": "Cuaderno Rivadavia", "categoria": "Cuadernos", "precio": 850},
#     {"nombre": "Resma A4", "categoria": "Papel", "precio": 3200},
#     {"nombre": "Corrector Líquido", "categoria": "Escritura", "precio": 450},
#     {"nombre": "Regla 30cm", "categoria": "Geometría", "precio": 280},
#     {"nombre": "Goma de Borrar", "categoria": "Escritura", "precio": 120},
#     {"nombre": "Marcadores x12", "categoria": "Arte", "precio": 2100},
#     {"nombre": "Tijera Escolar", "categoria": "Corte", "precio": 650},
#     {"nombre": "Plasticola 250ml", "categoria": "Adhesivos", "precio": 980},
#     {"nombre": "Carpeta 3 Solapas", "categoria": "Organización", "precio": 750}
# ]

# opcion = "0"

# while opcion != "5":

#     print("")
#     print(Fore.MAGENTA + "---Bienvenido al sistema de gestión de productos---")
#     print("")
#     print(Fore.YELLOW + "1. Agregar producto")    
#     print(Fore.YELLOW + "2. Ver productos")
#     print(Fore.YELLOW + "3. Buscar producto")
#     print(Fore.YELLOW + "4. Eliminar producto")
#     print(Fore.YELLOW + "5. Salir")
#     print("")

#     opcion = input(Fore.WHITE + "Elegí una opción para continuar: ")

#     match opcion:
#         case "1":
#             print(Fore.GREEN + "\nAgregar producto")

#             nombre = input(Fore.WHITE + "Ingresa el nombre del producto: ").strip().title()
#             while nombre == "" :
#                 print(Fore.RED + "Error: El nombre es obligatorio.")
#                 nombre = input(Fore.WHITE + "Ingresa el nombre del producto: ").strip().title()

#             categoria = input(Fore.WHITE + "Ingresa la categoría del producto: ").strip().title()
#             while categoria == "" :
#                 print(Fore.RED + "Error: La categoría es obligatoria.")
#                 categoria = input(Fore.WHITE + "Ingresa la categoría del producto: ").strip().title()

#             precio = input(Fore.WHITE + "Ingresa el precio del producto: ").strip()
#             while precio == "" or not precio.isdecimal():
#                 print(Fore.RED + "Error: El precio es obligatorio y debe ser un número entero.")
#                 precio = input(Fore.WHITE + "Ingresa el precio del producto: ").strip()

#             producto = {
#                 "nombre": nombre,
#                 "categoria": categoria,
#                 "precio": int(precio)
#             }
            
#             stock.append(producto)
#             print("")
#             print(Fore.GREEN + "¡Producto agregado con éxito!")

#         case "2":
#             print("")
#             print(Fore.MAGENTA + "Ver productos")
#             print("")
#             for contador, producto in enumerate(stock):
#                 print(Fore.YELLOW + f"Producto # {contador + 1}:")
#                 print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
#                 print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
#                 print(Fore.WHITE + f"  Precio: ${producto['precio']}")
#                 print("")

#         case "3":
#             print(Fore.MAGENTA + "\nBuscar producto")
#             busqueda = input(Fore.WHITE + "Ingresa el nombre del producto a buscar: ").strip().lower()
#             encontrado = False

#             print("")
#             print(Fore.MAGENTA + "Resultados de la búsqueda:")
#             print("")
            
#             for contador, producto in enumerate(stock):
#                 if busqueda in producto["nombre"].lower():
#                     print(Fore.GREEN + "Producto encontrado:")
#                     print("")
#                     print(Fore.YELLOW + f"Producto # {contador + 1}:")
#                     print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
#                     print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
#                     print(Fore.WHITE + f"  Precio: ${producto['precio']}")
#                     encontrado = True
#                     print("")
            
#             if encontrado == False:
#                 print(Fore.RED + "No se encontraron productos con ese nombre")

#         case "4":
#             print(Fore.MAGENTA + "\nEliminar producto")
#             eliminar = input(Fore.WHITE + "Ingresa el numero del producto a eliminar: ").strip()
#             while eliminar == "" or not eliminar.isdecimal():
#                 print(Fore.RED + "Error: El número de producto es obligatorio y debe ser un número entero.")
#                 eliminar = input(Fore.WHITE + "Ingresa el numero del producto a eliminar: ").strip()
#             encontrado = False
#             for contador, producto in enumerate(stock):
#                 if int(eliminar) == contador + 1:
#                     print("")
#                     print(Fore.GREEN + "¡Producto eliminado!")
#                     print("")
#                     print(Fore.YELLOW + f"Producto # {contador + 1}:")
#                     print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
#                     print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
#                     print(Fore.WHITE + f"  Precio: ${producto['precio']}")
#                     encontrado = True
#                     stock.remove(producto)
       
#             if encontrado == False:
#                 print(Fore.RED + "No existe el producto")
#         case "5":
#             print(Fore.MAGENTA + "\n¡Hasta luego!")
#         case _:
#             print(Fore.RED + "Opción no válida")


from colorama import init, Fore

init(autoreset=True)

stock = [
    {"ID": "1", "nombre": "Lapicera Azul", "categoria": "Escritura", "precio": 150, "cantidad": 45},
    {"ID": "2", "nombre": "Cuaderno Rivadavia", "categoria": "Cuadernos", "precio": 850, "cantidad": 12},
    {"ID": "3", "nombre": "Resma A4", "categoria": "Papel", "precio": 3200, "cantidad": 8},
    {"ID": "4", "nombre": "Corrector Líquido", "categoria": "Escritura", "precio": 450, "cantidad": 30},
    {"ID": "5", "nombre": "Regla 30cm", "categoria": "Geometría", "precio": 280, "cantidad": 18},
    {"ID": "6", "nombre": "Goma de Borrar", "categoria": "Escritura", "precio": 120, "cantidad": 60},
    {"ID": "7", "nombre": "Marcadores x12", "categoria": "Arte", "precio": 2100, "cantidad": 5},
    {"ID": "8", "nombre": "Tijera Escolar", "categoria": "Corte", "precio": 650, "cantidad": 22},
    {"ID": "9", "nombre": "Plasticola 250ml", "categoria": "Adhesivos", "precio": 980, "cantidad": 14},
    {"ID": "10", "nombre": "Carpeta 3 Solapas", "categoria": "Organización", "precio": 750, "cantidad": 9}
]

def pedir_texto(texto):
    x = input(Fore.WHITE + f"{texto}: ").strip().title()
    while x == "":
        print(Fore.RED + f"Error: {texto} no puede estar vacío.")
        x = input(Fore.WHITE + f"{texto}: ").strip().title()
    return x

def caratula(texto):
    print("\n")
    print(Fore.MAGENTA + "-----------------------------------------")
    print(Fore.MAGENTA + texto)
    print(Fore.MAGENTA + "-----------------------------------------")

opcion = "0"

while opcion != "7":
    print("")
    print(Fore.MAGENTA + "---Bienvenido al sistema de gestión de productos---")
    print("")
    print(Fore.YELLOW + "1. Agregar producto")
    print(Fore.YELLOW + "2. Ver productos")
    print(Fore.YELLOW + "3. Buscar producto")
    print(Fore.YELLOW + "4. Eliminar producto")
    print(Fore.YELLOW + "5. Actualizar producto")
    print(Fore.YELLOW + "6. Controlar stock bajo")
    print(Fore.YELLOW + "7. Salir")
    print("")
    opcion = input(Fore.WHITE + "Elegí una opción para continuar: ")

    match opcion:
        case "1":
            caratula("Agregar producto nuevo")

            nombre = pedir_texto("Nombre")
            categoria = pedir_texto("Categoría")

            precio = input(Fore.WHITE + "Precio: ").strip()
            while precio == "" or not precio.isdecimal():
                print(Fore.RED + "Error: El precio es obligatorio y debe ser un número entero.")
                precio = input(Fore.WHITE + "Precio: ").strip()
            precio = int(precio)


            if stock:
                max_id = max(int(p["ID"]) for p in stock)
                nuevo_id = str(max_id + 1)
            else:
                nuevo_id = "1"
            identificador = nuevo_id
            print(Fore.WHITE + f"ID asignado automáticamente: {identificador}")

            cantidad = input(Fore.WHITE + "Cantidad: ").strip()
            while cantidad == "" or not cantidad.isdigit():
                print(Fore.RED + "Error: La cantidad es obligatoria y debe ser un número entero.")
                cantidad = input(Fore.WHITE + "Cantidad: ").strip()
            cantidad = int(cantidad)

            producto = {
                "ID": identificador,
                "nombre": nombre,
                "categoria": categoria,
                "precio": precio,
                "cantidad": cantidad
            }
            stock.append(producto)
            print("")
            print(Fore.GREEN + "¡Producto agregado con éxito!")

        case "2":
            caratula("Visualizar productos")
            for contador, producto in enumerate(stock):
                print(Fore.YELLOW + f"Producto # {contador + 1}:")
                print(Fore.WHITE + f"  ID: {producto['ID']}")
                print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
                print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
                print(Fore.WHITE + f"  Precio: ${producto['precio']}")
                print(Fore.WHITE + f"  Cantidad: {producto['cantidad']}")
                print("")

        case "3":
            caratula("Buscar productos")
            busqueda = input(Fore.WHITE + "Nombre del producto a buscar: ").strip().lower()
            encontrado = False

            for contador, producto in enumerate(stock):
                if busqueda in producto["nombre"].lower():
                    print(Fore.GREEN + "Producto encontrado:")
                    print(Fore.YELLOW + f"Producto # {contador + 1}:")
                    print(Fore.WHITE + f"  ID: {producto['ID']}")
                    print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
                    print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
                    print(Fore.WHITE + f"  Precio: ${producto['precio']}")
                    print(Fore.WHITE + f"  Cantidad: {producto['cantidad']}")
                    encontrado = True
                    print("")

            if not encontrado:
                print(Fore.RED + "No se encontraron productos con ese nombre.")

        case "4":
            caratula("Eliminar productos")
            eliminar = input(Fore.WHITE + "Número del producto a eliminar: ").strip()
            while eliminar == "" or not eliminar.isdecimal():
                print(Fore.RED + "Error: El número debe ser un entero válido.")
                eliminar = input(Fore.WHITE + "Número del producto a eliminar: ").strip()

            eliminar = int(eliminar)
            encontrado = False

            for contador, producto in enumerate(stock):
                if eliminar == contador + 1:
                    print(Fore.GREEN + "¡Producto eliminado!")
                    print(Fore.YELLOW + f"Producto # {contador + 1}:")
                    print(Fore.WHITE + f"  ID: {producto['ID']}")
                    print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
                    print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
                    print(Fore.WHITE + f"  Precio: ${producto['precio']}")
                    print(Fore.WHITE + f"  Cantidad: {producto['cantidad']}")
                    stock.remove(producto)
                    encontrado = True
                    break

            if not encontrado:
                print(Fore.RED + "No existe ese producto.")

        case "5":
            caratula("Actualizar productos")
            busqueda = input(Fore.WHITE + "ID del producto a actualizar: ").strip()
            encontrado = False

            for contador, producto in enumerate(stock):
                if busqueda == producto["ID"]:
                    print(Fore.GREEN + "Producto encontrado:")
                    print(Fore.YELLOW + f"Producto # {contador + 1}:")
                    print(Fore.WHITE + f"  ID: {producto['ID']}")
                    print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
                    print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
                    print(Fore.WHITE + f"  Precio: ${producto['precio']}")
                    print(Fore.WHITE + f"  Cantidad: {producto['cantidad']}")
                    encontrado = True

                    nuevo_nombre = producto["nombre"]
                    nueva_categoria = producto["categoria"]
                    nuevo_precio = producto["precio"]
                    nueva_cantidad = producto["cantidad"]

                    desea = input(Fore.WHITE + "¿Actualizar nombre? (Si/No): ").strip().title()
                    if desea == "Si":
                        nuevo_nombre = pedir_texto("Nuevo nombre")

                    desea = input(Fore.WHITE + "¿Actualizar categoría? (Si/No): ").strip().title()
                    if desea == "Si":
                        nueva_categoria = pedir_texto("Nueva categoría")

                    desea = input(Fore.WHITE + "¿Actualizar precio? (Si/No): ").strip().title()
                    if desea == "Si":
                        precio = input(Fore.WHITE + "Nuevo precio: ").strip()
                        while precio == "" or not precio.isdecimal():
                            print(Fore.RED + "Error: El precio debe ser un número entero.")
                            precio = input(Fore.WHITE + "Nuevo precio: ").strip()
                        nuevo_precio = int(precio)

                    desea = input(Fore.WHITE + "¿Actualizar cantidad? (Si/No): ").strip().title()
                    if desea == "Si":
                        cantidad = input(Fore.WHITE + "Nueva cantidad: ").strip()
                        while cantidad == "" or not cantidad.isdigit():
                            print(Fore.RED + "Error: La cantidad debe ser un número entero.")
                            cantidad = input(Fore.WHITE + "Nueva cantidad: ").strip()
                        nueva_cantidad = int(cantidad)

                    stock[contador].update({
                        "nombre": nuevo_nombre,
                        "categoria": nueva_categoria,
                        "precio": nuevo_precio,
                        "cantidad": nueva_cantidad
                    })
                    print(Fore.GREEN + "Producto actualizado correctamente.")
                    break

            if not encontrado:
                print(Fore.RED + "No existe un producto con ese ID.")

        case "6":
            caratula("Controlar stock bajo")
            minima = input(Fore.WHITE + "Cantidad mínima de referencia: ").strip()
            while minima == "" or not minima.isdigit():
                print(Fore.RED + "Error: Debe ingresar un número entero.")
                minima = input(Fore.WHITE + "Cantidad mínima de referencia: ").strip()
            minima = int(minima)

            encontrado = False
            for contador, producto in enumerate(stock):
                if producto["cantidad"] < minima:
                    print(Fore.GREEN + "Producto con stock bajo:")
                    print(Fore.YELLOW + f"Producto # {contador + 1}:")
                    print(Fore.WHITE + f"  ID: {producto['ID']}")
                    print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
                    print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
                    print(Fore.WHITE + f"  Precio: ${producto['precio']}")
                    print(Fore.WHITE + f"  Cantidad actual: {producto['cantidad']}")
                    encontrado = True
                    print("")

            if not encontrado:
                print(Fore.GREEN + "No hay productos con stock bajo (por debajo de " + str(minima) + ").")

        case "7":
            print(Fore.MAGENTA + "\n¡Hasta luego!")

        case _:
            print(Fore.RED + "Opción no válida.")