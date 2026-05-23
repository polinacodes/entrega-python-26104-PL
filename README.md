# Entrega - Sistema de Gestión de Productos

Programa de consola desarrollado en Python para la gestión básica de un inventario de productos. Permite realizar operaciones Crear, Leer, Buscar y Eliminar sobre una lista de artículos de Librería.

## Funcionalidades

### 1. Agregar producto
Permite ingresar un nuevo producto al inventario solicitando:
- Nombre del producto (obligatorio)
- Categoría del producto (obligatorio)
- Precio del producto (obligatorio, debe ser un numero entero)

El sistema valida que todos los campos sean completados correctamente antes de agregar el producto.

### 2. Ver productos
Muestra un listado completo de todos los productos en el inventario con el siguiente formato:

Producto # 1:
  Nombre: Lapicera Azul
  Categoria: Escritura
  Precio: $150

### 3. Buscar producto
Busca productos por nombre con las siguientes características:
- Búsqueda parcial: encuentra productos que contengan la palabra ingresada
- No distingue mayúsculas/minúsculas
- Muestra todos los productos que coincidan con la búsqueda

### 4. Eliminar producto
Elimina un producto del inventario indicando su numero de posición en la lista. El sistema:
- Muestra los datos del producto antes de eliminarlo
- Confirma la eliminación exitosa
- Valida que el numero ingresado sea correcto

### 5. Salir
Finaliza la ejecución del programa con un mensaje de despedida.

## Características técnicas

- Desarrollado en Python 3
- Interfaz de consola con colores usando la librería Colorama
- Estructura de datos basada en diccionarios para cada producto
- Validación de datos de entrada
- Menú interactivo con opciones numéricas

## Estructura de datos

Cada producto se almacena como un diccionario con la siguiente estructura:
 ```bash
   {
    "nombre": "Nombre del producto",
    "categoria": "Categoria del producto",
    "precio": 0000
    } 
   ```

## Requisitos

- Python 3.6 o superior
- Libreria Colorama

## Instalacion

1. Clonar el repositorio:
   ```bash
   https://github.com/polinacodes/entrega-python-26104-PL.git 
   ```


2. Instalar dependencias:   
   ```bash
   pip install colorama 
   ```

3. Ejecutar el programa:
   ```bash
   python entrega.py  
   ```

## Uso

Al ejecutar el programa, se muestra un menú con 5 opciones. El usuario debe ingresar el numero de la opción deseada y seguir las instrucciones en pantalla.

El inventario inicial incluye 10 productos de Librería pre-cargados para facilitar las pruebas.

