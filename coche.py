class Coche:
    def __init__(self, matricula, modelo, marca, color, precio, cantidad=1):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.precio = precio
        self.cantidad = cantidad  # Stock disponible
    
    def mostrar_datos(self):
        """Muestra la información básica del coche."""
        print("\n" + "="*60)
        print("INFORMACIÓN DEL VEHÍCULO".center(60))
        print("="*60)
        print(f"{'Matrícula:':<15} {self.matricula}")
        print(f"{'Marca:':<15} {self.marca}")
        print(f"{'Modelo:':<15} {self.modelo}")
        print(f"{'Color:':<15} {self.color}")
        print(f"{'Precio:':<15} ${self.precio:,.2f}")
        print("="*60)
