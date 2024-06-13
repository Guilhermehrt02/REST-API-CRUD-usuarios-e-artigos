# API REST com FastAPI, JWT e PostgreSQL

Esta API foi desenvolvida utilizando FastAPI para criar endpoints que realizam operações CRUD em usuários, autenticação JWT e integração com banco de dados PostgreSQL.

## Funcionalidades

- **Signup**: Cria um novo usuário.
- **Login**: Autentica o usuário e retorna um token de acesso JWT.
- **Listar Usuários**: Lista todos os usuários cadastrados.
- **Detalhes do Usuário**: Retorna informações detalhadas de um usuário específico.
- **Atualizar Usuário**: Atualiza informações de um usuário existente.
- **Excluir Usuário**: Remove um usuário do banco de dados.

## Endpoints

### `POST /signup`

Cria um novo usuário.

### `POST /login`

Autentica o usuário e retorna um token JWT.

### `GET /`

Lista todos os usuários cadastrados.

### `GET /{usuario_id}`

Retorna informações detalhadas de um usuário específico.

### `PUT /{usuario_id}`

Atualiza informações de um usuário existente.

### `DELETE /{usuario_id}`

Remove um usuário do banco de dados.

## Requisitos

- Python 3.7+
- FastAPI
- SQLAlchemy
- asyncpg
- PyJWT

## Execução
```bash
uvicorn main:app --reload
```
## Estrutura do Projeto
1. **app/**
- **__init__.py:** Inicialização da aplicação.
- **main.py:** Configuração principal da API.
- **config.py:** Configurações da aplicação, incluindo conexão com o banco de dados.
- **models/:** Modelos de dados da aplicação.
- **schemas/:** Esquemas de validação de entrada e saída.
- **routers/:** Roteadores (API endpoints) da aplicação.
- **core/:** Módulos principais da aplicação, como autenticação e segurança.
- **dependencies/:** Dependências da aplicação, como sessão do banco de dados e autenticação do usuário.
