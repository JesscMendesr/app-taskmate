from fastapi import APIRouter, HTTPException, Depends
from models import Cliente
from services.cliente_service import ClienteService
from auth import get_usuario_atual  # Função para obter o usuário logado

router = APIRouter()
cliente_service = ClienteService()

@router.post("/clientes")
def criar_cliente(cliente: Cliente):
    try:
        cliente_service.criar_cliente(cliente)
        return {"message": "Cliente criado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/clientes")
def listar_clientes(usuario_id: int = Depends(get_usuario_atual)):
    try:
        clientes = cliente_service.listar_clientes(usuario_id)
        return {"clientes": clientes}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))