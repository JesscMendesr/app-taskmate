from database import get_db
from auth import criptografar_senha, verificar_senha


class UsuarioRepository:
    def criar(self, usuario):
        db = get_db()
        # Criptografa a senha antes de salvar
        senha_criptografada = criptografar_senha(usuario.senha)
        db.execute('''
        INSERT INTO usuarios (nome, email, senha)
        VALUES (?, ?, ?)
        ''', (usuario.nome, usuario.email, senha_criptografada))
        db.commit()

    def autenticar(self, email: str, senha: str):
        db = get_db()
        usuario = db.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
        if usuario and verificar_senha(senha, usuario['senha']):
            return usuario
        return None