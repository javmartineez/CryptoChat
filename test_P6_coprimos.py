import pytest
import modular

@pytest.mark.parametrize("a,b,salida_esperada",[
    (14,20,False),
    (14,15,True),
    (1,13,True),
    (0,20,False)   
])
def test_coprimos_basico(a: int, b:int, salida_esperada: bool) -> None:
    assert(modular.coprimos(a,b)==salida_esperada)