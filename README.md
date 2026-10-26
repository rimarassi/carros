# Sistema de Gerenciamento de Carros

Projeto desenvolvido em **Python e Django**, com o objetivo de realizar o cadastro e gerenciamento de veículos.

A aplicação utiliza PostgreSQL como banco de dados e conta com funcionalidades de cadastro, consulta, edição e exclusão de carros, além de integração com a API da OpenAI.

## Tecnologias utilizadas

- Python
- Django
- PostgreSQL
- HTML e CSS
- OpenAI API

## Requisitos

Para executar o projeto, é necessário ter instalado:

- Python
- PostgreSQL
- Pip
- Dependências disponíveis no arquivo `requirements.txt`

## Instalação

Clone o repositório:

```bash
git clone https://github.com/rimarassi/carros.git
```

Acesse a pasta do projeto:

```bash
cd carros
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executar o projeto

Após configurar a conexão com o PostgreSQL no arquivo `app/settings.py`, execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Após isso, o sistema estará disponível em:

http://127.0.0.1:8000/
