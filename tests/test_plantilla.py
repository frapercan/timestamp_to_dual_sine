from plantilla_programas_python.plantilla import EncapsulacionEnClase


parametro1 = []
parametro2 = 'prueba'
def test_tonto():
    objeto = EncapsulacionEnClase(parametro1,parametro2)
    assert objeto.parametro1 == []
    assert objeto.parametro2 == 'prueba'
