from os import system
from datetime import datetime
# Importaciones para el concesionario
from concesionario import Concesionario
from venta import Venta
from detalle_compra import detalleCompra
from empleado import Empleado, pedir_datos_empleado
from vendedor import Vendedor
from clientes import Cliente
from coche import Coche
from coche_nuevo import CocheNuevo
from coche_usado import CocheUsado
# Importaciones para el taller
from taller import Taller
from reparacion import Reparacion
from reparacion_mecanico import ReparacionMecanico

from datos_prueba import cargar_datos_prueba

class Menu:
    def __init__(self):
        self.concesionario = Concesionario()
        self.taller = Taller()
        cargar_datos_prueba(self.concesionario, self.taller)

# -------------------------Vendedores-----------------------------------
    #Metodo que obtiene los dato del vendedor, subclase de Empleado; por eso se hace llamado de la funcion pedir_datos_empleado() para solicitar los datos que se necesitan
    def registrar_vendedor(self):
        system("cls")
        print("--- Registrar un vendedor ---")
        #Valida que el dni no se repita, se hace llamado a la funcion buscar_empleado() del archivo concesionario.py
        def validar_dni_unico(dni):
            return self.concesionario.buscar_empleado(dni) == -1
            
        dni, nombre, apellidos, fecha_contratacion, salario = pedir_datos_empleado(validar_dni_unico)

        # Crear objeto vendedor
        vendedor = Vendedor(dni, nombre, apellidos, fecha_contratacion, salario)

        if self.concesionario.registro_vendedor(vendedor) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: Vendedor registrado correctamente")
            print("+++++++++++++++++++++++++++++++++")
        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo registrar el vendedor")
            print("++++++++++++++++++++++++++")

        input("Presione cualquier tecla para continuar")

    #Listo a los vendedores
    def listado_vendedores(self):
        system("cls")
        self.concesionario.listar_vendedores()
        input("\nPresione cualquier tecla para continuar...")


    #Metodo que llama al metodo modifica_vendedor del archivo Tienda para modificar un vendedor
    def modificar_vendedores(self):
        system("cls")
        print("--- Modificar vendedor ---")
        dni_vendedor = int(input("Ingrese el DNI del vendedor que quiere modificar: "))
        if self.concesionario.modifica_vendedor(dni_vendedor) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: Vendedor modificado correctamente")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo modificar el vendedor")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")


# ----------------------Mecanico---------------------------------
    def registrar_mecanico(self):
        system("cls")
        print("--- Registrar un mecánico ---")
        
        # Validar DNI único
        def validar_dni_unico(dni):
            return self.concesionario.buscar_empleado(dni) == -1
            
        # Obtener datos básicos del empleado
        dni, nombre, apellidos, fecha_contratacion, salario = pedir_datos_empleado(validar_dni_unico)
        
        # Obtener datos específicos del mecánico
        from mecanico import Mecanico
        especialidad, nivel_experiencia = Mecanico.pedir_datos_mecanico()

        # Crear objeto mecánico
        mecanico = Mecanico(dni, nombre, apellidos, fecha_contratacion, salario, especialidad, nivel_experiencia)

        if self.concesionario.registro_mecanico(mecanico) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: Mecánico registrado correctamente")
            print("+++++++++++++++++++++++++++++++++")
        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo registrar el vendedor")
            print("++++++++++++++++++++++++++")

        input("Presione cualquier tecla para continuar")

    #Listo a los vendedores
    def listado_mecanicos(self):
        system("cls")
        self.concesionario.listar_mecanicos()
        input("\nPresione cualquier tecla para continuar...")


    #Metodo que llama al metodo modifica_vendedor del archivo Tienda para modificar un vendedor
    def modificar_mecanico(self):
        system("cls")
        print("--- Modificar vendedor ---")
        dni_mecanico = int(input("Ingrese el DNI del vendedor que quiere modificar: "))
        if self.concesionario.modifica_mecanico(dni_mecanico) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: Vendedor modificado correctamente")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo modificar el vendedor")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")


    #Metodo que llama al metodo eliminar_empleado del archivo Tienda para eliminar un vendedor
    def eliminar_empleado(self):
        system("cls")
        print("--- Eliminar vendedor ---")
        dni_vendedor = int(input("Ingrese el DNI del vendedor que quiere eliminar: "))
        if self.concesionario.eliminar_empleado(dni_vendedor) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: El vendedor fue eliminado")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo eliminar el vendedor")
            print("++++++++++++++++++++++++++")
        
        input("\nPresione cualquier tecla para continuar...")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Clientes
    #Metodo que obtiene los dato del vendedor, los instancia para enviarlos como argumento, llama al metodo registro_vendedor
    #del archivo Tienda para guardar al vendedor en una lista y devuelve una respuesta
    def registrar_clientes(self):
        system("cls")
        print("--- Registrar un cliente ---")
        while True:
            try:
                dni = input("Ingrese el DNI del cliente (solo números, 8-15 dígitos): ")
                # Validar que el DNI tenga entre 8 y 15 dígitos
                if not dni.isdigit() or len(dni) < 8 or len(dni) > 15:
                    print("Error: El DNI debe contener solo números y tener entre 8 y 15 dígitos")
                    continue
                dni = int(dni)

                if self.concesionario.buscar_cliente(dni) != -1:
                    print("Error: Ya existe un cliente con ese DNI")
                    continue
            except ValueError:
                print("Error: Por favor ingrese un número válido")
                continue
            break

        while True:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            if not nombre_cliente.replace(' ', '').isalpha():
                print("Error: El nombre solo puede contener letras y espacios")
                continue
            if len(nombre_cliente) < 2 or len(nombre_cliente) > 50:
                print("Error: El nombre debe tener entre 2 y 50 caracteres")
                continue
            break
    
        while True:
            apellidos_cliente = input("Ingrese los apellidos del cliente: ").strip()
            if not apellidos_cliente.replace(' ', '').replace('.', '').isalpha():
                print("Error: Los apellidos solo pueden contener letras, espacios y puntos")
                continue
            if len(apellidos_cliente) < 2 or len(apellidos_cliente) > 100:
                print("Error: Los apellidos deben tener entre 2 y 100 caracteres")
                continue
            break

        direccion_cliente = input("Ingrese el domicilo del cliente: ")
        
        while True:
            try:
                tel_cliente = input("Ingrese el telefono del cliente: ")
                if not tel_cliente.isdigit():
                    print("Error: El telefono solo puede contener numeros")
                    continue
                if len(tel_cliente) < 8 or len(tel_cliente) > 15:
                    print("Error: El teléfono debe tener entre 8 y 15 dígitos")
                    continue
                tel_cliente = int(tel_cliente)
                break
                
            except ValueError:
                print("Error: Por favor ingrese un número válido")

        cliente = Cliente(dni, nombre_cliente, apellidos_cliente, direccion_cliente, tel_cliente)

        if self.concesionario.registro_cliente(cliente) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: Cliente registrado correctamente")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo registrar el cliente")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")


    #Listo a los clientes
    def listado_clientes(self):
        system("cls")
        self.concesionario.listar_clientes()
        input("\nPresione cualquier tecla para continuar...")

        #Metodo que llama al metodo modifica_cliente del archivo concesionario.py para modificar un cliente
    def modificar_cliente(self):
        system("cls")
        dni_cliente = int(input("Ingrese el DNI del cliente que quiere modificar: "))

        if self.concesionario.modifica_cliente(dni_cliente) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: El cliente modificado correctamente")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo modificar el cliente")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")


    #Metodo que llama al metodo elimina_cliente del archivo concesionario.py para eliminar un cliente
    def eliminar_cliente(self):
        system("cls")
        id_cliente = int(input("Ingrese el id del cliente que desea eliminar: "))

        if self.concesionario.elimina_cliente(id_cliente) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: El cliente fue eliminado")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo eliminar el cliente")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")


