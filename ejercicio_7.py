"""
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""
    
def lista_cuadrado(*args):
    """
    Funcion recibe lista y calcula el cuadrado de cada numero de la misma.

    Parametro:
    args: Lista de numeros.

    Devuelve:
    El cuadtado de cada numero de la lista.
    """
    lista_x = []
    for n in args:
        # x = pow(n, 2) Elimino esta linea para agregar en el metodo append directamente la operacion.
        lista_x.append(pow(n,2))
    return lista_x

print(lista_cuadrado(1,2,3,4,5))

# ALF:

# def square(*sample):
#     """Función que calcula los cuadrados de una lista de números.
#     Parámetros
#     *sample: Es una secuencia de números separados por comas.
#     Devuelve una lista con los cuadrados de los números de sample.
#     """
#     list = []
#     for i in sample:
#         list.append(i**2)
#     return list

# print(square(1, 2, 3, 4, 5))
# print(square(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))



