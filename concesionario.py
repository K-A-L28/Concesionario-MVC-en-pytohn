from os import system
from venta import Venta
from detalle_compra import detalleCompra
from vendedor import Vendedor
from mecanico import Mecanico
from clientes import Cliente
from coche import Coche

class Concesionario:
    def __init__(self):
        self.productos = []
        self.empleados = []  # aquí guardamos Vendedor, Mecanico o Encargado
        self.clientes = []
        self.coches = []
        self.ventas = []  # Lista para almacenar las ventas

    # ------------------- Métodos para Vendedores -------------------
    # Método para buscar un vendedor
    def buscar_vendedor(self, dni):
        """Devuelve el índice de un vendedor por DNI o -1 si no existe"""
        for i, empleado in enumerate(self.empleados):
            if isinstance(empleado, Vendedor) and empleado.dni == dni:
                return i
        return -1

    # Metodo para registrar un vendedor
    def registro_vendedor(self, vendedor):
        """Agrega un vendedor si no existe"""
        if self.buscar_vendedor(vendedor.dni) == -1:
            self.empleados.append(vendedor)
            return True
        return False

    # Metodo para listar vendedores
    def listar_vendedores(self):
        """Muestra todos los vendedores registrados"""
        vendedores = [e for e in self.empleados if isinstance(e, Vendedor)]
        if not vendedores:
            print("La lista de vendedores está vacía...")
        else:
            print("--- Listado de vendedores ---")
            for vendedor in vendedores:
                vendedor.mostrar_datos()

    # Metodo para modificar un vendedor
    def modifica_vendedor(self, dni_vendedor):
        """Modifica los datos de un vendedor existente"""
        pos_vendedor = self.buscar_vendedor(dni_vendedor)
        if pos_vendedor == -1:
            print("Error: No se encontró el vendedor")
            return False

        vendedor = self.empleados[pos_vendedor]
        
        try:
            print("\nSeleccione el dato que desea modificar:")
            print("1. Nombre")
            print("2. Apellidos")
            print("3. Fecha de contratación")
            print("4. Salario")
            print("5. Comisión")
            print("0. Cancelar")

            opcion = input("\nIngrese su opción: ")

            if opcion == "1":
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if nuevo_nombre:
                    vendedor.nombre = nuevo_nombre
            elif opcion == "2":
                nuevos_apellidos = input("Nuevos apellidos: ").strip()
                if nuevos_apellidos:
                    vendedor.apellidos = nuevos_apellidos
            elif opcion == "3":
                from empleado import validar_fecha
                while True:
                    nueva_fecha = input("Nueva fecha de contratación (YYYY-MM-DD): ").strip()
                    if validar_fecha(nueva_fecha):
                        vendedor.fecha_contratacion = nueva_fecha
                        break
            elif opcion == "4":
                while True:
                    try:
                        nuevo_salario = float(input("Nuevo salario: "))
                        if nuevo_salario > 0:
                            vendedor.salario = nuevo_salario
                            break
                        print("El salario debe ser mayor a 0")
                    except ValueError:
                        print("Por favor ingrese un número válido")
            elif opcion == "5":
                while True:
                    try:
                        nueva_comision = float(input("Nuevo porcentaje de comisión (ej. 0.3 para 30%): "))
                        if 0 <= nueva_comision <= 1:
                            vendedor.comision = nueva_comision
                            break
                        print("La comisión debe estar entre 0 y 1 (0% a 100%)")
                    except ValueError:
                        print("Por favor ingrese un número válido")
            elif opcion == "0":
                print("Operación cancelada")
                return False
            else:
                print("Opción no válida")
                return False
                
            print("\nVendedor actualizado correctamente")
            return True
            
        except Exception as e:
            print(f"Error al modificar el vendedor: {e}")
            return False

    # ------------------------- Métodos para Mecánicos -------------------------

    # Metodo para buscar un mecanico
    def buscar_mecanico(self, dni):
        """Devuelve el índice de un mecánico por DNI o -1 si no existe"""
        for i, empleado in enumerate(self.empleados):
            if isinstance(empleado, Mecanico) and empleado.dni == dni:
                return i
        return -1

    # Metodo para registrar un mecanico
    def registro_mecanico(self, mecanico):
        """Agrega un mecánico si no existe"""
        if self.buscar_mecanico(mecanico.dni) == -1:
            self.empleados.append(mecanico)
            return True
        return False

    # Metodo para listar mecanicos
    def listar_mecanicos(self):
        """Muestra todos los mecánicos registrados"""
        mecanicos = [e for e in self.empleados if isinstance(e, Mecanico)]
        if not mecanicos:
            print("No hay mecánicos registrados...")
        else:
            print("--- Listado de mecánicos ---")
            for mecanico in mecanicos:
                mecanico.mostrar_datos()
                
    # Metodo para modificar un mecanico
    def modifica_mecanico(self, dni_mecanico):
        """Modifica los datos de un mecánico existente"""
        pos_mecanico = self.buscar_mecanico(dni_mecanico)
        if pos_mecanico == -1:
            print("Error: No se encontró el mecánico")
            return False

        mecanico = self.empleados[pos_mecanico]
        
        try:
            print("\nSeleccione el dato que desea modificar:")
            print("1. Nombre")
            print("2. Apellidos")
            print("3. Fecha de contratación")
            print("4. Salario")
            print("5. Especialidad")
            print("6. Nivel de experiencia")
            print("0. Cancelar")

            opcion = input("\nIngrese su opción: ")

            if opcion == "1":
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if nuevo_nombre:
                    mecanico.nombre = nuevo_nombre
            elif opcion == "2":
                nuevos_apellidos = input("Nuevos apellidos: ").strip()
                if nuevos_apellidos:
                    mecanico.apellidos = nuevos_apellidos
            elif opcion == "3":
                from empleado import validar_fecha
                while True:
                    nueva_fecha = input("Nueva fecha de contratación (YYYY-MM-DD): ").strip()
                    if validar_fecha(nueva_fecha):
                        mecanico.fecha_contratacion = nueva_fecha
                        break
            elif opcion == "4":
                while True:
                    try:
                        nuevo_salario = float(input("Nuevo salario: "))
                        if nuevo_salario > 0:
                            mecanico.salario = nuevo_salario
                            break
                        print("El salario debe ser mayor a 0")
                    except ValueError:
                        print("Por favor ingrese un número válido")
            elif opcion == "5":
                nueva_especialidad = input("Nueva especialidad: ").strip()
                if nueva_especialidad:
                    mecanico.especialidad = nueva_especialidad
            elif opcion == "6":
                niveles = ['Junior', 'Semi-Senior', 'Senior']
                print("\nNiveles disponibles:")
                for i, nivel in enumerate(niveles, 1):
                    print(f"{i}. {nivel}")
                while True:
                    try:
                        opcion_nivel = int(input("Seleccione el nuevo nivel: "))
                        if 1 <= opcion_nivel <= len(niveles):
                            mecanico.nivel_experiencia = niveles[opcion_nivel - 1]
                            break
                        print(f"Por favor ingrese un número entre 1 y {len(niveles)}")
                    except ValueError:
                        print("Por favor ingrese un número válido")
            elif opcion == "0":
                print("Operación cancelada")
                return False
            else:
                print("Opción no válida")
                return False
                
            print("\nMecánico actualizado correctamente")
            return True
            
        except Exception as e:
            print(f"Error al modificar el mecánico: {e}")
            return False

    # --- Métodos generales para empleados ---
    def buscar_empleado(self, dni):
        """Devuelve el índice de un empleado por DNI o -1 si no existe"""
        for i, empleado in enumerate(self.empleados):
            if empleado.dni == dni:
                return i
        return -1

    # Metodo para eliminar un empleado
    def eliminar_empleado(self, dni):
        """Elimina un empleado por DNI después de confirmación"""
        index = self.buscar_empleado(dni)
        if index == -1:
            print("Error: No se encontró el empleado")
            return False
        
        # Mostrar datos del empleado antes de eliminar
        print("\n--- Datos del empleado a eliminar ---")
        self.empleados[index].mostrar_datos()
        print("+" * 50 + "\n")
        
        while True:
            try:
                respuesta = input("¿Está seguro de eliminar a este empleado? (S/n): ").lower()
                if respuesta == 's':
                    del self.empleados[index]
                    print("Empleado eliminado correctamente")
                    return True
                elif respuesta == 'n':
                    print("Operación cancelada")
                    return False
                else:
                    raise ValueError("Respuesta no válida. Por favor ingrese 'S' para confirmar o 'n' para cancelar.")
            except ValueError as e:
                print(f"Error: {e}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Procesos del Cliente
    #Metodo para buscar un cliente repetido
    def buscar_cliente(self, dni):
        for i in range(len(self.clientes)):
            if self.clientes[i].dni == dni:
                return i
        return -1

    #Metodo para registrar un cliente
    def registro_cliente(self, cliente):
        if self.buscar_cliente(cliente.dni) == -1:
            self.clientes.append(cliente)
            return True
        return False

    #Metodo para listar a todos los clientes
    def listar_clientes(self):
        if not self.clientes:
            print("La lista esta vacia...")
        else:
            print("--- Listado de clientes ---")
            for cliente in self.clientes:
                cliente.mostrar_datos()

    #Metodo para modificar uno de los datos del vendedor 
    def modifica_cliente(self, dni_cliente):
        pos_cliente = self.buscar_cliente(dni_cliente)
        if pos_cliente != -1:
            if self.clientes[pos_cliente].dni == dni_cliente:
                try:
                    print("Seleccione la opcion que quiere modificar?")
                    print("1. Modificar el nombre del cliente")
                    print("2. Modificar el apellido del cliente")
                    print("3. Modificar el telefono del cliente")
                    print("4. Modificar el domicilio del cliente")

                    opcion = int(input("Ingrese su opcion: "))

                    if opcion == 1:
                        while True:
                            nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ").strip()
                            if not nuevo_nombre.replace(' ', '').isalpha():
                                print("Error: El nombre solo puede contener letras y espacios")
                                continue
                            if len(nuevo_nombre) < 2 or len(nuevo_nombre) > 50:
                                print("Error: El nombre debe tener entre 2 y 50 caracteres")
                            break
    
                        self.clientes[pos_cliente].nombre_cliente = nuevo_nombre
                        return True

                    elif opcion == 2:
                        while True:
                            nuevos_apellidos = input("Ingrese los nuevos apellidos del cliente: ").strip()
                            if not nuevos_apellidos.replace(' ', '').replace('.', '').isalpha():
                                print("Error: Los apellidos solo pueden contener letras, espacios y puntos")
                                continue
                            if len(nuevos_apellidos) < 2 or len(nuevos_apellidos) > 100:
                                print("Error: Los apellidos deben tener entre 2 y 100 caracteres")
                            break
                        self.clientes[pos_cliente].apellidos_cliente = nuevos_apellidos
                        return True

                    elif opcion == 3:
                        nuevo_dirección = input(f"Ingrese la nueva dirección del cliente: ")
                        self.clientes[pos_cliente].dirección_cliente = nuevo_dirección
                        return True

                    elif opcion == 4:
                        while True:
                            nuevo_telefono = input(f"Ingrese el nuevo telefono del cliente: ")
                            if not nuevo_telefono.isdigit():
                                print("Error: El telefono solo puede contener numeros")
                                continue
                            if len(nuevo_telefono) < 8 or len(nuevo_telefono) > 15:
                                print("Error: El teléfono debe tener entre 8 y 15 dígitos")
                                continue
                            break
                        nuevo_telefono = int(nuevo_telefono)
                        
                        self.clientes[pos_cliente].tel_cliente = nuevo_telefono
                        return True

                    else:
                        return False
                except ValueError:
                    print("Dato inválido")

    #Metodo para mostrar los datos de un solo cliente
    def mostrar_cliente(self, dni_cliente):
        pos_cliente = self.buscar_cliente(dni_cliente)
        if pos_cliente != -1:
            self.clientes[pos_cliente].mostrar_datos()

    #Metodo para eliminar un cliente
    def elimina_cliente(self, dni_cliente):
        pos_cliente = self.buscar_cliente(dni_cliente)
        if pos_cliente != -1:
            ver_cliente = self.mostrar_cliente(dni_cliente)
            print("++++++++++++++++++++++++++++++++++++++++++\n")
        
            while True:
                try:
                    respuesta = input(f"Esta seguro de eliminar a este cliente? (S/n): ").lower()
                    if respuesta == 's':
                        del(self.clientes[pos_cliente])
                        return True

                    elif respuesta == 'n':
                        return False
                        break
                    
                    else:
                        raise ValueError("esta respuesta no es valida")
                    
                except ValueError as e:
                        print(f"Error {e}")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ------------------- Métodos para Coches -------------------
    # Método para buscar un coche por matrícula
    def buscar_coche(self, matricula):
        """Busca un coche por su matrícula y devuelve su índice o -1 si no existe"""
        for i in range(len(self.coches)):
            if self.coches[i].matricula.lower() == matricula.lower():
                return i
        return -1

    # Método para registrar un coche
    def registro_coche(self, coche):
        if self.buscar_coche(coche.matricula) == -1:
            self.coches.append(coche)
            return True
        return False
        
        
    # Metodo para modificar un coche
    def modifica_coche(self, matricula):
        pos_coche = self.buscar_coche(matricula)
        if pos_coche == -1:
            print("Error: No se encontró un coche con esa matrícula.")
            return False
            
        coche = self.coches[pos_coche]
        
        try:
            while True:
                print("\n--- Menú de Modificación de Coche ---")
                print(f"Matrícula actual: {coche.matricula}")
                print(f"1. Modelo actual: {coche.modelo}")
                print(f"2. Marca actual: {coche.marca}")
                print(f"3. Color actual: {coche.color}")
                print(f"4. Precio actual: ${coche.precio:,.2f}" if hasattr(coche, 'precio') else "4. Precio actual: No disponible")
                print(f"5. Cantidad en stock: {coche.cantidad}" if hasattr(coche, 'cantidad') else "5. Cantidad en stock: No disponible")
                print("0. Guardar cambios y salir")
                
                opcion = input("\nSeleccione el dato a modificar (0-5): ")
                
                if opcion == "0":
                    print("\nCambios guardados exitosamente.")
                    return True
                    
                elif opcion == "1":
                    nuevo_modelo = input("Ingrese el nuevo modelo: ")
                    if nuevo_modelo.strip():
                        coche.modelo = nuevo_modelo
                        print("Modelo actualizado correctamente.")
                    else:
                        print("Error: El modelo no puede estar vacío.")
                        
                elif opcion == "2":
                    nueva_marca = input("Ingrese la nueva marca: ")
                    if nueva_marca.strip():
                        coche.marca = nueva_marca
                        print("Marca actualizada correctamente.")
                    else:
                        print("Error: La marca no puede estar vacía.")
                        
                elif opcion == "3":
                    nuevo_color = input("Ingrese el nuevo color: ")
                    if nuevo_color.strip():
                        coche.color = nuevo_color
                        print("Color actualizado correctamente.")
                    else:
                        print("Error: El color no puede estar vacío.")
                        
                elif opcion == "4":
                    while True:
                        try:
                            nuevo_precio = float(input("Ingrese el nuevo precio: "))
                            if nuevo_precio > 0:
                                coche.precio = nuevo_precio
                                print("Precio actualizado correctamente.")
                                break
                            else:
                                print("Error: El precio debe ser mayor a cero.")
                        except ValueError:
                            print("Error: Por favor ingrese un valor numérico válido.")
                            
                elif opcion == "5":
                    while True:
                        try:
                            nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
                            if nueva_cantidad >= 0:
                                coche.cantidad = nueva_cantidad
                                print("Cantidad en stock actualizada correctamente.")
                                break
                            else:
                                print("Error: La cantidad no puede ser negativa.")
                        except ValueError:
                            print("Error: Por favor ingrese un número entero válido.")
                            
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
                    
                input("\nPresione Enter para continuar...")
                
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return False
            
    #Metodo para listar coches
    def listar_coches(self):
        print("--- Listado de Coches ---")
        if not self.coches:
            print("No hay coches registrados.")
        else:
            for coche in self.coches:
                coche.mostrar_datos()

    
    #Metodo para mostrar los datos de un coche
    def mostrar_coche(self, matricula):
        pos_coche = self.buscar_coche(matricula)
        if pos_coche != -1:
            self.coches[pos_coche].mostrar_datos()

    #Metodo para eliminar un coche
    def elimina_coche(self, matricula):
        pos_coche = self.buscar_coche(matricula)
        if pos_coche != -1:
            ver_coche = self.mostrar_coche(matricula)

            while True:
                try:
                    respuesta = input("Esta seguro de eliminar este coche? (S/n)").lower()
                    if respuesta == 's':
                        del(self.coches[pos_coche])
                        return True
                    elif respuesta == 'n':
                        return False
                        break
                    else:
                        raise ValueError("esta respuesta no es valida")
                except ValueError as e:
                    print(f"Error: {e}")

# ------------------- Métodos para Ventas -------------------
    # Método para buscar una venta por ID
    def buscar_venta(self, id_venta):
        """Busca una venta por su ID y devuelve su índice o -1 si no existe"""
        for i, venta in enumerate(self.ventas):
            if venta.id_venta == id_venta:
                return i
        return -1


    def registro_venta(self, venta):
        venta_idx = self.buscar_venta(venta.id_venta)
        
        if venta_idx == -1:
            # Si no existe, agregar nueva venta
            self.ventas.append(venta)
            print(f"Venta {venta.id_venta} registrada en la lista de ventas.")
        else:
            # Si ya existe, actualizar la venta existente
            self.ventas[venta_idx] = venta
            print(f"Venta {venta.id_venta} actualizada en la lista de ventas.")
        
        # Vincular la venta al vendedor SOLO si está confirmada. Si no lo está, aseguramos que no quede asociada.
        vendedor_vinculado = False
        for empleado in self.empleados:
            if hasattr(empleado, 'ventas_realizadas') and str(empleado.dni) == str(venta.dni_vendedor):
                vendedor_vinculado = True
                if getattr(venta, 'estado', None) == 'Confirmada':
                    if venta not in empleado.ventas_realizadas:
                        empleado.ventas_realizadas.append(venta)
                        print(f"Venta {venta.id_venta} registrada en vendedor {empleado.dni}")
                    else:
                        print(f"Venta {venta.id_venta} ya estaba en el vendedor {empleado.dni}, no se duplicó.")
                else:
                    # Asegurar que ventas pendientes/anuladas no queden en el vendedor
                    empleado.ventas_realizadas = [v for v in empleado.ventas_realizadas if v.id_venta != venta.id_venta]
                break
        if not vendedor_vinculado:
            print(f"Advertencia: No se encontró un vendedor con DNI {venta.dni_vendedor}")
        
        return True

    def eliminar_venta(self, id_venta):
        """Elimina una venta por su ID y devuelve True si tuvo éxito"""
        venta_idx = self.buscar_venta(id_venta)
        if venta_idx != -1:
            del self.ventas[venta_idx]
            return True
        return False
        
    # Método para registrar un detalle de compra
    def registro_detalle_compra(self, detalle_compra):
        # Buscar la venta correspondiente
        for venta in self.ventas:
            if venta.id_venta == detalle_compra.id_compra:
                # Verificar si el detalle ya existe para actualizarlo
                for detalle_existente in venta.detalles:
                    if detalle_existente.matricula == detalle_compra.matricula:
                        detalle_existente.cantidad = detalle_compra.cantidad
                        detalle_existente.precio = detalle_compra.precio
                        return True
                # Si no existe, lo agregamos
                venta.detalles.append(detalle_compra)
                return True
        return False

    def listar_ventas(self):
        print("--- Listado de Ventas ---")
        if not self.ventas:
            print("No hay ventas registradas.")
        else:
            for venta in self.ventas:
                venta.mostrar_datos()

    def modifica_venta(self, id_venta):

        pos_venta = self.buscar_venta(id_venta)
        if pos_venta == -1:
            print("Error: No existe una venta con ese ID.")
            return False
            
        venta = self.ventas[pos_venta]
        
        try:
            while True:
                print("\n--- Menú de Modificación de venta ---")
                print(f"1. Forma de pago actual: {venta.forma_pago}")
                print(f"2. Estado actual: {venta.estado}")
                print("3. Cancelar")
                
                
                opcion = input("\nSeleccione el dato de la venta que desea modificar (1-3): ")
                # Menu para mostrar las diferentes formas de pago
                if opcion == "1":
                    system("cls")
                    print("--- Cambiar Forma de Pago ---")
                    print("\nFormas de pago disponibles:")
                    print("1. Efectivo")
                    print("2. Tarjeta de crédito")
                    print("3. Transferencia bancaria")
                    print("4. Cancelar modificación")
                    
                    try:
                        opcion_de_pago = int(input("\nSeleccione la forma de pago: "))
                        if opcion_de_pago == 1:
                            venta.forma_pago = "Efectivo"
                            print("\nForma de pago actualizada a: Efectivo")
                        elif opcion_de_pago == 2:
                            venta.forma_pago = "Tarjeta de crédito"
                            print("\nForma de pago actualizada a: Tarjeta de crédito")
                        elif opcion_de_pago == 3:
                            venta.forma_pago = "Transferencia bancaria"
                            print("\nForma de pago actualizada a: Transferencia bancaria")
                        elif opcion_de_pago == 4:
                            print("Modificación cancelada")
                            continue
                        else:
                            print("Opción no válida. No se realizaron cambios.")
                            return
                    except ValueError:
                        print("Por favor ingrese un número válido.")
                #Menu para mostrar los diferentes estados de la venta 
                elif opcion == "2":
                    system("cls")
                    print(f"--- Cambiar estado de la venta {venta.id_venta} ---")
                    print("\nEstados de la venta:")
                    print("1. Pendiente")
                    print("2. En curso")
                    print("3. Completado")
                    print("4. Cancelar modificación")
                    
                    try:
                        opcion_de_estado = int(input("\nSeleccione el estado para la venta: "))
                        if opcion_de_estado == 1:
                            venta.estado = "Pendiente"
                            print("\nEstado actualizado a: Pendiente")
                        elif opcion_de_estado == 2:
                            venta.estado = "En curso"
                            print("\nEstado actualizado a: En curso")
                        elif opcion_de_estado == 3:
                            venta.estado = "Completado"
                            print("\nEstado actualizado a: Completado")
                        elif opcion_de_estado == 4:
                            print("Modificación cancelada")
                            continue
                        else:
                            print("Opción no válida. No se realizaron cambios.")
                            return
                    except ValueError:
                        print("Por favor ingrese un número válido.")
                        
                elif opcion == "3":
                    print("Modificación cancelada")
                    return
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
                    
                input("\nPresione Enter para continuar...")
                
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return False

    def anula_venta(self, id_venta):
        pos_venta = self.buscar_venta(id_venta)
        if pos_venta != -1:
            if self.ventas[pos_venta].id_venta == id_venta:
                venta = self.ventas[pos_venta]
                estado_anterior = venta.estado
                venta.estado = "Anulada"
                print("Estado de la venta anulada")

                # Si la venta estaba confirmada, devolver el stock de cada coche involucrado
                if estado_anterior == "Confirmada":
                    for detalle in venta.detalles:
                        idx_coche = self.buscar_coche(detalle.matricula)
                        if idx_coche != -1:
                            self.coches[idx_coche].cantidad += detalle.cantidad
                        else:
                            print(f"Advertencia: No se encontró el coche con matrícula {detalle.matricula} para restaurar stock")

                # Quitar la venta del vendedor si estuviera asociada
                for empleado in self.empleados:
                    if empleado.ventas_realizadas and empleado.dni == venta.dni_vendedor:
                        empleado.ventas_realizadas = [v for v in empleado.ventas_realizadas if v.id_venta != id_venta]
                        break
                return True
            return False
        
                
                    
