from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    email: str
    senha: str

class Tarefa(BaseModel):
    titulo: str
    descricao: str
    prazo: str
    prioridade: str
    usuario_id: int

class Cliente(BaseModel):
    nome: str
    email: str
    telefone: str
    usuario_id: int