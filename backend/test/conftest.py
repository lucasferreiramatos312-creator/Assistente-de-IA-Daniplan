import pytest
from backend.contrato_ia import RespostaIA , Dimensoes, Precisao

VALIDOS_PREC = dict(precisao_largura="EXATA",
                    precisao_altura="APROXIMADA", precisao_profundidade="NAO_INFORMADA")

@pytest.fixture
def make_precisao():
    def _make(**overrides):
        return Precisao(**{**VALIDOS_PREC, **overrides})
    return _make

@pytest.fixture
def make_dimensoes(make_precisao):
    def _make(**overrides):
        VALIDOS_DIM =  dict(largura=4.75, altura=3.12, profundidade=None,
                    unidade="M", precisao=make_precisao())
        return Dimensoes(**{**VALIDOS_DIM, **overrides})
    return _make