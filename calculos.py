# Funciones para leer, validar y resumir las ventas de ventas.csv
import csv
from datetime import date


COLUMNAS = ["fecha", "producto", "precio"]
IVA = 0.21



def leer_ventas(ruta):
    # Lee el CSV y devuelve una lista de ventas ya validadas
    with open(ruta, newline="", encoding="utf-8-sig") as f:
        lector = csv.DictReader(f)
        if lector.fieldnames != COLUMNAS:
            raise ValueError(f"Columnas inesperadas: {lector.fieldnames}")
        return [validar_venta(fila) for fila in lector]


def validar_venta(fila):
    # Comprueba una fila: fecha AAAA-MM-DD y precio mayor que cero
    date.fromisoformat(fila["fecha"])
    precio = float(fila["precio"])
    if precio <= 0:
        raise ValueError(f"Precio no válido: {precio}")
    return {"fecha": fila["fecha"], "producto": fila["producto"], "precio": precio}


def total(ventas):
    # Suma los precios y redondea a 2 decimales
    return round(sum(v["precio"] for v in ventas), 2)


def total_por_producto(ventas):
    # Agrupa por producto, por ejemplo {"cafe": 3.0, "te": 1.2}
    resumen = {}
    for v in ventas:
        resumen[v["producto"]] = round(resumen.get(v["producto"], 0) + v["precio"], 2)
    return resumen


def con_iva(precio):
    # Añade el IVA a un precio
    return round(precio * (1 + IVA), 2)