# ----------------------Coche---------------------------------
    def registrar_coche(self):
        system("cls")
        print("--- Registrar un coche ---")
        print("1. Coche Nuevo")
        print("2. Coche Usado")
        
        while True:
            try:
                opcion = int(input("\nSeleccione el tipo de coche (1-2): "))
                if opcion not in [1, 2]:
                    print("Opción inválida. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido.")
        
        # Datos comunes a ambos tipos de coche
        while True:
            try:
                matricula = input("\nIngrese la matrícula: ").strip().upper()
                if not matricula:
                    print("La matrícula no puede estar vacía.")
                    continue
                # Verificar si ya existe un coche con esta matrícula
                if self.concesionario.buscar_coche(matricula) != -1:
                    print("Error: Ya existe un coche con esta matrícula.")
                    input("\nPresione cualquier tecla para continuar...")
                    continue
                break
            except Exception as e:
                print(f"Error: {e}")
                continue
        
        modelo = input("Ingrese el modelo: ").strip()
        marca = input("Ingrese la marca: ").strip()
        color = input("Ingrese el color: ").strip()
        
        while True:
            try:
                precio = float(input("Ingrese el precio: "))
                if precio <= 0:
                    print("El precio debe ser mayor a 0.")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido para el precio.")
        
        # Crear el tipo de coche correspondiente
        if opcion == 1:  # Coche Nuevo
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad en stock: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un número entero válido para la cantidad.")
            
            coche = CocheNuevo(matricula, modelo, marca, color, precio, cantidad)

            if self.concesionario.registro_coche(coche) == True:
                print("+++++++++++++++++++++++++++++++++")
                print("Info: Coche registrado correctamente")
                print("+++++++++++++++++++++++++++++++++")
            else:
                print("++++++++++++++++++++++++++")
                print("Error: No se pudo registrar el coche")
                print("++++++++++++++++++++++++++")

            input("\nPresione cualquier tecla para continuar...")

        else:  # Coche Usado
            while True:
                try:
                    kilometraje = int(input("Ingrese el kilometraje: "))
                    if kilometraje < 0:
                        print("El kilometraje no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("Por favor ingrese un número entero válido para el kilometraje.")
            
            # Para coches usados, por defecto cantidad = 1 ya que son vehículos únicos
            coche = CocheUsado(matricula, modelo, marca, color, precio, kilometraje, cantidad=1)
            
            if self.concesionario.registro_coche(coche) == True:
                print("+++++++++++++++++++++++++++++++++")
                print("Info: Coche registrado correctamente")
                print("+++++++++++++++++++++++++++++++++")
            else:
                print("++++++++++++++++++++++++++")
                print("Error: No se pudo registrar el coche")
                print("++++++++++++++++++++++++++")

            input("\nPresione cualquier tecla para continuar...")
            
    # Metodo para listar coches
    def listado_coches(self):
        system("cls")
        self.concesionario.listar_coches()
        
        input("\nPresione cualquier tecla para continuar...")

    # Metodo para modificar un coche
    def modificar_coche(self):
        system("cls")
        while True:
            try:
                matricula = input("\nIngrese la matrícula: ").strip().upper()
                if not matricula:
                    print("La matrícula no puede estar vacía.")
                    continue
            except Exception as e:
                print(f"Error: {e}")
                continue
            break
        
        if self.concesionario.modifica_coche(matricula) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: El coche modificado correctamente")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo modificar el coche")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")

    # Metodo para eliminar un coche
    def eliminar_coche(self):
        system("cls")
        matricula = input("Ingrese la matrícula del coche que desea eliminar: ")
        if self.concesionario.elimina_coche(matricula) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: El coche fue eliminado")
            print("+++++++++++++++++++++++++++++++++")
        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo eliminar el coche")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")

