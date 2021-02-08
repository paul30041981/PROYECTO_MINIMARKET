from models.usuario import Usuario
from models.rol import Rol
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question, genera_codigo_by_texto


class UsuarioController:
    def __init__(self):
        self.usuario = Usuario()
        self.rol = Rol()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Usuarios
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_usuarios()
                elif respuesta == 2:
                    self.search_usuario()
                elif respuesta == 3:
                    self.insert_usuario()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_usuarios(self):
        try:
            print('''
            ==========================
                Listar Usuarios
            ==========================
            ''')
            usuarios = self.usuario.get_usuarios('id_usuario')
            lista_usuarios = []
            if usuarios:
                for user in usuarios:
                    buscar_rol = self.rol.get_rol({'id_rol': user[7]})
                    lista_usuarios.append((
                        user[0],
                        user[1],
                        user[2],
                        user[3],
                        user[4],
                        user[5],
                        user[6],
                        buscar_rol[1]
                 ))
            print(print_table(lista_usuarios, ['ID', 'Tipo Doc', 'Num Doc', 'Codigo', 'Nombre', 'Ap. Paterno', 'Ap. Materno', 'Rol']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_usuario(self):
        print('''
        ========================
            Buscar Usuario
        ========================
        ''')
        try:
            cod_usuario = input_data("Ingrese el Codigo del usuario >> ")
            user = self.usuario.get_usuario({
                'codigo': str(cod_usuario)
            })
            lista_usuarios = []
            if user:
                buscar_rol = self.rol.get_rol({'id_rol': user[7]})
                lista_usuarios.append((
                    user[0],
                    user[1],
                    user[2],
                    user[3],
                    user[4],
                    user[5],
                    user[6],
                    buscar_rol[1]
                ))
                print(print_table(lista_usuarios, ['ID', 'Tipo Doc', 'Num Doc', 'Codigo', 'Nombre', 'Ap. Paterno', 'Ap. Materno', 'Rol']))
     
                if question('¿Deseas dar mantenimiento al usuario?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_usuario(cod_usuario)
                    elif respuesta == 2:
                        self.delete_usuario(cod_usuario)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_usuario(self):
        print('Seleccion el Tipo de Documento del usuario >>')
        lista_menu = ["DNI", "RUC", "PASAPORTE", "OTRO"]
        respuesta = Menu(lista_menu).show()
        if respuesta == 1:
            tipo_doc='DNI'
        elif respuesta == 2:
            tipo_doc='RUC'
        elif respuesta == 3:
            tipo_doc='PASAPORTE'
        else:
            tipo_doc='OTRO'

        num_doc = input_data('Ingrese el Numero Documento del usuario >> ')
        nombre = input_data('Ingrese el Nombre del usuario >> ')
        ap_paterno = input_data('Ingrese el Apellido Paterno del usuario >> ')
        ap_materno = input_data('Ingrese el Apellido Materno del usuario >> ')
        codigo = genera_codigo_by_texto(ap_paterno + ap_materno)

        print('Seleccion el Rol del Usuario >>')
        lista_roles = self.rol.get_roles('id_rol')
        lista_menu_roles = []
        for rol_ in lista_roles:
            lista_menu_roles.append(rol_[1])
        id_rol = Menu(lista_menu_roles).show()

        password = input_data('Ingrese la contraseña del usuario >> ')

        self.usuario.insert_usuario({
            'tipo_doc': tipo_doc,
            'num_doc': num_doc,
            'codigo': codigo,
            'nombre': nombre,
            'ap_paterno': ap_paterno,
            'ap_materno': ap_materno,
            'id_rol': int(id_rol),
            'password': password
        })
        print('''
        ================================
            Nuevo usuario agregado
        ================================
        ''')
        self.all_usuarios()

    def update_usuario(self, cod_usuario):
        
        print('Seleccion el Nuevo Tipo de Documento del usuario >>')
        lista_menu = ["DNI", "RUC", "PASAPORTE", "OTRO"]
        respuesta = Menu(lista_menu).show()
        if respuesta == 1:
            tipo_doc='DNI'
        elif respuesta == 2:
            tipo_doc='RUC'
        elif respuesta == 3:
            tipo_doc='PASAPORTE'
        else:
            tipo_doc='OTRO'

        num_doc = input_data('Ingrese el Nuevo Numero Documento del usuario >> ')
        nombre = input_data('Ingrese el Nuevo Nombre del usuario >> ')
        ap_paterno = input_data('Ingrese el Nuevo Apellido Paterno del usuario >> ')
        ap_materno = input_data('Ingrese el Nuevo Apellido Materno del usuario >> ')

        print('Seleccion el Nuevo Rol del Usuario >>')
        lista_roles = self.rol.get_roles('id_rol')
        lista_menu_roles = []
        for rol_ in lista_roles:
            lista_menu_roles.append(rol_[1])
        id_rol = Menu(lista_menu_roles).show()

        password = input_data('Ingrese la Nueva Contraseña del Usuario >> ')

        self.usuario.update_usuario({
            'codigo': cod_usuario
        }, {
            'tipo_doc': tipo_doc,
            'num_doc': num_doc,
            'nombre': nombre,
            'ap_paterno': ap_paterno,
            'ap_materno': ap_materno,
            'id_rol': int(id_rol),
            'password': password
        })
        print('''
        ============================
            Usuario Actualizado
        ============================
        ''')

    def delete_usuario(self, cod_usuario):
        self.usuario.delete_usuario({
            'codigo': cod_usuario
        })
        print('''
        =========================
            Usuario Eliminado
        =========================
        ''')

    def valida_existe__codigo_usuario(self, codigo):

        buscar_usuario = self.usuario.get_usuario({
            'codigo': codigo
        })

        if buscar_usuario:
          return True

        return False
    
    def login_usuario(self, codigo, password):

        buscar_usuario = self.usuario.get_usuario({
            'codigo': codigo,
            'password': password
        })

        if buscar_usuario:
          return buscar_usuario

        return None

    def input_usuario(self, texto_codigo_usuario):
        while True:
            try:
                cod_usuario = input(texto_codigo_usuario).strip()
                if (self.valida_existe__codigo_usuario(cod_usuario) == False):
                    raise ValueError('')
                break
            except ValueError:
                print('Usuario No existe. Intente Nuevamente.')
        return cod_usuario


        
    def get_rol_by_input_password(self, cod_usuario, texto_password_usuario):
        usuario = None

        while True:
            try:
                password = input(texto_password_usuario).strip()
                usuario = self.login_usuario(cod_usuario, password)
                if (usuario == None):
                    raise ValueError('')

                return usuario
            except ValueError:
                print('Logueo Incorrecto. Intente Nuevamente la Contraseña')

        return usuario

    def get_desc_rol_by_id_rol(self, id_rol):

        buscar_rol = self.rol.get_rol({'id_rol': id_rol})

        return buscar_rol[1]
        