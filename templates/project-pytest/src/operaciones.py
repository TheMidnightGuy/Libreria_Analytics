#Codigo principal.
#Se busca realizar operaciones para crear pruebas y testear con PyTest

#se definen funciones
#sumar, restar, dividir
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("no se puede dividir por cero")
    return a / b

