# TaskMate

O **TaskMate** é um sistema de gestão de tarefas e clientes para autônomos e pequenos empreendedores. Ele permite organizar tarefas, gerenciar clientes e acompanhar atividades de forma simples e eficiente.

---

## Funcionalidades

- **Gestão de Usuários**: Cadastro e autenticação com criptografia de senhas (bcrypt).
- **Gestão de Clientes**: Cadastro e listagem de clientes associados ao usuário logado.
- **Gestão de Tarefas**: Criação de tarefas com título, descrição, prazo e prioridade.

---

## Tecnologias

- **Backend**: Python, FastAPI, SQLite, bcrypt, JWT.
- **Ferramentas**: Postman, DB Browser for SQLite.

---

## Diagrama Entidade-Relacionamento (DER)

````plaintext
+-------------------+       +-------------------+       +-------------------+
|     usuarios      |       |     tarefas       |       |     clientes      |
+-------------------+       +-------------------+       +-------------------+
| id (PK)           |<------| usuario_id (FK)   |       | id (PK)           |
| nome              |       | id (PK)           |       | nome              |
| email             |       | titulo            |       | email             |
| senha             |       | descricao         |       | telefone          |
+-------------------+       | prazo             |       | usuario_id (FK)   |
                            | prioridade        |       +-------------------+
                            | cliente_id (FK)   |------>| id (PK)           |
                            +-------------------+
