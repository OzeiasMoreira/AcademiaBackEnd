from pydantic import BaseModel

class Aluno(BaseModel):
    idade : int
    sexo : str
    frequencia_semanal: int
    inverno: bool

class cadastrarAluno(BaseModel):
    id:int 
    nome:str
    cpf:str
    idade:int
    peso:float
    altura:float
    ingere_alcool:bool
    fuma:bool