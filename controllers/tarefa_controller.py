from fastapi import APIRouter, HTTPException
from models import Tarefa
from services.tarefa_service import TarefaService

router = APIRouter()
tarefa_service = TarefaService()

@router.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    try:
        tarefa_service.criar_tarefa(tarefa)
        return {"message": "Tarefa criada com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/tarefas/{usuario_id}")
def listar_tarefas(usuario_id: int):
    try:
        tarefas = tarefa_service.listar_tarefas(usuario_id)
        return {"tarefas": tarefas}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))