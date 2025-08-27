from coche import Coche

class CocheNuevo(Coche):
    def __init__(self, matricula, modelo, marca, color, precio, cantidad):
        super().__init__(matricula, modelo, marca, color, precio, cantidad)
    
    def mostrar_datos(self):
        """Muestra la información del coche nuevo."""
        super().mostrar_datos()
        print(f"{'Stock:':<15} {self.cantidad} unidades")
        print(f"{'Estado:':<15} Nuevo")
        print("="*60)
