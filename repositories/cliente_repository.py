from database import get_db

class ClienteRepository:
    def criar(self, cliente):
        db = get_db()
        db.execute('''
        INSERT INTO clientes (nome, email, telefone, usuario_id)
        VALUES (?, ?, ?, ?)
        ''', (cliente.nome, cliente.email, cliente.telefone, cliente.usuario_id))
        db.commit()
        
    def listar(self, usuario_id):
        db = get_db()
        clientes = db.execute('SELECT * FROM clientes WHERE usuario_id = ?', (usuario_id,)).fetchall()
        return clientes