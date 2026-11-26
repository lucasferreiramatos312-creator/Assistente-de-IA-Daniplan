import pytest

from backend.test.conftest import make_precisao

INVALIDOS = {

    "precisao_largura": [None, "", " " "INVALIDA",-10, 123, 1.5, [], {}, True, False],
    "precisao_altura": [None, "", " " "INVALIDA",-10, 123, 1.5, [], {}, True, False],
    "precisao_profundidade": [None, "", " " "INVALIDA",-10, 123, 1.5, [], {}, True, False],

}

CASOS = [
    (campo, valor)
    for campo, valores in INVALIDOS.items()
    for valor in valores

]

@pytest.mark.parametrize("campo, valor", CASOS, ids=[f"{campo}={valor!r}" for campo, valor in CASOS])
def test_precisao_invalidos(make_precisao,campo, valor):
    with pytest.raises(ValueError, match=campo):
        make_precisao(**{campo: valor})

def test_precisao_validos(make_precisao):
    p = make_precisao()
    assert p.precisao_largura == "EXATA"
    assert p.precisao_altura == "APROXIMADA"
    assert p.precisao_profundidade == "NAO_INFORMADA"