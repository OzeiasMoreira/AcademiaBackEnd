from pydantic import BaseModel

class aluno(BaseModel):
    idade : int
    sexo : str
    frequencia_semanal: int
    inverno: bool