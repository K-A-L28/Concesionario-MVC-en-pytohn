class Reparacion:
    def __init__(self, id_reparacion, fecha_registro, dni_cliente, matricula_coche, descripcion, estado, costoReparacion, fecha_entrada=None, fecha_salida=None):
        self.id_reparacion = id_reparacion
        self.fecha_registro = fecha_registro
        self.dni_cliente = dni_cliente
        self.matricula_coche = matricula_coche
        self.descripcion = descripcion
        self.estado = estado
        self.costoReparacion = costoReparacion        
        # Fechas (opcionales)
        self.fecha_entrada = fecha_entrada if fecha_entrada is not None else fecha_registro
        self.fecha_salida = fecha_salida  # Se mantiene None al inicio
        self.trabajos = []

    def agregar_trabajo(self, trabajo):
        self.trabajos.append(trabajo)
    
    def mostrar_datos(self):
        """Muestra la información completa de la reparación."""
        print("\n" + "="*60)
        print("FICHA DE REPARACIÓN".center(60))
        print("="*60)
        print(f"{'ID Reparación:':<20} {self.id_reparacion}")
        print(f"{'Fecha (registro):':<20} {self.fecha_registro}")
        print(f"{'DNI Cliente:':<20} {self.dni_cliente}")
        print(f"{'Matrícula Coche:':<20} {self.matricula_coche}")
        print(f"{'Estado:':<20} {self.estado}")
        print(f"{'Costo Reparación:':<20} ${self.costoReparacion:,.2f}")
        print(f"{'Entrada:':<20} {self.fecha_entrada}")
        print(f"{'Salida:':<20} {self.fecha_salida if self.fecha_salida is not None else 'Pendiente'}")
        print("-"*60)
        print("DESCRIPCIÓN:")
        print(f"{self.descripcion}")
        print("="*60)
        print("HISTORIAL DE TRABAJOS EN LA REPARACIÓN".center(60))
        print("="*60)

        for t in self.trabajos:
            fecha_txt = t.fechaAsignacion.strftime('%d/%m/%Y') if hasattr(t.fechaAsignacion, 'strftime') else str(t.fechaAsignacion)
            print(f"  - Mecánico {t.dni_mecanico}: {t.tareaRealizada} ({t.horasTrabajadas}h) en {fecha_txt}")


