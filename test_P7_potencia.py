import pytest
import modular


@pytest.mark.parametrize("base,exp,p,salida_esperada",[
    (2,3,7,1),    
    (7,8,9,4)   
])
def test_potencia_mod_p_basico(base: int, exp:int, p:int, salida_esperada: int) -> None:
    assert(modular.potencia_mod_p(base,exp,p)==salida_esperada)


def test_potencia_mod_p_cero():
    """ Este test comprueba que, en los casos esperados,
    realmente se lanza la excepción esperada"""
    with pytest.raises(ZeroDivisionError):
        modular.potencia_mod_p(2,3,0)
    with pytest.raises(ZeroDivisionError):
        modular.potencia_mod_p(0,0,7)
