import pytest
import modular


@pytest.mark.parametrize("n,salida_esperada",[
    (7,6),
    (15,8),
    (1,1)   
])
def test_euler_basico(n: int, salida_esperada: int) -> None:
    assert(modular.euler(n)==salida_esperada)
