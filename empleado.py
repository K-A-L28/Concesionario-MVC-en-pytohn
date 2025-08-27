class Empleado:
    def __init__(self, dni, nombre, apellidos, fecha_contratacion, salario):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_contratacion = fecha_contratacion
        self.salario = salario

    def mostrar_datos(self):
        print("\n" + "="*60)
        print("DATOS DEL EMPLEADO".center(60))
        print("="*60)
        print(f"{'DNI:':<20} {self.dni}")
        print(f"{'Nombre:':<20} {self.nombre}")
        print(f"{'Apellidos:':<20} {self.apellidos}")
        print(f"{'Fecha Contratación:':<20} {self.fecha_contratacion}")
        print(f"{'Salario:':<20} ${self.salario:,.2f}")
        print("="*60)
    
    def obtener_datos(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "fecha_contratacion": self.fecha_contratacion,
            "salario": self.salario
        }

def validar_fecha(fecha_str):
    """Valida que la fecha tenga el formato YYYY-MM-DD"""
    from datetime import datetime
    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        # Verificar que la fecha no sea en el futuro
        if fecha > datetime.now():
            print("Error: La fecha no puede ser futura")
            return False
        return True
    except ValueError:
        print("Error: Formato de fecha inválido. Use YYYY-MM-DD")
        return False

def pedir_datos_empleado(validar_dni_unico=None):
    while True:
        try:
            dni = input("Ingrese el DNI (solo números, 8-15 dígitos): ")
            # Validar que el DNI tenga entre 8 y 15 dígitos
            if not dni.isdigit() or len(dni) < 8 or len(dni) > 15:
                print("Error: El DNI debe contener solo números y tener entre 8 y 15 dígitos")
                continue
            dni = int(dni)
            
            # Validar que el DNI no exista en el sistema
            if validar_dni_unico and not validar_dni_unico(dni):
                print("Error: Ya existe un empleado con este DNI en el sistema")
                continue
                
            break
        except ValueError:
            print("Error: Por favor ingrese solo números para el DNI")
    
    while True:
        nombre = input("Ingrese el nombre: ").strip()
        if not nombre.replace(' ', '').isalpha():
            print("Error: El nombre solo puede contener letras y espacios")
            continue
        if len(nombre) < 2 or len(nombre) > 50:
            print("Error: El nombre debe tener entre 2 y 50 caracteres")
            continue
        break
    
    while True:
        apellidos = input("Ingrese los apellidos: ").strip()
        if not apellidos.replace(' ', '').replace('.', '').isalpha():
            print("Error: Los apellidos solo pueden contener letras, espacios y puntos")
            continue
        if len(apellidos) < 2 or len(apellidos) > 100:
            print("Error: Los apellidos deben tener entre 2 y 100 caracteres")
            continue
        break
    
    while True:
        fecha_contratacion = input("Ingrese la fecha de contratación (YYYY-MM-DD): ").strip()
        if validar_fecha(fecha_contratacion):
            break
    
    while True:
        try:
            salario = float(input("Ingrese el salario: "))
            if salario <= 0:
                print("Error: El salario debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido para el salario")
    
    return dni, nombre, apellidos, fecha_contratacion, salario
