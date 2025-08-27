from datetime import datetime
from detalle_compra import detalleCompra

class Venta:
    def __init__(self, id_venta, dni_vendedor, dni_cliente, forma_pago):
        self.id_venta = id_venta
        self.dni_vendedor = dni_vendedor
        self.dni_cliente = dni_cliente
        self.fecha_venta = datetime.now()
        self.forma_pago = forma_pago
        self.estado = 'Pendiente'
        self.detalles = []  # Initialize empty list for detalles
        self.fecha_creacion = datetime.now()
        self.fecha_actualizacion = datetime.now()
    
    def agregar_detalle(self, matricula, precio, cantidad=1):
        """Agrega un detalle de compra a la venta"""
        detalle = detalleCompra(self.id_venta, matricula, precio, cantidad)
        self.detalles.append(detalle)
        self.actualizar_estado()
        return detalle
    
    def actualizar_estado(self):
        """Actualiza el estado de la venta basado en los detalles"""
        if not self.detalles:
            self.estado = 'Pendiente'
        else:
            self.estado = 'Completada'
        self.fecha_actualizacion = datetime.now()
    
    def mostrar_datos(self):
        print("="*60)
        print("COMPROBANTE DE VENTA".center(60))
        print("="*60)
        print(f"{'ID Venta:':<15} {self.id_venta}")
        print(f"{'Fecha:':<15} {self.fecha_venta.strftime('%d/%m/%Y %H:%M')}")
        print("-"*60)
        print(f"{'DNI Vendedor:':<15} {self.dni_vendedor}")
        print(f"{'DNI Cliente:':<15} {self.dni_cliente}")
        print(f"{'Forma de pago:':<15} {self.forma_pago}")
        print(f"{'Estado:':<15} {self.estado}")
        print("-"*60)
        print("DETALLES DE LA COMPRA".center(60))
        print("-"*60)
        
        total = 0
        for i, detalle in enumerate(self.detalles, 1):
            subtotal = detalle.precio * detalle.cantidad
            total += subtotal
            print(f"{i}. Matrícula: {detalle.matricula}")
            print(f"   Cantidad: {detalle.cantidad}")
            print(f"   Precio unitario: ${detalle.precio:,.2f}")
            print(f"   Subtotal: ${subtotal:,.2f}")
            print("-"*60)
        
        print(f"{'TOTAL:':<15} ${total:>10,.2f}")
        print("="*60)
    
    def obtener_datos(self):
        return {
            'id_venta': self.id_venta,
            'dni_vendedor': self.dni_vendedor,
            'dni_cliente': self.dni_cliente,
            'fecha_venta': self.fecha_venta,
            'forma_pago': self.forma_pago,
            'estado': self.estado,
            'detalles': [d.obtener_datos() for d in self.detalles],
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion
        }
