from database import get_db

class ClienteRepository:
    def criar(self, cliente):
        db = get_db()
        db.execute('INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)',
        (cliente.nome, cliente.email, cliente.telefone))
        db.commit()

    def listar(self):
        db = get_db()
        clientes = db.execute('SELECT * FROM clientes').fetchall()
        return clientes