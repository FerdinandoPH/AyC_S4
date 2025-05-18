from copy import deepcopy
from typing import Tuple
import pandas as pd
def ej3_cambio_billetes(objetivo: int, valores_moneda: list, unidades_moneda: list) -> list:
    '''
    >>> ej3_cambio_billetes(10, [1, 5, 10], [2, 2, 2])
    [0, 0, 1]

    >>> ej3_cambio_billetes(10, [1, 5, 10], [2, 2, 0])
    [0, 2, 0]

    >>> ej3_cambio_billetes(2, [5, 10, 20], [5, 5, 5])
    [inf, inf, inf]

    >>> ej3_cambio_billetes(34, [1, 3, 7, 11], [5, 3, 1, 2])
    [2, 1, 1, 2]

    >>> ej3_cambio_billetes(2, [1, 5, 10], [2, 2, 2])
    [2, 0, 0]

    >>> ej3_cambio_billetes(50, [1, 5, 10], [2, 2, 2])
    [inf, inf, inf]
    '''
    valores_moneda_filtrados = []
    unidades_moneda_filtradas = []
    for i in range(len(unidades_moneda)):
        if unidades_moneda[i] > 0:
            valores_moneda_filtrados.append(valores_moneda[i])
            unidades_moneda_filtradas.append(unidades_moneda[i])
    valores_moneda = valores_moneda_filtrados
    unidades_moneda = unidades_moneda_filtradas
    cantidades_monedas = dict(zip(valores_moneda, unidades_moneda))
    print("\nSe busca obtener", objetivo, "con el mínimo número de las siguientes monedas disponibles", cantidades_monedas, "\n")
    c = [[{i: 0 for i in valores_moneda} for _ in range(objetivo + 1)] for _ in range(len(valores_moneda))]
    for i in range(len(cantidades_monedas)):
        for j in range(1, objetivo + 1):
            if i == 0:
                if j < valores_moneda[i] or 1 + c[i][j-valores_moneda[i]][valores_moneda[i]] > cantidades_monedas[valores_moneda[i]]:
                    c[i][j][valores_moneda[i]] = float('inf')
                else:
                    c[i][j][valores_moneda[i]] = 1 + c[i][j-valores_moneda[i]][valores_moneda[i]]
            else:
                if j < valores_moneda[i]:
                    c[i][j] = deepcopy(c[i-1][j])
                else:
                    nuevo_posible_valor = deepcopy(c[i][j-valores_moneda[i]])
                    nuevo_posible_valor[valores_moneda[i]] += 1
                    if nuevo_posible_valor[valores_moneda[i]] > cantidades_monedas[valores_moneda[i]]:
                        nuevo_posible_valor = deepcopy(c[i-1][j-valores_moneda[i]])
                        nuevo_posible_valor[valores_moneda[i]] += 1
                    c[i][j] = deepcopy(min(c[i-1][j], nuevo_posible_valor, key=lambda x: sum(x.values())))
    print("Matriz de soluciones:\n")
    imprimir_matriz_formateada(c)
    return c[-1][-1]
def imprimir_matriz_formateada(matriz):
    pd.set_option('display.max_rows', None)  # Mostrar todas las filas
    pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
    pd.set_option('display.width', 1000)  # Ajustar el ancho de la salida
    pd.set_option('display.colheader_justify', 'center')  # Centrar encabezados de columnas
    df = pd.DataFrame(matriz)
    print(df)
def subcadena_maxima(a: str, b: str) -> Tuple[int, str]:
    '''
    subcadena_maxima
    Dadas dos cadenas compuestas por 0s y 1s, devuelve la longitud de la subcadena común más larga y la subcadena misma.
    Los dígitos de la subcadena no tienen que ser consecutivos en la cadena original, pero deben estar en el mismo orden.

    >>> subcadena_maxima("0", "1111")
    (0, '')

    >>> subcadena_maxima("10001", "1")
    (1, '1')

    >>> subcadena_maxima("000", "1011101110")
    (3, '000')

    >>> subcadena_maxima("1111", "0111110")
    (4, '1111')
    '''
    cadena_mayor, cadena_menor = (a, b) if len(a)>len(b) else (b,a)
    matriz = []
    for i in range(len(cadena_mayor)): # Vamos creando una matriz de tamaño (len(cadena_mayor)) x (len(cadena_menor))
        matriz.append([])
        for j in range(len(cadena_menor)):
            if i == 0 or j == 0: # Para la primera fila y columna, el resultado es 0 o 1, y no se pueden sumar con
                                 # la fila o columna anterior de forma estándar.
                if cadena_mayor[i] == cadena_menor[j]: # Si coinciden...
                    matriz[i].append((1, cadena_menor[j]))
                else: # Si no coinciden...
                    if i == 0 and j == 0: # Si es el primer elemento, no hay subcadena común.
                        matriz[i].append((0, ""))
                    elif i == 0: # Si es la primera fila, no hay subcadena común nueva, pero se puede copiar el mejor resultado anterior.
                        matriz[i].append(matriz[i][j-1])
                    else: # Si es la primera columna, no hay subcadena común, pero se puede copiar el mejor resultado anterior.
                        matriz[i].append(matriz[i-1][j])
            else: # Para el resto de filas y columnas
                if cadena_mayor[i] == cadena_menor[j]:
                    # Si los caracteres coinciden, podemos ampliar la subcadena.
                    # Para ello, cogemos la subcadena más larga que aún no había tenido en cuenta la pareja de
                    # caracteres coincidentes, que es la que está en la diagonal superior izquierda, y añadimos 
                    # el nuevo carácter coincidente al final.
                    matriz[i].append((matriz[i-1][j-1][0] + 1, matriz[i-1][j-1][1] + cadena_menor[j]))
                else:
                    # Si no coinciden, tomamos la mejor opción que había con las subcadenas anteriores.
                    # De esta forma, aunque no haya una coincidencia directa, podemos hacer que los caracteres se propaguen,
                    # y que se tengan en cuenta coincidencias entre el nuevo caracter de una de las cadenas y uno de los
                    # caracteres anteriores de la otra cadena.
                    # Esto quiere decir que tomamos el máximo entre la subcadena de la fila anterior y la de la columna anterior.
                    matriz[i].append(max(matriz[i-1][j], matriz[i][j-1], key=lambda x: x[0]))
    #imprimir_matriz_formateada(matriz)
    return matriz[-1][-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    #print("\n",ej3_cambio_billetes(5, [1, 2], [1,2]))
