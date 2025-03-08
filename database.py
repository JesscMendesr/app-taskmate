import sqlite3

def get_db():
    conn = sqlite3.connect('app_taskmate.db')
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL 
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        prazo TEXT NOT NULL,
        prioridade TEXT NOT NULL,
        usuario_id INTEGER NOT NULL,
        cliente_id INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
        FOREIGN KEY (cliente_id) REFERENCES clientes (id)
    )
    ''')

    conn.commit()

criar_tabelas()