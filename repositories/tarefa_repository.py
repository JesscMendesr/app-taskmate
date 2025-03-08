from database import get_db

class TarefaRepository:
    def criar(self, tarefa):
        db = get_db()
        db.execute('INSERT INTO tarefas (titulo, descricao, prazo, prioridade, usuario_id) VALUES (?, ?, ?, ?, ?)',
        (tarefa.titulo, tarefa.descricao, tarefa.prazo, tarefa.prioridade, tarefa.usuario_id))
        db.commit()

    def listar(self, usuario_id):
        db = get_db()
        tarefas = db.execute('SELECT * FROM tarefas WHERE usuario_id = ?', (usuario_id,)).fetchall()
        return tarefas
