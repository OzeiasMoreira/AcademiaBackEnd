from pydantic import BaseModel, Field, validator
import re

class cadastrarAluno(BaseModel):
    id: int
    nome: str
    cpf: str = Field(..., min_length=11, max_length=14)
    idade: int
    peso: float
    altura: float
    ingere_alcool: bool
    fuma: bool
    endereco: str
    telefone: str = Field(..., min_length=10, max_length=15)

    @validator("cpf")
    def validar_cpf(cls, v):
        cpf = re.sub(r'\D', '', v)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            raise ValueError("CPF inválido")

        def calcular_digito(digs):
            s = sum(int(digs[i]) * (len(digs)+1 - i) for i in range(len(digs)))
            resto = s % 11
            return '0' if resto < 2 else str(11 - resto)

        if calcular_digito(cpf[:9]) != cpf[9] or calcular_digito(cpf[:10]) != cpf[10]:
            raise ValueError("CPF inválido")

        return cpf

    @validator("telefone")
    def validar_telefone(cls, v):
        telefone = re.sub(r'\D', '', v)
        if not (10 <= len(telefone) <= 11):
            raise ValueError("Número de telefone inválido")
        return telefone
