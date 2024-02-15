"""
Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""

def factorial(numero):
    """
    Funcion que devuelve el factorial de un numero entero positivo.

    Parametro:
    numero: Numero al que se le va a calcular el factorial.

    Devuelve:
    El factorial del numero que se le paso como parametro. 
    """
    contador = 1
    for n in range(1,numero+1):
        contador *= n    
    return contador

print(factorial(5))
print(factorial(10))
print(factorial(4))

# Pasos de mi solucion:
# Cree la variable contador que vale 1. Por medio de un ciclo for y de la funcion range, recorro desde el 1 hasta el numero (parametro). Con el operador *= voy multiplicando el contador con cada uno de los valores que va obteniendo n, y en cada vuelta va tomando un nuevo valor la variable contador por cada multiplicacion de la n en la iteracion, hasta llegar al valor final. Retorno el valor final, fuera del ciclo for. 

# OPERADOR NUEVO: *= -> x *= 3	x = x * 3
# contador *= n -> contador = contador * n

# ALF:
# def factorial(n):
    # """Función que calcula el factorial de un número entero positivo.
    # Parámetros
    # n: Es un entero positivo.
    # Devuelve el factorial de n.
    # """
#     tmp = 1
#     for i in range(n):
#         tmp *= i+1
#     return tmp

# print(factorial(5))
# print(factorial(20))
# --> En la solucion de alf, recorre de igual forma con el ciclo for y range desde 0 hasta el n del parametro, pero en el operador *= suma un 1, para "anular" de cierta manera el 0 y para que el ultimo numero de range, sea un numero superior a ese.
   
        
    
        


        
        








