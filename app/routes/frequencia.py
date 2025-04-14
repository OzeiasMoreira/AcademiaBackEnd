from fastapi import APIRouter
from typing import List
from datetime import date
from app.models.frequencia import FrequenciaRegistro

router = APIRouter()

frequencias = []

@router.post("/frequencia")
def registrar_frequencia(frequencia: FrequenciaRegistro):
    frequencias.append(frequencia)
    return {"mensagem": "Sua frequencia foi registrada."}

@router.get("/frequencia/geral")
def frequencia_geral():
    return {"total_presencas": len(frequencias)}

@router.get("/frequencia/aluno/{aluno_id}")
def frequencia_aluno(aluno_id: int):
    presencas = [f for f in frequencias if f.aluno_id == aluno_id]
    return {
        "aluno_id": aluno_id,
        "total_presencas": len(presencas),
        "datas": [p.data for p in presencas]
    }