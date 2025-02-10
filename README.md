En este README se explicará en que consiste el código del archivo "DepVentasMes.py" y el cómo funcionan sus métodos.

Nota: 
Este código de Python fue creado con ayuda de ChatGPT.<br>
Se hicieron multiples iteraciones, modificaciones y correcciones para comprobar que funcione correctamente y de acuerdo a las intrucciones dadas.

El código consiste en un programa para gestionar las ventas mensuales de tres departamentos distintos. Dichos departamentos son: Ropa, Deportes y Juguetería.
El usuario podrá ingresar los datos necesarios para cada venta (nombre del producto y su precio), así como eliminarlos, consultar o mostrar todas las ventas registradas.
La información de las ventas se almacenarán en arreglos, y a su vez en un archivo JSON. Conservando la información de las ventas aún despúes de haber cerrando el programa.

### Explicación del código:
**Imports:**\
__json:__ Esta librería permite agregar el código necesario para crear el archivo JSON donde la información se guardará, así como acceder a dicho archivo.\
__os:__ Esta librería permite agregar el código necesario para que el programa pueda acceder a la computadora del usuario, así como a sus archivos. Permitiendo crear el archivo JSON.

**Métodos:**\
__-init:__ Es el método constructor. Inicializa el arreglo de los departamentos, el arreglo de los  meses y carga los datos del archivo JSON al programa.\
__-cargar_datos:__ Verifica si existe el archivo JSON en la carpeta donde también se encuentra el archivo py del programa, de no ser así, crea el archivo.\
__-guardar_datos:__ Guarda los cambios que el usuario realice de las ventas dentro del archivo JSON, sobreescribiendo la información.\
__-insertar_datos:__ Agrega los datos de una venta en el departamento y mes seleccionados. Se puede registrar más de una venta por mes.\
__-eliminar_venta:__ Elimina una venta determinada (si existe), buscando por su departamento, mes y el nombre del articulo.\
__-buscar_venta:__ Permite buscar una venta determinada, buscando por su departamento, mes y nombre del artículo. Si dicha venta existe se mostrará.\
__-mostrar_ventas:__ Muestra todas las ventas registradas en el archivo JSON. Si no hay alguna venta registrada en algún mes de un departamento se mostrará el mesansaje "Sin ventas".\
__-menu:__ Despliega un menú, con dicho menú el usuario puede interactuar con el programa.

**Objetos:**\
__tienda:__ LLama a la clase "Tienda", y en la siguiente línea se accede al método del menú. Permitiendo ejecutar el programa.
