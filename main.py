from helpers.menu import Menu
from controllers.producto import ProductoController
from controllers.factura import FacturaController
from controllers.usuario import UsuarioController

def app():
    try:
        print('''
        ===============================================
            Autentificacion al Sistema Tienda Virtual
        ===============================================
        ''')
        usuario = UsuarioController()
        cod_usuario = usuario.input_usuario('Ingrese el codigo del usuario >> ')
        usuario_login = usuario.get_rol_by_input_password(cod_usuario,'Ingrese el password del usuario >> ')
        des_rol = usuario.get_desc_rol_by_id_rol(usuario_login[7])
        
        print(f'''
        ========================================================================================================
            Bienvenido al Sistema {usuario_login[4]} {usuario_login[5]}, Su Perfil es de {des_rol}  
        ========================================================================================================
        ''')

        if (des_rol):
            if des_rol == 'Administrador Sistema':
                menu_principal = ["Productos","Facturas","Usuarios", "Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
                    producto = ProductoController()
                    producto.menu()
                    if producto.salir:
                        app()
                elif respuesta == 2:
                    factura = FacturaController()
                    factura.menu()
                    if factura.salir:
                        app()
                elif respuesta == 3:
                    usuario = UsuarioController()
                    usuario.menu()
                    if usuario.salir:
                        app()
            elif des_rol == 'Almacen':
                menu_principal = ["Productos", "Salir"]
                respuesta = Menu(menu_principal).show()
                print(respuesta)
                if respuesta == 1:
                    producto = ProductoController()
                    producto.menu()
                    if producto.salir:
                        app()
            elif des_rol == 'Administrador Comercial':
                menu_principal = ["Facturas","Usuarios", "Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
                    factura = FacturaController()
                    factura.menu()
                    if factura.salir:
                        app()
                elif respuesta == 2:
                    usuario = UsuarioController()
                    usuario.menu()
                    if usuario.salir:
                        app()
            elif des_rol == 'Cajero':
                menu_principal = ["Facturas", "Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
                    factura = FacturaController()
                    factura.menu()
                    if factura.salir:
                        app()
            else:
                print('error')
        print (usuario)


  
        print("\n Gracias por utilizar el sistema \n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

app()