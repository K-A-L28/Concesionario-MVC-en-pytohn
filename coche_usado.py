from coche import Coche

class CocheUsado(Coche):
    def __init__(self, matricula, modelo, marca, color, precio, kilometraje, cantidad=1):
        super().__init__(matricula, modelo, marca, color, precio, cantidad)
        self.kilometraje = kilometraje
    
    def mostrar_datos(self):
        """Muestra la información del coche usado."""
        super().mostrar_datos()
        print(f"{'Kilometraje:':<15} {self.kilometraje} km")
        print(f"{'Estado:':<15} Usado")
        print("="*60)
