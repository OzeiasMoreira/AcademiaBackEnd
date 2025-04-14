from pydantic import BaseModel

class Aluno(BaseModel):
    idade : int
    sexo : str
    frequencia_semanal: int
    inverno: bool