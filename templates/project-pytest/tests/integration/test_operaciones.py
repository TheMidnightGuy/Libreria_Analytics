#llamamos las funciones creadas
import pytest 
from operaciones import suma, resta, dividir

#Realizamos una parametrización de los valores, de esta manera
#defimimos los valores para cada variable y podemos validar con
#PASSED/FAILED en una función que tiene distintos "assert".

# Parametrización para SUMA
@pytest.mark.parametrize("a, b, esperado",[
    (4, 6, 10), #se espera 10 como primer resultado
    (10, 8, 18), #se espera 20 como segundo resultado
])
#Creamos tests en base a las funciones que creamos anteriormente

def test_suma_output(a, b, esperado):
    #definimos y revisamos los outputs esperados
    assert suma(a,b) == esperado 
    assert suma(a,b) == esperado 
#------
# Parametrización para RESTA
@pytest.mark.parametrize("a, b, esperado",[
    (20, 10, 10),
    (30, 10, 20),
])

def test_resta_output(a, b, esperado):
    assert resta(a,b) == esperado
    assert resta(a,b) == esperado

#------
# Parametrización para DIVISIÓN
@pytest.mark.parametrize("a, b, esperado",[
    (25, 5, 5),
    (10, 2, 5),
])
def test_dividir_output(a, b, esperado):
    assert dividir(a,b) == esperado

#------
#def test_dividir_por_cero():
#    with pytest.raises(ZeroDivisionError) as exinfo:
#        dividir(10,0)
#    assert "No se puede dividir por cero" in str(exinfo.value)

    #Ya listas las funciones y los tests que las validan, ejecutamos
    #pytest en consola para obtener nuestros primeros resultados.


