# Menú

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
    print("---Bienvenido al sistema de gestión de productos---")
    print("")
    print("1. Agregar producto")    
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("")

    opcion = input("Elegí una opción para continuar: ")

    match opcion:
        case "1":
            print("Agregar producto")

            nombre = input("Ingresa el nombre del producto: ").strip().title()
            while nombre == "" :
                print("Error: El nombre es obligatorio.")
                nombre = input("Ingresa el nombre del producto: ").strip().title()

            categoria = input("Ingresa la categoría del producto: ").strip().title()
            while categoria == "" :
                print("Error: La categoría es obligatoria.")
                categoria = input("Ingresa la categoría del producto: ").strip().title()

            precio = input("Ingresa el precio del producto: ").strip()
            while precio == "" or not precio.isdigit():
                print("Error: El precio es obligatorio y debe ser un número entero.")
                precio = input("Ingresa el precio del producto: ").strip()

            producto = {
                "nombre": nombre,
                "categoria": categoria,
                "precio": int(precio)
            }
            
            stock.append(producto)
            print("¡Producto agregado con éxito!")

        case "2":
            print("")
            print("Ver productos")
            print("")
            for contador, producto in enumerate(stock):
                print(f"Producto # {contador + 1}:")
                print(f"  Nombre: {producto['nombre']}")
                print(f"  Categoría: {producto['categoria']}")
                print(f"  Precio: {producto['precio']}")
                print("")

        case "3":
            print("Buscar producto")
            busqueda = input("Ingresa el nombre del producto a buscar: ").strip().title()
            encontrado = False

            for contador, producto in enumerate(stock):
                if busqueda == producto["nombre"]:
                    print("Producto encontrado:")
                    print(f"Producto # {contador + 1}:")
                    print(f"  Nombre: {producto['nombre']}")
                    print(f"  Categoría: {producto['categoria']}")
                    print(f"  Precio: {producto['precio']}")
                    encontrado = True
                    print("")
            if encontrado == False:
                print("No existe el producto")

        case "4":
            print("Eliminar producto")
            eliminar = input("Ingresa el numero del producto a eliminar: ").strip()
            while eliminar == "" or not eliminar.isdecimal():
                print("Error: El número de producto es obligatorio y debe ser un número entero.")
                eliminar = input("Ingresa el numero del producto a eliminar: ").strip()
            encontrado = False
            for contador, producto in enumerate(stock):
                if int(eliminar) == contador + 1:
                    print("¡Producto eliminado!")
                    print(f"Producto # {contador + 1}:")
                    print(f"  Nombre: {producto['nombre']}")
                    print(f"  Categoría: {producto['categoria']}")
                    print(f"  Precio: {producto['precio']}")
                    encontrado = True
                    stock.remove(producto)
       
            if encontrado == False:
                print("No existe el producto")
        case "5":
            print("¡Hasta luego!")
        case _:
            print("Opción no válida")