# ------------------------------------------Ventas-----------------------------------------------
    # Metodo para registrar una venta
    def registrar_venta(self):
        system("cls")
        print("--- Registrar una venta ---")

        # Obtener ID de venta
        while True:
            try:
                id_venta = int(input("Ingrese el ID de la venta: "))
                if self.concesionario.buscar_venta(id_venta) != -1:
                    print("\nYa existe una venta con ese ID")
                    input("\nPresione cualquier tecla para continuar...")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número entero válido para el ID.")
                continue
        
        # Obtener DNI del vendedor
        while True:
            try:
                dni_vendedor = int(input("Ingrese el DNI del vendedor: "))
                vendedor_encontrado = False
                for empleado in self.concesionario.empleados:
                    if empleado.dni == dni_vendedor and isinstance(empleado, Vendedor):
                        vendedor_encontrado = True
                        break
                if not vendedor_encontrado:
                    print("Error: No se encontró un vendedor con este DNI o el empleado no es un vendedor.")
                    input("\nPresione cualquier tecla para continuar...")
                    return
                break
            except ValueError:
                print("Por favor ingrese un DNI válido.")
        
        # Obtener DNI del cliente
        while True:
            try:
                dni_cliente = int(input("Ingrese el DNI del cliente: "))
                cliente_encontrado = False
                for cliente in self.concesionario.clientes:
                    if cliente.dni == dni_cliente:
                        cliente_encontrado = True
                        break
                if not cliente_encontrado:
                    print("Error: No se encontró un cliente con este DNI.")
                    input("\nPresione cualquier tecla para continuar...")
                    return
                break
            except ValueError:
                print("Por favor ingrese un DNI válido.")
        

        # Obtener forma de pago
        while True:
            try:
                print("\nFormas de pago disponibles:")
                print("1. Efectivo")
                print("2. Tarjeta de crédito")
                print("3. Transferencia bancaria")
                forma_pago = int(input("Seleccione la forma de pago (1-3): "))
                if forma_pago not in [1, 2, 3]:
                    print("Por favor ingrese un número entero válido para la forma de pago.")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número entero válido para la forma de pago.")
        
        # Crear la venta
        formas_pago = {
            1: "Efectivo",
            2: "Tarjeta de crédito",
            3: "Transferencia bancaria"
        }
        forma_pago_str = formas_pago.get(forma_pago, "Desconocido")
        venta = Venta(id_venta, dni_vendedor, dni_cliente, forma_pago_str)
        
        # Registrar la venta primero
        if not self.concesionario.registro_venta(venta):
            print("Error: No se pudo registrar la venta.")
            input("\nPresione cualquier tecla para continuar...")
            return
            
        # Agregar coches a la venta
        while True:
            system("cls")
            print("--- Agregar coche a la venta ---")
            print("1. Agregar coche")
            print("2. Finalizar la venta")
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    # Mostrar lista de coches disponibles
                    print("\n--- Coches disponibles ---")
                    if not self.concesionario.coches:
                        print("No hay coches registrados en el sistema.")
                        input("\nPresione cualquier tecla para continuar...")
                        break
                        
                    for i, coche in enumerate(self.concesionario.coches, 1):
                        print(f"{i}. {coche.marca} {coche.modelo} - Matrícula: {coche.matricula} - Precio: ${coche.precio} - Stock: {coche.cantidad}")
                    
                    try:
                        coche_idx = int(input("\nSeleccione el número del coche: ")) - 1
                        if coche_idx < 0 or coche_idx >= len(self.concesionario.coches):
                            print("Número de coche inválido.")
                            input("\nPresione cualquier tecla para continuar...")
                            continue
                            
                        coche = self.concesionario.coches[coche_idx]
                        
                        if coche.cantidad <= 0:
                            print("No hay unidades disponibles de este coche.")
                            input("\nPresione cualquier tecla para continuar...")
                            continue
                            
                        try:
                            cantidad = int(input(f"Ingrese la cantidad (disponible: {coche.cantidad}): "))
                            if cantidad <= 0:
                                print("La cantidad debe ser mayor a cero.")
                                input("\nPresione cualquier tecla para continuar...")
                                continue
                                
                            if cantidad > coche.cantidad:
                                print(f"No hay suficientes unidades. Disponibles: {coche.cantidad}")
                                input("\nPresione cualquier tecla para continuar...")
                                continue
                            
                            # Crear y registrar el detalle de la compra
                            detalle = detalleCompra(id_venta, coche.matricula, coche.precio, cantidad)
                            if self.concesionario.registro_detalle_compra(detalle):
                                coche.cantidad -= cantidad  # Actualizar stock
                                print(f"\n{cantidad} unidad(es) de {coche.marca} {coche.modelo} agregada(s) a la venta.")
                            else:
                                print("Error al agregar el detalle de la venta.")
                            
                        except ValueError:
                            print("Por favor ingrese una cantidad válida.")
                            
                    except ValueError:
                        print("Por favor ingrese un número de coche válido.")
                        
                elif opcion == 2:
                    if not venta.detalles:
                        print("Venta finalizada.")
                        input("\nPresione cualquier tecla para continuar...")
                        continue
                    
                    # Variable para controlar si la venta fue confirmada
                    venta_confirmada = False
                    # Marcar que estamos en modo edición
                    venta.es_edicion = True
                    
                    while not venta_confirmada:
                        # Mostrar resumen de la venta
                        system("cls")
                        print("=== PREVISUALIZACIÓN DE LA VENTA ===")
                        print("Revise los datos de la venta antes de confirmar:")
                        print("-" * 50)
                        venta.mostrar_datos()
                        print("\nOpciones:")
                        print("1. Cambiar método de pago")
                        print("2. Modificar cantidad de un vehículo")
                        print("3. Eliminar un vehículo")
                        print("4. Confirmar y registrar venta")
                        print("5. Cancelar venta")
                        
                        try:
                            opcion_resumen = int(input("\nSeleccione una opción: "))
                            
                            if opcion_resumen == 1:  # Cambiar método de pago
                                print("\nMétodos de pago disponibles:")
                                print("1. Efectivo (10% descuento)")
                                print("2. Tarjeta de crédito (5% recargo)")
                                print("3. Transferencia bancaria (sin recargo)")
                                try:
                                    opcion_pago = int(input("Seleccione el método de pago: "))
                                    if opcion_pago == 1:
                                        venta.forma_pago = "Efectivo"
                                        print("Método de pago actualizado a: Efectivo (10% descuento)")
                                    elif opcion_pago == 2:
                                        venta.forma_pago = "Tarjeta de crédito"
                                        print("Método de pago actualizado a: Tarjeta de crédito (5% recargo)")
                                    elif opcion_pago == 3:
                                        venta.forma_pago = "Transferencia bancaria"
                                        print("Método de pago actualizado a: Transferencia bancaria (sin recargo)")
                                    else:
                                        print("Opción no válida. No se realizaron cambios.")
                                except ValueError:
                                    print("Por favor ingrese un número válido.")
                                input("\nPresione cualquier tecla para continuar...")
                                
                            elif opcion_resumen == 2:  # Modificar cantidad
                                if not venta.detalles:
                                    print("No hay vehículos para modificar.")
                                    input("\nPresione cualquier tecla para continuar...")
                                    continue
                                    
                                print("\nVehículos en la venta:")
                                for i, detalle in enumerate(venta.detalles, 1):
                                    coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                                    if coche:
                                        print(f"{i}. {coche.marca} {coche.modelo} - Cantidad: {detalle.cantidad}")
                                
                                try:
                                    idx = int(input("\nSeleccione el número del vehículo a modificar: ")) - 1
                                    if 0 <= idx < len(venta.detalles):
                                        detalle = venta.detalles[idx]
                                        coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                                        if coche:
                                            nueva_cantidad = int(input(f"Nueva cantidad (disponible: {coche.cantidad + detalle.cantidad}): "))
                                            if 0 < nueva_cantidad <= (coche.cantidad + detalle.cantidad):
                                                # Devolver la cantidad anterior al stock
                                                coche.cantidad += detalle.cantidad
                                                # Actualizar la cantidad
                                                coche.cantidad -= nueva_cantidad
                                                detalle.cantidad = nueva_cantidad
                                                print("Cantidad actualizada correctamente.")
                                            else:
                                                print("Cantidad no válida.")
                                    else:
                                        print("Número de vehículo no válido.")
                                except ValueError:
                                    print("Por favor ingrese un número válido.")
                                input("\nPresione cualquier tecla para continuar...")
                                
                            elif opcion_resumen == 3:  # Eliminar vehículo
                                if not venta.detalles:
                                    print("No hay vehículos para eliminar.")
                                    input("\nPresione cualquier tecla para continuar...")
                                    continue
                                    
                                print("\nVehículos en la venta:")
                                for i, detalle in enumerate(venta.detalles, 1):
                                    coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                                    if coche:
                                        print(f"{i}. {coche.marca} {coche.modelo} - Cantidad: {detalle.cantidad}")
                                
                                try:
                                    idx = int(input("\nSeleccione el número del vehículo a eliminar: ")) - 1
                                    if 0 <= idx < len(venta.detalles):
                                        detalle = venta.detalles.pop(idx)
                                        # Devolver la cantidad al stock
                                        coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                                        if coche:
                                            coche.cantidad += detalle.cantidad
                                        print("Vehículo eliminado de la venta.")
                                    else:
                                        print("Número de vehículo no válido.")
                                except ValueError:
                                    print("Por favor ingrese un número válido.")
                                input("\nPresione cualquier tecla para continuar...")
                                
                            elif opcion_resumen == 4:  # Confirmar venta
                                if not venta.detalles:
                                    print("No se puede confirmar una venta sin vehículos.")
                                    input("\nPresione cualquier tecla para continuar...")
                                    continue
                                
                                # Mostrar resumen final
                                system("cls")
                                print("=== RESUMEN FINAL DE LA VENTA ===")
                                venta.mostrar_datos()
                                
                                # Pedir confirmación final
                                confirmacion = input("\n¿Está seguro que desea registrar esta venta? (s/n): ").lower()
                                if confirmacion == 's':
                                    try:
                                        # Verificar si la venta ya existe (excluyendo la venta actual si es una edición)
                                        venta_idx = self.concesionario.buscar_venta(venta.id_venta)
                                        if venta_idx != -1 and (not hasattr(venta, 'es_edicion') or not venta.es_edicion):
                                            print("\nError: Ya existe una venta con este ID. Por favor, intente nuevamente.")
                                            input("\nPresione cualquier tecla para continuar...")
                                            continue
                                        
                                        # Actualizar el estado de la venta a Confirmada
                                        venta.estado = "Confirmada"
                                        venta.fecha_actualizacion = datetime.now()
                                        
                                        # Registrar la venta (esto ahora también actualiza el vendedor)
                                        if self.concesionario.registro_venta(venta):
                                            # Registrar los detalles de la venta
                                            for detalle in venta.detalles:
                                                if not self.concesionario.registro_detalle_compra(detalle):
                                                    print(f"Error al registrar el detalle para el vehículo con matrícula {detalle.matricula}")
                                            
                                            print("\n¡Venta registrada y confirmada exitosamente!")
                                            input("\nPresione cualquier tecla para volver al menú principal...")
                                            return  # Salir del método registrar_venta
                                        else:
                                            print("\nError inesperado al registrar la venta.")
                                    except Exception as e:
                                        print(f"\nError al procesar la venta: {str(e)}")
                                else:
                                    print("\nVenta no confirmada. Puede seguir realizando cambios.")
                                    input("\nPresione cualquier tecla para continuar...")
                                    
                            elif opcion_resumen == 5:  # Cancelar venta
                                # Preguntar confirmación
                                confirmacion = input("\n¿Está seguro que desea cancelar la venta? (s/n): ").lower()
                                if confirmacion == 's':
                                    # Devolver todas las cantidades al stock
                                    for detalle in venta.detalles:
                                        coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                                        if coche:
                                            coche.cantidad += detalle.cantidad

                                    # Actualizar el vendedor - eliminar la venta de sus ventas realizadas
                                    vendedor_idx = self.concesionario.buscar_vendedor(int(venta.dni_vendedor))
                                    if vendedor_idx != -1:
                                        vendedor = self.concesionario.empleados[vendedor_idx]
                                        # Buscar la venta por ID y eliminarla
                                        for i, v in enumerate(vendedor.ventas_realizadas):
                                            if v.id_venta == venta.id_venta:
                                                del vendedor.ventas_realizadas[i]
                                                break
                                    
                                    # Eliminar la venta si ya fue registrada
                                    if hasattr(venta, 'id_venta'):
                                        self.concesionario.eliminar_venta(venta.id_venta)
                                    
                                    print("\nVenta cancelada. Se han restablecido las cantidades en stock y eliminado el registro de la venta.")
                                    input("\nPresione cualquier tecla para volver al menú principal...")
                                    return  # Salir completamente del método registrar_venta
                                else:
                                    print("\nOperación cancelada. La venta no se ha cancelado.")
                                    input("\nPresione cualquier tecla para continuar...")
                                
                            else:
                                print("Opción no válida.")
                                input("\nPresione cualquier tecla para continuar...")
                                
                        except ValueError:
                            print("Por favor ingrese un número válido.")
                            input("\nPresione cualquier tecla para continuar...")
                            
                    # Verificar que hay vehículos antes de confirmar
                    if not venta.detalles:
                        print("No se puede confirmar una venta sin vehículos.")
                        input("\nPresione cualquier tecla para continuar...")
                        continue  # Volver al menú principal
                        
                    # Solo mostrar el resumen si la venta se confirmó
                    if opcion_resumen == 4:  # Solo si se confirmó la venta
                        print("=== Resumen de la Venta ===")
                        print(f"ID Venta: {venta.id_venta}")
                        print(f"Cliente DNI: {venta.dni_cliente}")
                        print(f"Vendedor DNI: {venta.dni_vendedor}")
                        print(f"Fecha: {venta.fecha_venta.strftime('%d/%m/%Y %H:%M:%S')}")
                        print(f"Forma de pago: {venta.forma_pago}")
                        print("\n--- Detalles de la compra ---")
                        total = 0
                    for detalle in venta.detalles:
                        subtotal = detalle.precio * detalle.cantidad
                        total += subtotal
                        print(f"- {detalle.cantidad} x Matrícula {detalle.matricula}: ${detalle.precio} c/u = ${subtotal}")
                        
                    print(f"\nTotal a pagar: ${total}")
                    print("\n¡Venta registrada exitosamente!")
                    input("\nPresione cualquier tecla para continuar...")
                    break
                    
                else:
                    print("Opción no válida.")
                    
            except ValueError:
                print("Por favor ingrese una opción válida.")
                
            input("\nPresione cualquier tecla para continuar...")
        
    # Metodo para realizar modificaciones en el registro de la venta
    # Metodo para agregar vehiculo a la venta
    def agregar_vehiculo_a_venta_en_registro(self, venta):
        system("cls")
        print("--- Agregar Vehículo a la Venta ---")
        
        # Mostrar vehículos disponibles
        print("\nVehículos disponibles:")
        vehiculos_disponibles = [c for c in self.concesionario.coches if c.cantidad > 0]
        
        if not vehiculos_disponibles:
            print("No hay vehículos disponibles en el inventario.")
            return
            
        for i, coche in enumerate(vehiculos_disponibles, 1):
            print(f"{i}. {coche.marca} {coche.modelo} - Matrícula: {coche.matricula} - Cantidad disponible: {coche.cantidad} - ${coche.precio}")
        
        try:
            opcion = int(input("\nSeleccione el número del vehículo a agregar: ")) - 1
            if 0 <= opcion < len(vehiculos_disponibles):
                coche = vehiculos_disponibles[opcion]
                cantidad = int(input(f"Ingrese la cantidad (disponible: {coche.cantidad}): "))
                
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a cero.")
                    return
                    
                if cantidad > coche.cantidad:
                    print("No hay suficiente stock disponible.")
                    return
                    
                # Verificar si el vehículo ya está en la venta
                for detalle in venta.detalles:
                    if detalle.matricula == coche.matricula:
                        print("Este vehículo ya está en la venta. Use la opción de modificar cantidad.")
                        return
                
                # Agregar el vehículo a la venta
                nuevo_detalle = detalleCompra(venta.id_venta, coche.matricula, cantidad, coche.precio)
                venta.detalles.append(nuevo_detalle)
                coche.cantidad -= cantidad
                print("\nVehículo agregado correctamente.")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor ingrese un número válido.")
            
    def modificar_cantidad_vehiculo_en_registro(self, venta):
        if not venta.detalles:
            print("No hay vehículos en esta venta para modificar.")
            return
            
        print("\nVehículos en la venta:")
        for i, detalle in enumerate(venta.detalles, 1):
            coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
            if coche:
                print(f"{i}. {coche.marca} {coche.modelo} - Cantidad actual: {detalle.cantidad}")
        
        try:
            opcion = int(input("\nSeleccione el número del vehículo a modificar: ")) - 1
            if 0 <= opcion < len(venta.detalles):
                detalle = venta.detalles[opcion]
                coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                
                if coche:
                    print(f"\nCantidad actual: {detalle.cantidad}")
                    print(f"Stock disponible: {coche.cantidad + detalle.cantidad}")
                    
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    
                    if nueva_cantidad <= 0:
                        print("La cantidad debe ser mayor a cero.")
                        return
                        
                    diferencia = nueva_cantidad - detalle.cantidad
                    
                    if diferencia > coche.cantidad:
                        print("No hay suficiente stock disponible.")
                        return
                        
                    # Actualizar cantidades
                    coche.cantidad += detalle.cantidad  # Devolver la cantidad anterior
                    coche.cantidad -= nueva_cantidad    # Restar la nueva cantidad
                    detalle.cantidad = nueva_cantidad   # Actualizar el detalle
                    
                    print("\nCantidad actualizada correctamente.")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor ingrese un número válido.")
            
    def eliminar_vehiculo_de_venta_en_registro(self, venta):
        if not venta.detalles:
            print("No hay vehículos en esta venta para eliminar.")
            return
            
        print("\nVehículos en la venta:")
        for i, detalle in enumerate(venta.detalles, 1):
            coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
            if coche:
                print(f"{i}. {coche.marca} {coche.modelo} - Cantidad: {detalle.cantidad}")
        
        try:
            opcion = int(input("\nSeleccione el número del vehículo a eliminar: ")) - 1
            if 0 <= opcion < len(venta.detalles):
                detalle = venta.detalles.pop(opcion)
                # Devolver la cantidad al stock
                coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                if coche:
                    coche.cantidad += detalle.cantidad
                print("\nVehículo eliminado de la venta.")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor ingrese un número válido.")
            
    def cambiar_forma_pago_en_registro(self, venta):
        system("cls")
        print("--- Cambiar Forma de Pago ---")
        print("\nFormas de pago disponibles:")
        print("1. Efectivo (10% descuento)")
        print("2. Tarjeta de crédito (5% de recargo)")
        print("3. Transferencia bancaria (sin recargo)")
        
        try:
            opcion = int(input("\nSeleccione la forma de pago: "))
            if opcion == 1:
                venta.forma_pago = "Efectivo"
                print("\nForma de pago actualizada a: Efectivo (10% de descuento)")
            elif opcion == 2:
                venta.forma_pago = "Tarjeta de crédito"
                print("\nForma de pago actualizada a: Tarjeta de crédito (5% de recargo)")
            elif opcion == 3:
                venta.forma_pago = "Transferencia bancaria"
                print("\nForma de pago actualizada a: Transferencia bancaria (sin recargo)")
            else:
                print("Opción no válida. No se realizaron cambios.")
                return
        except ValueError:
            print("Por favor ingrese un número válido.")
        
    def modificar_venta_en_registro(self, id_venta):
        system("cls")
        print("--- Modificar Venta ---")
        
        # Buscar la venta existente
        venta_idx = self.concesionario.buscar_venta(id_venta)
        if venta_idx == -1:
            print("Error: No se encontró la venta especificada.")
            input("\nPresione cualquier tecla para continuar...")
            return
            
        venta_original = self.concesionario.ventas[venta_idx]
        
        # Crear una copia de la venta para editar
        venta_editada = Venta(venta_original.id_venta)
        venta_editada.dni_cliente = venta_original.dni_cliente
        venta_editada.dni_vendedor = venta_original.dni_vendedor
        venta_editada.fecha_venta = venta_original.fecha_venta
        venta_editada.forma_pago = venta_original.forma_pago
        venta_editada.detalles = [detalle for detalle in venta_original.detalles]
        venta_editada.es_edicion = True  # Marcar que estamos editando
        
        # Restaurar las cantidades al stock antes de editar
        for detalle in venta_editada.detalles:
            coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
            if coche:
                coche.cantidad += detalle.cantidad
        
        # Ahora proceder con la edición
        while True:
            system("cls")
            print("=== Editar Venta ===")
            print(f"ID Venta: {venta_editada.id_venta}")
            print(f"Cliente DNI: {venta_editada.dni_cliente}")
            print(f"Vendedor DNI: {venta_editada.dni_vendedor}")
            print(f"Forma de pago: {venta_editada.forma_pago}")
            print("\n--- Detalles de la compra ---")
            
            if not venta_editada.detalles:
                print("No hay vehículos en esta venta.")
            else:
                for i, detalle in enumerate(venta_editada.detalles, 1):
                    coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                    if coche:
                        print(f"{i}. {coche.marca} {coche.modelo} - Cantidad: {detalle.cantidad} - ${detalle.precio} c/u")
            
            print("\nOpciones:")
            print("1. Agregar vehículo")
            print("2. Modificar cantidad")
            print("3. Eliminar vehículo")
            print("4. Cambiar forma de pago")
            print("5. Guardar cambios")
            print("6. Cancelar")
            
            try:
                opcion = int(input("\nSeleccione una opción: "))
                
                if opcion == 1:  # Agregar vehículo
                    self.agregar_vehiculo_a_venta_en_registro(venta_editada)
                elif opcion == 2:  # Modificar cantidad
                    self.modificar_cantidad_vehiculo_en_registro(venta_editada)
                elif opcion == 3:  # Eliminar vehículo
                    self.eliminar_vehiculo_de_venta_en_registro(venta_editada)
                elif opcion == 4:  # Cambiar forma de pago
                    self.cambiar_forma_pago_en_registro(venta_editada)
                elif opcion == 5:  # Guardar cambios
                    if not venta_editada.detalles:
                        print("No se puede guardar una venta sin vehículos.")
                        input("\nPresione cualquier tecla para continuar...")
                        continue
                        
                    # Actualizar la venta original con los cambios
                    venta_original.detalles = venta_editada.detalles
                    venta_original.forma_pago = venta_editada.forma_pago
                    venta_original.fecha_venta = venta_editada.fecha_venta
                    
                    # Actualizar el stock (ya restauramos las cantidades al inicio)
                    for detalle in venta_original.detalles:
                        coche = next((c for c in self.concesionario.coches if c.matricula == detalle.matricula), None)
                        if coche:
                            coche.cantidad -= detalle.cantidad
                    
                    print("\n¡Venta actualizada exitosamente!")
                    input("\nPresione cualquier tecla para continuar...")
                    return
                    
                elif opcion == 6:  # Cancelar
                    # Restaurar las cantidades al stock (ya se restauraron al inicio)
                    print("\nEdición de venta cancelada.")
                    input("\nPresione cualquier tecla para continuar...")
                    return
                else:
                    print("Opción no válida.")
                    
            except ValueError:
                print("Por favor ingrese un número válido.")
                
            input("\nPresione cualquier tecla para continuar...")

    # Metodo para listar ventas
    def listar_ventas(self):
        system("cls")
        self.concesionario.listar_ventas()
        input("\nPresione cualquier tecla para continuar...")

    # Metodo para modificar la venta
    def modificar_venta(self):
        system("cls")
        print("--- Modificar Venta ---")

        while True:
            try:
                id_venta = int(input("Ingrese el id de la venta: "))
                if self.concesionario.buscar_venta(id_venta) == -1:
                    print("Error: No existe venta con ese ID")
                    continue
            except Exception as e:
                print(f"Error: {e}")
                continue
            break
        
        resultado = self.concesionario.modifica_venta(id_venta)
        if resultado is True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: La venta fue modificada correctamente")
            print("+++++++++++++++++++++++++++++++++")
        elif resultado is False:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo modificar la venta")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")

    # Metodo para anular una venta
    def anular_venta(self):
        system("cls")
        print("--- Anular Venta ---")

        while True:
            try:
                id_venta = int(input("Ingrese el id de la venta: "))
                if self.concesionario.buscar_venta(id_venta) == -1:
                    print("Error: No existe venta con ese ID")
                    continue
            except Exception as e:
                print(f"Error: {e}")
                continue
            break
        
        if self.concesionario.anula_venta(id_venta) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: La venta fue anulada correctamente")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo anular la venta")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")


