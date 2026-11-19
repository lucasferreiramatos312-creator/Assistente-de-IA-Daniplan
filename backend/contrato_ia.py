from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

class Precisao(BaseModel):

    model_config = ConfigDict(extra="forbid")

    precisao_largura: None | Literal["EXATA", "APROXIMADA", "NAO_IMFORMADA", "NAO_INTERPRETADO"] = Field(..., description="Precisão da largura do móvel informada pelo cliente, caso a largura seja exata, envie como EXATA, caso a largura seja aproximada, envie como APROXIMADA, caso a largura não seja interpretada, envie como NAO_INTERPRETADO, caso a largura não tenha sido informada, envie como None")
    precisao_altura: None | Literal["EXATA", "APROXIMADA", "NAO_IMFORMADA", "NAO_INTERPRETADO"] = Field(..., description="Precisão da altura do móvel informada pelo cliente, caso a altura seja exata, envie como EXATA, caso a altura seja aproximada, envie como APROXIMADA, caso a altura não seja interpretada, envie como NAO_INTERPRETADO, caso a altura não tenha sido informada, envie como None")
    precisao_profundidade: None | Literal["EXATA", "APROXIMADA", "NAO_IMFORMADA", "NAO_INTERPRETADO"] = Field(..., description="Precisão da profundidade do móvel informada pelo cliente, caso a profundidade seja exata, envie como EXATA, caso a profundidade seja aproximada, envie como APROXIMADA, caso a profundidade não seja interpretada, envie como NAO_INTERPRETADO, caso a profundidade não tenha sido informada, envie como None")

class Dimensoes(BaseModel):

    model_config = ConfigDict(extra="forbid")
 
    largura: float | None = Field(default=None, gt=0, description="Largura do móvel informada pelo cliente, caso não tenha sido informada, envie como None.")
    altura: float | None = Field(default=None, gt=0, description="Altura do móvel informada pelo cliente, caso não tenha sido informada, envie como None.")
    profundidade: float | None = Field(default=None, gt=0, description="Profundidade do móvel informada pelo cliente, caso não tenha sido informada, envie como None.")

    unidade: None | Literal["CM", "M", "NAO_INTERPRETADO", "NAO_ESPECIFICADO"]  = Field(default=None, description="Unidade de medida das dimensões do móvel, caso não tenha sido informada, envie como None. Caso a unidade não seja interpretada, envie como NAO_INTERPRETADO, caso a unidade não seja especificada , envie como NAO_ESPECIFICADO")
    precisao: Precisao = Field(..., description="Precisão das medidas do móvel informadas pelo cliente")

class RespostaIA(BaseModel):

    model_config = ConfigDict(extra="forbid")
    
    intencao: Literal["ORCAMENTO", "COMPARACAO", "DUVIDA", "AJUDA", "NAO_INTERPRETADO", "NAO_ESPECIFICADO","OUTRO"] = Field(...,description="Inteção do cliente no contexto da conversa, enviei como OUTRO toda vez que a intenção não se encaixe nas opções listadas, caso não intreprete a mensagem envie como NAO_INTERPRETADO, caso o cliente não forneça a intenção, envie como NAO_ESPECIFICADO" )
    tipo_movel: Literal["GUARDA_ROUPA", "COZINHA_PLANEJADA", "ESTANTE", "ARAMARIO", "PAINEL", "GABINETE", "NAO_INTERPRETADO", "OUTRO"] = Field(...,description="Tipo do movel solicitado pelo cliente, envie como OUTRO para todo movel que não se encaixe nos tipos listados")
    medidas_movel: Dimensoes = Field(..., description="Medidas do móvel informadas pelo cliente")
    localizacao_cliente: str | None | Literal["NAO_INTERPRETADO"] = Field(default=None,description="Localização informada pelo cliente, caso não tenha sido informada, envie como None. Caso a localização não seja interpretada, envie como NAO_INTERPRETADO")

