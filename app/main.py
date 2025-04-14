from fastapi import FastAPI
from app.routes import previsao
from app.routes import frequencia
from app.routes import aluno


app = FastAPI(
    title="API Academia Força Local",
    description="BackEnd com IA para prever evasão de alunos da academia",
    version="1.0.0"
)

app.include_router(previsao.router)

app.include_router(frequencia.router)

app.include_router(aluno.router)

@app.get("/")
def home():
    return {"mensagem": "API da academia Força Local está ativa! "}

