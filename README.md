# Instruções para rodar o backend

## Requisitos:

- Docker
- Python3 instalado
- Poetry

## Condigurando o .env

Copie para um arquivo .env o .env.example fornecido

## Database

Inicialmente, vamos rodar nosso banco MySQL.
Basta rodar `docker compose up -d` que ele criará o container com o banco que vamos utilizar para a aplicação.

## Deps & Poetry

O Poetry é um gerenciador de pacotes que nos ajuda a organizar e instalar as dependências de projetos python.

Primeiro garanta que ele está instalado com `poetry -v`.

Caso não esteja, [instale seguindo a doc oficial](https://python-poetry.org/docs/).

Após instalado:

1. Rode um `poetry shell` para entrar no amviente virtual.
2. Em seguida `poetry install` irá instalar as dependências necessárias.

## Rodando a migration

Agora que temos as dependências instaladas, podemos rodar:

`alembic upgrade head`

Ele irá criar as tabelas necessárias para a aplicação.

## Rodando o projeto

Se todas dependências foram instaladas corretamente, você conseguirá rodar o projeto com o uvicorn.
`uvicorn src.main:app --reload`

## Acessando docs

Agora ele deve estar rodando na porta 8000.
Acesse http://localhost:8000/docs para ter acesso ao Swagger da aplicação.

Em caso de dificuldades estou à disposição para ajudar.
(11) 96383-5105
