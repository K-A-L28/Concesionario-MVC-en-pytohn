from os import system
from datetime import datetime
from mecanico import Mecanico
from coche import Coche
from reparacion import Reparacion
from reparacion_mecanico import ReparacionMecanico

class Taller:
    def __init__(self):
        self.reparaciones = []
        
    # Metodo para buscar una reparacion
    def buscar_reparacion(self, id_reparacion):
        for i in range(len(self.reparaciones)):
            if self.reparaciones[i].id_reparacion == id_reparacion:
                return i
        return -1

    # Metodo para registrar una reparacion
    def registro_reparacion(self, reparacion):
        if self.buscar_reparacion(reparacion.id_reparacion) == -1:
            self.reparaciones.append(reparacion)
            return True
        return False
    
    # Metodo para registrar una reparacion_mecanico
    def registro_reparacion_mecanico(self, reparacion_mecanico):
        idx = self.buscar_reparacion(reparacion_mecanico.id_reparacion)

        if idx == -1:
            return False
        # Adjunta el trabajo del mecánico a la reparación existente
        self.reparaciones[idx].agregar_trabajo(reparacion_mecanico)
        return True

# Metodos para listar las reparaciones
    # Metodo para listar todas las reparaciones
    def listar_reparaciones(self):
        print("--- Listado de Reparaciones ---")
        if not self.reparaciones:
            print("No hay reparaciones registradas.")
        else:
            for reparacion in self.reparaciones:
                reparacion.mostrar_datos()

    # Metodo para listar todas las reparaciones anuladas
    def listar_reparaciones_anuladas(self):
        print("--- Listado de Reparaciones anuladas ---")
        anuladas = [r for r in self.reparaciones if getattr(r, 'estado', None) == "Anulada"]
        if not anuladas:
            print("No hay reparaciones anuladas.")
            return
        for reparacion in anuladas:
            reparacion.mostrar_datos()

    # Metodo para listar todas las reparaciones completadas
    def listar_reparaciones_completadas(self):
        print("--- Listado de Reparaciones completadas ---")
        completadas = [r for r in self.reparaciones if getattr(r, 'estado', None) == "Completado"]
        if not completadas:
            print("No hay reparaciones completadas.")
            return
        for reparacion in completadas:
            reparacion.mostrar_datos()

    # Metodo para modificar una reparacion
    def modifica_reparacion(self, id_reparacion):
        pos_reparacion = self.buscar_reparacion(id_reparacion)
        if pos_reparacion != -1:
            if self.reparaciones[pos_reparacion].id_reparacion == id_reparacion:
                try:
                    print("Seleccione la opcion que quiere modificar?")
                    print("1. Modificar el estado de la raparación")
                    print("2. Modificar el costo de la raparación")

                    opcion = int(input("Ingrese su opcion: "))

                    if opcion == 1:
                        self.reparaciones[pos_reparacion].estado = "Completado"
                        # Guardar fecha de salida normalizada (DD/MM/AAAA)
                        self.reparaciones[pos_reparacion].fecha_salida = datetime.now().strftime("%d/%m/%Y")
                        print("Estado de la reparación completada")
                        print("Fecha de salida: ", self.reparaciones[pos_reparacion].fecha_salida)
                        return True

                    elif opcion == 2:
                        while True:
                            nuevo_costo = int(input("Ingrese el nuevo costo de la raparación: "))
                            if nuevo_costo < 0:
                                print("Error: El costo no puede ser negativo")
                                continue
                            break
                            
                        self.reparaciones[pos_reparacion].costoReparacion = nuevo_costo
                        print("Nuevo costo de la reparación: ", self.reparaciones[pos_reparacion].costoReparacion)
                        return True

                    else:
                        return False
                except ValueError:
                    print("Dato inválido")

    # Metodo para anular una reparacion
    def anular_reparacion(self, id_reparacion):
        pos_reparacion = self.buscar_reparacion(id_reparacion)
        if pos_reparacion != -1:
            if self.reparaciones[pos_reparacion].id_reparacion == id_reparacion:
                self.reparaciones[pos_reparacion].estado = "Anulada"
                print("Estado de la reparación anulada")
                return True
            return False
        
        
