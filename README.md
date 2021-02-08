# PROYECTO_MINIMARKET

PASOS:
1. ingresar a pgadmin
2. crear base de datos con el nombre minimarket
3. Ingresar a consola de windows ejecutar CMD
4. ubicarse en la ruta del archivo MINIMARKET_DUMP.sql que esta dentro de este proyecto
5. ejecutar :  psql -U postgres -W -h 127.0.0.1 minimarket < MINIMARKET_DUMP.sql
---te pedira la clave de conexion de tu usuario postgresql,la ingresas.
6. Listo ya tienes la base de datos instalada.


Para Iniciar el proyecto:

1. Ejecutar:
   python main.py
2. Loguearse al usuario administrador de sistema con las siguientes credenciales:
   codigo de usuario: 202126175116
   password: 40880382

3. El sistema permite la creacion de productos, facturas, detalle de facturas y de usuarios del sistema de 4 roles:
   
   "Cajero"
   "Administrador Comercial"
   "Almacen"
   "Administrador Sistema"

   Segun el rol del usuario, este tendra un menu de acceso que es dinamico.
   
4. Al crear un Usuario de sistema se genera su codigo de Usuario, y password el cual servira para accecer al sistema.
