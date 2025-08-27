class Reparacion:
    def __init__(self, id_reparacion, fecha, dni_cliente, matricula_coche, descripcion, estado, costoReparacion):
        self.id_reparacion = id_reparacion
        self.fecha = fecha
        self.dni_cliente = dni_cliente
        self.matricula_coche = matricula_coche
        self.descripcion = descripcion
        self.estado = estado
        self.costoReparacion = costoReparacion
        self.trabajos = []

    def agregar_trabajo(self, trabajo):
        self.trabajos.append(trabajo)
    
    def mostrar_datos(self):
        """Muestra la información completa de la reparación."""
        print("\n" + "="*60)
        print("FICHA DE REPARACIÓN".center(60))
        print("="*60)
        print(f"{'ID Reparación:':<20} {self.id_reparacion}")
        print(f"{'Fecha:':<20} {self.fecha}")
        print(f"{'DNI Cliente:':<20} {self.dni_cliente}")
        print(f"{'Matrícula Coche:':<20} {self.matricula_coche}")
        print(f"{'Estado:':<20} {self.estado}")
        print(f"{'Costo Reparación:':<20} ${self.costoReparacion:,.2f}")
        print("-"*60)
        print("DESCRIPCIÓN:")
        print(f"{self.descripcion}")
        print("="*60)
        for t in r.trabajos:
            print(f"  - Mecánico {t.dni_mecanico}: {t.tarea_realizada} ({t.horas_trabajadas}h, tarifa ${t.tarifa_hora}) en {t.fecha_asignacion.strftime('%d/%m/%Y')}")


