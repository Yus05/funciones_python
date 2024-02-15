"""
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
"""
def diccionario(*args):
    """
    Funcion que recibe una lista de numeros y devuelve la media, la varianza y la desviacion tipica de esa lista.

    Parametros:
    args: Lista de numeros.

    Devuelve:
    Un diccionario con la media, varianza y desviacion tipica.
    """
    media = sum(args)/len(args)
    contador = 0
    for n in args:
        var = (n - media)**2 
        contador += var
    var = contador / (len(args)-1)
    desviación = var**0.5

    diccionario = {"media": media, 
                   "variacion": var, 
                   "desviacion": desviación}
    return diccionario

# print(diccionario(13, 17, 12, 18, 20, 15))
print(diccionario(1, 2, 3, 4, 5))

# ALF:
# def square(sample):
#     """Función que calcula los cuadrados de una lista de números.
#     Parámetros
#     sample: Es una lista de números
#     Devuelve una lista con los cuadrados de los números de la lista sample.
#     """
#     list = []
#     for i in sample:
#         list.append(i**2)
#     return list

# def statistics(sample):
#     """Función que calcula la media, varianza y desviación típica de una muestra de números.
#     Parámetros
#     sample: Es una lista de números
#     Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
#     """
#     stat = {}
#     stat['media'] = sum(sample)/len(sample)
#     stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
#     stat['desviacion tipica'] = stat['varianza']**0.5
#     return stat

# print(statistics([1, 2, 3, 4, 5]))
