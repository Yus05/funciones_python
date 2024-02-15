"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""
def total_factura(monto, iva=21):
    """
    Funcion que aplica el IVA a una factura.

    Parametros:
    monto: Cantidad sin IVA.
    iva: porcentaje de IVA a aplicar a la factura.

    Devuelve:
    El total de la factura con el IVA agregado.
    """
    return int(monto + (iva * monto)/100)

print(total_factura(1000, 13))
print(total_factura(1000))

# ALF:
# def invoice(amount, vat=21):
    # """Función de aplica el IVA a una factura.
    # Parametros
    # amount: Es la cantidad sin IVA
    # vat: Es el porcentaje de IVA
    # Devuelve el total de la factura una vez aplicado el IVA. 
    # """
#     return amount + amount*vat/100

# print(invoice(1000,10))
# print(invoice(1000))


# AHORA, siempre debo comparar mis soluciones con las de alf. Para ampliar mis conocimientos, ver codigo mas limpio y eficaz.