# ------------------------------------------Modulo del taler-------------------------------------
    def registrar_reparacion(self):
        system("cls")
        print("--- Registrar reparación ---")
        
        # Validar ID de reparación
        while True:
            try:
                id_reparacion = int(input("Ingrese el ID de la reparación: "))
                if id_reparacion <= 0:
                    print("Error: El ID debe ser un número positivo")
                    continue
                # Validar que el id no exista
                if self.taller.buscar_reparacion(id_reparacion) != -1:
                    print("Error: Ya existe una reparación con ese ID")
                    continue
            except ValueError:
                print("Error: Por favor ingrese un número válido")
                continue
            break

        # Validar fecha de registro de la reparación
        while True:
            try:
                fecha_input = input("Ingrese la fecha de registro de la reparación (DD/MM/AAAA) o presione Enter para usar la fecha actual: ").strip()
                if not fecha_input:
                    # Usar fecha actual
                    fecha_registro = datetime.now().strftime("%d/%m/%Y")
                    print(f"Usando fecha actual: {fecha_registro}")
                    break
                else:
                    # Validar formato de fecha
                    fecha_norm = fecha_input.replace('-', '/').replace('.', '/').strip()
                    fecha_registro_obj = datetime.strptime(fecha_norm, "%d/%m/%Y")
                    # Verificar que la fecha no sea futura
                    if fecha_registro_obj > datetime.now():
                        print("Error: La fecha no puede ser futura")
                        continue
                    # Guardar la fecha normalizada (DD/MM/AAAA)
                    fecha_registro = fecha_norm
                    break
            except ValueError:
                print("Error: Formato de fecha inválido. Use DD/MM/AAAA")
                continue

        # Validar DNI del cliente
        while True:
            dni_cliente = int(input("Ingrese el DNI del cliente: "))
                
            if self.concesionario.buscar_cliente(dni_cliente) == -1:
                print("Error: No existe un cliente registrado con ese DNI")
                continue
            break

        # Validar fecha de entrada del vehículo
        while True:
            try:
                entrada_input = input("Ingrese la fecha de entrada del vehículo (DD/MM/AAAA) o presione Enter para usar la misma fecha de registro: ").strip()
                if not entrada_input:
                    fecha_entrada = fecha_registro
                    print(f"Usando fecha de registro: {fecha_registro}")
                    break
                else:
                    fecha_norm = entrada_input.replace('-', '/').replace('.', '/').strip()
                    fecha_entrada_obj = datetime.strptime(fecha_norm, "%d/%m/%Y")
                    fecha_registro_obj = datetime.strptime(fecha_registro, "%d/%m/%Y")
                    if fecha_entrada_obj > datetime.now():
                        print("Error: La fecha de entrada no puede ser futura")
                        continue
                    if fecha_entrada_obj > fecha_registro_obj:
                        print("Error: La fecha de entrada no puede ser posterior a la fecha de registro")
                        continue
                    fecha_entrada = fecha_norm
                    break
            except ValueError:
                print("Error: Formato de fecha inválido. Use DD/MM/AAAA")
                continue

        # Validar matrícula del coche
        while True:
            matricula_coche = input("Ingrese la matrícula del coche: ").strip().upper()
            if self.concesionario.buscar_coche(matricula_coche) == -1:
                print("Error: No existe un coche registrado con esa matricula")
                continue
            break

        # Validar descripción
        while True:
            descripcion = input("Ingrese la descripción de la reparación: ").strip()
            if not descripcion:
                print("Error: La descripción no puede estar vacía")
                continue
            if len(descripcion) < 10:
                print("Error: La descripción debe tener al menos 10 caracteres")
                continue
            if len(descripcion) > 500:
                print("Error: La descripción no puede exceder 500 caracteres")
                continue
            break

        # Estado por defecto en 'Pendiente' luego se puede modificar
        estado = 'Pendiente'

        # Validar costo de reparación
        while True:
            try:
                costo_input = input("Ingrese el costo de la reparación (o presione Enter para $0.00): ").strip()
                if not costo_input:
                    costoReparacion = 0.0
                    break
                else:
                    costoReparacion = float(costo_input)
                    if costoReparacion < 0:
                        print("Error: El costo no puede ser negativo")
                        continue
                    if costoReparacion > 1000000:
                        print("Error: El costo parece demasiado alto. Verifique el valor")
                        continue
                    break
            except ValueError:
                print("Error: Por favor ingrese un número válido")
                continue

        # Mostrar resumen antes de crear la reparación
        print("\n" + "="*60)
        print("RESUMEN DE LA REPARACIÓN".center(60))
        print("="*60)
        print(f"{'ID Reparación:':<20} {id_reparacion}")
        print(f"{'Fecha:':<20} {fecha_registro}")
        print(f"{'DNI Cliente:':<20} {dni_cliente}")
        print(f"{'Matrícula Coche:':<20} {matricula_coche}")
        print(f"{'Entrada:':<20} {fecha_entrada}")
        print(f"{'Estado:':<20} {estado}")
        print(f"{'Costo:':<20} ${costoReparacion:,.2f}")
        print("-"*60)
        print("DESCRIPCIÓN:")
        print(f"{descripcion}")
        print("="*60)

        # Confirmar registro
        while True:
            confirmacion = input("\n¿Desea registrar esta reparación? (s/n): ").lower()
            if confirmacion in ['s', 'si', 'sí']:
                try:
                    # Crear objeto reparación (fecha_salida se deja None inicialmente)
                    reparacion = Reparacion(
                        id_reparacion=id_reparacion,
                        fecha_registro=fecha_registro,
                        dni_cliente=dni_cliente,
                        matricula_coche=matricula_coche,
                        descripcion=descripcion,
                        estado=estado,
                        costoReparacion=costoReparacion,
                        fecha_entrada=fecha_entrada,
                        fecha_salida=None,
                    )
                    
                    # Registrar la reparación
                    if self.taller.registro_reparacion(reparacion):
                        print("\n+++++++++++++++++++++++++++++++++")
                        print("Info: Reparación registrada correctamente")
                        print("+++++++++++++++++++++++++++++++++")
                        
                        # Preguntar si desea agregar mecánicos ahora
                        agregar = input("\n¿Desea asignar mecánicos y registrar tareas ahora? (s/n): ").lower()
                        if agregar in ['s', 'si', 'sí']:
                            self.registrar_reparacion_mecanico(id_reparacion)
                        else:
                            print("\nLa reparación quedó pendiente sin mecánicos asignados.")
                        
                    else:
                        print("\n++++++++++++++++++++++++++")
                        print("Error: No se pudo registrar la reparación")
                        print("++++++++++++++++++++++++++")
                    break
                except Exception as e:
                    print(f"\nError al crear la reparación: {str(e)}")
                    break
            elif confirmacion in ['n', 'no']:
                print("\nRegistro de reparación cancelado")
                break
            else:
                print("Por favor responda 's' para sí o 'n' para no")

