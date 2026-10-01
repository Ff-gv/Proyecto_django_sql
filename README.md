# Proyecto_django_sql
Se crea una aplicacion web que utiliza una base de datos Mysql, esta aplicacion cumple con CRUD, se configura y se realizan consultas SQL para verificar la funcionalidad.
Se crean la app gestion dentro de mi aplicacion django_sql, esta contiene los modelos, htmls, vistas, urls y forms necesarios para su funcionamiento. Se crean los modelos Cliente, Cuenta, Transaccion, Descripcion y Descuento. Cada uno de estos modelos presenta una relacion distinta, Cliente tiene relacion uno a muchos, cuenta con transaccion es uno a muchos. La explicacion de un cliente puede tener muchas cuentas, y una cuenta puede tener muchas transacciones. las tablas de descripcion y descuento presentan otro tipo de relacion, descripcion es una relacion de uno a uno; en este caso solo se coloca pelo, pero es una tabla que puede ser expandida y indicaria caracteristicas que solo le pertenencen a una sola persona, por lo que lo haria uno a uno. Descuento es muchos a muchos ya que muchas cuentas pueden tener muchos descuentos.
Se procede con preparar el ambiente virtual, instalando paquetes para nuestro proyecto, creando las variables locales y configurando static y templates. Se crean los modelos, se procede a crear forms para ingreso de formularios; se agrega campos a admin para poder editar, se realizan pruebas en shell, se procede a crear las vistas, crear un archivo urls.py y sus html respectivos.
Los html estan bajo la jerarquia de base.html, que es el template que manda en la configuracion y que entrega el esqueleto de la pagina, se usa un css de static para proporcionar las configuraciones esteticas.

## Consultas SQL
Se procede a realizar consultas sql para probar el funcionamiento de los modelos:

Se crean 3 entradas de clientes:

<img width="921" height="173" alt="1" src="https://github.com/user-attachments/assets/c72b3ed8-248a-4bf3-9945-ab96741356e7" />

se asocian los clientes a distintas cuentas, demostrando que la relacion creada en las tablas no causa errores al ingresar los datos:

<img width="662" height="53" alt="2" src="https://github.com/user-attachments/assets/3546b8b8-ffcd-4607-b5f3-0d3eb21e55fb" />

se crean registros de transacciones asociados a las cuentas:

<img width="836" height="161" alt="3" src="https://github.com/user-attachments/assets/08c01f8f-e08d-4e43-a072-f788c3b527f2" />

Se usa el orm para buscar todos los clientes registrados y se muestran 3 atributos:

<img width="914" height="230" alt="4" src="https://github.com/user-attachments/assets/83a4afc3-c4b1-4c61-ab1a-7401d36e6251" />

Se prueba actualizar un registro de una transaccion y se muestra en pantalla el exito del cambio:

<img width="476" height="183" alt="5" src="https://github.com/user-attachments/assets/24fbb2b3-08d7-4c90-97a4-528bcf56748a" />

Ahora se prueba la eliminacion de un registro de forma exitosa:

<img width="470" height="154" alt="6" src="https://github.com/user-attachments/assets/d82f9334-93c7-40fc-905c-9736e9ecf55f" />

Consultas realizadas con SQL utilizando de forma segura usando parametros:

<img width="891" height="110" alt="7" src="https://github.com/user-attachments/assets/f4811044-61d3-4244-95cc-3093eccc080f" />

Uso de connection para realizar una consulta de agregacion, en este caso, suma:

<img width="578" height="146" alt="8" src="https://github.com/user-attachments/assets/a786745f-4bf9-4860-8552-40ef7e3402bd" />

Se utiliza filtros en orm para obtener resultados basados en 2 condiciones:

<img width="538" height="90" alt="9" src="https://github.com/user-attachments/assets/16416d16-0a28-4d71-87fe-5ee7192b2350" />

Se prueba el metodo de exclusion, en este caso, la condicion es si la id=3, se cumple la condicion y se muestra el resultado con el registro omitido:

<img width="637" height="125" alt="10" src="https://github.com/user-attachments/assets/7de603d6-cd83-4aad-a920-a87c2e3df4ce" />

