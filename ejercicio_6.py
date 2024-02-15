"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""
# la función sum() en Python se utiliza para calcular la suma de los elementos de un iterable (como una lista, una tupla, un conjunto o un rango).
# La función len() devuelve la longitud (el número de elementos) de un objeto.

def media_lista(*args):
    """
    Funcion que calcula la media de una lista.

    Parametro:
    args: Lista de numeros.

    Devuelve:
    La media de la lista.
    """
    return sum(args)/len(args)
print(media_lista(4,3,2,7,10))

# ALF:
# def mean(*sample):
#     """Función que calcula la media de una muestra de números.
#     Parámetros
#     *sample: Secuencia de números separados por comas.
#     Devuelve la media de los números en *sample. 
#     """
#     return sum(sample)/len(sample)

# print(mean(1, 2, 3, 4, 5))
# print(mean(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))









