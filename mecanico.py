from empleado import Empleado

class Mecanico(Empleado):
    def __init__(self, dni, nombre, apellidos, fecha_contratacion, salario, especialidad, nivel_experiencia):
        super().__init__(dni, nombre, apellidos, fecha_contratacion, salario)
        self.especialidad = especialidad
        self.nivel_experiencia = nivel_experiencia

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"{'Tipo:':<20} Mecánico")
        print(f"{'Especialidad:':<20} {self.especialidad}")
        print(f"{'Nivel Experiencia:':<20} {self.nivel_experiencia}")
        print("="*60)
    
    def obtener_datos(self):
        """
        Devuelve un diccionario con todos los datos del mecánico
        """
        datos = super().obtener_datos()
        datos.update({
            "especialidad": self.especialidad,
            "nivel_experiencia": self.nivel_experiencia,
            "tipo": "Mecánico"
        })
        return datos
    
    @staticmethod
    def pedir_datos_mecanico():
        """
        Solicita al usuario los datos específicos del mecánico
        Retorna una tupla con (especialidad, nivel_experiencia)
        """
        # Obtener especialidad
        while True:
            especialidad = input("\nIngrese la especialidad del mecánico: ").strip()
            if especialidad and len(especialidad) <= 50:
                break
            print("Error: La especialidad no puede estar vacía y debe tener máximo 50 caracteres")
        
        # Obtener nivel de experiencia
        niveles_validos = ['Junior', 'Semi-Senior', 'Senior']
        while True:
            print("\nNiveles de experiencia disponibles:")
            for i, nivel in enumerate(niveles_validos, 1):
                print(f"{i}. {nivel}")
            
            try:
                opcion = input("Seleccione el nivel de experiencia (1-3): ")
                if not opcion:  # Verificar si la entrada está vacía
                    raise ValueError("La entrada no puede estar vacía")
                opcion = int(opcion)
                if 1 <= opcion <= len(niveles_validos):
                    nivel_experiencia = niveles_validos[opcion - 1]
                    break
                print(f"Error: Por favor ingrese un número entre 1 y {len(niveles_validos)}")
            except ValueError as e:
                print(f"Error: {str(e) if str(e) else 'Por favor ingrese un número válido'}")
        
        return (especialidad, nivel_experiencia)
