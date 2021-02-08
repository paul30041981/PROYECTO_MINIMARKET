from connection.conn import Connection


class Rol:
    def __init__(self):
        self.model = Connection('rol')

    def get_roles(self, order):
        return self.model.get_all(order)

    def get_rol(self, id_object):
        return self.model.get_by_id(id_object)

    def search_rol(self, data):
        return self.model.get_columns(data)

    def insert_rol(self, rol):
        return self.model.insert(rol)

    def update_rol(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_rol(self, id_object):
        return self.model.delete(id_object)
