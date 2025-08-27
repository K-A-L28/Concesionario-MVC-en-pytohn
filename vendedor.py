from empleado import Empleado

class Vendedor(Empleado):
    def __init__(self, dni, nombre, apellidos, fecha_contratacion, salario):
        super().__init__(dni, nombre, apellidos, fecha_contratacion, salario)
        self.ventas_realizadas = []
        self.comision = 0.3

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"{'Tipo:':<20} Vendedor")
        print(f"{'Comisión:':<20} {self.comision*100}%")
        print(f"{'Ventas realizadas:':<20} {len(self.ventas_realizadas)}")
        print("="*60)
    
    def obtener_datos(self):
        datos = super().obtener_datos()
        datos.update({
            "ventas_realizadas": self.ventas_realizadas,
            "comision": self.comision,
            "tipo": "Vendedor"
        })
        return datos
      
        
