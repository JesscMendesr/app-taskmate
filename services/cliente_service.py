from repositories.cliente_repository import ClienteRepository
from models import Cliente

class ClienteService:
    def __init__(self):
        self.cliente_repo = ClienteRepository()

    def criar_cliente(self, cliente: Cliente):
        # Lógica de negócios (ex: validações)
        if not cliente.nome or not cliente.email:
            raise ValueError("Nome e email são obrigatórios")
        self.cliente_repo.criar(cliente)

    def listar_clientes(self, usuario_id: int):
        return self.cliente_repo.listar(usuario_id)