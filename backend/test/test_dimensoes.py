import pytest


INVALIDOS_DIM = {

    "largura": ["", " ","INVALIDA",-10, [], {}, False],
    "altura": ["", " ", "INVALIDA",-10, [], {}, False],
    "profundidade": ["", " ", "INVALIDA",-10, [], {}, False],
    "unidade": ["", " ", "INVALIDA", -10, [], {}, False],

}

CASOS = [
    (campo, valor)
    for campo, valores in INVALIDOS_DIM.items()
    for valor in valores
]

@pytest.mark.parametrize("campo, valor", CASOS, ids=[f"{campo}={valor!r}" for campo, valor in CASOS],)
def test_dimensoes_invalidos(make_dimensoes, campo, valor):
    with pytest.raises(ValueError, match=campo):
        make_dimensoes(**{campo: valor})
        
def test_dimensao_informada_nao_pode_der_nao_informada(make_dimensoes, make_precisao):
    p = make_precisao(precisao_largura="NAO_INFORMADA")

    with pytest.raises(ValueError, match="largura"):
        make_dimensoes(largura=4.75,precisao=p)

def test_dimensao_nao_informada_nao_pode_ser_exata(make_dimensoes, make_precisao):
    p = make_precisao(precisao_largura="EXATA")

    with pytest.raises(ValueError, match="largura"):
        make_dimensoes(largura=None, precisao=p)

def test_dimensoes_informadas_nao_podem_ter_precisao_nao_informada(make_dimensoes, make_precisao):
    p = make_precisao(precisao_largura="NAO_INTERPRETADO")

    with pytest.raises(ValueError, match="largura"):
        make_dimensoes(largura=5.0, precisao=p)

def test_dimensoes_validos(make_dimensoes):
    d = make_dimensoes()
    assert d.largura == 4.75
    assert d.altura == 3.12
    assert d.profundidade is None
    assert d.unidade == "M"
    assert d.precisao.precisao_largura == "EXATA"
    assert d.precisao.precisao_altura == "APROXIMADA"
    assert d.precisao.precisao_profundidade == "NAO_INFORMADA"