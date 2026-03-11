calificaciones = [
    [78, 45, 50, 60, 65, 80, 100, 75],
    [80, 90, 90, 95, 80, 85, 87, 94],
    [60, 50, 75, 55, 61, 74, 53, 49]
]

#  | FOR EXTERIOR VUELTA | FOR INTERIOR VUELTA |   FOR INTERIOR lista_calificaciones        | FOR INTERIOR calificacion |
#. |      1              |       1             |  [78, 45, 50, 60, 65, 80, 100, 75]         |        78                 |
#. |.     1              |.      2             |.               "                           |        45                 |
#. |.     1              |.      3             |.               "                           |        50                 |
#. |.     1              |.      4             |.               "                           |        60                 |
#. |.     1              |.      5             |.               "                           |        65                 |
#. |.     1              |.      6             |.               "                           |        80                 |
#. |.     1              |.      7             |.               "                           |        100                |
#. |.     1              |.      8             |.               "                           |        75                 |
#. |.     2              |.      1             |. [80, 90, 90, 95, 80, 85, 87, 94]          |        80                 |
#. |.     2              |.      2             |.               "                           |        90                 |
#. |.     2              |.      3             |.               "                           |        90                 |
#. |.     2              |.      4             |.               "                           |        95                 |
#. |.     2              |.      5             |.               "                           |        80                 |
#. |.     2              |.      6             |.               "                           |        85                 |
#. |.     2              |.      7             |.               "                           |        87                 |
#. |.     2              |.      8             |.               "                           |        94                 |
#. |.     3              |.      1             |. [60, 50, 75, 55, 61, 74, 53, 49]          |        60                 |
#. |.     3              |.      2             |.               "                           |        50                 |
#. |.     3              |.      3             |.               "                           |        75                 |
#. |.     3              |.      4             |.               "                           |        55                 |
#. |.     3              |.      5             |.               "                           |        61                 |
#. |.     3              |.      6             |.               "                           |        74                 |
#. |.     3              |.      7             |.               "                           |        53                 |
#. |.     3              |.      8             |.               "                           |        49                 |
#

# Esta variable sirve para ir acumulando/sumando las calificaciones en cada iteracion
# suma_calificaciones = 0

# Necesito:
# 1. Sumar cada calificacion de la lista, a la variable suma_calificaciones

for lista_calificaciones in calificaciones:
    suma_calificaciones = 0 

    for calificacion in lista_calificaciones:
        suma_calificaciones = calificacion + suma_calificaciones
    print('===AQUI TERMINA UNA LISTA===')
    print('suma_calificaciones es: ', suma_calificaciones)

    promedio = suma_calificaciones / 8
    print(promedio)