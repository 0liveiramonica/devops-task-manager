# DevOps Task Manager

Aplicação web simples em Flask para demonstrar práticas de desenvolvimento e DevOps. Atualmente, o projeto disponibiliza uma página inicial e uma API que retorna uma lista estática de tarefas.

## Requisitos

- Python 3.10 ou superior
- `pip`

## Instalação

1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   No Linux ou macOS:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Execução

Inicie o servidor com:

```bash
python run.py
```

A aplicação ficará disponível em <http://localhost:5000>. O modo de desenvolvimento do Flask está habilitado no script de execução.

## Endpoints

### `GET /`

Retorna a página inicial da aplicação.

### `GET /api/tasks`

Retorna as tarefas cadastradas em formato JSON:

```json
[
  {
    "id": 1,
    "title": "Configurar Git",
    "status": "concluída"
  },
  {
    "id": 2,
    "title": "Criar container Docker",
    "status": "pendente"
  },
  {
    "id": 3,
    "title": "Configurar integração contínua",
    "status": "pendente"
  }
]
```

Exemplo usando `curl`:

```bash
curl http://localhost:5000/api/tasks
```

## Testes

Execute os testes com:

```bash
pytest
```

## Estrutura do projeto

```text
.
├── app/
│   ├── __init__.py   # Factory da aplicação Flask
│   └── routes.py     # Rotas da página inicial e da API
├── tests/
│   └── test_app.py   # Testes automatizados
├── requirements.txt  # Dependências Python
└── run.py            # Ponto de entrada do servidor
```

## Status do projeto

A API é somente leitura e utiliza dados estáticos. Persistência em banco de dados, criação/edição de tarefas e autenticação ainda não fazem parte da implementação atual.