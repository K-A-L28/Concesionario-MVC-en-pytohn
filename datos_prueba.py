from datetime import datetime
from clientes import Cliente
from coche import Coche
from coche_nuevo import CocheNuevo
from coche_usado import CocheUsado
from vendedor import Vendedor
from mecanico import Mecanico

def cargar_datos_prueba(concesionario, taller):
    """Carga datos de prueba en el sistema del concesionario y taller"""
    
    # Crear clientes de prueba
    clientes = [
        Cliente(12345678, "Juan", "Pérez García", "Calle Falsa 123", "600123456"),
        Cliente(23456789, "María", "López Martínez", "Avenida Siempreviva 456", "600234567"),
        Cliente(34567890, "Carlos", "González Ruiz", "Plaza Mayor 789", "600345678"),
        Cliente(45678901, "Ana", "Sánchez Díaz", "Calle del Sol 12", "600456789"),
        Cliente(56789012, "Pedro", "Martín Gómez", "Paseo de la Castellana 34", "600567890")
    ]
    
    # Añadir clientes al concesionario
    for cliente in clientes:
        concesionario.registro_cliente(cliente)
    
    # Crear coches nuevos de prueba
    coches_nuevos = [
        CocheNuevo("1234ABC", "Model S", "Tesla", "Rojo", 85000.0, 5),
        CocheNuevo("2345BCD", "ID.3", "Volkswagen", "Azul", 380, 6),
        CocheNuevo("3456CDE", "Model 3", "Tesla", "Negro", 55000.0, 4),
        CocheNuevo("4567DEF", "ID.4", "Volkswagen", "Verde", 450, 7),
        CocheNuevo("5678EFG", "Model X", "Tesla", "Plateado", 120000.0, 3)
    ]
    
    # Añadir coches nuevos al concesionario
    for coche in coches_nuevos:
        concesionario.registro_coche(coche)
    
    # Crear coches usados de prueba
    coches_usados = [
        CocheUsado("6789GHI", "Model S", "Tesla", "Rojo", 85000.0, 5),
        CocheUsado("7890JKL", "ID.3", "Volkswagen", "Azul", 380, 6),
        CocheUsado("8901MNO", "Model 3", "Tesla", "Negro", 55000.0, 4),
        CocheUsado("9012PQR", "ID.4", "Volkswagen", "Verde", 450, 7),
        CocheUsado("0123STU", "Model X", "Tesla", "Plateado", 120000.0, 3)
    ]

    for coche in coches_usados:
        concesionario.registro_coche(coche)

    # Crear vendedores de prueba
    vendedores = [
        Vendedor(12345678, "Juan", "Pérez García", "2022-01-01", 1000.0),
        Vendedor(23456789, "María", "López Martínez", "2022-02-01", 1200.0),
        Vendedor(34567890, "Carlos", "González Ruiz", "2022-03-01", 1400.0),
        Vendedor(45678901, "Ana", "Sánchez Díaz", "2022-04-01", 1600.0),
        Vendedor(56789012, "Pedro", "Martín Gómez", "2022-05-01", 1800.0)
    ]

    # Añadir vendedores al concesionario
    for vendedor in vendedores:
        concesionario.registro_vendedor(vendedor)

    # Crear mecanicos de prueba
    mecanicos = [
        Mecanico(12345678, "Juan", "Pérez García", "2022-01-01", 1000.0, "Electrónica", "Junior"),
        Mecanico(23456789, "María", "López Martínez", "2022-02-01", 1200.0, "Mecánica", "Senior"),
        Mecanico(34567890, "Carlos", "González Ruiz", "2022-03-01", 1400.0, "Electrónica", "Junior"),
        Mecanico(45678901, "Ana", "Sánchez Díaz", "2022-04-01", 1600.0, "Mecánica", "Senior"),
        Mecanico(56789012, "Pedro", "Martín Gómez", "2022-05-01", 1800.0, "Electrónica", "Junior")
    ]

    # Añadir mecanicos al concesionario
    for mecanico in mecanicos:
        
        concesionario.registro_mecanico(mecanico)