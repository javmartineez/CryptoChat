from typing import Dict
import pytest
import modular

@pytest.mark.parametrize("n,salida_esperada",[
    (1,{}),
    (2,{2:1}),
    (12,{2:2,3:1}),
    (0,{}),
    (-1,{}),
    (20,{2:2,5:1}),
    (-20,{2:2,5:1})
])

def test_factorizar_basico(n: int, salida_esperada: Dict[int,int]) -> None:
    assert(modular.factorizar(n)==salida_esperada)