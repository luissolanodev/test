calificaciones = [
    [78, 45, 50, 60, 65, 80, 100, 75],
    [80, 90, 90, 95, 80, 85, 87, 94],
    [60, 50, 75, 55, 61, 74, 53, 49]
]

#  | FOR 1 VUELTA | FOR 2 VUELTA |   FOR 1 lista_calificaciones        | FOR 2 calificacion |
#. |      1       |       1      |  [78, 45, 50, 60, 65, 80, 100, 75]  |        78          |
#. |.     1       |.      2      |.               "                    |        45          |
#. |.     1       |.      3      |.               "                    |        50          |
#. |.     1       |.      4      |.               "                    |        60          |
#. |.     1       |.      5      |.               "                    |        65          |
#. |.     1       |.      6      |.               "                    |        80          |
#. |.     1       |.      7      |.               "                    |        100         |
#. |.     1       |.      8      |.               "                    |        75          |
#. |.     2       |.      1      |. [80, 90, 90, 95, 80, 85, 87, 94]   |        80          |
#. |.     2       |.      2      |.               "                    |        90          |
#. |.     2       |.      3      |.               "                    |        90          |
#. |.     2       |.      4      |.               "                    |        95          |
#. |.     2       |.      5      |.               "                    |        80          |
#. |.     2       |.      6      |.               "                    |        85          |
#. |.     2       |.      7      |.               "                    |        87          |
#. |.     2       |.      8      |.               "                    |        94          |
#

for lista_calificaciones in calificaciones:
    for calificacion in lista_calificaciones:
        print(calificacion)
    print('===AQUI TERMINA UNA LISTA===')