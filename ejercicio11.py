"""
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 

Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
"""

def dictionary(phrase):
    """
    Funcion que recibe una frase y devuelve un diccionario con clave igual a cada palabra de la frase y valor igual a la frecuencia de cada palabra de la frase.

    Parametros:
    phrase: Frase.

    Devuelve:
    La frecuencia de cada palabra de la frase.
    """
    phrase = phrase.lower()
    phrase = phrase.split()
    frequency = {}
    for word in phrase:
        amount = phrase.count(word)
        frequency[word] = amount
    return frequency


def my_tuple(frequency):
    top_value = []
    for value in frequency.values():
        top_value.append(value)
        value_max = max(top_value)
    
    for key, value in frequency.items():
        if value == value_max:
            my_tuple = key, value
    top = tuple(my_tuple)
    
    return top


print(dictionary("Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"))

print(my_tuple(frequency={'como': 2, 'quieres': 1, 'que': 4, 'te': 1, 'quiera': 3, 'si': 1, 'el': 1, 'quiero': 2, 'me': 3, 'no': 1, 'quiere': 1}
))


# 2DA ALTERNATIVA ##########################################################################:

# def dictionary(phrase):
#     """
#     Funcion que recibe una frase y devuelve un diccionario con clave igual a cada palabra de la frase y valor igual a la frecuencia de cada palabra de la frase.

#     Parametros:
#     phrase: Frase.

#     Devuelve:
#     La frecuencia de cada palabra de la frase.
#     """
#     phrase = phrase.lower()
#     phrase = phrase.split()
#     frequency = {}
#     for word in phrase:
#         amount = phrase.count(word)
#         frequency[word] = amount
#     return frequency

# def my_tuple(func_dict, phrase):
#     frequency = dictionary(phrase)
#     top_value = []
#     for value in frequency.values():
#         top_value.append(value)
#     top = max(top_value)
    
#     for key, value in frequency.items():
#         if value == top:
#             my_tuple = key, value
#     top_word = tuple(my_tuple)
#     return top_word

    

# print(dictionary("Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"))

# print(my_tuple(dictionary, "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"))


# ALF SOLUTION ##########################################################################:

# def count_words(text):
#     """Función que cuenta el número de veces que aparece cada palabra en un texto.
#     Parámetros:
#         - text: Es una cadena de caracteres.
#     Devuelve: 
#         Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
#     """
#     text = text.split()
#     words = {}
#     for i in text:
#         if i in words:
#             words[i] += 1
#         else:
#             words[i] = 1
#     return words

# def most_repeated(words):
#     max_word = ''
#     max_freq = 0
#     for word, freq in words.items():
#         if freq > max_freq:
#             max_word = word
#             max_freq = freq
#     return max_word, max_freq

# text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
# print(count_words(text))
# print(most_repeated(count_words(text)))


