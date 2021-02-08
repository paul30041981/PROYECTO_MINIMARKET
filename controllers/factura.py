from models.factura import Factura
from models.detalle import Detalle
from models.producto import Producto
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question
from datetime import datetime
from controllers.producto import ProductoController


class FacturaController:
    def __init__(self):
        self.factura = Factura()
        self.detalle = Detalle()
        self.producto = Producto()
        self.producto_controler = ProductoController()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Facturas
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_facturas()
                elif respuesta == 2:
                    self.search_factura()
                elif respuesta == 3:
                    self.insert_factura()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_facturas(self):
        try:
            print('''
            ==========================
                Listar Facturas
            ==========================
            ''')
            facturas = self.factura.get_facturas('num_factura')
            print(print_table(facturas, ['Num Factura', 'Doc Cliente', 'Fecha', 'Precio Sin IGV', 'IGV', 'Total']))


            if facturas:
                if question('¿Deseas ver el Detalle de la Factura?'):
                  num_factura = input_data("Ingrese el Numero de Factura >> ", "int")
                  detalle = self.detalle.get_detalle({
                      'num_factura': num_factura
                  })
                  print(print_table(detalle, ['Num detalle', 'Num Factura', 'Id Producto', 'Cantidad', 'Precio Sin IGV']))

            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_factura(self):
        print('''
        ========================
            Buscar Factura
        ========================
        ''')
        try:
            num_factura = input_data("Ingrese el Numero de Factura >> ", "int")
            factura = self.factura.get_factura({
                'num_factura': num_factura
            })
            print(print_table(factura, ['Num Factura', 'Doc Cliente', 'Fecha', 'Precio Sin IGV', 'IGV', 'Total']))
            
            if factura:
                detalle = self.detalle.get_detalle({
                    'num_factura': num_factura
                })
                print(print_table(detalle, ['Num detalle', 'Num Factura', 'Id Producto', 'Cantidad', 'Precio Sin IGV']))

            if factura:
                if question('¿Deseas dar mantenimiento a la Factura?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_factura(num_factura)
                    elif respuesta == 2:
                        self.delete_factura(num_factura)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_factura(self):
        detalle = []
        i = 1
        monto_total = 0
        id_cliente = input_data('Ingrese el Numero de Documento del cliente >> ')
        self.producto_controler.all_productos()
        while True:
            match = False
            id_producto = int(input_data(f"\n Ingrese el id del producto numero {i} comprado>> ", "int"))
            for deta in detalle:
                if int(deta['id_producto']) == id_producto:
                    match =  True
            if match : 
                print ('Ustede ya ingreso este producto.')
                if question('¿Deseas agregar mas productos a la Compra?') == False:
                    break
            else:
                if (self.producto_controler.valida_disponibilidad_by_codproducto(id_producto)):
                    
                    while True:
                        cantidad = input_data(f"\n Ingrese la cantidad del producto numero {i} comprado>> ", "int")
                        buscar_producto = self.producto.get_producto({
                            'id_producto': id_producto
                        })
                        if (self.producto_controler.valida_disponibilidad_by_codproducto_cantidad(id_producto,cantidad ) == True):
                            break
                        else:
                            print ('\n La cantidad ingresada es mayor a la disponible. \n')

                    if buscar_producto:
                        precio = buscar_producto[3] * cantidad
                        monto_total = monto_total + precio
                        detalle.append({
                            'id_producto': id_producto,
                            'cantidad': cantidad,
                            'precio': precio
                        })
                    i = i + 1
                    if question('¿Deseas agregar mas productos a la Compra?') == False:
                        break
                else:
                    print("\n El producto escogido no tiene Stock.")

                    if question('¿Deseas agregar mas productos a la Compra?') == False:
                        break

        now = datetime.now()
        fecha_hora = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        self.factura.insert_factura({
            'id_cliente': id_cliente,
            'fecha': fecha_hora,
            'monto_total': monto_total,
            'igv': 0.18 * monto_total,
            'precio_total' : 1.18 * monto_total
        })
        facturas = self.factura.get_facturas('num_factura')
        if facturas:
            id_factura = facturas[len(facturas) - 1][0]
            print(detalle)
            for det in detalle:
                self.detalle.insert_detalle({
                    'num_factura': id_factura,
                    'id_producto': det['id_producto'],
                    'cantidad': det['cantidad'],
                    'precio': det['precio']
                })
                self.producto_controler.update_stock_of_compra_producto_by_codproducto_cantidad(det['id_producto'],det['cantidad'])

        print('''
        ================================
            Nueva factura agregada
        ================================
        ''')
        self.all_facturas()

    def update_factura(self, num_factura):
        id_cliente = input_data('Ingrese el nuevo Numero de Documento del cliente >> ')
        self.factura.update_factura({
            'num_factura': num_factura
        }, {
            'id_cliente': id_cliente
        })
        print('''
        ============================
            Factura Actualizada
        ============================
        ''')

    def delete_factura(self, num_factura):
        self.factura.delete_factura({
            'num_factura': num_factura
        })
        print('''
        =========================
            Factura Eliminada
        =========================
        ''')

