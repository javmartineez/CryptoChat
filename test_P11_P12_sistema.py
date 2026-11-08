from typing import List, Tuple
import pytest
import modular

@pytest.mark.parametrize("alist,blist,plist,salida_esperada",[
    ([2],[3],[5],(4,5)),
    ([2],[4],[6],(2,3)),
    ([1,4],[1,7],[3,11],(10,33)),
    #TO DO
])
def test_factorizar_basico(alist:List[int],blist:List[int],plist:List[int], salida_esperada: Tuple[int,int]) -> None:
    assert(modular.resolver_sistema_congruencias(alist,blist,plist)==salida_esperada)


@pytest.mark.parametrize("alist,blist,plist,salida_esperada",[
    ([2],[4],[6],(2,3)),
    ([1,4],[1,7],[3,11],(10,33)),
    #TO DO
])
def test_factorizar_no_coprimo(alist:List[int],blist:List[int],plist:List[int], salida_esperada: Tuple[int,int]) -> None:
    assert(modular.resolver_sistema_congruencias(alist,blist,plist)==salida_esperada)


@pytest.mark.parametrize("alist,blist,plist",[
    ([2],[3],[4]),
    ([1,1],[1,2],[5,5]),
    #TO DO
])
def test_sistema_incompatible(alist:List[int],blist:List[int],plist:List[int]):
    """ This test checks that, in the expected cases,
    the expected exception is actually raised"""
    with pytest.raises(modular.IncompatibleEquationError):
        modular.resolver_sistema_congruencias(alist,blist,plist)
    #TO DO: add a case where n is not invertible mod p
