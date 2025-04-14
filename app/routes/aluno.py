from fastapi import APIRouter
from typing import List
from app.models.aluno import AlunoCadastro

router = APIRouter()

alunos: List[AlunoCadastro] = []


@router.post("/alunos")
def cadastrar_aluno(aluno: AlunoCadastro):
    alunos.append(aluno)
    return {"mensagem": "Aluno cadastrado com sucesso.", "aluno": aluno}


@router.get("/alunos")
def listar_alunos():
    return alunos


@router.get("/alunos/{aluno_id}")
def buscar_aluno(aluno_id: int):
    for aluno in alunos:
        if aluno.id == aluno_id:
            return aluno

    return {"erro": "Aluno não encontrado"}
