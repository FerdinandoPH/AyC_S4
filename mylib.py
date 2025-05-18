from copy import deepcopy
from typing import Tuple
import pandas as pd
def ej3_cambio_billetes(cantidad :int, valBill :list, cantBill :list) -> list:
    """ Devuelve la cantidad de billetes necesarios para devolver una cantidad de dinero con la menor cantidad de billetes posibles con un numero limitado de billetes de cada tipo
    
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
    """
    matriz = []                                                                                     # O(1)
    for i in range(len(valBill)):                                                                   # O(nm^2)
        matriz.append([])                                                                           # O(1)
        for j in range(cantidad+1):                                                                 # O(nm)
            if j == 0:                                                                              # O(m)
                matriz[i].append([])                                                                # O(1)
                for k in range(len(valBill)):                                                       # O(m)
                    matriz[i][j].append(0)                                                          # O(1)
            else:
                matriz[i].append([])                                                                # O(1)
                for k in range(len(valBill)):                                                       # O(m)
                    matriz[i][j].append(float("inf"))                                               # O(1)
    

    for iMaxVal in range(len(valBill)):                                                             # O(nm^2)
        for cant in range(1, cantidad+1):                                                           # O(nm)
            if iMaxVal == 0 and cant < valBill[iMaxVal]:                                            # O(m)
                pass

            elif iMaxVal == 0:
                rellenar = cant // valBill[0]                                                       # O(1)
                if rellenar <= cantBill[0] and valBill[0]*rellenar == cant:                         # O(m)
                    matriz[0][cant][0] = rellenar                                                   # O(1)
                
                    for i in range(1, len(valBill)):                                                # O(m)
                        matriz[iMaxVal][cant][i] = 0                                                # O(1)
                
            elif cant < valBill[iMaxVal]:
                matriz[iMaxVal][cant] = matriz[iMaxVal-1][cant]                                     # O(1)

            else:
                temp = cant // valBill[iMaxVal]                                                     # O(1)
                if temp > cantBill[iMaxVal]:                                                        # O(1)
                    temp = cantBill[iMaxVal]                                                        # O(1)

                for i in range(len(valBill)):                                                       # O(m)
                    matriz[iMaxVal][cant][i] = matriz[iMaxVal-1][cant-(temp*valBill[iMaxVal])][i]   # O(1)
                if float("inf") not in matriz[iMaxVal][cant]:                                       # O(1)
                    matriz[iMaxVal][cant][iMaxVal] = temp                                           # O(1)
    
    return matriz[len(valBill)-1][cantidad]                                                         # O(1)
# O(nm^2) siendo n la cantidad y m el tamaño de la lista de billetes


def ej6_quidditch(apostado :float, calidades :list) -> float:
    """ Devuelve la cantidad de dinero ganada en una apuesta de quidditch dada la apuesta inicial y la calidad de los equipos sabiendo que un equipo tiene que ganar seis partidos en total para ganar el torneo

    >>> ej6_quidditch(1, [1, 2, 3, 4])
    208.875377339135

    >>> ej6_quidditch(100, [1, 1, 1, 1])
    400.0

    >>> ej6_quiditch(50, [10, 5, 20, 5])
    420.42058795339176

    >>> ej6_quidditch(10, [97, 1, 1, 1])
    10.000000014973988
    """
    matriz = []                                                                             # O(1)
    sumaCalidades = calidades[0] + calidades[1] + calidades[2] + calidades[3]               # O(1)
    probabilidades = [calidades[0]/sumaCalidades, calidades[1]/sumaCalidades, calidades[2]/sumaCalidades, calidades[3]/sumaCalidades] # O(1)
    for x in range(7):                                                                      # O(1)
        matriz.append([])                                                                   # O(1)
        for y in range(7):                                                                  # O(1)
            matriz[x].append([])                                                            # O(1)
            for z in range(7):                                                              # O(1)
                matriz[x][y].append([])                                                     # O(1)
                for w in range(7):                                                          # O(1)
                    matriz[x][y][z].append([])                                              # O(1)
                    if [x,y,z,w] == [0,0,0,0]:                                              # O(1)
                        matriz[0][0][0][0] = 1                                              # O(1)
                    else:
                        matriz[x][y][z][w] = 0                                              # O(1)
                        if w-1 >= 0 and z<6 and y<6 and x<6:                                # O(1)
                            matriz[x][y][z][w] += probabilidades[0] * matriz[x][y][z][w-1]  # O(1)
                        if z-1 >= 0 and w<6 and y<6 and x<6:                                # O(1)
                            matriz[x][y][z][w] += probabilidades[1] * matriz[x][y][z-1][w]  # O(1)
                        if y-1 >= 0 and w<6 and z<6 and x<6:                                # O(1)
                            matriz[x][y][z][w] += probabilidades[2] * matriz[x][y-1][z][w]  # O(1)
                        if x-1 >= 0 and w<6 and z<6 and y<6:                                # O(1)
                            matriz[x][y][z][w] += probabilidades[3] * matriz[x-1][y][z][w]  # O(1)

    res = 0                                                                                 # O(1)
    for x in range(6):                                                                      # O(1)
        for y in range(6):                                                                  # O(1)
            for z in range(6):                                                              # O(1)
                res += matriz[x][y][z][6]                                                   # O(1)
    
    return apostado / res                                                                   # O(1)
# O(1)
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
