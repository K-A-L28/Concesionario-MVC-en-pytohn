class detalleCompra:
    def __init__(self, id_compra, matricula, precio, cantidad=1):
        self.id_compra = id_compra
        self.matricula = matricula
        self.precio = precio
        self.cantidad = cantidad
    
    def obtener_datos(self):
        return {
            'id_compra': self.id_compra,
            'matricula': self.matricula,
            'precio': self.precio,
            'cantidad': self.cantidad
        }
