"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
--> El resultado del area de la 1era funcion, se va a utilizar en la 2da funcion. 
"""
# Area de un circulo: pi * radio al cuadrado.
# Volumen de un cilindro: multiplicar el área del circulo por la altura del cilindro.

def area_circulo(radio, pi=3.14):
    """
    Funcion que calcula el area de un circulo.

    Parametros:
    radio: Radio del circulo.
    pi: pi del circulo.

    Devuelve:
    El area del circulo.
    """
    return pi * radio**2
# --> Esta formula me hace la operacion del calculo del area de un circulo. 

def volumen_cilindro(radio, altura):
    """"""
    return area_circulo(radio) * altura
print(volumen_cilindro(3, 5))
# De esta manera si logro que la funcion volumen_cilindro sea mas independiente, ya que al momento de su llamado solo se deben proporcionar datos necesario como el radio y la altura, y con ese radio la funcion area_circulo hace su trabajo.


# def volumen_cilindro(area, h):
#     """
#     Funcion que devuelve el volumen de un cilindro.

#     Parametros:
#     area_circulo: Area de la base del cilindro.
#     h: Altura del cilindro.

#     Devuelve:
#     El volumen del cilindro.
#     """
#     return area * h

# print(volumen_cilindro(area_circulo(3), 5))
# --> Esta manera sigue siendo incorrecta, porque sigo dependiendo en la llamada de la funcion volumen_cilindro de la funcion area_circulo. Lo ideal es que la funcion que calcula el volumen sea independiente en el llamado.








# print(volumen_cilindro(area_circulo, 10))

# Hay un error, y es que en la llamada de la funcion volumen_cilindro es donde deberia meter los datos.



# Alf, calcula el area del circulo. Al calcular el volumen del cilindro usa directamente la funcion, no usa una variable en donde esta retornada la funcion. 














# AHORA, siempre debo comparar mis soluciones con las de alf. Para ampliar mis conocimientos, ver codigo mas limpio y eficaz.
