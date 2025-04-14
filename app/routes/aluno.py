from fastapi import APIRouter, HTTPException
from typing import List
from app.models.aluno import cadastrarAluno

router = APIRouter()

alunos: List[cadastrarAluno] = []


@router.post("/alunos")
def cadastrar_aluno(aluno: cadastrarAluno):
    for existente in alunos:
        if existente.id == aluno.id:
            raise HTTPException(status_code=400, detail="Já existe um aluno com este ID.")
        if existente.cpf == aluno.cpf:
            raise HTTPException(status_code=400, detail="Já existe um aluno com este CPF.") 

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

