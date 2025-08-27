from os import system
from mecanico import Mecanico
from coche import Coche
from reparacion import Reparacion
from reparacion_mecanico import ReparacionMecanico

class Taller:
    def __init__(self):
        self.reparaciones = []
        
    def buscar_reparacion(self, id_reparacion):
        for i in range(len(self.reparaciones)):
            if self.reparaciones[i].id_reparacion == id_reparacion:
                return i
        return -1

    def registro_reparacion(self, reparacion):
        if self.buscar_reparacion(reparacion.id_reparacion) == -1:
            self.reparaciones.append(reparacion)
            return True
        return False
    

    def listar_reparaciones(self):
        print("--- Listado de Coches ---")
        if not self.reparaciones:
            print("No hay coches registrados.")
        else:
            for reparacion in self.reparaciones:
                reparacion.mostrar_datos()