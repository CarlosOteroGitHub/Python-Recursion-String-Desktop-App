def reversa(cadena):
    if len(cadena) == 1:
        return cadena
    else:
        return reversa(cadena[1:len(cadena)]) + cadena[0]

print(reversa("dedo"))


"""

Programa de Recursividad que Invierte los Caracteres de una Cadena de Texto.

"""