# Metodo para agregar los trabajos realizados por los mecanico
    def registrar_reparacion_mecanico(self, id_reparacion=None):
        system("cls")
        print("--- Registrar trabajo de mecánico ---")
        
        # Si no recibimos ID, preguntamos
        if id_reparacion is None:
            while True:
                try:
                    id_reparacion = int(input("Ingrese el ID de la reparación: "))
                    if id_reparacion <= 0:
                        print("Error: El ID debe ser positivo")
                        continue
                    if self.taller.buscar_reparacion(id_reparacion) == -1:
                        print("Error: No existe reparación con ese ID")
                        continue
                except ValueError:
                    print("Error: Ingrese un número válido")
                    continue
                break
        else:
            # Validar que exista
            if self.taller.buscar_reparacion(id_reparacion) == -1:
                print("Error: No existe reparación con ese ID")
                input("\nPresione cualquier tecla para continuar...")
                return
        
        # Validar mecánico
        while True:
            dni_mecanico = int(input("Ingrese el DNI del mecánico asignado: "))
            if self.concesionario.buscar_mecanico( dni_mecanico) == -1:
                print("Error: No existe un empleado con ese DNI")
                continue
            break

        # Tarea realizada
        while True:
            tarea_realizada = input("Ingrese la tarea realizada (mínimo 5 caracteres): ").strip()
            if not tarea_realizada:
                print("Error: La tarea no puede estar vacía")
                continue
            if len(tarea_realizada) < 5:
                print("Error: La tarea debe ser más descriptiva")
                continue
            break

        # Horas trabajadas
        while True:
            try:
                horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
                if horas_trabajadas <= 0:
                    print("Error: Debe ser mayor a 0")
                    continue
                if horas_trabajadas > 100:
                    print("Error: Demasiadas horas, verifique")
                    continue
            except ValueError:
                print("Error: Ingrese un número válido")
                continue
            break

        # Fecha asignación (opcional actual)
        while True:
            fecha_input = input("Ingrese fecha de asignación (DD/MM/AAAA) o Enter para actual: ").strip()
            if not fecha_input:
                fecha_asignacion = datetime.now().strftime("%d/%m/%Y")
                print(f"Usando fecha actual: {fecha_asignacion}")
                break
            else:
                try:
                    # Acepta separadores '-', '/', '.' y normaliza a '/'
                    fecha_norm = fecha_input.replace('-', '/').replace('.', '/').strip()
                    fecha_obj = datetime.strptime(fecha_norm, "%d/%m/%Y")
                    if fecha_obj > datetime.now():
                        print("Error: La fecha no puede ser futura")
                        continue
                    # Normalizar salida a DD/MM/AAAA
                    fecha_asignacion = fecha_obj.strftime("%d/%m/%Y")
                    break
                except ValueError:
                    print("Error: Fecha inválida. Use DD/MM/AAAA (ej.: 27/08/2025)")
                    continue

        # Resumen antes de confirmar
        print("\n" + "="*60)
        print("RESUMEN DEL TRABAJO".center(60))
        print("="*60)
        print(f"{'ID Reparación:':<25} {id_reparacion}")
        print(f"{'DNI Mecánico:':<25} {dni_mecanico}")
        print(f"{'Fecha asignación:':<25} {fecha_asignacion}")
        print(f"{'Horas trabajadas:':<25} {horas_trabajadas}")
        print("-"*60)
        print("TAREA REALIZADA:")
        print(f"{tarea_realizada}")
        print("="*60)
        
        # Confirmar
        while True:
            confirmacion = input("\n¿Desea registrar este trabajo? (s/n): ").lower()
            if confirmacion in ['s','si','sí']:
                try:
                    reparacion_mec = ReparacionMecanico(
                        id_reparacion, dni_mecanico, tarea_realizada, 
                        horas_trabajadas, fecha_asignacion
                    )
                    if self.taller.registro_reparacion_mecanico(reparacion_mec):
                        print("\n+++++++++++++++++++++++++++++++++")
                        print("Info: Trabajo registrado correctamente")
                        print("+++++++++++++++++++++++++++++++++")
                    else:
                        print("\n++++++++++++++++++++++++++")
                        print("Error: No se pudo registrar el trabajo")
                        print("++++++++++++++++++++++++++")
                except Exception as e:
                    print(f"\nError al crear la ficha de trabajo: {str(e)}")
                break
            elif confirmacion in ['n','no']:
                print("\nRegistro cancelado")
                break
            else:
                print("Por favor responda 's' para sí o 'n' para no")

        input("\nPresione cualquier tecla para continuar...")

    # Metodo para listar las reparaciones
    def listado_reparaciones(self):
        system("cls")
        self.taller.listar_reparaciones()
        input("\nPresione cualquier tecla para continuar...")

    # Metodo para modificar las reparaciones
    def modificar_reparacion(self):
        system("cls")
        print("--- Modificar Reparación ---")

        while True:
            try:
                id_reparacion = int(input("\nIngrese el id de la reparacion: "))
                if self.taller.buscar_reparacion(id_reparacion) == -1:
                    print("Error: No existe reparacion con ese ID")
                    continue
            except Exception as e:
                print(f"Error: {e}")
                continue
            break
        
        if self.taller.modifica_reparacion(id_reparacion) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: La reparacion modificado correctamente")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo modificar la reparacion")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")

    # Metodo para anular las reparaciones
    def anular_reparacion(self):
        system("cls")
        print("--- Anular Reparación ---")

        while True:
            try:
                id_reparacion = int(input("\nIngrese el id de la reparacion: "))
                if self.taller.buscar_reparacion(id_reparacion) == -1:
                    print("Error: No existe reparacion con ese ID")
                    continue
            except Exception as e:
                print(f"Error: {e}")
                continue
            break
        
        if self.taller.anular_reparacion(id_reparacion) == True:
            print("+++++++++++++++++++++++++++++++++")
            print("Info: La reparacion fue anulada correctamente")
            print("+++++++++++++++++++++++++++++++++")

        else:
            print("++++++++++++++++++++++++++")
            print("Error: No se pudo anular la reparacion")
            print("++++++++++++++++++++++++++")

        input("\nPresione cualquier tecla para continuar...")

    # Metodo para listar solo reparaciones anuladas
    def listado_reparaciones_anuladas(self):
        system("cls")
        self.taller.listar_reparaciones_anuladas()
        input("\nPresione cualquier tecla para continuar...")

    # Metodo para listar solo reparaciones completadas
    def listado_reparaciones_completadas(self):
        system("cls")
        self.taller.listar_reparaciones_completadas()
        input("\nPresione cualquier tecla para continuar...")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def mostrar_menu_principal(self):
        while True:
            system("cls")
            print("=== Menú Principal ===")
            print("a. Ir a Concesionario")
            print("b. Ir a Taller")
            print("c. Salir")
            try:
                opcion = input("\nDigite una opción: ").lower()

                if opcion == 'a':
                    self.mostrar_menu_concesionario()
                elif opcion == 'b':
                    self.mostrar_menu_taller()
                elif opcion == 'c':
                    print("\n¡Gracias por usar el sistema!")
                    break
                else:
                    print("\nError - Opción no válida")
                    input("Presione Enter para continuar...")

            except Exception as e:
                print(f"\nError: {str(e)}")
                input("Presione Enter para continuar...")

    # Método para mostrar las opciones del concesionario
    def mostrar_menu_concesionario(self):
        while True:
            system("cls")
            print("+++++++++++++++++ Menú del Concesionario +++++++++++++++")
            print("\n- - Empleados - -")
            print("a. Registrar vendedor")
            print("b. Listar vendedores")
            print("c. Modificar vendedor")
            print("d. Registrar mecánico")
            print("e. Listar mecánicos")
            print("f. Modificar mecánico")
            print("g. Eliminar empleado")
            
            print("\n- - Clientes - -")
            print("h. Registrar cliente")
            print("i. Listar clientes")
            print("j. Modificar cliente")
            print("k. Eliminar cliente")

            print("\n- - Coches - -")
            print("l. Registrar coche")
            print("m. Listar coches")
            print("n. Modificar coche")
            print("o. Eliminar coche")
            
            print("\n- - Ventas - -")
            print("p. Registrar venta")
            print("q. Listar ventas")
            print("r. Modificar venta") 
            print("s. Anular venta")            
            
            print("\n- - Otros - -")
            print("t. Volver al menú principal")
            print("z. Salir del sistema")

            try:
                opcion = input("\nDigite una opción: ").lower()

                if opcion == 'a':
                    self.registrar_vendedor()
                elif opcion == 'b':
                    self.listado_vendedores()
                elif opcion == 'c':
                    self.modificar_vendedores()
                elif opcion == 'd':
                    self.registrar_mecanico()
                elif opcion == 'e':
                    self.listado_mecanicos()
                elif opcion == 'f':
                    self.modificar_mecanico()
                elif opcion == 'g':
                    self.eliminar_empleado()

                elif opcion == 'h':
                    self.registrar_clientes()
                elif opcion == 'i':
                    self.listado_clientes()
                elif opcion == 'j':
                    self.modificar_cliente()
                elif opcion == 'k':
                    self.eliminar_cliente()

                elif opcion == 'l':
                    self.registrar_coche()
                elif opcion == 'm':
                    self.listado_coches()
                elif opcion == 'n':
                    self.modificar_coche()
                elif opcion == 'o':
                    self.eliminar_coche()
                elif opcion == 'p':
                    self.registrar_venta()
                elif opcion == 'q':
                    self.listar_ventas()
                elif opcion == 'r':
                    self.modificar_venta()
                elif opcion == 's':
                    self.anular_venta()

                elif opcion == 't':
                    break  # Volver al menú principal
                elif opcion == 'z':
                    print("\n¡Gracias por usar el sistema del concesionario!")
                    exit()  # Salir completamente del programa
                else:
                    print("\nError - Opción no válida")
                    input("Presione Enter para continuar...")

            except Exception as e:
                print(f"\nError: {str(e)}")
                input("Presione Enter para continuar...")

    def mostrar_menu_taller(self):
        while True:
            system("cls")
            print("=== Menú del taller ===")
            print("a. Registrar reparación")
            print("b. Registrar trabajo de mecánico")
            print("c. Listar reparaciones")
            print("d. Listar reparaciones anuladas")
            print("e. Listar reparaciones completadas")
            print("f. Modificar reparación")
            print("g. Anular reparación")
            print("h. Volver al menú principal")
            print("z. Salir del sistema")
            try:
                opcion = input("\nDigite una opción: ").lower()

                if opcion == 'a':
                    self.registrar_reparacion()
                elif opcion == 'b':
                    self.registrar_reparacion_mecanico()
                elif opcion == 'c':
                    self.listado_reparaciones()
                elif opcion == 'd':
                    self.listado_reparaciones_anuladas()
                elif opcion == 'e':
                    self.listado_reparaciones_completadas()
                elif opcion == 'f':
                    self.modificar_reparacion()
                elif opcion == 'g':
                    self.anular_reparacion()
                elif opcion == 'h':
                    break  # Volver al menú principal
                elif opcion == 'z':
                    print("\n¡Gracias por usar el sistema del taller!")
                    exit()  # Salir completamente del programa
                else:
                    print("\nError - Opción no válida")
                    input("Presione Enter para continuar...")

            except Exception as e:
                print(f"\nError: {str(e)}")
                input("Presione Enter para continuar...")

# si el nombre es main, traiga este objeto
if __name__ == '__main__':
    menu = Menu() #Hago una instancia de la clase menu
    menu.mostrar_menu_principal()

cargar_datos_prueba(menu.concesionario, menu.taller)