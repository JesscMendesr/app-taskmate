from repositories.usuario_repository import UsuarioRepository
from models import Usuario

class UsuarioService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    def criar_usuario(self, usuario: Usuario):
        # Lógica de negócios (ex: validações)
        if not usuario.nome or not usuario.email or not usuario.senha:
            raise ValueError("Todos os campos são obrigatórios")
        self.usuario_repo.criar(usuario)

    def autenticar(self, email: str, senha: str):
        usuario = self.usuario_repo.autenticar(email, senha)
        if not usuario:
            raise ValueError("Credenciais inválidas")
        return usuario