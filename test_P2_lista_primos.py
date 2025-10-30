from typing import List
import pytest
import modular

@pytest.mark.parametrize("a,b,salida_esperada",[
    (1,11,[2,3,5,7]),
    (8,10,[]),
    (0,1, []),
    (-10, 0, [])
])
def test_lista_primos_basico(a: int, b:int, salida_esperada: List[int]) -> None:
    assert(modular.lista_primos(a,b)==salida_esperada)