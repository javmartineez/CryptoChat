import pytest
import modular

@pytest.mark.parametrize("n,salida_esperada",[
    (2,True),
    (3,True),
    (4,False),
    (5,True),
    (0, False),
    (1, False),
    (-1, False),
    (23, True)
])
def test_es_primo_basico(n: int, salida_esperada: bool) -> None:
    assert(modular.es_primo(n)==salida_esperada)