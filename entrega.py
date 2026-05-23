from colorama import init, Fore

init(autoreset=True)

stock = [
    {"nombre": "Lapicera Azul", "categoria": "Escritura", "precio": 150},
    {"nombre": "Cuaderno Rivadavia", "categoria": "Cuadernos", "precio": 850},
    {"nombre": "Resma A4", "categoria": "Papel", "precio": 3200},
    {"nombre": "Corrector Líquido", "categoria": "Escritura", "precio": 450},
    {"nombre": "Regla 30cm", "categoria": "Geometría", "precio": 280},
    {"nombre": "Goma de Borrar", "categoria": "Escritura", "precio": 120},
    {"nombre": "Marcadores x12", "categoria": "Arte", "precio": 2100},
    {"nombre": "Tijera Escolar", "categoria": "Corte", "precio": 650},
    {"nombre": "Plasticola 250ml", "categoria": "Adhesivos", "precio": 980},
    {"nombre": "Carpeta 3 Solapas", "categoria": "Organización", "precio": 750}
]

opcion = "0"

while opcion != "5":

    print("")
    print(Fore.MAGENTA + "---Bienvenido al sistema de gestión de productos---")
    print("")
    print(Fore.YELLOW + "1. Agregar producto")    
    print(Fore.YELLOW + "2. Ver productos")
    print(Fore.YELLOW + "3. Buscar producto")
    print(Fore.YELLOW + "4. Eliminar producto")
    print(Fore.YELLOW + "5. Salir")
    print("")

    opcion = input(Fore.WHITE + "Elegí una opción para continuar: ")

    match opcion:
        case "1":
            print(Fore.GREEN + "\nAgregar producto")

            nombre = input(Fore.WHITE + "Ingresa el nombre del producto: ").strip().title()
            while nombre == "" :
                print(Fore.RED + "Error: El nombre es obligatorio.")
                nombre = input(Fore.WHITE + "Ingresa el nombre del producto: ").strip().title()

            categoria = input(Fore.WHITE + "Ingresa la categoría del producto: ").strip().title()
            while categoria == "" :
                print(Fore.RED + "Error: La categoría es obligatoria.")
                categoria = input(Fore.WHITE + "Ingresa la categoría del producto: ").strip().title()

            precio = input(Fore.WHITE + "Ingresa el precio del producto: ").strip()
            while precio == "" or not precio.isdecimal():
                print(Fore.RED + "Error: El precio es obligatorio y debe ser un número entero.")
                precio = input(Fore.WHITE + "Ingresa el precio del producto: ").strip()

            producto = {
                "nombre": nombre,
                "categoria": categoria,
                "precio": int(precio)
            }
            
            stock.append(producto)
            print("")
            print(Fore.GREEN + "¡Producto agregado con éxito!")

        case "2":
            print("")
            print(Fore.MAGENTA + "Ver productos")
            print("")
            for contador, producto in enumerate(stock):
                print(Fore.YELLOW + f"Producto # {contador + 1}:")
                print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
                print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
                print(Fore.WHITE + f"  Precio: ${producto['precio']}")
                print("")

        case "3":
            print(Fore.MAGENTA + "\nBuscar producto")
            busqueda = input(Fore.WHITE + "Ingresa el nombre del producto a buscar: ").strip().lower()
            encontrado = False

            print("")
            print(Fore.MAGENTA + "Resultados de la búsqueda:")
            print("")
            
            for contador, producto in enumerate(stock):
                if busqueda in producto["nombre"].lower():
                    print(Fore.GREEN + "Producto encontrado:")
                    print("")
                    print(Fore.YELLOW + f"Producto # {contador + 1}:")
                    print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
                    print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
                    print(Fore.WHITE + f"  Precio: ${producto['precio']}")
                    encontrado = True
                    print("")
            
            if encontrado == False:
                print(Fore.RED + "No se encontraron productos con ese nombre")

        case "4":
            print(Fore.MAGENTA + "\nEliminar producto")
            eliminar = input(Fore.WHITE + "Ingresa el numero del producto a eliminar: ").strip()
            while eliminar == "" or not eliminar.isdecimal():
                print(Fore.RED + "Error: El número de producto es obligatorio y debe ser un número entero.")
                eliminar = input(Fore.WHITE + "Ingresa el numero del producto a eliminar: ").strip()
            encontrado = False
            for contador, producto in enumerate(stock):
                if int(eliminar) == contador + 1:
                    print("")
                    print(Fore.GREEN + "¡Producto eliminado!")
                    print("")
                    print(Fore.YELLOW + f"Producto # {contador + 1}:")
                    print(Fore.WHITE + f"  Nombre: {producto['nombre']}")
                    print(Fore.WHITE + f"  Categoría: {producto['categoria']}")
                    print(Fore.WHITE + f"  Precio: ${producto['precio']}")
                    encontrado = True
                    stock.remove(producto)
       
            if encontrado == False:
                print(Fore.RED + "No existe el producto")
        case "5":
            print(Fore.MAGENTA + "\n¡Hasta luego!")
        case _:
            print(Fore.RED + "Opción no válida")