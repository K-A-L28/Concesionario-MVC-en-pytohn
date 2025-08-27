class Cliente:
    def __init__(self, dni, nombre_cliente, apellidos_cliente, direccion_cliente, tel_cliente):

        self.dni = dni
        self.nombre_cliente = nombre_cliente
        self.apellidos_cliente = apellidos_cliente
        self.direccion_cliente = direccion_cliente
        self.tel_cliente = tel_cliente
  

    def mostrar_datos(self):
        print("\n" + "="*60)
        print("DATOS DEL CLIENTE".center(60))
        print("="*60)
        print(f"{'DNI:':<15} {self.dni}")
        print(f"{'Nombre:':<15} {self.nombre_cliente}")
        print(f"{'Apellidos:':<15} {self.apellidos_cliente}")
        print(f"{'Dirección:':<15} {self.direccion_cliente}")
        print(f"{'Teléfono:':<15} {self.tel_cliente}")
        print("="*60)
      
