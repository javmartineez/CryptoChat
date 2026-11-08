import pytest
import modular


@pytest.mark.parametrize("n,p,salida_esperada",[
    (2,7,4),
    (5,14,3)    
])
def test_inversa_mod_p_basico(n: int, p:int, salida_esperada: int) -> None:
    assert(modular.inversa_mod_p(n,p)==salida_esperada)


def test_potencia_mod_p_cero():
    """ Este test comprueba que, en los casos esperados,
    realmente se lanza la excepción esperada"""
    with pytest.raises(ZeroDivisionError):
        modular.inversa_mod_p(2,4) #NON-invertible case - the argument and the modulus are not coprime

