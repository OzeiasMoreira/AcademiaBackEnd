from pydantic import BaseModel
from datetime import date

class FrequenciaRegistro(BaseModel):
    aluno_id: int
    data: date