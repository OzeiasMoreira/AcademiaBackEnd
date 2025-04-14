from fastapi import APIRouter
from app.models.Aluno import Aluno
from app.models.modelo_ia import prever

router = APIRouter()

@router.post("/prever_evasao")
def prever_evasao(aluno : Aluno):

    dados = aluno.dict()
    risco = prever(dados)
    return {
        "risco_evasao": f"{risco * 100:.2f}%",
        "mensagem":"Predição realizada com sucesso"
    }
 