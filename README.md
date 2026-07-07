

# Entrega - Sistema de Gestión de Productos

Programa de consola desarrollado en Python para la gestión básica de un inventario de productos. Permite realizar operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar) y también controlar el stock mínimo.

## Funcionalidades

### 1. Agregar producto
Permite ingresar un nuevo producto al inventario. El sistema solicita:
- **Nombre** (obligatorio)
- **Categoría** (obligatorio)
- **Precio** (obligatorio, número entero)
- **Cantidad** (obligatorio, número entero)

El **ID** se asigna automáticamente tomando el último ID existente y sumando 1, garantizando que sea único. El sistema muestra el ID asignado para que el usuario lo conozca.

Todas las entradas son validadas (campos vacíos, tipos numéricos, etc.) antes de agregar el producto.

### 2. Ver productos
Muestra un listado completo de todos los productos en el inventario con el siguiente formato:

```text
Producto # 1:
  ID: 1
  Nombre: Lapicera Azul
  Categoria: Escritura
  Precio: $150
  Cantidad: 45
  ```

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

### 5. Actualizar producto

Permite modificar los datos de un producto existente buscándolo por su **ID**. El usuario puede elegir qué campos actualizar:

-   Nombre
-   Categoría
-   Precio
-   Cantidad
    

Para cada campo, el sistema pregunta si se desea modificar y, en caso afirmativo, solicita el nuevo valor con las mismas validaciones que al agregar.

### 6. Controlar stock bajo

Solicita al usuario una **cantidad mínima de referencia** y muestra todos los productos cuya cantidad actual sea **inferior** a ese valor. Esto ayuda a identificar rápidamente qué productos necesitan reposición.

### 7. Salir
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
    "ID": "0",
    "nombre": "Nombre del producto",
    "categoria": "Categoria del producto",
    "precio": 0000,
    "cantidad": 0
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

Al ejecutar el programa, se muestra un menú con 7 opciones. El usuario debe ingresar el numero de la opción deseada y seguir las instrucciones en pantalla.

El inventario inicial incluye 10 productos de Librería pre-cargados para facilitar las pruebas.
