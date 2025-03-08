from database import get_db

class UsuarioRepository:
    def criar(self, usuario):
        db = get_db()
        db.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)',(usuario.nome, usuario.email, usuario.senha))
        db.commit()

    def autenticar(self, email, senha):
        db = get_db()
        usuario = db.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?',(email, senha)).fetchone()
        return usuario