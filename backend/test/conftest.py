import pytest
from backend.contrato_ia import RespostaIA , Dimensoes, Precisao

VALIDOS_PREC = dict(precisao_largura="EXATA", precisao_altura="APROXIMADA", precisao_profundidade="NAO_INFORMADA")

@pytest.fixture
def make_precisao():
    def _make(**overrides):
        return Precisao(**{**VALIDOS_PREC, **overrides})
    return _make