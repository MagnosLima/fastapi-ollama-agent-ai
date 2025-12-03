# FastAPI + Ollama + Strands Agents (Calculator Tool)

Este projeto implementa uma API de Chat utilizando **FastAPI**,
integrando um **Agente de IA** baseado no SDK **Strands Agents**, com o
modelo **Qwen 3 (4B)** rodando localmente via **Ollama**.

O agente também utiliza uma *Tool* de matemática (`calculator`) capaz de
resolver expressões matemáticas simples automaticamente.

## Funcionalidades

-   API `/chat` utilizando FastAPI.
-   Agente IA usando **Strands Agents SDK**.
-   Integração local com **Ollama** (modelo Qwen 3 4B).
-   Tool matemática (calculator) capaz de interpretar expressões
    matemáticas.
-   Suporte a mensagens gerais.
-   Configuração completa via arquivo `.env`.

## Pré-requisitos

### 1. Python 3.10+

Verifique:

    python --version

### 2. Ollama

Instale via site oficial: https://ollama.com/

Baixar o modelo utilizado no projeto:

``` bash
ollama pull qwen3:4b
```
## Como configurar e rodar o projeto

### 1. Clone o repositório

    git clone https://github.com/MagnosLima/fastapi-ollama-agent-ai.git
    cd fastapi-ollama-agent-ai

### 2. Crie o ambiente virtual

Windows:

    python -m venv venv
    venv\Scripts\activate

Linux / Mac:

    python -m venv venv
    source venv/bin/activate

Git Bash:

    python -m venv venv
    source venv/Scripts/activate

### 3. Instale as dependências

    pip install -r requirements.txt

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` com:

    LLM_MODEL=qwen3:4b
    LLM_ENDPOINT=http://localhost:11434

### 5. Inicie o Ollama

    ollama serve
    ollama run qwen3:4b

### 6. Execute a aplicação

    uvicorn app.main:app --reload

Acesse: http://127.0.0.1:8000/docs

## Exemplo de requisição

POST `/chat`:

    {
      "message": "Quanto é 12 * (4 + 2)?"
    }

Resposta:

    {
      "response": "O resultado é 72."
    }

## Estrutura do projeto

```text
app/
 ├── agent/
 │   └── agent.py
 ├── core/
 │   └── config.py
 ├── schemas/
 │   └── chat.py
 └── main.py
.env
.env.example
.gitignore
README.md
requirements.txt
```

## Versionamento

O `.gitignore` garante que arquivos sensíveis e ambientes virtuais não
sejam versionados.

------------------------------------------------------------------------

## 👨‍💻 Autor

[Magnos Lima ](https://github.com/MagnosLima)
