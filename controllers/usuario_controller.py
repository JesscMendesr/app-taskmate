from fastapi import APIRouter, HTTPException
from models import Usuario
from services.usuario_service import UsuarioService

router = APIRouter()
usuario_service = UsuarioService()

@router.post("/usuarios")
def criar_usuario(usuario: Usuario):
    try:
        usuario_service.criar_usuario(usuario)
        return {"message": "Usuário criado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(email: str, senha: str):
    try:
        usuario = usuario_service.autenticar(email, senha)
        if usuario:
            return {"message": "Login bem-sucedido!"}
        else:
            raise HTTPException(status_code=401, detail="Credenciais inválidas")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))