from repositories.tarefa_repository import TarefaRepository
from models import Tarefa

class TarefaService:
    def __init__(self):
        self.tarefa_repo = TarefaRepository()

    def criar_tarefa(self, tarefa: Tarefa):
        # Lógica de negócios (ex: validações)
        if not tarefa.titulo or not tarefa.prazo:
            raise ValueError("Título e prazo são obrigatórios")
        self.tarefa_repo.criar(tarefa)

    def listar_tarefas(self, usuario_id: int):
        return self.tarefa_repo.listar(usuario_id)