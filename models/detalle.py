from connection.conn import Connection


class Detalle:
    def __init__(self):
        self.model = Connection('detalle')

    def get_detalles(self, order):
        return self.model.get_all(order)

    def get_detalle(self, id_object):
        return self.model.get_by_id(id_object)

    def search_detalle(self, data):
        return self.model.get_columns(data)

    def insert_detalle(self, detalle):
        return self.model.insert(detalle)

    def update_detalle(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_detalle(self, id_object):
        return self.model.delete(id_object)
