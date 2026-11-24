# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Nombre del estudiante: Pedro Pablo Giraldo Triana
# Identificación: 1022404897
# Grupo: 213022_864
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación (Código: 213022) - UNAD
# Fase 5 - Evaluación Final POA (Problema 3: Reabastecimiento de Inventario)
# Código Fuente: autoría propia
# -----------------------------------------------------------------------------


def calcular_cantidad_pedir(stock_actual: int, stock_minimo: int) -> int:
    """
    Determina la cantidad exacta de unidades a pedir para un artículo.

    Parámetros:
        stock_actual (int): Cantidad de unidades disponibles actualmente.
        stock_minimo (int): Cantidad mínima requerida en inventario.

    Retorna:
        int: Unidades faltantes si stock_actual < stock_minimo, o 0 en caso contrario.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


def generar_informe_reabastecimiento(matriz_inventario: list) -> None:
    """
    Recorre la matriz de inventario y muestra el nombre de cada artículo
    junto con la cantidad exacta que debe ser solicitada.
    """
    print("=" * 72)
    print("             INFORME DE REABASTECIMIENTO DE INVENTARIO")
    print("=" * 72)
    print(f"{'ARTÍCULO':<28} | {'ACTUAL':<8} | {'MÍNIMO':<8} | {'CANTIDAD A PEDIR':<18}")
    print("-" * 72)

    # R2 y R3: Recorrer cada fila de la matriz y calcular la cantidad a pedir
    for fila in matriz_inventario:
        codigo = fila[0]
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]

        cantidad_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)

        # R4: Mostrar el nombre del artículo y la cantidad exacta a solicitar
        print(
            f"{nombre:<28} | {stock_actual:<8} | {stock_minimo:<8} | {cantidad_pedir} unidades"
        )

    print("=" * 72)


def main() -> None:
    # R1: Matriz de inventario con al menos 5 artículos (6 artículos registrados)
    # Formato por fila: [Código, Nombre del artículo, Stock actual, Stock mínimo requerido]
    inventario = [
        ["ART-001", "Teclado Mecánico", 4, 10],       # Stock menor al mínimo -> Pedir 6
        ["ART-002", "Mouse Inalámbrico", 15, 10],     # Stock mayor al mínimo -> Pedir 0
        ["ART-003", "Monitor 24 pulgadas", 3, 8],     # Stock menor al mínimo -> Pedir 5
        ["ART-004", "Cable HDMI 2m", 12, 12],         # Stock igual al mínimo -> Pedir 0
        ["ART-005", "Memoria USB 64GB", 2, 15],       # Stock menor al mínimo -> Pedir 13
        ["ART-006", "Diadema", 13, 9],                # Stock mayor al mínimo -> Pedir 0
    ]

    generar_informe_reabastecimiento(inventario)


if __name__ == "__main__":
    main()