# 📝 Task Tracker CLI

Uma aplicação simples de linha de comando (CLI) para gerenciamento de
tarefas (to-do list), desenvolvida em **Python**, utilizando apenas
módulos nativos da linguagem.

Este projeto permite adicionar, atualizar, deletar, listar e alterar o
status de tarefas, armazenando os dados em um arquivo `tasks.json` no
diretório atual.

> Este projeto é baseado no desafio disponibilizado pelo site [roadmap.sh](https://roadmap.sh/projects/task-tracker).

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   ✅ Adicionar tarefas
-   ✏️ Atualizar tarefas
-   ❌ Deletar tarefas
-   🔄 Marcar tarefa como **em progresso**
-   ✔️ Marcar tarefa como **concluída**
-   📋 Listar todas as tarefas

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   Python 3
-   Módulos nativos:
    -   `sys`
    -   `os`
    -   `json`
    -   `datetime`

> ❗ Nenhuma biblioteca externa foi utilizada.

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    task-tracker/
    │
    ├── task_cli.py     # Arquivo principal (CLI)
    ├── services.py     # Regras de negócio
    ├── storage.py      # Manipulação do arquivo JSON
    └── tasks.json      # Arquivo gerado automaticamente

------------------------------------------------------------------------

## ⚙️ Como Executar

No terminal, dentro da pasta do projeto:

    python task_cli.py <comando> [argumentos]

Ou para ver a lista de comandos do projeto:

    python task_cli.py --help

------------------------------------------------------------------------

## 📌 Comandos Disponíveis

### ➕ Adicionar uma tarefa

    python task_cli.py add "Comprar pão"

Saída:

    Task added successfully (ID: 1)

------------------------------------------------------------------------

### ✏️ Atualizar uma tarefa

    python task_cli.py update 1 "Comprar pão e leite"

------------------------------------------------------------------------

### ❌ Deletar uma tarefa

    python task_cli.py delete 1

------------------------------------------------------------------------

### 🔄 Marcar como em progresso

    python task_cli.py mark-in-progress 1

------------------------------------------------------------------------

### ✔️ Marcar como concluída

    python task_cli.py mark-done 1

------------------------------------------------------------------------

### 📋 Listar todas as tarefas

    python task_cli.py list

Exemplo de saída:

    1 - Comprar pão - done
    Created: 2026-02-26T10:00:00
    Updated: 2026-02-26T10:05:00

------------------------------------------------------------------------

## 📄 Estrutura do `tasks.json`

Cada tarefa possui o seguinte formato:

``` json
{
  "id": 1,
  "description": "Comprar pão",
  "status": "todo",
  "createdAt": "2026-02-26T10:00:00",
  "updatedAt": "2026-02-26T10:00:00"
}
```

### 🏷️ Propriedades

|Campo  | Descrição |
|--|--|
| `id` |  Identificador único da tarefa |
|`description`|Descrição da tarefa|
|`status`|Status da tarefa (`todo`, `in-progress`, `done`)|
|`createdAt`|Data e hora de criação|
|`updatedAt`|Data e hora da última atualização|


------------------------------------------------------------------------

## 📌 Regras Importantes

-   O arquivo `tasks.json` é criado automaticamente caso não exista.
-   Os IDs são incrementais.
-   O status padrão ao criar uma tarefa é `todo`.
-   A aplicação trata casos de erro como:
    -   Comando inválido
    -   Tarefa inexistente
    -   Argumentos ausentes

------------------------------------------------------------------------

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte de um desafio para praticar:

-   Manipulação de arquivos
-   Leitura de argumentos via linha de comando
-   Estruturação de projetos em camadas
-   Manipulação de JSON
-   Organização de código em Python

------------------------------------------------------------------------

## 👨‍💻 Autor

Desenvolvido por Manoel Cândido 🚀